
'''
Tic-Tac-Toe: First Game
Author: Josiah Madondo
'''

#For resetting and updating the screen and the board after each player has played
import os

def main():
  # Declare all the variables we'll need
  pos = {1 : '1', 2 : '2', 3: '3', 4 : '4', 5 : '5', 
          6 : '6', 7 : '7',  8 : '8', 9 : '9'}
  playing, complete = True, False
  turn = 0
  prev_turn = -1

 #Game Loop
  while playing:
      # Reset the screen
      os.system('cls' if os.name == 'nt' else 'clear')

      # Draw the current Game Board
      draw_board(pos)
      print()

      # If an invalid turn occurred, let the player know
      if prev_turn == turn:
        print("Invalid spot selected, please pick another.")
      prev_turn = turn
      print("Player " + str((turn % 2) +1 ) + "'s turn: Pick your spot or press q to quit")
      print()

      # Get input and make sure it's valid
      choice = input()
      print()

      # The game has ended, 
      if choice == 'q':
          playing = False
      elif str.isdigit(choice) and int(choice) in pos:
        # Check if the spot is already taken.
        if not pos[int(choice)] in {"X", "O"}:
          # If not, update board and increment the turn
          turn += 1
          pos[int(choice)] = check_turn(turn)
        
      # Check if the game has ended (and if someone won)
      if check_for_win(dict, pos): playing, complete = False, True
      if turn > 8: playing = False
      
  # Update the board one last time. 
  os.system('cls' if os.name == 'nt' else 'clear')
  print()

  draw_board(pos)
  print()

  # If there was a winner, say who won
  if complete:
    if check_turn(turn) == 'X': print("Player 1 Wins!")
    else: print("Player 2 Wins!")
  else: 
    # Tie Game
    print("Game tied. No Winner")
    
  print("Thanks for playing!") 
  print()

#Function to draw the board.
def draw_board(pos):
  board = (f"|{pos[1]}|{pos[2]}|{pos[3]}|\n"
             f"|{pos[4]}|{pos[5]}|{pos[6]}|\n"
             f"|{pos[7]}|{pos[8]}|{pos[9]}|")
  print(board)


#Function to check whose turn to play
def check_turn(turn):
  if turn % 2 == 0: return 'O'
  else: return 'X'


#Function to check for a winner
def check_for_win(dict, pos):

  # Handle Horizontal Cases
  if   (pos[1] == pos[2] == pos[3]) \
    or (pos[4] == pos[5] == pos[6]) \
    or (pos[7] == pos[8] == pos[9]):
    return True

  # Handle Vertical Cases
  elif (pos[1] == pos[4] == pos[7]) \
    or (pos[2] == pos[5] == pos[8]) \
    or (pos[3] == pos[6] == pos[9]):
    return True

  # Diagonal Cases
  elif (pos[1] == pos[5] == pos[9]) \
    or (pos[3] == pos[5] == pos[7]):
    return True
    
  else: return False

if __name__ == "__main__":
    main()