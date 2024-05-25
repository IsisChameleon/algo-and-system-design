# Algorithm structure

https://leetcode.com/explore/interview/card/cheatsheets/720/resources/4723/

# Dynamic programming - check number_of_paths


# Finding n largest items in dictionary/hash map

    ```
    collection_sizes = defaultdict(int)
    # Variable to track the total size of all files
    total_size = 0
    
    # Accumulate sizes per collection and total size
    for file_name, collection_name, file_size in file_data:
        collection_sizes[collection_name] += file_size
        total_size += file_size
    
    # Finding the top N collections by size
    # Using a heap to keep the largest N sizes
    top_collections = heapq.nlargest(N, collection_sizes.items(), key=lambda x: x[1])
    ```

# lru

Using double linked list (deque) to store item
and a hash map to find them

operation: put
  .. check if in hashmap
            yes --> remove from linked list
     create or replace hashmap key
     insert into linked list at the back (most recently accessed)
     if capacity exceed delete linked list node from the front of the queue (least recently accessed) and from hashmap

# find position in sorted array

time_idx = bisect.bisect_right(self.times, t)
