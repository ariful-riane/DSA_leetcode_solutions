1#Program: Palindrome Number
2#Author: Ariful Riane
3#Input: an integar
4#Output: return the boolean whether the intergar is palindrome or not
5class Solution:
6    def isPalindrome(self, x: int) -> bool:
7        if x >= 0:
8            new = x % 10
9            remainder = x // 10
10            while remainder:
11                next = remainder % 10
12                new = new * 10 + next
13                remainder //= 10
14            return x == new
15        else:
16             return False