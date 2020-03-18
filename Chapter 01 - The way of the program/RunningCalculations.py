#If you run a 10 kilometer race in 43 minutes 30 seconds, what is your average time per mile? What is your average speed in miles per hour?

distance = int(input("How many kilometers will you be running?"))
time = int(input("How many minutes did it take you?"))

average_pace = distance / time

print(f"You ran {distance} kilometer ran in {time} minutes.  Your average {average_pace:.2f} kilometers per minute")