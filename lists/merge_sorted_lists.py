def merge_sorted_lists(sorted_lists: list[list[int]])-> list[int]:

    # assuming the lists are sorted in ascending order

    list_indexes = [0 for i in range(len(sorted_lists))]
    print(f"Array for list indexes: {list_indexes}")

    merged_list = []

    while not at_the_end_of_each_list(sorted_lists, list_indexes):
        current_values = [ sorted_list[j] if j < len(sorted_list) else int('+inf') for sorted_list in sorted_lists for j in list_indexes]
        print("Current values of the lists: ", current_values)
        min_tuple = min(enumerate(current_values), key=lambda x: x[1])

        # Extract the index and value from the tuple
        index_of_list_with_min_value, min_value = min_tuple

        list_indexes[index_of_list_with_min_value]+=1

        merged_list.append(min_value)

    return merged_list






def at_the_end_of_each_list(sorted_lists, list_indexes):
    
    print(f"at_the_end_of_each_list {sorted_lists} indexes {list_indexes}")

    number_of_sorted_lists = len(list_indexes)
    length_of_ith_list = lambda i, sorted_lists:  len(sorted_lists[i])

    for i in range(number_of_sorted_lists):
        list_index = list_indexes[i]
        if list_index < length_of_ith_list:
            return False
        
    return True








    
