# Pilot
Pilot is a python library for traversing object trees and graphs. It is currently in pre-alpha.

1. [Usage](#usage)
2. [Documentation](#documentation)
    - [Classes](#classes)
    - [Callbacks](#callbacks)
    - [Nodes](#nodes)

# Usage

Download and include the library:
```
$ pip install pilot
```

The first step is to define a callback:

```
from pilot import Callback, Pilot

def my_callback(node):
    print node.key, node.id

callback = Callback(my_callback)
```

Now, define the pilot object and execute a flight:

```
data = {'test': 1}
pilot = Pilot(callbacks=[callback])
pilot.fly(data)
>> None 1
>> test 2
```

See the documentation for more details!

# Documentation

#### ```pilot.fly(self, object, rootkey=None, rootpath=None, rootparent=None)```
The primary method for traversing an object and injecting callbacks into the traversal. The flight will generate a ```Node``` for each bit of data it encounters, and will make that node available on the data through a ``__node__`` property. Warning: this means the process will ocassionally change the underlying classes of objects to support adding the ```__node__``` property.

**Config options**:

- ```run_callbacks``` *(true|false)*: Set this to false to skip callbacks completely.
- ```callbacks```: an array of callback objects. See the Callback section for more information.
- ```traversal_mode```: the mode for traversing the tree. Options are ```depth``` for *depth-first* processing and ```breadth``` for *breadth-first* processing.
- ```structure```: Options are ```tree``` (default) and ```graph```. Graphs add nodes as "neighbors" rather than parent/child.
- ```node_visit_limit```: An integer that defines how many times to allow visits to nodes. (Only applicable to graphs.) Set to ```-1``` to allow infinite. Note that infinite trees will process indefinitely - use ```walk.break()``` in a callback to end the processing manually.


The configuration defaults to the following:

```
structure = "Tree"
node_visit_limit = 1
traversal_mode = 'depth'
run_callbacks = True
```

#### ```Pilot.halt()``` *(static method)*:
Calling this method within a callback will halt processing completely. This allows for early exit, and limited processing of infinite trees.


### Callbacks

We want to be able to execute custom functionality on certain properties within our object tree. For example, if we wanted to print the count of all friends for any ```person``` object we encounter, we could write a callback object for the ```friends``` property. The general form of a callback object is:

```
data = [
    {'name': 'Jim', 'friends': [{},{}]},
    {'name': 'Jane', 'friends': [{},{},{}]},
    {'name': 'Joe', 'friends': []}
]

def count_friends(node):
    try:
        node.val['name']
    except: # not a person        
        return
    person = node.val
    friends = person.get('friends', None)
    if friends:
        print person.get("name") + " has " + str(len(friends)) + " friends."
    else:
        print person.get("name") + " has no friends."

from pilot import Callback, Pilot
callback = DictCallback(count_friends, containers=['dict'])
Pilot(callbacks=[callback]).fly(data)
```

Here are the keyword args you can supply in a callback configuration, most of which act as filters:

- ```containers```: an array of containers to run on. Options are ```'dict'```, ```'list'```, and ```'value'```. If unspecifed, the callback will run on any container.
- ```keys```: an array of keys to run on. The callback will check the key of the property against this list. If unspecified, the callback will run on any key.
- ```positions```: an array of positions in the traversal to run on. Options are ```'pre'``` (before any list/object is traversed), and ```'post'``` (after any list/object is traversed). For properties of container-type ```'value'```, these two run in immediate succession. If unspecifed, the callback will run ```'post'```.

The callback function will be passed a single argument: a node object. 

### Nodes

Node objects represent a single node in the tree, providing metadata about the value, its parents, siblings, and children. Nodes have the following properties:

- ```key```: The key of this property as defined on it's parent. For example, if this callback is running on the ```'weight'``` property of a ```person```, the ```key``` would be ```'weight'```. Note that this will be ```undefined``` for properties in arrays.
- ```value```: The value of the property. To use the above example, the value would be something like ```'183'```.
- ```container```: The type of container of the property.
- ```encountered```: The number of times the current walk has processed the node.
- ```id```: A unique id for the node (within the context of Walk);

You may also call the following methods off of a node object. Keep in mind that some of the node accessors may not be populated yet based on where you are in your traversal:

- ```isRoot()```: Returns a boolean of whether the node is an orphan (no parents.)
- ```parent()```: The first node under which the property exists. ```node.parent``` is another instance of node, and will have all the same properties. This is a convenience method that's useful in trees, where only one parent is possible.
- ```parents()```: A method that returns parents of a node. An optional search parameters object can be passed in to filter the list to all who have matching key-values. For example, ```node.parents(key='name', val='Tom')``` will return all parents where ```key == 'name'``` and ```val == 'Tom'```.
- ```children()```: A method that returns children of a node (i.e. all nodes whose parent is this node.) An optional search parameters object can be passed in to filter the list to all who have matching key-values. For example, ```node.children(key='name', val='Tom')``` will return all children where ```key == 'name'``` and ```val == 'Tom'```.
- ```neighbors()```: A method that returns adjacent (non-parent, non-child) nodes, for use in graphs. An optional search parameters object can be passed in to filter the list to all who have matching key-values. For example, ```node.neighbors(key='name', val='Tom')``` will return all neighbors where ```key == 'name'``` and ```val == 'Tom'```.
- ```siblings()```: A method that returns all nodes that exist alongside the current node within its parents. For parents of container ```'object'```, this includes all other properties of the parent object. For parents of type ```'array'```, this includes all other nodes in that array. 
- ```roots()```: A method that returns all connected root nodes.
- ```ancestors()```: A method that returns a list of all ancestor nodes, going back to the root.
