
#BINARY SEARCH

# Implementation of Binary Search Algorithm:
# binary search uses divide and conquer
# we will leverage the fact that our list is sorted



def binary_search(l, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1
    if low > high:
        return -1
    midpoint = (high + low) // 2


    if target==l[midpoint]:
        return midpoint
    elif target<l[midpoint]:
        return binary_search(l, target, low=0, high= midpoint -1)
    elif target>l[midpoint]:
        return binary_search(l, target, low= midpoint + 1, high = len(l) -1)

    else:
        return -1


if __name__ == "__main__":

    lists = [1,2,4,6,45,7,3,78,2,45,77,43,5,6,7,22,3,5,6]

    lists.sort()

    print(binary_search(lists, 22))