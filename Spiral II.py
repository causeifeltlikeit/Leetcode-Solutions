
n=3
matrix = [[None for _ in range(n)] for _ in range(n)]
x = 0
y = 0
left = 0
top = 0
right = n - 1
bottom = n - 1
direction = 0
index = 1
matrix[y][x] = index
index = index +1
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
    matrix[y][x] = index
    index =index +1
print(matrix)