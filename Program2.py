def redact_message(message, letters):
    redacted_message = ""
    removed_count = 0

    for character in message:
        if character.lower() in letters:
            redacted_message += "_"
            removed_count += 1
        else:
            redacted_message += character

    return redacted_message, removed_count

def main():

    while True:

        message = input("Type a phrase or 'quit' to exit the program: ")

        if message.lower().strip() == "quit":
            break

        letters = input("Enter letters to redact, seperated by commas: ")
        letters = letters.lower().replace(" ", "").split(",")

        redacted_message, remove_count = redact_message(message,letters)

        print(f"Redacted message: {redacted_message}")
        print(f"Number of letters removed: {remove_count}")

    print("Thank you, goodbye!")


main()