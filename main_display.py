from tkinter import*

#TK root window
root = Tk ()

#Backround image
image = PhotoImage(file = "bg.png")
background_label = Label(root, image=image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

#Input console
console = Text(root, bg = 'black', fg = 'white', height = 1, insertbackground = 'white')
console.insert(END, '->')

#The map
map_label = Label(root,text = 'MAP',  bg = '#3a3f2d', fg = 'white', width = 20 )

#Inventory display console
inv_txt = Text(root, bg = '#262820',fg = 'white', width = 23, height = 15)

#Stats display console
stats_txt = Text(root, bg = '#3a3f2d', fg = 'white', width = 22, height = 10)

#Output console
out_console = Text(root, bg = 'black', fg = 'white')

#Choice console
choice_console = Text(root, bg = 'black', fg = 'white', height = 10)

#Display and layout of all components
console.grid(row = 4, column = 1, columnspan = 3)
map_label.grid(row = 1, column = 1)
inv_txt.grid(row = 1, column = 3, rowspan = 2)
stats_txt.grid(row = 2, column = 1)
out_console.grid(row = 1, column = 2, rowspan = 2)
choice_console.grid(row = 3, column = 1, columnspan = 3)

#The main loop
root.mainloop()
