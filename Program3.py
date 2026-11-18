
def get_guides():

    guides = []

    guide_count = int(input("How many guides sold cookies?: "))

    for number in range(1, guide_count + 1):
        name = input(f"Enter the name of guide {number}: ")
        boxes = int(input("Enter the nuumber of boxes sold: "))

        guides.append([name,boxes])

    return guides

def calculate_average(guides):
    total = 0

    for guide in guides:
        total += guide[1]

    return total / len(guides)

def get_highest_sales(guides):
    highest = 0

    for guide in guides:
        if guide[1] > highest:
            highest = guide[1]

    return highest

def display_results(guides, average, highest):
    print(f"Average boxes sold: {average:.2f}")
    print("Guide Prizes: ")

    for guide in guides:
        name = guide[0]
        boxes = guide[1]

        if boxes == 0:
            prize = "No prize"

        elif boxes == highest:
            prize = "Trip to Girl Guide Jamboree"

        elif boxes > average:
            prize = "Badge"

        else:
            prize = "Share of the remaining cookies"

        print(f"{name}: {boxes} boxes - {prize}")

def main():
    print("Welcome to the Girl Guide Cookie Sell off!")

    guides = get_guides()

    if len(guides) == 0:
        print("No guides entered")
        return

    average = calculate_average(guides)
    highest = get_highest_sales(guides)

    display_results(guides, average, highest)


main()