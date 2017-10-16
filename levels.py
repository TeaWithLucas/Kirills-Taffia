""" The level class that is responsible for navigation on the map for that level """

from utilities import clear
from map import *

from ASCII import draw_ascii
class Level():
    def __init__(self, id, title):
        self.id = id
        self.title = title
        self.intro_text = 'This level is about the uni'
        self.current_room = room_reception

    def start(self):
        clear()
        #print(self.intro_text)
        #print_level()
        draw_ascii('map.txt')
        #print('\n\n\n\n Press ENTER to continue...')
        a = input()
        self.level_main()

    def show_room(self, room):
        clear()
        print('\n' + room.name.upper() + '\n')
        print(room.description + '\n')


    def exit_leads_to(self, exits, direction):

        return rooms[exits[direction]].name

    def print_line(self, direction, leads_to):

        print('Go ' + direction.upper() + ' to ' + leads_to + '.')

    def display_exits(self, exits):
        print('Select action:')
        for exit in exits:
            self.print_line(exit, self.exit_leads_to(exits, exit))

    def exit_selection(self,exits):
        while True:

            #display the options
            self.display_exits(exits)
            #get input
            ans = input()
            #normalise input

            #validate input

            return ans

    def move_player(self, exits, direction):

        return rooms[exits[direction]]

    #the level loop
    def level_main(self):
        while True:

            #Display current situation
            self.show_room(self.current_room)
            #Get exits
            exits = self.current_room.exits
            #Let player select exit
            direction = self.exit_selection(exits)
            #move the player
            self.current_room = self.move_player(exits, direction)




########################################
level_reception = Level(1, 'uni')
