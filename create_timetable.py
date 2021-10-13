import json

def caculate_time(hour, minute, delta):
    minute += delta
    if minute >= 60:
        hour += 1
        minute -= 60
    elif minute < 0:
        hour -= 1
        minute += 60
    return hour, minute

# 한대앞역 기준 배차 간격, 시간, 행선
timetable_interval_weekdays = [(8, 0, 22, 0, 30, "C"), (8, 10, 10, 30, 5, "DH"), (10, 40, 14, 50, 10, "DH"), (15, 00, 17, 20, 5, "DH"), (17, 40, 18, 50, 10, "DH")]
timetable_interval_weekends = [(8, 0, 22, 0, 60, "C")]

timetable_weekdays = {}
timetable_weekends = {}

for x in timetable_interval_weekdays:
    start_hour, start_minute, end_hour, end_minute, interval, heading = x
    hour = start_hour
    minute = start_minute
    while hour <= end_hour or minute <= end_minute:
        if f"{str(hour).zfill(2)}:{str(minute).zfill(2)}" in timetable_weekdays.keys() and heading == "C":
            timetable_weekdays[f"{str(hour).zfill(2)}:{str(minute).zfill(2)}"] = heading
        elif f"{str(hour).zfill(2)}:{str(minute).zfill(2)}" not in timetable_weekdays.keys():
            timetable_weekdays[f"{str(hour).zfill(2)}:{str(minute).zfill(2)}"] = heading
        hour, minute = caculate_time(hour, minute, interval)
        if hour > end_hour or (hour == end_hour and minute > end_minute):
            break

a_list = []
for key, value in timetable_weekdays.items():
    a_list.append({"time": key, "type": value})

with open("D:\\Projects\\hyuabot-backend-golang\\shuttle\\timetable\\semester\\week.json", "w") as f:
    json.dump(sorted(a_list, key=lambda x: x["time"]), f, indent=4, sort_keys=True)

for x in timetable_interval_weekends:
    start_hour, start_minute, end_hour, end_minute, interval, heading = x
    hour = start_hour
    minute = start_minute
    while hour <= end_hour or minute <= end_minute:
        if f"{str(hour).zfill(2)}:{str(minute).zfill(2)}" in timetable_weekends.keys() and heading == "C":
            timetable_weekends[f"{str(hour).zfill(2)}:{str(minute).zfill(2)}"] = heading
        elif f"{str(hour).zfill(2)}:{str(minute).zfill(2)}" not in timetable_weekends.keys():
            timetable_weekends[f"{str(hour).zfill(2)}:{str(minute).zfill(2)}"] = heading
        hour, minute = caculate_time(hour, minute, interval)
        if hour > end_hour or (hour == end_hour and minute > end_minute):
            break

a_list = []
for key, value in timetable_weekends.items():
    a_list.append({"time": key, "type": value})

with open("D:\\Projects\\hyuabot-backend-golang\\shuttle\\timetable\\semester\\weekend.json", "w") as f:
    json.dump(sorted(a_list, key=lambda x: x["time"]), f, indent=4, sort_keys=True)