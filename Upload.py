import npyscreen

class Upload(npyscreen.ActionForm):
    def create(self):
        self.file = self.add(npyscreen.TitleFilenameCombo, name="Filename:")


    def on_ok(self):
        self.parentApp.gdrive.create(self.file.value)

    def on_cancel(self):
        self.parentApp.switchForm("MAIN")