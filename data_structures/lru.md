# LRU

Example of usage of double ended queue (deque) and hash tables

## What is LRU


An LRU (Least Recently Used) cache is a type of data storage that holds a fixed number of items and evicts the least recently used item when it needs space for a new item. This concept is often used in systems where it's critical to manage memory efficiently, such as in operating systems, database management systems, and caching solutions in web technologies. 

## Key Concepts  
  
Fixed Size: The cache has a maximum capacity, which means it can only hold a fixed number of items. Once the capacity is reached, older items need to be evicted to make room for new ones.
Eviction Policy: The LRU cache evicts the least recently used items first. This is based on the assumption that items accessed recently are more likely to be accessed again soon.
Usage: Useful in scenarios where you want quick access to items that are frequently used without maintaining all items in memory, which can be costly.

##  How does an LRU cache work? Explains the mechanism and choice of data structures.

An LRU (Least Recently Used) cache is a cache replacement policy that removes the least recently accessed item when the cache reaches its capacity limit, making room for new items. The typical implementation of an LRU cache combines two data structures: a hash map and a double-ended queue (deque).

Hash Map: This is used for fast lookups. The key in the hash map corresponds to the key of the cache item, and the value is a pointer or reference to the corresponding node in the deque, which holds the cache item’s value. This allows for O(1) time complexity for access operations.

Double-Ended Queue: The deque, implemented using a doubly linked list, stores the keys of the cache items. The most recently used items are near one end (front), and the least recently used items are at the other end (back). When an item is accessed or added to the cache, it is moved to or placed at the front of the deque. When the cache exceeds its capacity, items from the back (the least recently used items) are evicted.

This combination of a hash map and a deque ensures that all essential operations—adding items, accessing items, and evicting items—are done in constant time, which is crucial for the performance of the cache.


### Operations  
Access: When an item is accessed, it is moved to the front (or end, depending on implementation) of the deque, indicating that it has been most recently used.
Insertion: When a new item is added, it is also placed at the front of the deque. If the cache is full, the item at the back of the deque (the least recently used item) is removed.
Deletion: To remove an item, it must be found in the hash table and then removed from the deque, which requires adjusting pointers in the doubly linked list.
Complexity


So you need to be able to:
1) Find item
2) remove item from its position
3) add (new) item to front (push to front)
4) pop item from back (least recently used side)
5) pop item from anywhere [1) + 2) to invalidate item from cache]


Time Complexity: Both get and put operations should ideally be O(1).
Space Complexity: O(n), where n is the capacity of the cache.

## Real world example of LRU cache

* Can you identify a real-world application for an LRU cache * 

One compelling real-world application of an LRU cache is in web browser caching. When you visit web pages, the browser can store the contents of these pages (like HTML files, images, and scripts) in its cache. With an LRU cache policy, the browser ensures that the most recently accessed pages are kept available, while older, less frequently accessed pages are discarded from the cache when it reaches its capacity. This significantly speeds up the loading time of frequently visited pages and reduces data usage and latency by not requiring these pages to be fetched from the internet every time they are accessed.

Another example is in content delivery networks (CDNs), where LRU caches are used to manage which content is stored at network edges, allowing quick delivery of popular content to users and efficiently updating the cache with newer or now popular content as access patterns change.

These examples highlight the effectiveness of LRU caches in enhancing the performance and efficiency of systems that rely on quick data retrieval and intelligent management of limited storage resources.

## When to use LRU instead of other caches?

### Other cache policies

FIFO (First In, First Out)
Random Replacement
most frequently used

recency works well for web applications and CDN : improved hit rate



# DEQUE

double ended queue

often implemented with doubly linked list

Advantages of Using a Doubly Linked List for a Deque:
O(1) Time Complexity for Insertions and Deletions: Items can be added or removed from both the front and the rear of the deque in constant time. This is facilitated by the fact that each node in a doubly linked list contains links to both its predecessor and successor, allowing easy addition and removal without needing to traverse the entire list.
Bidirectional Access: The ability to easily move forwards or backwards through the list (thanks to the two-way linking) is particularly useful for operations that require access to both the front and the back of the deque.
Dynamic Size: Unlike arrays, a doubly linked list does not require a predefined fixed size. This flexibility allows the deque to expand and contract as needed, based on the number of elements it currently holds.

Typical Operations:
push_front: Add an element at the front of the deque. Update the head pointer and adjust the backward link of the existing head.
push_back: Add an element at the rear of the deque. Update the tail pointer and adjust the forward link of the existing tail.
pop_front: Remove an element from the front of the deque. Move the head pointer to the next element and adjust links accordingly.
pop_back: Remove an element from the rear of the deque. Move the tail pointer to the previous element and adjust links accordingly.