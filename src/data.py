import datetime
import scheduler
import sqlite3

class MetaData:
    def __init__(self,project_path):
        self.schedule = None
        self.lesson_resource_map = {}
        self.lesson_date_map = {}
        self.last_unique_lesson_index = 0
        self.project_path = project_path

    def add_tag(self,tag,lesson_id):
        pass

    def remove_tag(self,tag,lesson_id):
        pass

    def edit_long_description(self,text,lesson_id):
        pass

    def edit_short_description(self,text,lesson_id):
        pass

    def save_all(self):
        pass

    def load_all(self,plan_path):
        pass
