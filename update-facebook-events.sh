curl --silent "<your facebook events url>" -o ~/.config/facebook-events/facebook-events.ics >/dev/null

# if divide-events.py is not in the current folder, then add your path to it here instead of the './'
python ./divide-events.py >/dev/null
