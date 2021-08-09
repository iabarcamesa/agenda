from datetime import datetime, timedelta
from app.entities import Appointment

week_days = ['MON','TUE','WED','THU','FRI','SAT','SUN']

class GenerateCalendar:

    def __init__(self, month, year, practitioner):
        self.month = month
        self.year = year
        self.practitioner = practitioner

    def execute(self):
        calendar_grid = self.__calendar_grid()
        for appointment in self.__appointments():
            week, day = self.__grid_for_day(appointment.date_time.day)
            calendar_grid[week][day]['appointments'].append(str(appointment.patient))
        return calendar_grid

    def __appointments(self):
        return Appointment.find_by_month_and_year_and_practitioner(
            self.month, 
            self.year, 
            self.practitioner)

    def __calendar_grid(self):
        calendar_grid = {}
        first_grid_day = datetime(self.year, self.month, 1) \
            - timedelta(days=datetime(self.year, self.month, 1).weekday())
        grid_day_number = 0
        for week_number in range(6):
            for day in week_days:
                week = calendar_grid.get(week_number, {})
                week[day] = {'day': (first_grid_day + timedelta(days=grid_day_number)).day, 
                             'appointments': []}
                calendar_grid[week_number] = week
                grid_day_number +=1
        return calendar_grid

    def __grid_for_day(self, day):
        first_month_day_grid_number = datetime(self.year, self.month, 1).weekday()
        day_grid_number = first_month_day_grid_number + day
        week = int(day_grid_number/7)
        day = week_days[datetime(self.year, self.month, day).weekday()]
        return week, day


