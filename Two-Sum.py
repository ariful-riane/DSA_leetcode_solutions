1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        dic = {}
4        i = 0
5        while i < len(nums):
6            dic[nums[i]] = i
7            i += 1
8        i = 0
9        while i < len(nums):
10            sec_target = target - nums[i]
11            if sec_target in dic and dic[sec_target] != i:
12                return [i, dic[sec_target]]
13            i += 1