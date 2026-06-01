# Initial setup
total_seats = 350
remaining_seats = total_seats

total_bookings = 0
tickets_sold = 0
rejected_bookings = 0

while True:
    print("\nAvailable seats:", remaining_seats)

    # Input number of tickets
    tickets = int(input("Enter number of tickets (0 to exit): "))

    # Exit condition
    if tickets == 0:
        break

    # Check ticket limit
    if tickets < 1 or tickets > 15:
        print("Invalid number of tickets (1-15 allowed)")
        continue

    # Check seat availability
    if tickets > remaining_seats:
        print("Not enough seats available")
        continue

    valid_booking = True
    ages = []

    # Input ages
    for i in range(tickets):
        age = int(input(f"Enter age of person {i+1}: "))

        if age < 12:
            valid_booking = False
            continue   # skip invalid age but continue loop

        ages.append(age)

    # Booking decision
    if valid_booking and len(ages) == tickets:
        print(f"BOOKING CONFIRMED - {tickets} tickets")
        total_bookings += 1
        tickets_sold += tickets
        remaining_seats -= tickets
    else:
        print("BOOKING REJECTED - Age restriction")
        rejected_bookings += 1

    # Stop if theatre full
    if remaining_seats == 0:
        print("Theatre is fully booked!")
        break

# Final Report
print("\n--- FINAL REPORT ---")
print("Total Bookings:", total_bookings)
print("Total Tickets Sold:", tickets_sold)
print("Rejected Bookings:", rejected_bookings)
print("Remaining Seats:", remaining_seats)