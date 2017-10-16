
""" THIS IS THE MAIN GAME CLASS IT CONTAINS THE MAIN GAME LOOP AND LOGIC ASWELL AS MENU FUNCTIONS"""
from ASCII import *
from utilities import clear
import time
from player import Player
from levels import *

class Game():
    #constructor called on creation
    def __init__(self): 
        self.running = True
        self.title = 'The Game'
        self.game_levels = [level_reception]

    #run main loop
    def run_game(self):
        while self.running:
            self.main_menu()

    #displays the main menu of the game
    def main_menu(self):
        #Display
        clear()
        draw_anim_ascii('welcome.txt')
        print('\n \n \n \n')
        #print(self.title.upper() + '\n')
        print('                     Select:\n\n                      a.New Game\n                      b.Load Game\n                      c.Exit\n\n')

        #Take input
        inp = input('->')
        if inp == 'a':
            new_player = Player()
            self.new_game_menu(new_player)

        elif inp == 'b':
            pass
        elif inp == 'c':
            quit()
        else:
            clear()
            print('Enter a valid option')
            time.sleep(1)

    #Start a new game at the level of the new player
    def new_game_menu(self, player_obj):
        clear()
        print('Enter new character name:\n ')
        new_name = input('->')

        player_obj.name = new_name
        self.start_level(player_obj.level)

    #init the level
    def start_level(self, level_id):
        for level in self.game_levels:
            if level.id == level_id:
                level.start()



#######################################

main_game = Game()
main_game.run_game()
