

def get_hours():
    hours = []

    for day in range(1,6):
        worked = float(input(f"Enter Hours for day {day}: "))
        hours.append(worked)

    return hours

def display_highest_hours(hours):
    highest = max(hours)

    print("Day(s) with the most hours worked: ")

    for day, worked in enumerate(hours,start=1):
        if worked == highest:
            print(f"Day {day} - {worked} hours")


def display_total_average(hours):
    total = sum(hours)
    average = total / len(hours)

    print(f"Total hours worked: {total}")
    print(f"Average hours worked: {average:.2f}")


def display_insufficent_hours(hours):
    print("Days with less than 7 hours worked: ")

    found = False

    for day, worked in enumerate(hours, start=1):
        if worked < 7:
            print(f"Day {day} - {worked} hours")
            found = True

    if not found:
        print("None")

def main():
    print("Welcome to the Time Sheet program!")

    hours = get_hours()

    display_highest_hours(hours)
    display_total_average(hours)
    display_insufficent_hours(hours)

main()