from gi.repository import Gtk

class TestWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,title="TESTING",border_width=10)
        self.connect("delete-event",Gtk.main_quit)

        self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=10)
        
        row1 = Gtk.Box(spacing=10)

        self.label1 = Gtk.Label()
        row1.pack_start(self.label1,True,True,10)

        row2 =  Gtk.Box(spacing=10)

        self.button_hello = Gtk.Button(label="Add Hello")
        self.button_hello.connect("clicked",self.hello)
        row2.pack_start(self.button_hello,True,False,0)

        self.row3 = Gtk.Box(spacing=10)

        self.entry = Gtk.Entry()
        self.entry.set_icon_from_stock(1,Gtk.STOCK_ADD)
        self.entry.connect("icon-press",self.add_extra)
        self.row3.pack_start(self.entry,True,True,0)
        
        self.vbox.pack_start(row1,True,True,0)
        self.vbox.pack_start(row2,True,True,0)
        self.vbox.pack_start(self.row3,True,True,0)

        self.add(self.vbox)
        self.show_all()

    def hello(self,button):
        self.label1.set_text(self.label1.get_text()+"hello")
        if self.row3 is not None:
            self.row3.destroy()


    def add_extra(self,entry,icon_pos,event):
        new_win = Gtk.Window(title="Choose a day")
        cal = Gtk.Calendar()
        cal.connect("day-selected",self.mark)
        cal.connect("day-selected-double-click",self.date)
        new_win.add(cal)
        new_win.show_all()

    def date(self,calendar):
        datestr = str(calendar.get_date()[1])+"/"+ str(calendar.get_date()[2]) +"/" + str(calendar.get_date()[0])
        self.entry.set_text(datestr)
        calendar.get_parent().destroy()

    def mark(self,calendar):
        calendar.mark_day(calendar.get_date()[2])

win = TestWindow()
Gtk.main()

