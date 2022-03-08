class Solution:
    def lengthOfLongestSubstring(self, s):
        unique_chars = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            # inside while loop if right has encountered a dupe
            while s[right] in unique_chars: # abcabcbb
                unique_chars.remove(s[left])
                left += 1 
            
            unique_chars.add(s[right]) # MUST BE HERE. WHY?????
            max_len = max(max_len, right - left + 1)
  
        return max_len