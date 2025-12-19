1#Program: Two Sum
2#Author: Ariful Riane
3#Input: a list of intergars and a target value
4#Output: list of the indexes of the values which adds up to get the target value
5class Solution:
6    def twoSum(self, nums: List[int], target: int) -> List[int]:
7        dic = {}
8        i = 0
9        while i < len(nums):
10            dic[nums[i]] = i
11            i += 1
12        i = 0
13        while i < len(nums):
14            sec_target = target - nums[i]
15            if sec_target in dic and dic[sec_target] != i:
16                return [i, dic[sec_target]]
17            i += 1