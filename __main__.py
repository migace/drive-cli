from GoogleDrive import GoogleDrive
from MainMenu import MainMenu
from Upload import Upload
import npyscreen

# This application class serves as a wrapper for the initialization of curses
# and also manages the actual forms of the application

class DriveCli(npyscreen.NPSAppManaged):
    def onStart(self):
        self.gdrive = GoogleDrive()
        self.addForm("MAIN", MainMenu)
        self.addForm("DRIVE", DataGrid)
        self.addForm("UPLOAD", Upload)

class MyGrid(npyscreen.GridColTitles):
    def custom_print_cell(self, actual_cell, cell_display_value):
        pass

class MoreButton(npyscreen.ButtonPress):
    def whenPressed(self):
        return self.parent.more()

class DataGrid(npyscreen.Form):
    def create(self):
        self.add(npyscreen.TitleFixedText, name="DriveCLI", editable=False)
        self.gd = self.add(MyGrid, max_height=18)
        self.gd.values = []
        self.gd.values.append(
            self.gd.set_grid_values_from_flat_list(self.parentApp.gdrive.getFilesList())
        )
        self.add(MoreButton, name="More")

    def more(self):
        nextPageToken = self.parentApp.gdrive.getNextPageToken()
        self.gd.values.append(
            self.gd.set_grid_values_from_flat_list(
                self.gd.getValuesFlatList() +
                self.parentApp.gdrive.getFilesList(
                    nextPageToken=nextPageToken
                ),
                reset_cursor=False
            )
        )
        self.display()

    def afterEditing(self):
        self.parentApp.setNextForm("MAIN")


if __name__ == '__main__':
    DriveCli().run()
