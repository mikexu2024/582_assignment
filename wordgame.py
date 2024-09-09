#We will use two threads in this game. One thread is countdown() function
#which is used to countdown 15 seconds. The other thread is user_input()
#function which is used to input words. 

import threading
import time
import random

class WordGame:
    word_list = {
        'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'R': 1,
        'S': 1, 'T': 1, 'D': 2, 'G': 2, 'B': 3, 'C': 3, 'M': 3, 'P': 3,
        'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4, 'K': 5, 'J': 8, 'X': 8,
        'Q': 10, 'Z': 10,
    }

    def __init__(self, rounds=10, countdown_time=15):
        self.total_score = 0  
        self.rounds_played = 0  # Number of rounds have already played
        self.rounds = rounds  # Total rounds
        self.countdown_time = countdown_time  # seconds of countdown 
        self.stop_event = threading.Event()  # Thread event to stop user's input
        self.countdown_finished = threading.Event()  # Thread event to finish countdown
        self.quit_game = False  # Flag of quiting the game

    def countdown(self, seconds):
        print(f"Countdown Start! There are total {seconds} seconds left.")
        while seconds > 0:  #continue countdown until seconds<0
            if self.stop_event.is_set():  #To stop countdown
                print("Countdown stopped!", end='')
                return                    
            print(f"\rThere are {seconds} seconds left", end='')
            time.sleep(1)
            seconds -= 1
        print("Countdown over! Press Enter to next round!")
        self.countdown_finished.set()  # To indicate that countdown finish

    def calculate_score(self, word): # Calculate the score of a given word
        #for loop to get and sum the score of each letter from word_list and get word score
        return sum(self.word_list.get(letter, 0) for letter in word) 
         

    def user_input(self):  #To enter words from the keyboard
        n = random.randint(1, 10) # n is the certain length of words users should enter
        print(f"\nRound {self.rounds_played + 1}: Please enter a word with {n} letters:\n")

        self.stop_event.clear()  # Clear the stop event for each round
        self.countdown_finished.clear()  # Clear the countdown finished event

        countdown_thread = threading.Thread(target=self.countdown, args=(self.countdown_time,)) #create countdown thread
        countdown_thread.start()  #start countdown thread

        user_input_word = ''
        while not self.countdown_finished.is_set():
            user_input_word = input(f"Enter a word with exactly {n} letters or type 'quit' to end the game: ").upper()
            if user_input_word == 'QUIT': #user enter quit from keyboard, game will stop.
                self.stop_event.set()
                self.quit_game = True  # Set the quit flag to True
                return  # Exit the round
            if len(user_input_word) == n and user_input_word.isalpha(): 
                #user enter the word that meets the long and is english letter in wordlist.
                self.stop_event.set()  #the countdown stop
                break
            else:
                print(f"Invalid input. Please enter a word with {n} letters.")
        
        if not self.quit_game:
            score = self.calculate_score(user_input_word) # Calculate the score
            self.total_score += score
            print(f"You entered: {user_input_word}, and the score for this round is: {score}. Total score: {self.total_score}")
            print("-"*80)
    def start_game(self):
        # start game
        while self.rounds_played < self.rounds and not self.quit_game:
            self.user_input()  # Handle user input for the current round
            if self.quit_game:
                break  # Exit the game loop if the user quits
            self.rounds_played += 1 # round increase by 1 to next round 
            print(f"\nMoving to next round...")
            print("---------------------------------------")

        print(f"Game over! Your total score is: {self.total_score}")


if __name__ == "__main__":
    game = WordGame(rounds=10, countdown_time=15)
    game.start_game()
