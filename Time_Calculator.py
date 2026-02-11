def add_time(start_time, duration_time, day_of_week=""):
    x = start_time.replace(':', " ")
    x = x.split()
    hours, minutes, meridian = x
    if meridian == "PM" and hours != "12":
        total_minutes = (int(hours) * 60) + (int(minutes)) + (12 * 60)
    elif meridian == "AM" and hours != "12" or (meridian == "PM" and hours == "12"):
        total_minutes = (int(hours) * 60) + (int(minutes))
    else:
        total_minutes = (int(minutes))

    dur_hours, dur_minutes = duration_time.split(":")
    total_duration_minutes = (int(dur_hours) * 60) + (int(dur_minutes))
    result_time = total_duration_minutes + total_minutes
    result_hours = (result_time // 60)
    result_hours2 = result_hours
    result_minutes = (result_time % 60)
    result_meridian = ""
    result_days = 0
    if result_hours > 24:
        result_days = (result_time // 1440)
        result_hours = result_hours % 24
        if 12 < result_hours <= 24:
            result_hours = result_hours - 12
        elif result_hours == 0:
            result_hours = result_hours + 12
    elif 12 < result_hours <= 24:
        result_hours = result_hours - 12
        if result_hours == 0:
            result_hours = result_hours + 12
    elif result_hours == 0:
        result_hours = result_hours + 12
    if result_minutes < 10:
        result_minutes = f'0{result_minutes}'

    day_dict = {"Monday": 1, "Tuesday": 2, "Wednesday": 3,
                "Thursday": 4, "Friday": 5, "Saturday": 6,
                "Sunday": 7, }
    day_value = 0
    if day_of_week.title() in day_dict:
        day_value = day_dict[day_of_week.title()]
    new_day = day_value + result_days
    new_day_higher = new_day
    while new_day > 7:
        new_day = new_day - 7
    for key, value in day_dict.items():
        if new_day == value and day_of_week != '':
            day_of_week = key

    total_minutes2 = (result_hours2 * 60) + int(result_minutes)
    while total_minutes2 > 1440:
        total_minutes2 = total_minutes2 - 1440

    if ((total_minutes2 < 720 < total_minutes or
            total_minutes2 > 720 > total_minutes) or
            (result_hours == 12 and hours != 12)):
        if meridian == "AM":
            result_meridian = "PM"
        elif meridian == "PM":
            result_meridian = "AM"
    else:
        result_meridian = meridian
    if day_of_week == "":
        if ((new_day - day_value) == 1 or
                ((new_day - day_value) == 0 and meridian == "PM"
                 and result_meridian == "AM")):
            return f'{result_hours}:{result_minutes} {result_meridian} (next day)'
        elif (new_day - day_value) > 1:
            return (f'{result_hours}:{result_minutes} {result_meridian}'
                    f' ({new_day_higher - day_value} days later)')
        else:
            return f'{result_hours}:{result_minutes} {result_meridian}'
    else:
        if ((new_day - day_value) == 1 or
                ((new_day - day_value) == 0 and meridian == "PM"
                 and result_meridian == "AM")):
            return f'{result_hours}:{result_minutes} {result_meridian}, {day_of_week} (next day)'
        elif (new_day_higher - day_value) > 1:
            return (f'{result_hours}:{result_minutes} '
                    f'{result_meridian}, {day_of_week} ({new_day_higher - day_value} days later)')
        else:
            return f'{result_hours}:{result_minutes} {result_meridian}, {day_of_week}'
