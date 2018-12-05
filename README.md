# Add your facebook events to your calendar, grouped by the paritipation you selected (going, interested, unanswered)

We are not fans of facebook either, but it is still used to publish many events.
This projects lets you download the event list, group them by what you answered about participating in them.
The resulting ics files can be added as separate calenders to your favorite calendar application (as KDE's KOrganizer for example).

# Requirements:
- cron or other system which executes a command regularly
- curl
- python (3)
- a calendar capable of displaying ics files (and update the events ehen the files change)

# Steps:

1. Find the link to your facebook events ics file:
- open https://www.facebook.com/events/hosting/ in the browser
- right click to "Upcoming Events", and copy the link location.

2. Dowload the update-events.sh and the divide-events.py files from this git repository.

2. Insert your event list url (link) in the update-facebook-events.sh

3. Add it to your cron to run regularly (every 15 min. for example). This will keep your events calendar up to date.

4. Add the calendars created by the script to your calendar. You will find them in the ~/.config/facebook-events folder.
