# https://www.techiedelight.com/longest-alternating-subarray-problem/


def longest_alternating_sub_array(array: list):
    # stores length of longest alternating sublist found so far
    max_length = 1

    # stores ending index of longest alternating sublist found so far
    end_index = 0

    # stores length of longest alternating sublist ending at current position
    current_length = 1
    for i in range(1, len(array)):
        if array[i] * array[i - 1] < 0:
            current_length += 1
            if current_length > max_length:
                max_length = current_length
                end_index = i
        else:
            current_length = 1

    print(array[end_index - max_length: end_index + 1])


longest_alternating_sub_array([1, -2, 6, 4, -3, 2, -4, 3, -1])
