minutes_control = int(input())
seconds_control = int(input())
length = float(input())
seconds_for_100_meters = int(input())

all_seconds = (minutes_control * 60) + seconds_control
time_reduction = (length / 120) / 2.5
Petar_time = all_seconds + time_reduction

if Petar_time < (length * seconds_for_100_meters):
    print("Petar Mitsin won an Olympic quota!")
    print(f"His time is {Petar_time:.3f}.")
else:
    time_difference = Petar_time - (length * seconds_for_100_meters)
    print(f"No, Petar failed! He was {time_difference:.3f} second slower.")
    