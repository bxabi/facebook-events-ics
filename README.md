# Add your facebook events to your calendar, grouped by the paritipation you selected (going, interested, unanswered)

We are not fans of facebook either, but it is still used to publish many events.
This projects lets you download the event list, group them by what you answered about participating in them.
The resulting ics files can be added as separate calendars to your favorite calendar application (as KDE's KOrganizer for example).

# Requirements:
- cron or other system which executes a command regularly
- curl
- python (3)
- a calendar capable of displaying ics files (and update the events ehen the files change)

# Steps:

1. Find the link to your facebook events ics file:
- open https://www.facebook.com/events/hosting/ in the browser
- right click to "Upcoming Events", and copy the link location.

2. Clone this repository

3. Run 
`pip install -r requirements.txt` for global install
or `pip install --user -r requirements.txt` to install just for your user

4. Insert your event list url (link) in the update-facebook-events.sh

5. Add it to your cron to run regularly (every 15 min. for example). This will keep your events calendar up to date.

6. Add the calendars created by the script to your calendar. You will find them in the ~/.config/facebook-events folder.


# Possible TODO:
For KDE users to make the setup easier, it would be possible to provide this functionality as an Akonadi resource. (Akonadi has a facebook events resource already but it doesn't work)
