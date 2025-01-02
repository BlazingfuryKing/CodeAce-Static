import random

class minHeap:
    # this is a minHeap that only handles only positive integers
    def __init__(self, size):
        # _count stores the number of node currently in minHeap
        self._count = 0
        # _size stores the maximum number of node minHeap can take
        self._size = size
        # _tree is a 1D array which stores the nodes in minHeap
        # -1 means there is no item
        self._tree = [-1]*size

    def is_full(self):
        return self._count == self._size

    # Task 3.1
    # PSEUDO code
    def add(self, newItem):
        if not self.is_full():
            self._tree[self._count] = newItem
            curr_ptr = self._count
            parent_ptr = (curr_ptr - 1)//2
            while not (curr_ptr == 0 or self._tree[parent_ptr] <= newItem):
                temp = self._tree[parent_ptr]
                self._tree[parent_ptr] = newItem
                self._tree[curr_ptr] = temp
                
                curr_ptr = parent_ptr
                parent_ptr = (curr_ptr - 1)//2
            self._count += 1
        else:
            print("Heap is full. Cannot add.")

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
                        # A. Swap curr node with left node
                        self._tree[curr_ptr], self._tree[left_ptr] = self._tree[left_ptr], self._tree[curr_ptr]
                        curr_ptr = left_ptr
                    elif self._tree[right_ptr] < self._tree[left_ptr] and self._tree[right_ptr] < self._tree[curr_ptr]:
                        # B. Swap curr node with right node
                        self._tree[curr_ptr], self._tree[right_ptr] = self._tree[right_ptr], self._tree[curr_ptr]
                        curr_ptr = right_ptr
                    else:
                        done = True                    
                else:
                    #has only left child
                    if self._tree[left_ptr] < self._tree[curr_ptr]:
                        # C. Swap curr node with left node
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

    # Task 3.2
    def sort(self):
        result = []
        for i in range(self._count):
            result.append(self.remove_minimum())
        return result

    # Task 3.3
    def display_all_paths(self):
        def helper(node_ptr, partial_solution):
            if node_ptr < self._count and (node_ptr*2 + 1) >= self._count and (node_ptr*2 + 2) >= self._count:
                print(partial_solution + str(self._tree[node_ptr]))
            else:
                if (node_ptr*2 + 1) < self._count:
                    helper(node_ptr*2 + 1, partial_solution + str(self._tree[node_ptr]) + " ")
                if (node_ptr*2 + 2) < self._count:    
                    helper(node_ptr*2 + 2, partial_solution + str(self._tree[node_ptr]) + " ")
        helper(0, "")

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
