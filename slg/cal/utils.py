# -*- coding: UTF-8 -*-
from calendar import HTMLCalendar

from .models import Event


class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__()

    # formats a day as a td
    # filter events by day
    def formatday(self, day, events):
        events_per_day = events.filter(start_time__day=day)
        d = ''
        for event in events_per_day:
            d += f'<li> {event.get_html_url} </li>'

        if day != 0:
            return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
        return '<td></td>'

    def diaEspanol(self, valor):
        listaDia = ['Lun', 'Mar', 'Mie', 'Jue', 'Vie', 'Sab', 'Dom']
        if valor == 'Mon':
            return listaDia[1]
        elif valor == 'Tue':
            return listaDia[2]
        elif valor == 'Wed':
            return listaDia[3]
        elif valor == 'Thu':
            return listaDia[4]
        elif valor == 'Fri':
            return listaDia[5]
        elif valor == 'Sat':
            return listaDia[6]
        elif valor == 'Sun':
            return listaDia[7]

    # formats a week as a tr
    def formatweek(self, theweek, events):
        listaMes = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo',
                    'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, events)

        return f'<tr> {week} </tr>'

    # formats a month as a table
    # filter events by year and month
    def formatmonth(self, withyear=True):
        events = Event.objects.filter(start_time__year=self.year, start_time__month=self.month)

        cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, events)}\n'
        return cal
