"""
Letter Combinations of a Phone Number
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
"""
from collections import deque

class Solution:
    def letterCombinations(self, digits: str):
        """
        The basic idea is sort of creating next possible states using a BFS sort of algorithm. 
        We initialize the queue with the chars of the first digit.
        Then we look at the next digit, and append to currently popped item from queue()
        If we have reached the length of the digit i.e. we have two digits and the created/appended string is also of length 2, then we can add it to 
        the result list.
        If we have not reached the length, we append it back to the queue. 
        
        Things that tripped me: 
        - always code base and edge cases first i.e. empty string. 1 digit only.
        - took me a LONG while to figure out how to know which digit to look at. Turns out, it depended on the item we just popped from queue and its length
        - the digit we want to look at is at the idx = len(popped item)
        - didn't realize that we need to keep going untill q is empty. Its a BFS, ofcourse you wait till you empty the queue. 
        
        """
        # edge case
        if digits == "": return []
        
        # we could have stored the chars as a list instead of str i.e. ["a", "b", "c"] instead of "abc"
        table = {"1": "", "2": "abc", "3": "def", "4": "ghi", "5":"jkl", "6": "mno", "7":"pqrs", "8": "tuv", "9":"wxyz"}
        
        # simple base case
        if len(digits) == 1: return list(table[digits[0]])
        
        # main algo
        q = deque()
        _ = [q.append(c) for c in list(table[digits[0]])]
        
        res = []
        visited = set()
        while q:
            current_char = q.pop()
            visited.add(current_char)
            current_idx = len(current_char)
            # digit we want to use to create the next set of states
            current_digit = digits[current_idx]
            current_digit_chars = list(table[current_digit]) 
            
            for next_char in current_digit_chars:
                sub = current_char + next_char
                if len(sub) == len(digits):
                    res.append(sub)
                else:
                    if sub not in visited: q.append(sub) # does it help of we cross check if its in the queue already or not? or a visited set? 
        
        return sorted(res)
        
        