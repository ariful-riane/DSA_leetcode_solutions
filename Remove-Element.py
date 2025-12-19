11#Program: Remove Element
22#Author: Ariful Riane
33#Input: a list of integars and a value
44#Output: return the remaining length of the list after removing the value
5class Solution:
6    def removeElement(self, nums: List[int], val: int) -> int:
7        i = 0
8        while i < len(nums):
9            if nums[i] == val:
10                del nums[i]
11            else:
12                i+=1
13