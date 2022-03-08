class Solution:
    def groupAnagrams(self, strs):
        """
        Two words are anagrams if their char freq is exactly the same.
        OR 
        two words are anagrams if their sorted string is the same.
        Idea:
        - for each word, create counter. Store in a list at the same idx as the word.
        - for each word, look at the other elems and their counter, add to result when c1 == c2.
        - this is O(n^2)
        
        How can we make it less than O(n^2)?
        
        Sort each word - O(nlogn)
        Convert into set to get unique groups - O(n)
        iterate through each word in sorted list, add to dict if not in dict. dict[word] = [word] - O(n)
        if we see word that is in dict, append append to list
        get all values of dict.
        
        RUNTIME: O(num of words * slogs) where s = length of longest word
        """
        
        word_map = {}
        
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in word_map:
                word_map[sorted_word].append(word)
            else:
                word_map[sorted_word] = [word]
            
        all_groups = list(word_map.values())
        
        return all_groups