class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Idea:
        - Iterate over s, starting at 0. This will be our middle char of the palindrome.
        - Then we expand out wards from middle, checking if the next chars are same or not.
        - If not, we know its not a palindrome, and we move on.
        EDGE CASE: 
        - For odd palindromes, left=right=i, but for even, right needs to be i+1

        """
        longest_palindromic_sub = ""
        
        for i in range(len(s)):
            left = right = i
            # ODD PALINDROMES
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if len(s[left:right+1]) > len(longest_palindromic_sub):
                    longest_palindromic_sub = s[left:right+1]
                left -= 1
                right += 1
            
            left = i
            right = i + 1
            # EVEN PALINDROMES
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if len(s[left:right+1]) > len(longest_palindromic_sub):
                    longest_palindromic_sub = s[left:right+1]
                left -= 1
                right += 1
        
        return longest_palindromic_sub