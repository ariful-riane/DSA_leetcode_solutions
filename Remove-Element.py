1#Program: Remove Element
2#Author: Ariful Riane
3#Input: a list of integars and a value
4#Output: return the remaining length of the list after removing the value
5class Solution:
6    def removeElement(self, nums: List[int], val: int) -> int:
7        write = 0
8        for read in range(len(nums)):
9            if nums[read] != val:
10                nums[write] = nums[read]
11                write += 1
12        return write
13
14