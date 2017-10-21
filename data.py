from classes import *

#Items
book_item = Item('Book', 'an old book', 'This is a very old looking book.')
gun_item = Item('Gun', 'a shiny gun', 'This is a very reliable weapon.')

#Characters
char_narrator = Actor('narrator_tag', 'yellow', "Narrator")
example_guy = Actor('sec_char_tag','orange','Mr Hodge Hodgeson')

#Locations
menu = Location('','',[])
flat_loc = Location('Flat', 'You arrive back at your flat, the kitchen is a mess, empty dominoes boxes everywhere. Your laptop is on the counter. You realise that this space would be an ideal place to start making your own drugs. ', [book_item, gun_item])



#Stages
stg_start = Stage(menu,'start', 'Main Menu', [{'speaker':char_narrator, 'dialog':(draw_ascii('welcome.txt') + '\n\n\n\n\n' + 'Welcome  Krill')}],  {'start': 'act1', 'exit':'start'})
stg_act1 = Stage(flat_loc,'act1', 'Act1', [
	{'speaker':char_narrator, 'dialog':''},
	{'speaker':example_guy, 'dialog':'Dico quando invidunt ei sit. Et bonorum delicata cum, per falli praesent explicari ea. Usu et tale error dissentiet, cum an laboramus aliquando repudiandae. Munere eloquentiam disputationi in vix. Tota salutandi rationibus eu pro, ius no persius menandri. Eam ut purto case instructior, decore periculis reprehendunt mei in, ea dicat cotidieque cum.'},
	{'speaker':char_narrator, 'dialog':'Indoctum ocurreret cu duo, propriae deseruisse philosophia in est. Nam id tale timeam alienum, purto elaboraret qui no. At vim ferri labitur ceteros, nam eu dictas recteque intellegebat. Vis ea amet sumo, pro ex tacimates repudiare consetetur, id eos legimus omittam referrentur. Ne sea ludus voluptaria rationibus. Ad oratio consulatu aliquando ius, duo legere probatus et.'},
	{'speaker':example_guy, 'dialog':'Nisl postulant ne eos. Ut eos vide dolor urbanitas, ipsum legere instructior no eam. Quo eu affert recusabo partiendo, his ne accusam probatus facilisi. Soleat forensibus definiebas ex vix.'},
	{'speaker':char_narrator, 'dialog':'Porro graeco semper ei quo, per iudico percipit ut. Exerci luptatum elaboraret mel ex, no sed debet commodo dolores. Erat liber tantas at vis. Ut possit prompta feugiat nec, summo interesset an his, debitis probatus convenire id vix. Nobis dissentiunt sed ei, cum at impetus viderer definiebas. Ius cu nominavi mediocrem, an mel iriure dolorum, et veritus inciderint ius. Ad case virtute eleifend est.'},
	{'speaker':example_guy, 'dialog':'Id eum dicunt ullamcorper, ne sea enim appareat. Omnium repudiare eu ius. Vero dicit sea te, mea ad iuvaret sensibus. Ex vis doming commodo theophrastus, prima civibus laboramus his cu. Ius ea soluta mollis erroribus, modus novum eu has.'}
	],  {'yes': 'start', 'no': 'lost'})
#stg_main_menu = Stage('main menu', 'main menu', [{'speaker':example_guy, 'dialog':'Welcome  Krill'}], ['Start', 'Exit'])
#stg_other_menu = Stage('other menu', 'other menu', [{'speaker':char_narrator, 'dialog':'Welcome  Krill'}],  ['Start', 'Exit'])
#stg_new_game = Stage('new game', 'new game', [{'speaker':example_guy, 'dialog':'Welcome  Krill'}],  ['Start', 'Exit'])
#stg_load_game = Stage('load game', 'load game', [{'speaker':char_narrator, 'dialog':'Welcome  Krill'}],  ['Start', 'Exit'])
#stg_exit = Stage('exit', 'Exiting', [{'speaker':example_guy, 'dialog':'Bye'}],  [])
stg_lost = Stage(menu,'lost', 'You Loose', [{'speaker':char_narrator, 'dialog':'You lost'}],  ['Start', 'Exit'])

stages = {
	'start': stg_start,
	'act1' : stg_act1,
	'lost' : stg_lost
}




item_names = []
#for item in global_game_items:
	#item_names.append(item.id)

directions = ['north', 'south', 'east', 'west']
action_cmds = ['move', 'take', 'drop']

keep_words = action_cmds + directions + item_names
