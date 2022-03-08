class Solution:
    def compress(self, chars) -> int:
        """
        ["a","a","b","b","c","c","c"]
        
        
        - Have two pointers, first and second, initialized to 0
        - Since we have to do this all IN PLACE, we need to keep track of the idx where we insert/update the char
          in the char array. Thats the idx_last_inserted
        - move second until we hit a different char.
        - when we do, we get the count of how many times we have seen the elem at index first: second - first.
        - if the diff > 1, we add the elem and the count to result array
        - if the diff > 9, we have to add each digit as an individual char in result array. 
        - then move first to second, and increment second by 1 and repeat
    
        """
        
        first = 0
        second = 0
        
        idx_last_inserted = 0
        while first < len(chars):
            # MISTAKE: We want to keep moving second untill we hit a new char. I mistakenly only moved it only
            # when matched.
            while second < len(chars) and chars[first] == chars[second]:
                second += 1
            
            # At this point second points to a diff char
            count = second - first
            idx_last_inserted +=1 # THIS WORKS BECAUSE IN LINE 63, WE OVERWRITE WITH A NUMBER WHEN COUNT > 1 
            chars[idx_last_inserted] = chars[first]
            if count > 1:
                for s in str(count):
                    chars[idx_last_inserted] = s
                    idx_last_inserted += 1
            first = second
        
        # MISTAKE: Need to return the length of the modified array.
        return idx_last_inserted