"""
You will be given a list of file names, the collection the file belongs to and the size of each file. 
Write a program to find the top N collections by size and the total size of all the files in the system. 
Follow up - collections can be nested, find top N collections by size.
"""

def find_top_collections(file_data, N):
    from collections import defaultdict
    import heapq
    
    # Dictionary to hold the total size for each collection
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
    
    return top_collections, total_size


# to test