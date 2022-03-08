"""
Given two words source and target, and a list of words words, find the length of the shortest series of edits that transforms source to target.
Each edit must change exactly one letter at a time, and each intermediate word (and the final target word) must exist in words.
If the task is impossible, return -1

Example
source = “bit”, target = "dog"
words = [“but”, “put”, “big”, “pot”, “pog”, “dog”, “lot”]

output: 5
explanation: bit -> but -> put -> pot -> pog -> dog has 5 transitions.
"""

"""
BIGGEST TAKEAWAY
Each node needs to carry the min edits took to go from source to it. In our example example: from bit, we can go to but and big. Going to big is a bust, and if we still do min_edits += 1
"""

from collections import deque

def shortestWordEditPath(source, target, words):
    """
    @param source: str
    @param target: str
    @param words: str[]
    @return: int
    """
    if target not in words: return -1
  
    q = deque()
    q.append((source, 0))
    visited = set()
    while q:
        curr, curr_edit = q.pop()
        if curr == target:
            return curr_edit
        visited.add(curr)
        # need to find all words that are one edit away
        one_edit_away = [word for word in words if isOneEditAway(curr, word)]
        if one_edit_away:
            _ = [q.append((word, curr_edit + 1)) for word in one_edit_away if word not in visited]
        else:
              return -1
    
    return -1

def isOneEditAway(word1, word2):
    p1 = 0
    p2 = 0
    diff = 0 #According to test case, edit does not include add/remove. otherwise: diff = abs(len(word1) - len(word2))

    if len(word1) != len(word2): return False
    
    while p1 < len(word1) and p2 < len(word2) and diff < 2:
        if word1[p1] != word2[p2]:
            diff += 1
        p1 += 1
        p2 += 1

    return diff < 2
