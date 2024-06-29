'''

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

'''

from typing import List

def containsDuplicate(nums: List[int]) -> bool:
    # loop through each element in the arry
    # mark the occurance in a dictionary
    d = {}
    for ele in nums:
        if ele in d:
            return True # there is a duplicate element
        d[ele] = d.get(ele, 0) + 1
    
    print(d)
    return False


if __name__ == '__main__':
    arr = [1,1,1,3,3,4,3,2,4,2]
    res = containsDuplicate(nums=arr)
    print(res)