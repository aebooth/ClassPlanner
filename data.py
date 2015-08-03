import schedule

class Data:
    def __init__(self,schedule=None):
        self.days = {}
        if schedule is not None:
            index = 0
            for day in schedule:
                self.days[index] = day.strftime("%A %d %B %Y")
