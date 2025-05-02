
print("hello world")
speed = int(input("Enter driver's speed: "))

if speed < 5:
    print("Speed too low or invalid input.")
elif speed >= 75:
    print("Issue speeding fine")
elif speed > 60:
    print("Issue warning")
else:
    print("No action")
