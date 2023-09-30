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
    (8, 0, 8, 0, 30, "C", "dormitory_o", "dormitory_i"), 
    (8, 10, 9, 0, 5, "DH", "dormitory_o", "dormitory_i"), 
    (9, 10, 9, 50, 10, "DH", "dormitory_o", "dormitory_i"), 
    (10, 0, 18, 50, 10, "DH", "dormitory_o", "dormitory_i"), 
    (13, 0, 15, 30, 30, "C", "dormitory_o", "dormitory_i"), 
    (18, 0, 18, 30, 30, "C", "dormitory_o", "dormitory_i"), 
    (19, 0, 22, 0, 15, "C", "dormitory_o", "dormitory_i"), 
    (8, 20, 9, 50, 30, "DY", "dormitory_o", "dormitory_i"), 
    (10, 20, 12, 20, 30, "DY", "dormitory_o", "dormitory_i"), 
    (16, 0, 17, 30, 30, "DY", "dormitory_o", "dormitory_i"),
]
timetable_interval_weekends = [(8, 50, 21, 50, 30, "C", "dormitory_o", "dormitory_i")]

timetable_weekdays = {}
timetable_weekends = {}

for start_hour, start_minute, end_hour, end_minute, interval, heading, start_stop, end_stop in timetable_interval_weekdays:
    hour = start_hour
    minute = start_minute
    while hour <= end_hour or minute <= end_minute:
        if f"{str(hour).zfill(2)}:{str(minute).zfill(2)}" not in timetable_weekdays.keys():
            timetable_weekdays[f"{str(hour).zfill(2)}:{str(minute).zfill(2)}"] = []
        if f"{str(hour).zfill(2)}:{str(minute).zfill(2)}" in timetable_weekdays.keys() and heading == "C":
            timetable_weekdays[f"{str(hour).zfill(2)}:{str(minute).zfill(2)}"] = [{"heading": heading, "startStop": start_stop, "endStop": end_stop}]
        else:
            timetable_weekdays[f"{str(hour).zfill(2)}:{str(minute).zfill(2)}"].append({"heading": heading, "startStop": start_stop, "endStop": end_stop})
        hour, minute = caculate_time(hour, minute, interval)
        if hour > end_hour or (hour == end_hour and minute > end_minute):
            break

a_list = []
for key, value in timetable_weekdays.items():
    for item in value:
        a_list.append([item["heading"], key, item["startStop"], item["endStop"]])
with open("./vacation_session/week.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(sorted(a_list, key=lambda x: x[1]))

for start_hour, start_minute, end_hour, end_minute, interval, heading, start_stop, end_stop in timetable_interval_weekends:
    hour = start_hour
    minute = start_minute
    while hour <= end_hour or minute <= end_minute:
        if f"{str(hour).zfill(2)}:{str(minute).zfill(2)}" not in timetable_weekends.keys():
            timetable_weekends[f"{str(hour).zfill(2)}:{str(minute).zfill(2)}"] = []
        if f"{str(hour).zfill(2)}:{str(minute).zfill(2)}" in timetable_weekends.keys() and heading == "C":
            timetable_weekends[f"{str(hour).zfill(2)}:{str(minute).zfill(2)}"] = [{"heading": heading, "startStop": start_stop, "endStop": end_stop}]
        else:
            timetable_weekends[f"{str(hour).zfill(2)}:{str(minute).zfill(2)}"].append({"heading": heading, "startStop": start_stop, "endStop": end_stop})
        hour, minute = caculate_time(hour, minute, interval)
        if hour > end_hour or (hour == end_hour and minute > end_minute):
            break

a_list = []
for key, value in timetable_weekends.items():
    for item in value:
        a_list.append([item["heading"], key, item["startStop"], item["endStop"]])

with open("./vacation_session/weekend.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(sorted(a_list, key=lambda x: x[1]))
