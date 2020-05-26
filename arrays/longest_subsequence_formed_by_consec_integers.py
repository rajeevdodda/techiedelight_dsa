# https://www.techiedelight.com/find-longest-subsequence-formed-by-consecutive-integers/


def longest_consec_integers(array: list):
    # construct a set out of input elements
    s = set(array)

    # initialize result by 1
    max_length = 1

    # do for each element of the input sequence
    for i in array:
        # check if current element i is candidate for starting of a sequence
        # i.e. previous element (i - 1) don't exist in the set
        if i - 1 not in s:
            length = 1
            # check for presence of elements i+1, i+2, i+3.. i+len in the set
            while i + length in s:
                length += 1
            max_length = max(length, max_length)

    print(max_length)


longest_consec_integers([2, 0, 6, 1, 5, 3, 7]
                        )
