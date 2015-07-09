from gi.repository import Gtk

class LessonWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,title = "a test")
        self.table = Gtk.Table(2,2,True)
        day_label = Gtk.Label("Day:")
        self.table.attach(day_label,0,1,0,1)
        self.day_text = Gtk.Entry()
        self.table.attach(self.day_text,1,3,0,1)
        lesson_label = Gtk.Label("Lesson:")
        self.table.attach(lesson_label,0,1,1,2)
        self.lesson_text = Gtk.Entry()
        self.table.attach(self.lesson_text,1,3,1,2)
        self.add(self.table)


win = LessonWindow() 
win.connect("delete-event",Gtk.main_quit)
win.show_all()
Gtk.main()
