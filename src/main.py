from gi.repository import Gtk
import scheduler
import transitions


class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,title="Class Planner",border_width=10)
        self.data = None
        self.unsaved_changes = False
        self.connect("delete-event",self.check_for_save)

    def change_panel(self,panel_name,data):
        for child in self.get_children():
            child.destroy()
        if panel_name == "scheduler_init":
            self.add(scheduler.SchedulerInit().panel)
            self.show_all()
        elif panel_name == "scheduler_days":
            self.add(scheduler.SchedulerDays(data).panel)
            self.show_all()
        elif panel_name == "scheduler_landing":
            self.add(transitions.SchedulerLanding().panel)
            self.show_all()

    def check_for_save(self,window,event):
        Gtk.main_quit()
            
win = MainWindow()
win.add(transitions.StartUpLanding().panel)
win.show_all()
Gtk.main()
