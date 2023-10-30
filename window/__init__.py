import tkinter as tk
from .widgets import icons

class screen(tk.Tk):
    # Define class attributes
    height = 300
    width = 300
    primary = "#37373b"
    secondary = "white"
    faded = "white"
    length = 0

    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.geometry(f"{self.width}x{self.height}")
        self.canv = tk.Canvas(self, bg=self.primary, borderwidth=0, highlightthickness=1, width=self.width,
        	height=self.height, highlightbackground="black")
        self.canv.pack()

    def settitle(self, title="My App1"):
        self.title(title)

    def setgeometry(self, width=width, height=height):
        self.width = width
        self.height = height
        self.geometry(f"{self.width}x{self.height}")
        self.canv.config(width=self.width, height=self.height)

    def setmode(self, mode="dark"):
        if mode.lower() ==  "light":
            self.primary = "lightgray"
            self.secondary = "#37373b"
            self.faded = "gray"

        elif mode.lower() == "dark":
            self.primary = "#37373b"
            self.secondary = "white"
            self.faded = "white"

        self.canv.config(bg=self.primary)


    #------------------------------------Create Widgets-----------------------------------------

    def create_label(self,
    	text="Fake Label",
    	font="Lato",
    	size="10",
    	ttype="bold",
    	color=None,
    	background=None,
    	x=None,
    	y=None,
    	top=50,
    	bottom=0):

    	self.length += top
    	x = x or self.width/2
    	y = y or self.length
    	color = color or self.secondary
    	background = background or self.primary
    	label = tk.Label(self.canv, text=text, font=f"{font} {size} {ttype}", fg=color, bg=background)
    	self.canv.create_window(x,y, window=label)
    	self.length += bottom
    	return label

    def create_button(self,
    	text = "Fake Button",
    	font="Lato",
    	size="10",
    	ttype="bold",
    	color=None,
    	background=None,
    	x=None,
    	y=None,
    	on_click=None,
    	padx=0,
    	pady=0,
    	top=50,
    	bottom=0):

    	self.length += top
    	x = x or self.width/2
    	y = y or self.length
    	color = color or self.primary
    	background = background or self.secondary
    	button = tk.Button(self.canv, text=text, font=f"{font} {size} {ttype}", fg=color, bg=background,
    		command=on_click, borderwidth=0, relief="flat", padx=padx, pady=pady)
    	self.canv.create_window(x,y, window=button)
    	self.length += bottom
    	return button

    def create_lineentry(self,
    	x=None,
    	y=None,
    	on_focus="blue",
    	width=20,
    	text="",
    	color="blue",
    	label="Enter text",
    	border=True,
    	on_enter=None,
    	top=50,
    	bottom=0):

    	self.length += top
    	x = x or self.width/2
    	y = y or self.length

    	self.canv.create_text(x-(width*2.5),y-20,text=label,fill=color,font="Lato 8 bold", anchor='e')
    	entry = tk.Entry(self.canv, width=width, fg="#37373b", bg="white", borderwidth=0, font="Lato 12",
            highlightbackground=color,highlightthickness=1,highlightcolor=on_focus)
    	entry.insert(1, text)

    	if border != True:
    		entry.config(fg=self.secondary, bg=self.primary, highlightthickness=0)
    		self.canv.create_line(x-((width*10)/2)+10,y+15,x+((width*10)/2)-10,y+15,fill=color)
    	self.canv.create_window(x,y, window=entry)
    	entry.bind("<Return>", on_enter)
    	self.length += bottom
    	return entry

    def create_icon(self,
    	x=None,
    	y=None,
    	color="blue",
    	size=15,
    	icon="right",
    	top=50,
    	bottom=0):

    	self.length += top
    	x = x or self.width/2
    	y = y or self.length

    	try:
    		self.canv.create_text(x,y, text=icons.icons[icon], fill=color, font=f"Webdings {size}")
    	except KeyError:
    		self.length -= top
    		print(f"'{icon}' icon does not exist")

    def run(self):
    	self.mainloop()