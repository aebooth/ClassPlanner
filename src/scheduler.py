from gi.repository import Gtk
import datetime

class SchedulerInit():
    def __init__(self):
        #Info variables
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
                dialog = Gtk.MessageDialog(self.panel.get_parent(),Gtk.DialogFlags.MODAL,Gtk.MessageType.WARNING,Gtk.ButtonsType.OK,"End year must come \n after start year!!")
                dialog.run()
                dialog.destroy()
            elif self.start_date[1] > self.end_date[1]:
                entry.set_text("")
                dialog = Gtk.MessageDialog(self.panel.get_parent(),Gtk.DialogFlags.MODAL,Gtk.MessageType.WARNING,Gtk.ButtonsType.OK,"End month must come \n after start month (in same year)!!")
                dialog.run()
                dialog.destroy()
            elif self.start_date[2] > self.end_date[2]:
                entry.set_text("")
                dialog = Gtk.MessageDialog(self.panel.get_parent(),Gtk.DialogFlags.MODAL,Gtk.MessageType.WARNING,Gtk.ButtonsType.OK,"End day must come \n after start day (in same month)!!")
                dialog.run()
                dialog.destroy()    
            else:
                entry.set_text(retval)
        else:
            entry.set_text(retval)
        
    def get_days(self,button):
        if self.start_entry.get_text() == "":
            dialog = Gtk.MessageDialog(self.panel.get_parent(),Gtk.DialogFlags.MODAL,Gtk.MessageType.WARNING,Gtk.ButtonsType.OK,"Must give a start date!")
            dialog.run()
            dialog.destroy()
        elif self.end_entry.get_text() == "":
            dialog = Gtk.MessageDialog(self.panel.get_parent(),Gtk.DialogFlags.MODAL,Gtk.MessageType.WARNING,Gtk.ButtonsType.OK,"Must give an end date!")
            dialog.run()
            dialog.destroy()
        else:
            days = Schedule(self.dd_list[self.schedule_dd.get_active_iter()][0],self.start_date,self.end_date)
            self.panel.get_parent().change_panel("scheduler_days",days)

            
class SchedulerDays:
    def __init__(self,schedule):
        self.panel = Gtk.VBox(border_width=10)
        self.panel.set_homogeneous(False)
        self.schedule = schedule

        self.scrollpane = Gtk.ScrolledWindow()

        self.liststore = Gtk.ListStore(str,bool)

        self.days_view = Gtk.TreeView(self.liststore)
        
        current_day = schedule.get_day_as_datetime(1)-datetime.timedelta(days=10)

        while current_day.toordinal() <= (schedule.get_last_day()+datetime.timedelta(days=10)).toordinal():
            self.liststore.append([current_day.strftime("%A %d %B %Y"),(current_day in schedule.get_days_as_datetime())])
            current_day += datetime.timedelta(days=1)
        
        day_label = Gtk.CellRendererText()
        self.days_view.append_column(Gtk.TreeViewColumn("Date",day_label,text=0))

        day_toggle = Gtk.CellRendererToggle()
        self.days_view.append_column(Gtk.TreeViewColumn("Included",day_toggle,active=1))
        day_toggle.connect("toggled",self.toggle_days)

        self.button = Gtk.Button("Finish Schedule")
        self.button.connect("clicked",self.on_button_clicked)

        self.panel.pack_start(Gtk.Label("Days"),True,True,10)
        
        self.scrollpane.add(self.days_view)
        self.scrollpane.set_size_request(200,400)
        self.panel.pack_start(self.scrollpane,True,True,10)

        self.panel.pack_start(self.button,True,True,10)

    def on_button_clicked(self,button):
        pass
        
    def toggle_days(self,wigdet,path):
        self.liststore[path][1] = not self.liststore[path][1]
        
            
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
