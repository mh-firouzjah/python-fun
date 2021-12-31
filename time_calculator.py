"""Time Calculator
takes in two required parameters and one optional parameter:

a start time in the 12-hour clock format (ending in AM or PM)
a duration time that indicates the number of hours and minutes
(optional) a starting day of the week, case insensitive
The function should add the duration time to the start time and return the result.

If the result will be the next day, it should show (next day) after the time.
If the result will be more than one day later, it should show (n days later)
after the time, where "n" is the number of days later.

If the function is given the optional starting day of the week parameter,
then the output should display the day of the week of the result.
The day of the week in the output should appear after the time and
before the number of days later.

add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)
"""

from datetime import datetime as dt
from datetime import timedelta as td


def add_time(st: str, dur: str, wd: str = None):
    dl = ["sunday",
          "monday",
          "tuesday",
          "wednesday",
          "thursday",
          "friday",
          "saturday",
          ]

    t = dt.strptime(st, "%I:%M %p")
    dh, dm = dur.split(':')
    nt = t + td(hours=int(dh), minutes=int(dm))
    days = (nt.date() - t.date()).days
    ad = "(next day)" if days == 1 else f"({days} days later)" if days else ''
    if wd:
        nwd = (dl.index(wd.lower()) + days) % 7
        return nt.strftime(
            "%-I:%M %p") + ", " + dl[nwd].capitalize() + (f' {ad}' if ad else '')
    return nt.strftime(
        "%-I:%M %p") + (f' {ad}' if ad else '')


print(add_time("9:15 PM", "5:30"))
