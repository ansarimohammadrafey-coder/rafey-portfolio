print("===================================")
print("   SOCIETY MAINTENANCE MANAGEMENT")
print("===================================")

residents = {}

while True:

    print("\n========== MENU ==========")
    print("1. Add Resident")
    print("2. View Residents")
    print("3. Search Resident")
    print("4. Pay Maintenance")
    print("5. View Pending Payments")
    print("6. View Society Summary")
    print("7. Exit")
    print("==========================")

    choice = input("Enter your choice: ")

    # Add Resident
    if choice == "1":

        flat = input("Enter flat number: ")
        name = input("Enter resident name: ")
        phone = input("Enter phone number: ")
        maintenance = float(input("Enter monthly maintenance amount: "))

        residents[flat] = {
            "name": name,
            "phone": phone,
            "maintenance": maintenance,
            "status": "Pending"
        }

        print("Resident added successfully!")

    # View Residents
    elif choice == "2":

        print("\n========== RESIDENTS ==========")

        if not residents:
            print("No residents found.")

        else:
            for flat, details in residents.items():

                print("\nFlat Number:", flat)
                print("Name:", details["name"])
                print("Phone:", details["phone"])
                print("Maintenance:", details["maintenance"])
                print("Status:", details["status"])

    # Search Resident
    elif choice == "3":

        flat = input("Enter flat number to search: ")

        if flat in residents:

            details = residents[flat]

            print("\n========== RESIDENT DETAILS ==========")
            print("Flat Number:", flat)
            print("Name:", details["name"])
            print("Phone:", details["phone"])
            print("Maintenance:", details["maintenance"])
            print("Status:", details["status"])

        else:
            print("Resident not found.")

    # Pay Maintenance
    elif choice == "4":

        flat = input("Enter flat number: ")

        if flat in residents:

            residents[flat]["status"] = "Paid"

            print("Maintenance payment marked as Paid.")

        else:
            print("Resident not found.")

    # Pending Payments
    elif choice == "5":

        print("\n========== PENDING PAYMENTS ==========")

        found = False

        for flat, details in residents.items():

            if details["status"] == "Pending":

                print(
                    "Flat:",
                    flat,
                    "| Name:",
                    details["name"],
                    "| Amount:",
                    details["maintenance"]
                )

                found = True

        if not found:
            print("No pending payments.")

    # Society Summary
    elif choice == "6":

        total_residents = len(residents)
        paid = 0
        pending = 0
        total_collection = 0
        total_pending = 0

        for details in residents.values():

            if details["status"] == "Paid":

                paid += 1
                total_collection += details["maintenance"]

            else:

                pending += 1
                total_pending += details["maintenance"]

        print("\n========== SOCIETY SUMMARY ==========")
        print("Total Residents:", total_residents)
        print("Paid Residents:", paid)
        print("Pending Residents:", pending)
        print("Total Collection:", total_collection)
        print("Total Pending:", total_pending)

    # Exit
    elif choice == "7":

        print("Thank you for using Society Maintenance Management!")
        break

    else:

        print("Invalid choice! Please try again.")