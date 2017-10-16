"""The room class. Rooms will for maps which will be assigned to levels. The rooms will determine the story. """

class Room():
    def __init__(self, name, des, exits, items):
        self.name = name
        self.description = des
        self.exits = exits
        self.items = items

##########################################
#Create the rooms
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
