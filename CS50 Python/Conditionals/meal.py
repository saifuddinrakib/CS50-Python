def main():
    answer = input("What time is it? ")
    time = convert(answer)

    if 7.0 <= time <= 8.0:
        print("breakfast time")
    elif 12.0 <= time <= 13.0:
        print("lunch time")
    elif 18.0 <= time <= 19.0:
        print("dinner time")

# Conversion function
def convert(time):
    # Split the time string into hours and minutes
    hours, minutes = time.split(":")

    # Convert minutes to hours in decimal form (e.g., 30 minutes = 0.5 hours)
    new_minute = float(minutes) / 60

    # Return the total time in hours
    return float(hours) + new_minute

if __name__ == "__main__":
    main()
