import hashlib
import bisect

class ConsistentHashing:
    def __init__(self, nodes=None, replicas=3):
        self.replicas = replicas
        self.ring = dict()
        self.sorted_keys = []
        if nodes:
            for node in nodes:
                self.add_node(node)

    def add_node(self, node):
        for i in range(self.replicas):
            key = self.hash(str(node) + str(i))
            self.ring[key] = node
            bisect.insort(self.sorted_keys, key)

    def remove_node(self, node):
        for i in range(self.replicas):
            key = self.hash(str(node) + str(i))
            if key in self.ring:
                del self.ring[key]
                self.sorted_keys.remove(key)

    def get_node(self, key_str):
        if not self.ring:
            return None
        key = self.hash(key_str)
        pos = bisect.bisect(self.sorted_keys, key)
        if pos == len(self.sorted_keys):
            pos = 0
        return self.ring[self.sorted_keys[pos]]

    def hash(self, key_str):
        return int(hashlib.md5(key_str.encode('utf-8')).hexdigest(), 16)
    
if __name__ == '__main__':


    # Example usage
    nodes = ['http://localhost:5001', 'http://localhost:5002', 'http://localhost:5003']
    ch = ConsistentHashing(nodes)

    # Adding a new node
    ch.add_node('http://localhost:5004')

    # Removing a node
    ch.remove_node('http://localhost:5002')

    # Getting the node for a given key
    node = ch.get_node('some_request_path')
    print(f"The request should be forwarded to: {node}")
