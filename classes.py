from functions import *

""" These are the classes which are the structures for different objects in the game """

class Player():
	def __init__(self):
		self.name = ''
		self.health = 100
		self.inv = []
		self.level = 1

"""The room class. Rooms will for maps which will be assigned to levels. The rooms will determine the story. """

class Room():
	def __init__(self, name, des, exits, items):
		self.name = name
		self.description = des
		self.exits = exits
		self.items = items


""" The level class that is responsible for navigation on the map for that level """

class Level():
	def __init__(self, id, title, intro_text, current_room):
		self.id = id
		self.title = title
		self.intro_text = intro_text
		self.current_room = current_room

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



class Game():
	#constructor called on creation
	def __init__(self, level): 
		self.running = True
		self.title = 'The Game'
		self.game_levels = level

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
		print('					 Select:\n\n					  a.New Game\n					  b.Load Game\n					  c.Exit\n\n')

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
