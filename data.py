from classes import *
from functions import *

book_item = Item('Book', 'an old book', 'This is a very old looking book.')
gun_item = Item('Gun', 'a shiny gun', 'This is a very reliable weapon.')

inventory = [book_item, gun_item]


#Create the room
none = Room('', '', '', '')
room_hall = Room('Hall', 'You enter a long hall with various portraits on the walls.', {'north' : 'Reception'}, ['notebook'] )
room_reception = Room('Reception', 'You enter the main reception of the building. The room is empty.', {'south': 'Hall', 'west':'Cafe', 'north': 'Class', 'east':'Office'},[])
room_office = Room('Office', 'You step into a well iluminated office with a paintig of a snowy landscape on the wall.',{'west' : 'Reception'}, ['notebook'] )
room_cafe = Room('Cafe', 'Before you is a busy cafe. The barista is strugling to keep up with the work load and looks at you desperately as you walk in.', {'east' : 'Reception'}, ['notebook'] )
room_class = Room('Class', 'You enter an empty class room. On the black board you notice a complicated equation.', {'south' : 'Reception'}, ['notebook'] )
#room dictionary for navigation

rooms = {
	'Reception' : room_reception,
	'Hall' : room_hall,
	'Office': room_office,
	'Cafe': room_cafe,
	'Class': room_class
}


level_reception = Level(1, 'uni', 'This level is about the uni', rooms['Reception'])

stg_start = Stage('start', 'Main Menu', [draw_ascii('welcome.txt') + '\n\n\n\n\n' + 'Welcome  Krill'],  ['Start', 'Exit'])
stg_act1 = Stage('act1', 'Act1', ['You slowly come to your sences.', 'There are voices outside of your office and it looks like you have fallen asleep while working.', 'Welcome  Krill', 'where is my cat', 'Welcome  Krill', 'where is my cat'],  ['Attack', 'Attack'])
stg_main_menu = Stage('main menu', 'main menu', ['Welcome  Krill'], ['Start', 'Exit'])
stg_other_menu = Stage('other menu', 'other menu', ['Welcome  Krill'],  ['Start', 'Exit'])
stg_new_game = Stage('new game', 'new game', ['Welcome  Krill'],  ['Start', 'Exit'])
stg_load_game = Stage('load game', 'load game', ['Welcome  Krill'],  ['Start', 'Exit'])
stg_exit = Stage('exit', 'Exiting', ['Welcome  Krill'],  ['Start', 'Exit'])
stg_lost = Stage('lost', 'You Loose', ['You lost'],  ['Start', 'Exit'])

stages = [stg_start, stg_main_menu, stg_other_menu, stg_new_game, stg_load_game, stg_exit]
