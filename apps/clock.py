from datetime import *

class Time:
    def time(self):
        now = datetime.now()
        print(now.ctime())