# I'm redoing this but with much simpler everything (12/14/23)

def time_calculator(start_time="12:00 AM", duration="0:0", start_day_of_week=""):
    # We first need to know our start time in minutes
    x = start_time.replace(":", " ")
    start_hours, start_minutes, start_meridian = x.split()
    total_start_minutes = (int(start_hours) * 60) + int(start_minutes)
    if start_meridian == "PM":
        total_start_minutes += 720
    if start_hours == "12":
        total_start_minutes -= 720

    # We then need to know our duration in minutes and the resulting,
    # added time, in units of days, hours, and minutes.
    dur_hours, dur_minutes = duration.split(":")
    total_dur_minutes = (int(dur_hours) * 60) + int(dur_minutes)
    new_time = total_dur_minutes + total_start_minutes
    new_time_temp = 0 + new_time
    new_days = new_time_temp // 1440
    new_hours = (new_time_temp % 1440) // 60
    display_hours = new_hours
    if display_hours == 0:
        display_hours += 12
    elif display_hours > 12:
        display_hours -= 12
    new_minutes = ((new_time_temp % 1440) % 60)
    display_minutes = new_minutes
    if new_minutes < 10:
        display_minutes = str(new_minutes).zfill(2)

    # We now need the new meridian
    total_new_minutes = new_hours * 60 + new_minutes
    new_meridian = "AM" if total_new_minutes < 720 else "PM"

    # We now need to calculate what day it is
    day_dict = {"Monday": 1, "Tuesday": 2, "Wednesday": 3,
                "Thursday": 4, "Friday": 5, "Saturday": 6,
                "Sunday": 7}
    new_day_of_week = ""
    if start_day_of_week.title() in day_dict:
        start_day_value = day_dict[start_day_of_week.title()]
        new_day_value = start_day_value + new_days
        new_day_value_temp = 0 + new_day_value
        while new_day_value_temp > 7:
            new_day_value_temp -= 7
        for day_of_week, day_value in day_dict.items():
            if new_day_value_temp == day_value:
                new_day_of_week = day_of_week

    return f'{display_hours}:{display_minutes} {new_meridian}, {new_day_of_week} ({new_days} days later)'


print(time_calculator("2:53 PM", "0:08", "Tuesday"))
