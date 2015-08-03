from gi.repository import Gtk
import datetime

class SchedulerInit():
    def __init__(self):
        #Info variables
        self.school_year_name = ""
        self.start_date = None
        self.end_date = None

        #UI Helper variables. Wiring up signals
        builder = Gtk.Builder()
        builder.add_from_file("SchedulerInit.glade")

        self.panel = builder.get_object("main_box")
        
        self.dd_list = builder.get_object("schedules")
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
        retval = str(calendar.get_date()[1]+1)+"/"+ str(calendar.get_date()[2]) +"/" + str(calendar.get_date()[0])
        if entry.get_name() == "end":
            self.end_date = calendar.get_date()
        else:
            self.start_date = calendar.get_date()
        calendar.get_parent().destroy()
        calendar.destroy()
        if self.start_date is not None and  self.end_date is not None:
            if self.start_date[0] > self.end_date[0]:
                entry.set_text("")
                dialog = Gtk.MessageDialog(None,Gtk.DialogFlags.MODAL,Gtk.MessageType.WARNING,Gtk.ButtonsType.OK,"End year must come \n after start year!!")
                dialog.run()
                dialog.destroy()
            elif self.start_date[1] > self.end_date[1]:
                entry.set_text("")
                dialog = Gtk.MessageDialog(None,Gtk.DialogFlags.MODAL,Gtk.MessageType.WARNING,Gtk.ButtonsType.OK,"End month must come \n after start month (in same year)!!")
                dialog.run()
                dialog.destroy()
            elif self.start_date[2] > self.end_date[2]:
                entry.set_text("")
                dialog = Gtk.MessageDialog(None,Gtk.DialogFlags.MODAL,Gtk.MessageType.WARNING,Gtk.ButtonsType.OK,"End day must come \n after start day (in same month)!!")
                dialog.run()
                dialog.destroy()    
            else:
                entry.set_text(retval)
        else:
            entry.set_text(retval)
        
    def get_days(self,button):
        if self.name_entry.get_text() == "":
            dialog = Gtk.MessageDialog(None,Gtk.DialogFlags.MODAL,Gtk.MessageType.WARNING,Gtk.ButtonsType.OK,"Must give school year a name!")
            dialog.run()
            dialog.destroy()
        else:
            days = Schedule(self.dd_list[self.schedule_dd.get_active_iter()][0],self.start_date,self.end_date)
            self.panel.get_parent().change_panel("scheduler_days",days)

            
class SchedulerDays:
    def __init__(self,schedule):
        builder = Gtk.Builder()
        builder.add_from_file("SchedulerDays.glade")
        self.panel = builder.get_object("main_box")
        self.schedule = schedule
        self.liststore = Gtk.ListStore(str)#,bool)
        
        current_day = schedule.get_day_as_datetime(1)

        i = 0##
        while current_day.toordinal() <= schedule.get_last_day().toordinal():
            #print(current_day.strftime("%A %d %B %Y"))##
            self.liststore.append([current_day.strftime("%A %d %B %Y")])#,(current_day in schedule.get_days_as_datetime())])
            current_day += datetime.timedelta(days=1)
            print(self.liststore[self.liststore.get_iter(i)][0])##
            i += 1##
            
        self.days_view = builder.get_object("days_view")
        self.days_view.set_model(self.liststore)
        day_label = Gtk.CellRendererText()
        self.days_view.append_column(Gtk.TreeViewColumn("Date",day_label,text=0))
        
            
class Schedule:
    def __init__(self,schedule_type,start_date,end_date):
        self.__days = []
        start = datetime.date(start_date[0],start_date[1],start_date[2])
        end = datetime.date(end_date[0],end_date[1],end_date[2])
        day = start
        if schedule_type == "Traditional":
            while day.toordinal() <= end.toordinal():
                if day.weekday() < 5:
                    self.__days.append(day)
                day += datetime.timedelta(days=1)
        elif schedule_type == "Block":
            while day.toordinal() <= end.toordinal():
                if day.weekday() < 5:
                    self.__days.append(day)
                day += datetime.timedelta(days=2)

    def get_days_as_datetime(self):
        return self.__days


    def get_day_as_datetime(self,day_num):
        return self.__days[day_num-1]

    def get_days_as_string(self):
        ret = []
        for day in self.__days:
            ret.append(day.strftime("%A %d %B %Y"))
        return ret

    def get_day_as_string(self,day_num):
        return self.days[day_num-1].strftime("%A %d %B %Y")

    def add_day_from_string(self,day_string):
        brand_new_day = datetime.strptime(day_string,"%A %d %B %Y")
        day_num = len(self.__days) - 1
        while day_num > 0 and self.__days[day_num].toordinal() > brand_new_day.toordinal():
            day_num = day_num - 1
        self.__days.insert(day_num + 1,brand_new_day)

    def get_last_day(self):
        return self.__days[len(self.__days)-1]
