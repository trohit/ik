"""
2 Sum In A Sorted Array
Given an array sorted in non-decreasing order and a target number,
find the indices of the two values from the array that sum up to the given target number.

Example
{
"numbers": [1, 2, 3, 5, 10],
"target": 7
}

Output: [1, 3]
"""
def pair_sum_sorted_array(numbers, target):
    """
    Args:
     numbers(list_int32)
     target(int32)
    Returns:
     list_int32
    """
    # Write your code here.
    dd = {} # num_to_pos_dd
    for i, v in enumerate(numbers):
        
        need = target - v
        # print(f"need {need} as complementary of {v}")
        # continue
        if need in dd:
            # print(f"found {need} at pos {dd[need]} as complementary of {v}@{i} ")
            # print(f"ret [{i}, {dd[need]}]")
            return [i, dd[need]]
        else:
            # print(f"dd[{v}] = {i}")
            dd[v] = i
    # indexes not found
    return [-1, -1]
