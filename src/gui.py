from gi.repository import Gtk

class YearPanel(Gtk.Box):
    def __init__(self):
        Gtk.Box.__init__(self, orientation=Gtk.Orientation.VERTICAL)

        #Information variables for YearPanel
        self.school_year_name=""
        self.start_date=None
        self.end_date=None
        self.holidays=[]

        #Main box that all the components are laid out in
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=10)

        #Adding the School Year label and entry
        box1 = Gtk.Box(spacing=10)
        box1.pack_start(Gtk.Label("School Year:"),True,True,10)
        self.year_entry = Gtk.Entry()
        self.year_entry.connect("changed",self.year_update)
        box1.pack_start(self.year_entry,True,True,10)
        vbox.pack_start(box1,True,True,10)

        #MAke sure that we have initialized the calendar pop-up window to none
        self.cal_win = None

        box2 = Gtk.Box(spacing=10)
        box2.pack_start(Gtk.Label("Start Date:"),True,True,10)
        self.start_entry = Gtk.Entry(editable=False)
        self.start_entry.set_icon_from_stock(1,Gtk.STOCK_ADD)
        self.start_entry.connect("icon-press",self.pick_a_date,False)
        box2.pack_start(self.start_entry,True,True,10)
        vbox.pack_start(box2,True,True,10)

        box3 = Gtk.Box(spacing=10)
        box3.pack_start(Gtk.Label("End Date:"),True,True,10)
        self.end_entry = Gtk.Entry(editable=False)
        self.end_entry.set_icon_from_stock(1,Gtk.STOCK_ADD)
        self.end_entry.connect("icon-press",self.pick_a_date,True)
        box3.pack_start(self.end_entry,True,True,10)
        vbox.pack_start(box3,True,True,10)

        self.holiday_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=10)
        self.holiday_box.pack_start(Gtk.Label("Holidays"),True,True,0)
        self.holiday_entry = Gtk.Entry()
        self.holiday_entry.set_icon_from_stock(1,Gtk.STOCK_ADD)
        self.holiday_entry.connect("icon-press",self.pick_a_date)
        self.holiday_box.pack_start(self.holiday_entry,True,True,10)
        vbox.pack_start(self.holiday_box,True,True,0)

        self.pack_start(vbox,True,True,0)

    def year_update(self,entry):
        self.school_year_name = entry.get_text()

    def pick_a_date(self,entry,icon_pos,event,is_end):
        if self.cal_win is not None:
            self.cal_win.destroy()
        self.cal_win = Gtk.Window(title="Choose a day")
        cal = Gtk.Calendar()
        cal.connect("day-selected-double-click",self.date,entry,is_end)
        self.cal_win.add(cal)
        self.cal_win.show_all()

    def date(self,calendar,entry,is_end):
        retval = str(calendar.get_date()[1])+"/"+ str(calendar.get_date()[2]) +"/" + str(calendar.get_date()[0])
        calendar.get_parent().destroy()
        if is_end:
            self.end_date = calendar.get_date()
        else:
            self.start_date = calendar.get_date()

        if self.start_date is not None and  self.end_date is not None:
            if self.start_date[0] <= self.end_date[0] and self.start_date[1] <= self.end_date[1] and self.start_date[2] < self.end_date[2]:
                entry.set_text(retval)
            else:
                entry.set_text("")
                dialog = Gtk.MessageDialog(None,Gtk.DialogFlags.MODAL,Gtk.MessageType.WARNING,Gtk.ButtonsType.OK,"End date must come \n after start date!!")
                dialog.run()
                dialog.destroy()
        else:
            entry.set_text(retval)

win = Gtk.Window(title="Class Planner")
win.connect("delete-event", Gtk.main_quit)
win.set_border_width(10)
win.add(YearPanel())
win.show_all()
Gtk.main()
