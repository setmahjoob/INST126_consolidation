import random

# Function: Roll three dice
def roll_dice():
   """
   Rolls three dice and returns the results as a list of integers.
  
   Returns:
       list: A list of three integers representing dice rolls.
   """
   return [random.randint(1, 6) for _ in range(3)]

# Function: Check if a roll results in "tuple out"
def is_tuple_out(dice):
   """
   Checks if all three dice have the same value.
  
   Args:
       dice (list): A list of three integers representing dice rolls.
  
   Returns:
       bool: True if all dice are the same, False otherwise.
   """
   return dice[0] == dice[1] == dice[2]

# Function: Play a single turn for a player
def play_turn(player_name):
   """
   Simulates a player's turn in the game. Rolls dice and allows re-rolls based on game rules.
  
   Args:
       player_name (str): The name of the player taking the turn.
  
   Returns:
       int: The score for the player's turn.
   """
   print(f"\n{player_name}'s turn!")
   dice = roll_dice()
   print(f"Initial roll: {dice}")
  
   if is_tuple_out(dice):
       print("Tuple out! No points for this turn.")
       return 0

   fixed_dice = [d for d in dice if dice.count(d) > 1]
   print(f"Fixed dice: {fixed_dice}")

   while True:
       # Identify which dice can be re-rolled
       reroll_indices = [i for i, d in enumerate(dice) if dice.count(d) == 1]
       if not reroll_indices:
           break
      
       # Ask if the player wants to re-roll
       reroll_choice = input("Re-roll unfixed dice? (y/n): ").strip().lower()
       if reroll_choice != 'y':
           break
      
       # Re-roll only the unfixed dice
       for i in reroll_indices:
           dice[i] = random.randint(1, 6)
       print(f"Re-rolled dice: {dice}")
      
       if is_tuple_out(dice):
           print("Tuple out! No points for this turn.")
           return 0

   score = sum(dice)
   print(f"{player_name} scores {score} points.")
   return score

# Function: Main gameplay loop
def play_game():
   """
   Manages the overall gameplay loop for the Tuple Out Dice Game. Keeps track of scores and determines the winner.
   """
   print("Welcome to the Tuple Out Dice Game!")
   print("The first player to reach 50 points wins!\n")
  
   # Setup
   players = ["Player 1", "Player 2"]
   scores = {player: 0 for player in players}
   max_score = 50

   # Game loop
   while max(scores.values()) < max_score:
       for player in players:
           scores[player] += play_turn(player)
           print(f"Current scores: {scores}")
           if scores[player] >= max_score:
               break
  
   # Determine winner
   winner = max(scores, key=scores.get)
   print(f"\nGame over! {winner} wins with {scores[winner]} points!")

# Function: Run the game
def run():
   """
   The entry point for running the Tuple Out Dice Game.
   """
   play_game()

# Call to run the game
run()