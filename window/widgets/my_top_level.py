import tkinter as tk

class MyToplevel(tk.Toplevel):
    # Define class attributes
    height = 300
    width = 300
    primary = "#37373b"
    secondary = "white"
    faded = "white"
    length = 0

    def __init__(self, master=None,**kwargs):
        super().__init__(master, **kwargs)
        self.overrideredirect(True)
        self.geometry(f"{self.width}x{self.height}")

        self.topbar = tk.Canvas(self, bg="white", borderwidth=0, highlightthickness=0, width=self.width,
        	height=30)
        self.topbar.pack()
        self.topbar.bind("<ButtonPress-1>", self.startmove)
        self.topbar.bind("<ButtonRelease-1>", self.stopmove)
        self.topbar.bind("<B1-Motion>", self.domove)

        self.canv = tk.Canvas(self, bg=self.primary, borderwidth=0, highlightthickness=1, width=self.width,
        	height=self.height-30, highlightbackground="black")
        self.canv.pack()

        self.thetitle = tk.Label(self.topbar, text="FakeApp", font="Lato 12 bold", fg="#37373b", bg="white")
        self.topbar.create_window(self.width/2, 13, window=self.thetitle, tags="title_label")

        self.minimizer = tk.Label(self.topbar, text="~", font="Lato 13 bold", fg="gray", bg="white")
        self.topbar.create_window(self.width-40, 13, window=self.minimizer, tags="minimize_label")
        #self.cancellab.bind("<Enter>", self.on_cancel_enter)
        #self.cancellab.bind("<Leave>", self.on_cancel_leave)

        self.cancellab = tk.Label(self.topbar, text="x", font="Lato 13 bold", fg="gray", bg="white")
        self.topbar.create_window(self.width-20, 13, window=self.cancellab, tags="cancel_label")
        self.cancellab.bind("<Enter>", self.on_cancel_enter)
        self.cancellab.bind("<Leave>", self.on_cancel_leave)
        self.cancellab.bind("<Button-1>", self.destroyer)

        self._x = 0
        self._y = 0

        self.icons = {"correct":"a", "bicycle":"b", "square":"c", "shield":"d", "gift":"e", "firetruck":"f", 
        "fsquare":"g", "ambulance":"h", "info":"i", "plane":"j", "fan":"k", "star":"l", "man":"m", "circle":"n", 
        "ferry":"o", "police":"p", "reload":"q", "wrong":"r", "question":"s", "train":"t", "bus":"u", "truck":"v", 
        "flag":"w", "cancel1":"x", "cancel2":"y", "nocigarette":"z", "houses":"B", "city":"C", "desert":"E",
        "bank":"G", "house":"I", "tree":"K", "magnify":"L", "mountain":"M", "eye":"N", "ear":"O", "speak":"U",
        "silent":"V", "speaker_l":"W", "speaker_r":"X", "heart":"Y", "flower":"Z", "maximize":"1", "minimize":"2", 
        "left":"3", "right":"4", "up":"5", "down":"6", "fastforward":"8", "fastbackward":"7", "before":"9", 
        "after":":", "underscore":"0", "msgleft":"(", "msgright":")", "msgmiddle":"*", "medal":"&", "chats":"^", 
        "cup":"%", "shades":"$", "scarf":"-", "msgs":"_", "face":"#", "tools":"@", "spider":"!", "pins":"'", 
        "web":'"', "pause":";", "pepper":",", "fontsize":">", "save":"?", "line":"|", "active":"="}

    #---------------------------------------Set_Basics---------------------------------------------

    def settitle(self, title="FakeApp"):
        self.thetitle.config(text=title)

    def setgeometry(self, width=width, height=height):
        self.width = width
        self.height = height
        self.geometry(f"{self.width}x{self.height}")
        self.canv.config(width=self.width, height=self.height)
        self.topbar.config(width=self.width)
        self.topbar.coords("title_label", self.width/2, 13)
        self.topbar.coords("cancel_label", self.width-20, 13)
        self.topbar.coords("minimize_label", self.width-40, 13)

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

    #--------------------------------------Bindings--------------------------------------------

    def on_cancel_enter(self, event):
        self.cancellab.config(fg="#37373b")

    def on_cancel_leave(self, event):
        self.cancellab.config(fg="gray")

    def destroyer(self, event):
        self.destroy()

    def startmove(self, event):
    	self._x = event.x
    	self._y = event.y

    def stopmove(self, event):
    	self._x = None
    	self._y = None

    def domove(self, event):
    	deltax = event.x - self._x
    	deltay = event.y - self._y

    	x = self.winfo_x() + deltax
    	y = self.winfo_y() + deltay

    	self.geometry(f"+{x}+{y}")


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
    		self.canv.create_text(x,y, text=self.icons[icon], fill=color, font=f"Webdings {size}")
    	except KeyError:
    		self.length -= top
    		print(f"'{icon}' icon does not exist")
    	#I want to add a way in which the user can do like vertical split or horizontal split with scroll capacity


    #def create_image(self,
        #x=None,
        #y=None,)