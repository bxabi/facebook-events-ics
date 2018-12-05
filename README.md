# facebook-events-ics
Add your facebook events to your calendar, grouped by the paritipation you selected (going, interested, unanswered)

We are not fans of facebook either, but it is still used to publish many events.
This projects lets you download the event list, group them by what you answered about participating in them.
The resulting ics files can be added as separate calenders to your favorite calendar application (as KDE's KOrganizer for example).

Find the link to your facebook events ics file:
- open https://www.facebook.com/events/hosting/ in the browser
- right click to "Upcoming Events", and copy the link location.

update-facebook-events.sh: Bash script which can be added to cron to periodically download the facebook events.
divide-events.ics: Creates 4 calendar files based on the one downloaded from facebook.
