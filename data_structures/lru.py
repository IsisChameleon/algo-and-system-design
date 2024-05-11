class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.hashmap = {}
        # Dummy nodes to help simplify adding and removing nodes from the list
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key in self.hashmap:
            node = self.hashmap[key]
            self._remove(node)
            self._add(node)
            return node.value
        return -1

    def put(self, key, value):
        if key in self.hashmap:
            node = self.hashmap[key]
            self._remove(node)
        else:
            node = Node(key, value)
            self.hashmap[key] = node

        # add node to doubly linked list just before the tail (most recent)
        self._add(node)

        if len(self.hashmap) > self.capacity:
            # Remove the least recently used item which is the item just after the head
            lru = self.head.next
            self._remove(lru)
            del self.hashmap[lru.key]

    def _add(self, node):
        # Always add the new node right before the tail
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def _remove(self, node):
        # Remove an existing node from the linked list
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev