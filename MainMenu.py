import npyscreen

class MainMenu(npyscreen.FormBaseNew):
    def create(self):
        self.add(npyscreen.TitleFixedText, editable=False, name="DriveCLI")
        self.add(npyscreen.ButtonPress, name="Your drive", when_pressed_function=lambda: self.parentApp.switchForm("DRIVE"))
        self.add(npyscreen.ButtonPress, name="Upload", when_pressed_function=lambda: self.parentApp.switchForm("UPLOAD"))
        self.add(npyscreen.ButtonPress, name="Quit (Q)",   when_pressed_function=lambda: self.parentApp.switchForm(None))
        self.add_handlers({"q": lambda x: self.parentApp.switchForm(None),
                           "Q": lambda x: self.parentApp.switchForm(None)})
