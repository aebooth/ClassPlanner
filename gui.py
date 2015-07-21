from gi.repository import Gtk

class YearWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="New Year")
        self.connect("delete-event", Gtk.main_quit)
        self.set_border_width(10)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=10)

        box1 = Gtk.Box(spacing=10)
        box1.pack_start(Gtk.Label("School Year:"),True,True,10)
        self.year_entry = Gtk.Entry()
        box1.pack_start(self.year_entry,True,True,10)
        vbox.pack_start(box1,True,True,10)

        box2 = Gtk.Box(spacing=10)
        box2.pack_start(Gtk.Label("Start Date:"),True,True,10)
        self.start_entry = Gtk.Entry()
        self.start_entry.set_icon_from_stock(1,Gtk.STOCK_ADD)
        self.start_entry.connect("icon-press",self.pick_a_date)
        box2.pack_start(self.start_entry,True,True,10)
        vbox.pack_start(box2,True,True,10)

        box3 = Gtk.Box(spacing=10)
        box3.pack_start(Gtk.Label("End Date:"),True,True,10)
        self.end_entry = Gtk.Entry()
        self.end_entry.set_icon_from_stock(1,Gtk.STOCK_ADD)
        self.end_entry.connect("icon-press",self.pick_a_date)
        box3.pack_start(self.end_entry,True,True,10)
        vbox.pack_start(box3,True,True,10)

        self.holiday_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=10)
        self.holiday_box.pack_start(Gtk.Label("Holidays"),True,True,0)
        self.holiday_entry = Gtk.Entry()
        self.holiday_entry.set_icon_from_stock(1,Gtk.STOCK_ADD)
        self.holiday_entry.connect("icon-press",self.pick_a_date)
        self.holiday_box.pack_start(self.holiday_entry,True,True,10)
        vbox.pack_start(self.holiday_box,True,True,0)
        
        self.add(vbox)
        self.show_all()

    def pick_a_date(self,entry,icon_pos,event):
        new_win = Gtk.Window(title="Choose a day")
        cal = Gtk.Calendar()
        cal.connect("day-selected-double-click",self.date,entry)
        new_win.add(cal)
        new_win.show_all()

    def date(self,calendar,entry):
        retval = str(calendar.get_date()[1])+"/"+ str(calendar.get_date()[2]) +"/" + str(calendar.get_date()[0])
        calendar.get_parent().destroy()
        entry.set_text(retval)

win = YearWindow()
Gtk.main()
