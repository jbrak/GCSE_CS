day = 50
hour = 7

class Alarm:
    date = 1
    door_open = False
    time = 9

    def alarm(self):
        if self.door_open == True and self.date >= 340:
            print("Alarm\nAlarm\nAlarm")

        elif self.door_open == True and self.date <= 2:
            print("Alarm\nAlarm\nAlarm")

        elif self.door_open == True and self.time >= 18 :
            print("Alarm\nAlarm\nAlarm")

        elif self.door_open == True and self.time <= 6:
            print("Alarm\nAlarm\nAlarm")

front_door = Alarm()
front_door.door_open = True
front_door.date = day
front_door.time = hour

front_door.alarm()
