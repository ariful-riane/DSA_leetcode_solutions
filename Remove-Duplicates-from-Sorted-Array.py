1#Program: Remove Duplicates from Sorted Array
2#Author: Ariful Riane
3#Input: a list of integars
4#Output: return the list after removing the duplicates
5
6class Solution:
7    def removeDuplicates(self, nums: List[int]) -> int:
8        write = 1
9        for read in range(1, len(nums)):
10            if nums[read] != nums[read - 1]:
11                nums[write] = nums[read]
12                write += 1
13        return write