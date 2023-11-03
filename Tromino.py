from operator import truediv
import random
import time

n = 8
L = [] # list of trominoes
def create(n):
    M = []
    for i in range (n):
        temp = []
        for j in range (n):
            temp.append(0)
        M.append(temp)
    r = random.randint(0, n-1)
    c = random.randint(0, n-1)
    M[r][c] = -1
    return M

A = create(n)

def place(x1, y1, x2, y2, x3, y3):
    """
    Records the given Tromino's placement via coordinates in the master list L
    And fills in the taken spots in the grid A
    """
    T = tuple(((x1, y1),(x2, y2), (x3, y3)))
    L.append(T)
    n = len(L)
    A[x1][y1] = n
    A[x2][y2] = n
    A[x3][y3] = n
    
def Tromino(x_start, y_start, x_end, y_end):
    '''
    x_start is the row starting value, x_end row ending val
    Recursively splits given grid into 4 sections, finding an empty spot to place the Tromino
    '''
    if x_start >= x_end or y_start >= y_end:
        return A
    if x_end-x_start == 2:
        midTromino(x_start, y_start, x_end, y_end)
    else:
        midTromino(x_start, y_start, x_end, y_end)
        Tromino(x_start, y_start, (x_start+x_end)//2, (y_start+y_end)//2)
        Tromino(x_start, ((y_start+y_end)//2)+1, (x_start+x_end)//2, y_end)
        Tromino(((x_start+x_end)//2)+1, y_start, x_end, (y_start+y_end)//2)
        Tromino(((x_start+x_end)//2)+1, ((y_start+y_end)//2)+1, x_end, y_end)

def midTromino(x_start, y_start, x_end, y_end):
    """
    Takes a starting row position, b ending row; i starting column position, j ending column
    Calculates where Tromino should go and places it
    """
    # 4 middle positions
    TopLeft = (x_start+x_end)//2, (y_start+y_end)//2
    TopRight = ((x_start+x_end)//2), ((y_start+y_end)//2) +1
    LowLeft = ((x_start+x_end)//2) + 1, (y_start+y_end)//2
    LowRight = ((x_start+x_end)//2) + 1, ((y_start+y_end)//2) + 1
    r, c = 0, 0
    for k in range (x_start,x_end+1):
        for l in range (y_start,y_end+1):
            if A[k][l] != 0:
                r = k
                c = l
                break
    if r <= (x_start+x_end)//2 and c <= (y_start+y_end)//2:
        place(TopRight[0], TopRight[1], LowRight[0], LowRight[1], LowLeft[0], LowLeft[1])
        return 
    elif r <= (x_start+x_end)//2 and c > (y_start+y_end)//2:
        place(TopLeft[0], TopLeft[1], LowLeft[0], LowLeft[1], LowRight[0], LowRight[1])
        return
    elif r > (x_start+x_end)//2 and c <= (y_start+y_end)//2:
        place(TopLeft[0], TopLeft[1], TopRight[0], TopRight[1], LowRight[0], LowRight[1])
        return
    else:
        place(TopLeft[0], TopLeft[1], TopRight[0], TopRight[1], LowLeft[0], LowLeft[1])
        return

start = time.time()
Tromino(0,0,n-1,n-1)
end = time.time()
print(end - start)

# printing the final grid
print ("Final Grid!")
for i in range(len(A)) :
    for j in range (len(A)):
        print (A[i][j], end='   ')
    print ()

# printing the trominos
print ("Coordinates of Trominos", L)