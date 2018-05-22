# Linked List task
Interview task for linked list

### Given
Class Node wich has 2 attributes - `value` and `next`

`value` integer key

`next` - object of the Node class

### What should be done
Create `find_delete_sort(node, key)` which delete all nodes with `value == key` in the linked list started with `node` 

### Approach
1. Trying to find first element in the linked list with `value != key` and set is as a `new_head` for the returned list
2. Suppose that resultant list is already sorted. We take the next element in the original list, check if `value != key` and insert it in the necessary place in returned list. If `value == key` take the next element in the original list
3. Insert function. Compare `value` of passed node with all the values of the nodes in resultant list. As soon as passed node value less or equal the checked node value, passed node is inserted. Function returns head of resultant list
4. Do this steps 2-3 until all elements in the orifinal list are checked.

Additional checks:
1. If node was checked, `is_used` attribute is set to the node. I helps to avoid infinite loops for the looped linked list. Before returning new list `is_used` attribute is deleted from all the nodes
2. Function arguments check. Input arguments should be instances of the `Node` and `int` classes
3. Node value check. If Node value is not `int`, function stops due further it requires to compare Node values via logical operations
4. Added `__str__` magic method for debugging purposes
