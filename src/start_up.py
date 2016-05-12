from gi.repository import Gtk
import os
import data

class StartUpLanding:
    def __init__(self):
        self.panel = Gtk.VBox()
        self.panel.pack_start(Gtk.Label("Welcome to the Class Planner!\n What would you like to do?"),True,True,5)
        self.new_button = Gtk.Button("Create New Plan")
        self.new_button.connect("clicked",self.new_plan)
        self.panel.pack_start(self.new_button,True,True,5)
        self.edit_button = Gtk.Button("Edit Existing Plan")
        self.edit_button.connect("clicked",self.edit_plan)
        self.panel.pack_start(self.edit_button,True,True,5)

    def new_plan(self,button):
        done = False
        while not done:
            dialog = Gtk.FileChooserDialog(title="Select a project folder",parent=self.panel.get_parent(),action=Gtk.FileChooserAction.CREATE_FOLDER,buttons=(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,"Select",Gtk.ResponseType.OK))
            dialog.set_default_size(800,400)
            response = dialog.run()
            if response == Gtk.ResponseType.OK:
                if not os.path.isdir(dialog.get_filename()+"/.plan"):
                    self.panel.get_parent().data = data.MetaData(dialog.get_filename())
                    os.mkdir(dialog.get_filename()+"/.plan")
                    self.panel.get_parent().change_panel("scheduler_init",self.panel.get_parent().data)
                    done = True
                else:
                    warning = Gtk.MessageDialog(self.panel.get_parent(),Gtk.DialogFlags.MODAL,Gtk.MessageType.WARNING,Gtk.ButtonsType.OK,"A ClassPlanner plan already exists for this directory!")
                    warning.run()
                    warning.destroy()
            elif response == Gtk.ResponseType.CANCEL:
                done = True
            dialog.destroy()

    def edit_plan(self,button):
        pass


class SchedulerLanding():
    def __init__(self):
        self.panel = Gtk.VBox()
        self.panel.pack_start(Gtk.Label("What would you like to do?"),True,True,5) 
        self.new_button = Gtk.Button("Create New Schedule")
        self.new_button.connect("clicked",self.new_schedule)
        self.panel.pack_start(self.new_button,True,True,5)
        self.edit_button = Gtk.Button("Import Schedule from File")
        self.edit_button.connect("clicked",self.import_schedule)
        self.panel.pack_start(self.edit_button,True,True,5)

    def new_schedule(self):
        pass

    def import_schedule(self):
        pass
