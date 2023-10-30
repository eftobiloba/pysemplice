import window

first_screen = window.screen()
first_screen.setgeometry(700, 400)
first_screen.settitle("My first app")
first_screen.setmode("light")

first_screen.create_icon(icon="face", color="blue", size=30, top=67)
header = first_screen.create_label(text="User Login", color="blue", size=15, top=40)
username = first_screen.create_lineentry(label="Enter username", border=False, color=first_screen.faded, top=70, width=30)
email = first_screen.create_lineentry(label="Enter email", border=True, color=first_screen.faded, top=60, width=30)
password = first_screen.create_lineentry(label="Enter password", border=True, color=first_screen.faded, top=60, width=30)
submit = first_screen.create_button(text="Submit", padx=30, background="blue", color="white", pady=7, top=80)

first_screen.run()