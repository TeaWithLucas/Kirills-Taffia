from classes import *

book_item = Item('Book', 'an old book', 'This is a very old looking book.')
gun_item = Item('Gun', 'a shiny gun', 'This is a very reliable weapon.')



char_narrator = Actor("Narrator")
example_guy = Actor("Mr Hodge Hodgeson")


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

stg_start = Stage('start', 'Main Menu', [{'speaker':char_narrator, 'dialog':(draw_ascii('welcome.txt') + '\n\n\n\n\n' + 'Welcome  Krill')}],  ['Start', 'Exit'])
stg_act1 = Stage('act1', 'Act1', [
	{'speaker':char_narrator, 'dialog':'Lorem ipsum dolor sit amet, sea ei ridens signiferumque, vel no graece altera viderer. Has diam nibh no. Pro in noster probatus eleifend, saepe graecis corpora quo ei. Debitis definitiones quo ad, tollit eirmod patrioque ad vim, dico dolore assentior ut mel. Vel epicurei intellegam ex. Cum probatus theophrastus an, per id tota virtute.'}, 
	{'speaker':example_guy, 'dialog':'Dico quando invidunt ei sit. Et bonorum delicata cum, per falli praesent explicari ea. Usu et tale error dissentiet, cum an laboramus aliquando repudiandae. Munere eloquentiam disputationi in vix. Tota salutandi rationibus eu pro, ius no persius menandri. Eam ut purto case instructior, decore periculis reprehendunt mei in, ea dicat cotidieque cum.'}, 
	{'speaker':char_narrator, 'dialog':'Indoctum ocurreret cu duo, propriae deseruisse philosophia in est. Nam id tale timeam alienum, purto elaboraret qui no. At vim ferri labitur ceteros, nam eu dictas recteque intellegebat. Vis ea amet sumo, pro ex tacimates repudiare consetetur, id eos legimus omittam referrentur. Ne sea ludus voluptaria rationibus. Ad oratio consulatu aliquando ius, duo legere probatus et.'}, 
	{'speaker':example_guy, 'dialog':'Nisl postulant ne eos. Ut eos vide dolor urbanitas, ipsum legere instructior no eam. Quo eu affert recusabo partiendo, his ne accusam probatus facilisi. Soleat forensibus definiebas ex vix.'}, 
	{'speaker':char_narrator, 'dialog':'Porro graeco semper ei quo, per iudico percipit ut. Exerci luptatum elaboraret mel ex, no sed debet commodo dolores. Erat liber tantas at vis. Ut possit prompta feugiat nec, summo interesset an his, debitis probatus convenire id vix. Nobis dissentiunt sed ei, cum at impetus viderer definiebas. Ius cu nominavi mediocrem, an mel iriure dolorum, et veritus inciderint ius. Ad case virtute eleifend est.'}, 
	{'speaker':example_guy, 'dialog':'Id eum dicunt ullamcorper, ne sea enim appareat. Omnium repudiare eu ius. Vero dicit sea te, mea ad iuvaret sensibus. Ex vis doming commodo theophrastus, prima civibus laboramus his cu. Ius ea soluta mollis erroribus, modus novum eu has.'}
	],  ['Attack', 'Attack'])
stg_main_menu = Stage('main menu', 'main menu', [{'speaker':example_guy, 'dialog':'Welcome  Krill'}], ['Start', 'Exit'])
stg_other_menu = Stage('other menu', 'other menu', [{'speaker':char_narrator, 'dialog':'Welcome  Krill'}],  ['Start', 'Exit'])
stg_new_game = Stage('new game', 'new game', [{'speaker':example_guy, 'dialog':'Welcome  Krill'}],  ['Start', 'Exit'])
stg_load_game = Stage('load game', 'load game', [{'speaker':char_narrator, 'dialog':'Welcome  Krill'}],  ['Start', 'Exit'])
stg_exit = Stage('exit', 'Exiting', [{'speaker':example_guy, 'dialog':'Welcome  Krill'}],  ['Start', 'Exit'])
stg_lost = Stage('lost', 'You Loose', [{'speaker':char_narrator, 'dialog':'You lost'}],  ['Start', 'Exit'])

stages = [stg_start, stg_main_menu, stg_other_menu, stg_new_game, stg_load_game, stg_exit]

item_names = []
#for item in global_game_items:
	#item_names.append(item.id)

directions = ['north', 'south', 'east', 'west']
action_cmds = ['move', 'take', 'drop']

keep_words = action_cmds + directions + item_names