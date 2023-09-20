# Taking User Name
name = input("Enter your name:\n")

# Taking the time
time = int(input("Enter what time is it:\n"))

# Setting the Greeting
greet = "Good"

if time<=11:
    print(greet, "Morning", name)
elif time>11 and time<=14:
    print(greet, "Noon", name)
elif time>14 and time<=16:
    print(greet, "Afternoon", name)
elif time>16 and time<=19:
    print(greet, "Evening", name)
elif time>19 and time<=24:
    print(greet, "Night", name)
else:
    print("Invalid Time Format")

