## Problem 1:
# Given an array of strings, group anagrams together.

# Example:
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]

# Note:
# All inputs will be in lowercase.
# The order of your output does not matter.

# Time Complexity: O(nk) where n is the number of strings, and k is the average length of the strings in the input
import collections
from typing import List


class Solution:
    primes = []
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)

        # we simply find the prime product for each string
        # prime product for anagrams will be the same
        # as they contain the same chars with the same frequency
        for s in strs:
            primeProduct = self.getPrimeProduct(s)
            # then we store the prime product as the key in our map with a list of strings
            # that have the same prime product
            if primeProduct not in d:
                d[primeProduct] = []
            d[primeProduct].append(s)
        
        # in the end we will have a map with prime product as key and value as anagrams
        # return the values in the map as a list
        return list(d.values())
    
    # Complexity O(k) where k is average length of strings in strs 
    def getPrimeProduct(self, s: str) -> int:
        if not self.primes:
            self.primes = self.getFirstNPrimes(26)

        result = 1
        for c in s:
            result *= self.primes[ord(c) - ord('a')]
        
        return result
    
    def getFirstNPrimes(self, n: int) -> list:
        primes = []
        num = 2
        while len(primes) < n:
            isPrime = True
            for p in primes:
                if num % p == 0:
                    isPrime = False
                    break
            if isPrime:
                primes.append(num)
            num += 1
        return primes