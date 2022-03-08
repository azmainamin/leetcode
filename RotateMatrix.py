def rotateMatrix(matrix):
    left, right = 0, len(matrix) - 1

    while left < right:
        top, bottom = left, right # nxn matrix

        for i in range(right - left): # how ever many left in the middle
            # save top left to tmp
            tmp = matrix[top][left + i] # think of next item after 0, we go right

            # save bottom left to top left
            matrix[top][left + i] = matrix[bottom - i][left] # going up the col

            # save bottom right to bottom left
            matrix[bottom - i][left] = matrix[bottom][right - i]

            # save top right to bottom right
            matrix[bottom][right - i] = matrix[top + i][right]

            # save top right to bottom left
            matrix[top + i][right] = tmp
        
        left += 1
        right -= 1
    
    return matrix
