import random

class minHeap:
    # this is a minHeap that only handles only positive integers
    def __init__(self, size):
        # count stores the number of data item currently in minHeap
        self._count = 0
        # size stores the maximum number of data item minHeap can take
        self._size = size
        # tree is a 1D array which stores the data items as nodes in minHeap
        # -1 means there is no item
        self._tree = [-1]*size

    def is_full(self):
        return self._count == self._size

    # Task 3.1
    # PSEUDO code
    PROCEDURE add(newItem)
        IF minHeap is not full THEN
        
            tree[count] <- newItem
            curr_ptr <- count
            parent_ptr <- QUOTIENT((curr_ptr - 1) DIV 2)
            
            REPEAT
                SWAP (tree[parent_ptr], tree[curr_ptr])                
                curr_ptr <- parent_ptr
                parent_ptr <- QUOTIENT((curr_ptr - 1) DIV 2)
            UNTIL curr_ptr EQUAL TO 0 OR tree[parent_ptr] <= newItem
            
            INCREMENT count BY 1
        ELSE
            OUTPUT "Heap is full. Cannot add."
        END IF
    END PROCEDURE

    def remove_minimum(self):
        if self._count != 0:
            root = self._tree[0]
            self._count -= 1
            temp = self._tree[self._count]
            self._tree[0] = temp
            self._tree[self._count] = -1
            

            done = False
            curr_ptr = 0
            left_ptr = curr_ptr*2 + 1
            right_ptr = curr_ptr*2 + 2
            while not done and left_ptr < self._count:
                if right_ptr < self._count:
                    #has left and right children
                    if self._tree[left_ptr] < self._tree[right_ptr] and self._tree[left_ptr] < self._tree[curr_ptr]:
                        self._tree[curr_ptr], self._tree[left_ptr] = self._tree[left_ptr], self._tree[curr_ptr]
                        curr_ptr = left_ptr
                    elif self._tree[right_ptr] < self._tree[left_ptr] and self._tree[right_ptr] < self._tree[curr_ptr]:
                        self._tree[curr_ptr], self._tree[right_ptr] = self._tree[right_ptr], self._tree[curr_ptr]
                        curr_ptr = right_ptr
                    else:
                        done = True                    
                else:
                    #has only left child
                    if self._tree[left_ptr] < self._tree[curr_ptr]:
                        self._tree[curr_ptr], self._tree[left_ptr] = self._tree[left_ptr], self._tree[curr_ptr]
                        curr_ptr = left_ptr
                    else:
                        done = True

                left_ptr = curr_ptr*2 + 1
                right_ptr = curr_ptr*2 + 2
            return root
        else:
            print("Tree is empty. Cannot remove.")
            return -1

    
    def sort(self):
        # Task 3.2
        # Make use of the function remove_minimum which is implemented for you,
        # implement sort() which returns a sorted list of the items in minHeap.
        # Take note that by calling remove_minimum, the root node is removed from minHeap.
        pass

    
    def display_all_paths(self):
        # Task 3.3
        # Implement display_path which will display all paths from the root of minHeap to its leaves.
        #
        # Hint: minHeap is actually a complete binary tree
        # It is a binary tree in which every level, except possibly the last,
        # is completely filled, and all nodes are as far left as possible.
        #
        # This means that the tree array indices from 0 to count -1 contain all the items in minHeap
        # and nothing after count.
        pass

def test():
    test_value = [58, 36, 3, 9, 87]
    h1 = minHeap(5)
    for value in test_value:
        h1.add(value)
    print(h1.sort())
test()
            
def test_32(n):
    test_value = random.sample(range(1,100), n)
    h1 = minHeap(n)
    for value in test_value:
        h1.add(value)
    print(h1.sort())

print("task 3.2")
print("1st run")
test_32(15)
print("2nd run")
test_32(15)
print("3rd run")
test_32(15)
print()

def test_33(n):
    test_value = random.sample(range(1,100), n)
    h1 = minHeap(n)
    for value in test_value:
        h1.add(value)
    h1.display_all_paths()

print("task 3.3")
print("1st run")
test_33(5)
print("2nd run")
test_33(10)
print("3rd run")
test_33(15)
