from gi.repository import Gtk
import datetime


class SchedulerInit:
    def __init__(self):
        #Info variables
        self.school_year_name = ""
        self.start_date = None
        self.end_date = None
        self.holidays = []

        #UI Helper variables. Wiring up signals
        builder = Gtk.Builder()
        builder.add_from_file("SchedulerUI.glade")

        self.panel = builder.get_object("main_box")

        self.schedule_dd = builder.get_object("schedule_dd")
        cell = Gtk.CellRendererText()
        self.schedule_dd.pack_start(cell,True)
        self.schedule_dd.add_attribute(cell,'text',0)

        self.name_entry = builder.get_object("name_entry")

        self.start_entry = builder.get_object("start_entry")
        self.start_entry.connect("icon-press",self.pick_a_date)

        self.end_entry = builder.get_object("end_entry")
        self.end_entry.connect("icon-press",self.pick_a_date)

        builder.get_object("the_button").connect("clicked",self.get_days)

        self.cal_win = None

    def pick_a_date(self,entry,icon_pos,event):
        if self.cal_win is not None:
            self.cal_win.destroy()
        self.cal_win = Gtk.Window(title="Choose a day")
        cal = Gtk.Calendar()
        cal.connect("day-selected-double-click",self.date,entry)
        self.cal_win.add(cal)
        self.cal_win.show_all()

    def date(self,calendar,entry):
        retval = str(calendar.get_date()[1])+"/"+ str(calendar.get_date()[2]) +"/" + str(calendar.get_date()[0])
        calendar.get_parent().destroy()
        if entry.get_name() == "end":
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
    def get_days(self,button):
        if self.name_entry.get_text() == "":
            dialog = Gtk.MessageDialog(None,Gtk.DialogFlags.MODAL,Gtk.MessageType.WARNING,Gtk.ButtonsType.OK,"Must give school year a name!")
            dialog.run()
            dialog.destroy()
        else:
            pass

class Schedule:
    def __init__(self,schedule_type,start_date,end_date):
        self.days = []
        start = datetime.date(self.start_date[0],self.start_date[1],self.start_date[2])
        end = datetime.date(self.end_date[0],self.end_date[1],self.end_date[2])
        day = start
        if schedule_type == "Traditional":
            delta = datetime.timedelta(days=1)
            while day is not end:
                if day.weekday() < 5:
                    self.days.append(day)
                day = day + delta

        elif schedule_type == "Block":
            delta = datetime.timedelta(days=2)
            while day is not end:
                if day.weekday() < 5:
                    self.days.append(day)
                day = day + delta

    def get_days_as_datetime():
        return self.days


    def get_day_as_datetime(day_num):
        return self.days[day_num-1]

    def get_days_as_string():
        ret = []
        for day in self.days:
            ret.append(day.strftime("%A %d %B %Y"))
        return ret

    def get_day_as_string(day_num):
        return self.days[day_num-1].strftime("%A %d %B %Y")
