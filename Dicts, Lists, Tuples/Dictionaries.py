student_grades = [90.1, 80.8, 75.5]                     #Lists
studentgrades = {"Mary": 90.1, "Aaron": 808., "John": 7.5} 
temperatures = {"Monday": 94, "Tuesday": 89}            #Dictionaries

mysum = sum(student_grades)
length = len(student_grades)
mean = mysum / length
print(mean)


monday_temps = (90, 92, 89)             #Tuple - like a list but cannot add to it
print(monday_temps)   
color_codes = ((9, 10, 11), (12, 13, 14))   #Tuples inside of tuple
print(color_codes)

monday_temps2 = [90, 92, 89]            #Adding values to list using append
monday_temps2.append(94)
print(monday_temps2)

#Task - assign a dictionary to variable 'day_temperatures'. The dictionary
#should contain 3 keys, and each key should contain a tuple as value. Each
#tuple should contain three floats.

day_temperatures = {"morning": (1.1, 2.3, 3.4), "noon": (4.4, 5.5, 6.7), "evening": (6.5, 4.5, 9.0)}
print(day_temperatures)

