#Ex. 1 - Next day's date.
'''
Напишете програма на Python, за да получите следващия ден от дадена дата (въведена от потребителя).
'''

try:
    year = int(input("Input a year: "))
    month = int(input("Input a month [1-12]: "))
    day = int(input("Input a day [1-31]: "))

    if month < 1 or month > 12:
        print("Error: Month must be between 1 and 12.")

    if day < 1 or day > 31:
        print("Error: Day must be between 1 and 31.")

    is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    if month in [1, 3, 5, 7, 8, 10, 12]:
        days_in_month = 31
    elif month in [4, 6, 9, 11]:
        days_in_month = 30
    elif month == 2:
        if is_leap:
            days_in_month = 29
        else:
            days_in_month = 28
    
    if day > days_in_month:
        print(f"Error: Month {month} only has {days_in_month} days.")
    else:
        day += 1

        if day > days_in_month:
            day = 1
            month += 1
            
            if month > 12:
                month = 1
                year += 1

        print(f"The next date is [yyyy-mm-dd] {year}-{month}-{day}")

except ValueError:
    print("Invalid Input! Please enter only whole numbers (integers).")