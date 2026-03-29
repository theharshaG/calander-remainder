from datetime import datetime
while True:
    print("\n1. Add Reminder")
    print("2. View All")
    print("3. Search by Date")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        date = input("Enter date (YYYY-MM-DD): ")
        try:
            datetime.strptime(date,"%Y-%m-%d")
        except:
            print("Invalid date format (use YYYY-MM-DD)")
            continue 
        event = input("Enter event: ")
        

        with open("reminder.txt", "a") as file:
            file.write(date + "," + event + "\n")

        print("Reminder added")

    elif choice == "2":
        try:
            with open("reminder.txt", "r") as file:
                print("\n--- Reminders ---")
                for line in file:
                    print(line.strip())
        except FileNotFoundError:
            print("No reminders found")

    elif choice == "3":
        search = input("Enter date (YYYY-MM-DD): ")
        found = False

        try:
            with open("reminder.txt", "r") as file:
                for line in file:
                    date, event = line.strip().split(",")

                    if date == search:
                        print("Event:", event)
                        found = True

            if not found:
                print("No events on this date")

        except FileNotFoundError:
            print("No reminders found")

    elif choice == "4":
        print("Bye")
        break

    else:
        print("Invalid choice")
