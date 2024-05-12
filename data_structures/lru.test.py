import unittest
from lru import LRUCache, Node

class TestLRUCache(unittest.TestCase):

    def test_lru_cache(self):
        lru_cache = LRUCache(2)

        # Test initial cache state
        self.assertIsNone(lru_cache.get(1), "Cache should return None for missing key")

        # Test put and get operations
        lru_cache.put(1, 1)
        self.assertEqual(lru_cache.get(1), 1, "Cache should return value for existing key")

        # Test updating existing key
        lru_cache.put(1, 10)
        self.assertEqual(lru_cache.get(1), 10, "Cache should return updated value for existing key")

        # Test eviction policy
        lru_cache.put(2, 2)
        lru_cache.put(3, 3)  # This should evict key 1
        self.assertIsNone(lru_cache.get(1), "Cache should evict least recently used key")
        self.assertEqual(lru_cache.get(2), 2, "Cache should return value for existing key")
        self.assertEqual(lru_cache.get(3), 3, "Cache should return value for existing key")

        # Test capacity
        self.assertEqual(len(lru_cache.hashmap), 2, "Cache should not exceed its capacity")

    def test_lru_cache_capacity_zero_or_negative(self):
        with self.assertRaises(ValueError):
            LRUCache(0)
        with self.assertRaises(ValueError):
            LRUCache(-1)

if __name__ == '__main__':
    unittest.main()
