from ics import Calendar
import datetime
import pytz
from os.path import expanduser
import re

CONFIG_PATH = expanduser("~") + "/.config/facebook-events/"

# read in the events downloaded from facebook
with open(CONFIG_PATH + "facebook-events.ics", 'r', newline="\r\n") as my_file:
    fileContent = my_file.read()
    # put the Organizer CN in quotes - because if it contains \, the parser fails.
    fileContent = re.sub("ORGANIZER;CN=(.*):MAILTO:", 'ORGANIZER;CN="\\1":MAILTO:', fileContent)
    mergedCalendar = Calendar(fileContent)

calendars = {"ACCEPTED": Calendar(), "NEEDS-ACTION": Calendar(), "TENTATIVE": Calendar(), "TENTATIVE-PAST": Calendar()}

now = pytz.utc.localize(datetime.datetime.utcnow())

# group the events in different calendars based on the action taken
for event in mergedCalendar.events:
    for line in event.extra:
        if line.name == "PARTSTAT":
            goingType = line.value
            break

    #event.description = event.description.replace('\r\n', '')

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
