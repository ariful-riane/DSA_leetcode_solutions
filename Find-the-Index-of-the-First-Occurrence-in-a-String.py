1class Solution:
2    def strStr(self, haystack: str, needle: str) -> int:
3        length = len(needle)
4        i = 0
5        while i + length <= len(haystack):
6            if haystack[i:length + i] == needle:
7                return i
8            else:
9                i+=1
10        return -1