import csv

def caculate_time(hour, minute, delta):
    minute += delta
    if minute >= 60:
        hour += 1
        minute -= 60
    elif minute < 0:
        hour -= 1
        minute += 60
    return hour, minute

# 셔틀콕 기준 배차 간격, 시간, 행선
timetable_interval_weekdays = [
    (10, 0, 10, 30, 5, "DH", "Dormitory"), (10, 40, 11, 0, 10, "DH", "Dormitory"), (11, 15, 12, 0, 15, "DH", "Dormitory"), (12, 10, 12, 50, 10, "DH", "Dormitory"), (13, 15, 14, 45, 30, "DH", "Dormitory"),
    (15, 10, 16, 0, 10, "DH", "Dormitory"), (16, 6, 18, 24, 6, "DH", "Dormitory"), (18, 40, 18, 50, 10, "DH", "Dormitory"),
    (8, 0, 8, 20, 5, "DH", "Shuttlecock"), (8, 23, 8, 50, 3, "DH", "Shuttlecock"), (8, 55, 9, 20, 5, "DH", "Shuttlecock"), (9, 23, 9, 50, 3, "DH", "Shuttlecock"), (9, 55, 9, 55, 1, "DH", "Shuttlecock"),
    (8, 20, 9, 50, 30, "DY", "Shuttlecock"), (10, 20, 12, 20, 30, "DY", "Dormitory"), (16, 0, 17, 30, 30, "DY", "Dormitory"),
    (7, 50, 7, 50, 1, "C", "Dormitory"), (13, 0, 15, 30, 30, "C", "Dormitory"), (18, 0, 18, 30, 30, "C", "Dormitory"), (19, 0, 21, 30, 10, "C", "Dormitory"), (21, 45, 23, 0, 15, "C", "Dormitory")
]
timetable_interval_weekends = [(8, 50, 21, 50, 30, "C", "Dormitory")]

timetable_weekdays = {}
timetable_weekends = {}

for x in timetable_interval_weekdays:
    start_hour, start_minute, end_hour, end_minute, interval, heading, start_stop = x
    hour = start_hour
    minute = start_minute
    while hour <= end_hour or minute <= end_minute:
        if f"{str(hour).zfill(2)}:{str(minute).zfill(2)}" not in timetable_weekdays.keys():
            timetable_weekdays[f"{str(hour).zfill(2)}:{str(minute).zfill(2)}"] = []
        if f"{str(hour).zfill(2)}:{str(minute).zfill(2)}" in timetable_weekdays.keys() and heading == "C":
            timetable_weekdays[f"{str(hour).zfill(2)}:{str(minute).zfill(2)}"] = [{"heading": heading, "startStop": start_stop}]
        else:
            timetable_weekdays[f"{str(hour).zfill(2)}:{str(minute).zfill(2)}"].append({"heading": heading, "startStop": start_stop})
        hour, minute = caculate_time(hour, minute, interval)
        if hour > end_hour or (hour == end_hour and minute > end_minute):
            break

a_list = []
for key, value in timetable_weekdays.items():
    for item in value:
        a_list.append([item["heading"], key, item["startStop"]])
with open("./semester/week.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(sorted(a_list, key=lambda x: x[1]))

for x in timetable_interval_weekends:
    start_hour, start_minute, end_hour, end_minute, interval, heading, start_stop = x
    hour = start_hour
    minute = start_minute
    while hour <= end_hour or minute <= end_minute:
        if f"{str(hour).zfill(2)}:{str(minute).zfill(2)}" not in timetable_weekends.keys():
            timetable_weekends[f"{str(hour).zfill(2)}:{str(minute).zfill(2)}"] = []
        if f"{str(hour).zfill(2)}:{str(minute).zfill(2)}" in timetable_weekends.keys() and heading == "C":
            timetable_weekends[f"{str(hour).zfill(2)}:{str(minute).zfill(2)}"] = [{"heading": heading, "startStop": start_stop}]
        else:
            timetable_weekends[f"{str(hour).zfill(2)}:{str(minute).zfill(2)}"].append({"heading": heading, "startStop": start_stop})
        hour, minute = caculate_time(hour, minute, interval)
        if hour > end_hour or (hour == end_hour and minute > end_minute):
            break

a_list = []
for key, value in timetable_weekends.items():
    for item in value:
        a_list.append([item["heading"], key, item["startStop"]])

with open("./semester/weekend.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(sorted(a_list, key=lambda x: x[1]))
