class Node:

    """
    A node of a doubly linked list, used to implement the LRU cache.
    """
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    """
    A Least Recently Used (LRU) cache implemented using a hashmap and a doubly linked list.
    """
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("Capacity must be a positive integer")
        self.capacity = capacity
        self.hashmap = {}
        # Dummy nodes to help simplify adding and removing nodes from the list
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.hashmap:
            node = self.hashmap[key] # find node
            self._remove(node) # move it to the front of the queue
            self._add(node)
            return node.value
        return None

    # def put(self, key, value):
    #     if key in self.hashmap:
    #         node = self.hashmap[key]
    #         self._remove(node)
    #     else:
    #         node = Node(key, value)
    #         self.hashmap[key] = node

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self._remove(self.hashmap[key])
        node = Node(key, value)
        self.hashmap[key] = node
        # add node to doubly linked list just before the tail (most recent)
        self._add(node)

        if len(self.hashmap) > self.capacity:
            # Remove the least recently used item which is the item just after the head
            lru = self.head.next
            self._remove(lru)
            del self.hashmap[lru.key]

    def _add(self, node: Node) -> None:
        # Always add the new node right before the tail
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def _remove(self, node: Node) -> None:
        # Remove an existing node from the linked list
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node