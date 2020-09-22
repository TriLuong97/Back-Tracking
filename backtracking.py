#Python implmenentation of the backtracking algorithm in Computer Science


#Example 1: The Knight Tour problem: 
# The knight is placed on the first block of an empty board and, moving according to the rules of chess, must visit each square exactly once.

#Naive approach: is to generate all tours one by one and check if the generated tours satisfies the constraints: 

#Backtracking approach: 
#If all squares are visited: print the solution

#Else: 
#1. Add one of the next moves to the solution vector and recursively check if this move leads to a solution. (A knight can make maximum eight moves. We choose one of the 8 moves in this step)
#2. If the move chosen in the above step doesn't lead to a solution then remove this move from the solution vector and try other alternative moves
#3. If none of the alternatives work then return the false (Returning fase will remove the previously added item in recursion and if false is returned by the initial call of recursion then "no solution exists")
##chessboard size
n = 8

def isSafe(x, y, board):
    '''
    A utility function to check if i, j are valid indexes for N*N chessboard
    '''
    if(x>=0 and y>=0 and x < n and y < n and board[x][y] == -1):
        return True

    return False

def printSolution(n, board):
    '''
        A utility function to print the chessboards matrix
    '''
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=' ')
        print()

def solveKT(n):
    '''
        This function solves the Knight Tour prblem using BackTracking.
        This function mainly uses solveKTUtil() to solve the problem. It returns 
        false if no complete tour is possible, otherwise, return true and prints the tour. 
    '''

    #Initialization of the board matrix: 
    board = [[-1 for i in range(n)]for i in range(n)]

    #move_x and move_y define the next move of the Knight
    #move_x is for the next value in the x coordinate
    #move_y is for the next value in the y coordinate
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]

    #Since the Knight is initially at the first block 
    board[0][0] = 0

    #Step counter for knight's position
    position = 1

    #Checking if the solution exist or not:
    if not solveKTUtil(n, board, 0, 0, move_x, move_y, position):
        print("Solution does not exist!")

    else:
        printSolution(n, board)

def solveKTUtil(n, board, curr_x, curr_y, move_x, move_y, position):
    '''
        A recursive utility function to solve Knight Tour problem
    '''

    if(position == n**2):
        return True

    #Try all next moves from the current coordinate x, y:
    for i in range(8):
        new_x = curr_x + move_x[i]
        new_y = curr_y + move_y[i]
        if(isSafe(new_x, new_y, board)):
            board[new_x][new_y] = position
            if(solveKTUtil(n, board, new_x, new_y, move_x, move_y, position+1)):
                return True

            #Backtracking: 
            board[new_x][new_y] = -1

    return False

# solveKT(n)



# Problem #2: N-queens problem: Given a chess board N x N cells, we need to place N queens in such a place that no queen is attacked at all 
#by any other queen. A queen can be attack horizontally, vertically, and diagonally. 
global N 
N = 4

#Helper method to draw out the board with queen being placed on it
def printBoardOut(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j])

#A utility function to check if a queen can 
# be placed on board[row][col]. Note that this 
# function is called when "col" queens are 
# already placed in columns from 0 to col - 1. 
# So we need to check only the left side of the attacking queens
def isSafe(board, row, col):

    #Check on this row on the left side
    for i in range(col):
        if(board[row][i] == 1):
            return False

    #check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    #Check lower diagonal on the left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

#helper method to solve the problem
def solveNQUtil(board, col):
    #base case: If all queens are placed then return true
    if col >= N:
        return True

    #Consider this column and try placing 
    #this queen in all rows one by one
    for i in range(N):

        if isSafe(board, i, col):
            #place this queen in the board[i][col]
            board[i][col] = 1

            #recur to place rest of the queens: 
            if solveNQUtil(board, col + 1) == True:
                return True

            #if placing queen in boards[i][col]
            # doesnt lead to a solution, then check queen in the 
            board[i][col] = 0

    #if the queen cannot be placed in any row
    # in this col then return false

    return False


def solveNQ():
    board = [[0,0,0,0],
             [0,0,0,0],
             [0,0,0,0],
             [0,0,0,0]]

    if solveNQUtil(board, 0) == False:
        print ("Solution does not exist")


    printBoardOut(board)

    return True

# solveNQ()

#Problem 3: Leetcode 79: Word Search
#Problem statement:
'''
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.

'''

#we will approach this problem with a dfs approach
def exist(board, word):
    #base case: 
    if not board: 
        return False

    if not word: 
        return False
    #getting the dimension of the board
    m = len(board)
    n = len(board[0])

    #create a visited arrat to keep track of the visited neighbors of a node
    visited = [[False for i in range(0, m)] for j in range(0, n)]

    for i in range(m):
        for j in range(n):
            if dfs(i, j, word, visited, board):
                return True
    return False
        

#create a helper method to handle dfs alogrithm:
def dfs(i,j, word, visited, board):
    #getting the dimension of the board
    m = len(board)
    n = len(board[0])

    #Any element being checked in this function will
    #automatically get put into the visited array right on the spot
    visited[i][j] == True
    #Base case: 
    if not word: 
        return False
    
    if not (0 <= i < m and 0<=j<n):
        return False
    #if the current element in the board is not anywhere
    #in the word list, then return false
    if board[i][j] != word[0]:
        return False
    #checking the neighboring node to see if they are already in
    #visited array or not
    if not visited[i][j+1] or not visited[i][j-1] or not visited[i+1][j] or not visited[i-1][j]:
        result = dfs(i, j+1, word[1:], visited, board) or dfs(i, j-1, word[1:], visited, board) or dfs(i+1, j, word[1:], visited, board) or dfs(i-1, j, word[1:], visited, board)

    return result


#driver code: 
test_board =[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

test_word = "ABCCED"

# print(exist(test_board, test_word))

#backtracking problem: #77. Combination
#Problem statement: 
'''
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

You may return the answer in any order.
Example 1:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
Example 2:

Input: n = 1, k = 1
Output: [[1]]
 

Constraints:

1 <= n <= 20
1 <= k <= n
'''
def combine(n, k):
    #base case: 
    if not n or not k: 
        return None
    
    res = []

    dfs([], 0, res, n, k)
    return res

#DFS method to construct the combination array from the list
def dfs(searchArray, index, result, n, k):
    #base case: 
    if len(searchArray) == k:
        result.append(searchArray)
        return 

    for i in range(index + 1, n +1):
        dfs(searchArray + [i], i, result, n, k)

    
#helper method to find the 



#driver code: 
num = 4
k = 2

print(combine(num, k))

