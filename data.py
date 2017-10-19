from classes import *
from functions import *

book_item = Item('Book', 'an old book', 'This is a very old looking book.')
gun_item = Item('Gun', 'a shiny gun', 'This is a very reliable weapon.')
player = Actor()
player.inv.append(book_item)
player.inv.append(gun_item)


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

stg_start = Stage('start')
stg_main_menu = Stage('main menu')
stg_other_menu = Stage('other menu')
stg_new_game = Stage('new game')
stg_load_game = Stage('load game')
stg_exit = Stage('exit')

stages = [stg_start, stg_main_menu, stg_other_menu, stg_new_game, stg_load_game, stg_exit]