def get_name():
    name = input("Enter your name: ").strip()
    return name if name else "Friend"


def get_age():
    while True:
        age_str = input("Enter your age: ").strip()
        if not age_str:
            print("Age cannot be empty. Please enter a number.")
            continue
        try:
            age = int(age_str)
            if age < 0:
                print("Age can't be negative. Try again.")
                continue
            return age
        except ValueError:
            print("Please enter a valid integer for age.")


def main():
    name = get_name()
    age = get_age()

    # Using + operator
    print("\nUsing + operator:")
    print("Hello, " + name + ". You are " + str(age) + " years old.")

    # Using f-string
    print("\nUsing f-string:")
    print(f"Hello, {name}. You are {age} years old.")


if __name__ == "__main__":
    main()
