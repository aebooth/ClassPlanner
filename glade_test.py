from gi.repository import Gtk

builder = Gtk.Builder()
builder.add_from_file("glade_gui.glade")

win = builder.get_object("main_win")

schedule_dd = builder.get_object("schedule_dd")
cell = Gtk.CellRendererText()
schedule_dd.pack_start(cell,True)
schedule_dd.add_attribute(cell,'text',0)

win.show_all()

def schedule_dd_changed_cb(combo):
    pass

#print(builder.get_object("schedule_dd").get_model()[builder.get_object("schedule_dd").get_model().get_iter(0)][0])

win.connect("delete-event",Gtk.main_quit)
Gtk.main()
