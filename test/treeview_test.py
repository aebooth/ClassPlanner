from gi.repository import Gtk

window = Gtk.Window()
window.connect("delete-event",Gtk.main_quit)

box = Gtk.Box()

model = Gtk.ListStore(str)
model.append(["Benjamin"])
model.append(["Charles"])
model.append(["alfred"])
model.append(["Alfred"])
model.append(["David"])
model.append(["charles"])
model.append(["david"])
model.append(["benjamin"])
treeView = Gtk.TreeView(model)
renderer = Gtk.CellRendererText()
column = Gtk.TreeViewColumn("Title", renderer, text=0)
treeView.append_column(column)

box.pack_start(treeView,True,True,0)
window.add(box)
window.show_all()

Gtk.main()


