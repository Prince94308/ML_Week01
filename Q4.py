#Task-4
temperatures = []

print("Enter temperatures for 5 days:")

i = 1
while i <= 5:
    temp_input = input("Day {} temperature: ".format(i))
    
    if temp_input.replace('.', '', 1).isdigit():
        temp = float(temp_input)
        temperatures.append(temp)
        i += 1
    else:
        print("Invalid input. Please enter a number.")


total = 0
for t in temperatures:
    total += t

average = total / len(temperatures)

print("\nTemperatures entered:", temperatures)
print("Average temperature over 5 days: {:.2f}°C".format(average))


