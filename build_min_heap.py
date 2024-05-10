# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        print(f"Initial Array: {array}")
        self.heap = self.buildHeap(array)
        print(f"Heap: {self.heap}")

    def buildHeap(self, array):
        # Write your code here.
        # find last parent
        self.heap = array
        index_last = len(self.heap)-1
        parent_index = self._getParent(index_last)
        for p in reversed(range(parent_index+1)):
            self.siftDown(p)
        return self.heap
        

    def siftDown(self, index_new):
        # TO remove smallest value with a pop by putting it at the end of the array
        # we swap it with the end of the array, and then we siftdown the new root to its
        # right position
        # Write your code here.
        index_children=self._getChildren(index_new)
        while ( index_children[0] is not None ) \
            and ( index_children[0] is not None and self.heap[index_children[0]] < self.heap[index_new] \
                 or index_children[1] is not None and self.heap[index_children[1]] < self.heap[index_new] ):

            if index_children[1] is None:
                min_child_index = index_children[0]
            else:
                min_child_index = index_children[0] if self.heap[index_children[0]]<=self.heap[index_children[1]] else index_children[1]

            print(f'About to sift down this value {self.heap[index_new]} > {self.heap[min_child_index]}') 
            self._swap(min_child_index, index_new)
            index_new = min_child_index
            index_children=self._getChildren(index_new)

    def siftUp(self, index_new):
        # Write your code here.
        # check last value and siftUp
        index_parent = self._getParent(index_new)
        while index_parent is not None and self.heap[index_parent] > self.heap[index_new]:
            self._swap(index_parent, index_new)
            index_new = index_parent
            index_parent = self._getParent(index_new)
                
                

    def peek(self):
        # Write your code here.
        return self.heap[0]

    def remove(self):
        # Write your code here.
        self._swap(0, len(self.heap)-1)
        # put the one we want to remove at the end
        self.siftDown(0)
        min_value = self.heap.pop()
        print(f"Heap after remove: {self.heap}")
        return min_value

    def insert(self, value):
        # Write your code here.
        self.heap.append(value)
        self.siftUp(len(self.heap)-1)
    
    def _swap(self, i, j):
        if i < 0 or i > len(self.heap)-1:
            return
        if j < 0 or j > len(self.heap)-1:
            return
        value_i = self.heap[i]
        self.heap[i]=self.heap[j]
        self.heap[j]=value_i

    def _getParent(self, i):
        if i == 0:
            return None
        return (i-1)//2

    def _getChildren(self, i):
        ch1 = i*2+1 if i*2+1 < len(self.heap) else None
        ch2 = i*2+2 if i*2+2 < len(self.heap) else None
        return (ch1, ch2)