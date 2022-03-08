class Solution:
    def spiralOrder(self, matrix):
        """
        Layer by layer
        00, 01,02,12,22,21,20,10,11
        
        How do i find how many layers?
        
        Keep track of first_row, last_row, first_col, last_col.
        Initialization:
            first_row = 0
            last_row = matrix.length
            first_col = 0
            last_col = matrix[i].length
        
        Iterate in pairs: first_row + last_col, last_row + first_col.
        As we create our list, keep track of idxs that we have visited, so we before adding to result, we check if its already visited
        Once a pair iteration has completed, update each for the four pointers: first++, last--
        """
        rows = len(matrix)
        cols = len(matrix[0])
        
        first_row = 0
        last_row = rows - 1 #do i need -1
        
        first_col = 0
        last_col = cols - 1 # do i need -1
        
        result = []
        visited = set()
        
        while first_row <= last_row and first_col <= last_col:
            # first_row + last_col
            ## first_row
            for i in range(last_col):
                if (first_row, i) not in visited: 
                    result.append(matrix[first_row][i])
                    visited.add((first_row, i))
            ## last col
            for i in range(last_row):
                if (i, last_col) not in visited: 
                    result.append(matrix[i][last_col])
                    visited.add((i, last_col))


            ## last row + first col
            ## we need to iterate from last to first in these iterations

            ## last row is fixed. but cols need to be back to front
            for i in range(last_col,-1,-1):
                if (last_row, i) not in visited: 
                    result.append(matrix[last_row][i])
                    visited.add((last_row, i))

            ## first col is fixed. but rows need to be back to front
            for i in range(last_row,-1,-1):
                if (i, first_col) not in visited: 
                    result.append(matrix[i][first_col])
                    visited.add((i, first_col))

            first_row +=1
            last_row -= 1

            first_col += 1
            last_col -= 1
            
        return result
        