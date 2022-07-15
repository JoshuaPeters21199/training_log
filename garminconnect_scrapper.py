import datetime
# import pandas - Having troubles installing pandas library on macbook

from garminconnect import (
    Garmin,
)

#why wont I push

# Login to Garmin connect
inp_username = input('Username/Email: ')
inp_password = input('Password: ')
api = Garmin(inp_username, inp_password)
api.login()

# Get data from past activities
start_date = input("\nType the start date and end date for the running data you would like to receive.\nStart Date('YYYY-MM-DD'): ")
end_date = input("End Date('YYYY-MM-DD): ")
activities = api.get_activities_by_date(start_date, end_date)
for i in range(len(activities)):
    get_activity_info = activities[i]
    date = get_activity_info['startTimeLocal']
    distance = round(get_activity_info['distance'] / 1609.34, 2)

    # Calculate pace
    duration = datetime.timedelta(seconds=get_activity_info['duration'])
    # pace = pandas.to_datetime(duration / distance).round('1s')
    pace = duration / distance

    elevation_gain = round(get_activity_info['elevationGain'])
    elevation_loss = round(get_activity_info['elevationLoss'])
    print(f"\nDate: {date}\nDistance: {distance} mi\nDuration: {duration}\nPace: {pace} min/mi\nElevation Gain: {elevation_gain}ft\nElevation Loss: {elevation_loss}ft")