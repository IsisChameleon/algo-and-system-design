def merge_sorted_lists(sorted_lists: list[list[float]])-> list[float]:

    # assuming the lists are sorted in ascending order

    list_indexes = [0 for i in range(len(sorted_lists))]
    
    merged_list = []

    while not at_the_end_of_each_list(sorted_lists, list_indexes):

        current_values = []
        for i, sorted_list in enumerate(sorted_lists):
            current_value = sorted_list[list_indexes[i]] if list_indexes[i] < len(sorted_list) else float('+inf')
            current_values.append(current_value)

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
        if list_index < length_of_ith_list(i, sorted_lists):
            return False
        
    return True








    
