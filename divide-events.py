from ics import Calendar
import datetime
import pytz
from os.path import expanduser

CONFIG_PATH = expanduser("~") + "/.config/facebook-events/"

# read in the events downloaded from facebook
with open(CONFIG_PATH + "facebook-events.ics", 'r', newline="\r\n") as my_file:
    lines = my_file.readlines()
    mergedCalendar = Calendar(lines)

calendars = {"ACCEPTED": Calendar(), "NEEDS-ACTION": Calendar(), "TENTATIVE": Calendar(), "TENTATIVE-PAST": Calendar()}

now = pytz.utc.localize(datetime.datetime.utcnow())

# group the events in different calendars based on the action taken
for event in mergedCalendar.events:
    for line in event._unused:
        if line.name == "PARTSTAT":
            goingType = line.value
            break

    event.description = event.description.replace('\r\n', '')

    if goingType == "NEEDS-ACTION":
        if event.end.datetime > now:
            c = calendars[goingType]
            c.events.add(event)
        else:
            print("Unanswered event in the past: " + str(event.begin) + " " + event.name)
    else:
        if goingType == "TENTATIVE":
            if event.end.datetime > now:
                c = calendars[goingType]
                c.events.add(event)
            else:
                c = calendars[goingType + "-PAST"]
                c.events.add(event)
        else:
            c = calendars[goingType]
            c.events.add(event)

for key, value in calendars.items():
    with open(CONFIG_PATH + key + '.ics', 'w') as f:
        f.writelines(value)
