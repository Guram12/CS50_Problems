def convert(time):
    hour, minute = time.split(':')
    hour = int(hour)
    minute = int(minute)
    return hour + minute / 60

def main():
    time_input =(input("enter time"))
    time_in_hours = convert(time_input)
    if 7 <= time_in_hours <= 8:
        print("breakfast time")
    elif 12 <= time_in_hours <= 13:
        print("lunch time")
    elif 18 <= time_in_hours <= 19:
        print("dinner time")
    else:
        pass

if __name__ == "__main__":
    main()