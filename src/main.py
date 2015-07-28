from gi.repository import Gtk
import scheduler

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,title="Class Planner",border_width=10)
        self.add(scheduler.SchedulerInit().panel)
        self.show_all()
        self.connect("delete-event",Gtk.main_quit)
        Gtk.main()

    def change_panel(self,panel_name):
        for child in self.get_children():
            child.destroy()
        if panel_name == "scheduler_init":
            self.add(scheduler.SchedulerInit().panel)
            self.show_all()

MainWindow()
