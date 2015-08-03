from gi.repository import Gtk
import scheduler


class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,title="Class Planner",border_width=10)
        self.connect("delete-event",Gtk.main_quit)

    def change_panel(self,panel_name,data=None):
        for child in self.get_children():
            child.destroy()
        if panel_name == "scheduler_init":
            self.add(scheduler.SchedulerInit().panel)
            self.show_all()
        elif panel_name == "scheduler_days":
            self.add(scheduler.SchedulerDays(data).panel)
            self.show_all()

win = MainWindow()
win.change_panel("scheduler_init")
Gtk.main()
