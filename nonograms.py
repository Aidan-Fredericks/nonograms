#nonagram puzzle by ALEX AIDAN ROHAN 
import random

class Generator:


  def __init__(self, size = 5):
    self.size = size
    self.solution = [['⬛', '⬛', '⬛', '⬜', '⬛'], ['⬛', '⬛', '⬜', '⬜', '⬛'], ['⬜', '⬜', '⬜', '⬛', '⬜'], ['⬜', '⬜', '⬛', '⬛', '⬜'], ['⬜', '⬛', '⬛', '⬛', '⬜']]
    self.rules = [['3 1', '2 1', '1', '2', '3', '2', '2 1', '1 2', '3', '2']]

  def generate_solution(self,size=5):
    self.size = 5
    board = [['⬜']*size for x in range(size)]
    count = 0
    while count <= 13:
      for r in range(len(board)):
        for c in range(len(board)):
          if random.randint(0,100) > 50:
            board[c]="⬛"
            count +=1
    self.solution = board

  def generate_rules(self):
    rules = []
    for r in range(len(self.solution)):
      count = 0
      for c in range(len(self.solution)):
        if self.board[r][c] == "⬛":
          count += 1
      rules.append(count)
    for c in range(len(self.solution)):
      count = 0
      for r in range(len(self.solution)):
        if self.board[c][r] == "⬛":
          count += 1
        rules.append(count)
    return rules

  def check(self, game_board):
    for r in range(len(game_board)):
      for c in range(len(game_board[0])):
        if game_board[r][c] != self.solution[r][c]:
          return False
    return True
    
class GameBoard:
  # make a board with size and rules for each row and column. order is r5 -> r1, then c1 -> c5 (down then across)
  def __init__(self, size = 5, rules = ['3 1', '2 1', '1', '2', '3', '2', '2 1', '1 2', '3', '2']):
    #creating blank square board
    self.size = size
    self.board = [['⬜']*size for x in range(size)]

    #creating valid rows and columns according to size
    rows = ['r' + str(i+1) for i in range(size)]
    row_values = rules[:size]
    col = ['c' + str(i+1) for i in range(size)]
    col_values = rules[size:]

    # make sure there are rules for every row and column and no extra
    if len(row_values) != size or len(col_values) != size:
      raise Exception('Rules don\'t match board size!')
      
    # creating the dictionaries for columns and rows and their respective rules
    self.rows = {r:v for (r,v) in zip(rows, row_values)} 
    self.col = {c:v for (c,v) in zip(col, col_values)} 

    # self.rules = {'r1':'3 1','r2':'2 1','r3':'1','r4':'2','r5':'3','c1':'2','c2':'2 1','c3':'1 2','c4':'3','c5':'2'}

  def show(self):
    for row in range(self.size):
      for char in self.board[row]:
        print(char, end = '') # place things adjacent to each other
      print(f' {self.rows["r" + str(row+1)]}') # place respective rule

    # print column rules
    # still doesnt support more than two rules in a column
    column_rules = []
    for col in range(self.size):
      rule = self.col['c' + str(col + 1)]
      print(rule[0], end = ' ') # print first part of the rule
      if len(rule) > 1: # if the rule has more than one number, add the rest to the column_rules list to prepare the second row of column rules
        column_rules.append(rule[2:])
      else: # fill empty spaces with spaces for formatting
        column_rules.append(' ')
    print()
    print(*column_rules)

  # click functions, pretty self explanatory
  def lclick(self, col, row):
    if self.board[row-1][col-1] != '⬜':
      self.board[row-1][col-1] = '⬜'
    else:
      self.board[row-1][col-1] = '⬛'
    self.show()

  def xclick(self, col, row):
    self.board[row-1][col-1] = '❌'
    self.show()

  def clear(self):
    for i in self.board:
      for j in range(len(self.board)):
        i[j] = '⬜'
    self.show()

  def test(self):
    print(self.board)
# testing the game, not final
gameEnd = False

myboard = GameBoard()
print('here is your puzzle !!!!!!')
myboard.show()
print('Type f (for fill) or x (for crossout), followed by x and y coordinates\nTop left coordinate is 11\n You can also use f on a black square to make it white (ex. f12)\n Type d when done\n Type c to clear the board\n')

# Creates the solution to the board, currently just the preloaded one
solution = Generator()
#solution.generate_solution() !!! Don't uncomment this and next line unless not using preloaded
#solution.generate_rules()

while not gameEnd:
  click = input()
  if click in ('C','c'):
    myboard.clear()
  elif click[0] in ('d'):
    if solution.check(myboard.board):
      print("you win!!!")
      exit()
    else:
       print("not right")
  elif len(click) != 3 or click[0] not in ('f','F','x','X','d'):
    print('input should be 3 characters!')
  elif int(click[1]) > myboard.size or int(click[2]) > myboard.size:
    print('coordinates must be on the grid!')
  elif click[0] in ('f','F'):
    myboard.lclick(int(click[1]),int(click[-1]))
  elif click[0] in ('x','X'):
    myboard.xclick(int(click[1]),int(click[-1]))
  

#⬛⬜❌
# solution to preload below (use for testing purposes)
#11, 21, 31, 51
#12, 22, 52
#43
#34, 44
#25, 35, 45
