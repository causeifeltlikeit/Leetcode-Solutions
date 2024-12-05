class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        spiral = []
        x = 0
        y = 0
        left = 0
        top = 0
        right = len(matrix[0]) - 1
        bottom = len(matrix) - 1
        direction = 0
        spiral.append(matrix[y][x])
        while True:
            if direction == 0:
                if x == right:
                    x = x - 1
                    y = y + 1
                    direction = 1
                    top = top + 1
                x = x + 1
                
            elif direction == 1:
                if y == bottom:
                    y = y - 1
                    x = x - 1
                    direction = 2
                    right = right - 1
                y = y + 1
                
            elif direction == 2:
                if x <= left:
                    x = x + 1
                    y = y - 1
                    direction = 3
                    bottom = bottom - 1
                x = x - 1
                
            elif direction == 3:
                if y <= top:
                    y = y + 1
                    x = x + 1
                    direction =  0
                    left = left + 1
                y = y - 1
                
            if (left > right) or (top > bottom):
                break
            spiral.append(matrix[y][x])
        return spiral