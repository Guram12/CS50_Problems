from datetime import date, datetime
import inflect
import sys

def main():
    user = input("Date of birth (YYYY-MM-DD): ")
    try:
        current_time = date.today()
        converted_user = datetime.fromisoformat(user).date()  # Convert string to datetime object
        time_difference = subtract_minutes(converted_user, current_time)
        converted_difference = convert(time_difference)
        print(converted_difference)
    except ValueError:
        sys.exit("Wrong format")

def convert(minutes):
    p = inflect.engine()
    words = p.number_to_words(int(minutes), andword="")
    words = words.replace(" and", ",")  # Remove "and" conjunction
    words = words.capitalize()
    words = words + " minutes"
    return words

def subtract_minutes(td1, td2):
    delta = td2 - td1
    minutes = delta.total_seconds() / 60
    return minutes

if __name__ == "__main__":
    main()

















