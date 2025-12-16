#Ex. 5
'''
Напишете програма, в която се създава списък с М на брой
елементи, като М се въвежда от потребителя и М е цяло число между
15 и 45 (15 =< М <= 45). 

Да се провери входа (дали условието "15 =< М <= 45" е изпълнено). 
Списъкьт се запълва с положителни цели числа от потребителя, като числата трябва да са в 
интервала от 50 до 350 включително и да не се повтарят.

Да се намери броят на елементите от този списък с нечетна стойност;

Да се намери индекса на елемента с максимална четна стойност от този списък;

Да се създаде втори списък и в него да се включват тези
елементи от първия списък, които са кратни на 3;

Да се намери сумата на елементите от втория списък;

Да се изтрият всички елементи от втория списък с нечетен
индекс.
'''

m = 0
while True:
    try:
        user_input = input("Enter M (between 15 and 45): ")
        m = int(user_input)
        
        if 15 <= m <= 45:
            break
        else:
            print("Invalid input! M must be between 15 and 45.")
            
    except ValueError:
        print("Please enter a valid integer.")

# Rules: 50 <= number <= 350 and No duplicates
list_1 = []
print(f"Please enter {m} unique numbers (between 50-350):")

while len(list_1) < m:
    try:
        num = int(input(f"Enter number {len(list_1) + 1}/{m}: "))
        
        # Check range
        if num < 50 or num > 350:
            print("Number must be between 50 and 350.")
            continue
            
        # Check for duplicates
        if num in list_1:
            print("Number already exists in list. No duplicates allowed.")
            continue
            
        list_1.append(num)

    except ValueError:
        print("Please enter a valid integer.")

print(f"\nList 1: {list_1}")

# --- Count odd numbers ---
count_odd = 0
for num in list_1:
    if num % 2 != 0:
        count_odd += 1

print(f"Count of odd elements: {count_odd}")

# --- Index of element with Maximum EVEN value ---
max_even_val = -1
max_even_index = -1

for i in range(len(list_1)):
    num = list_1[i]
    
    if num % 2 == 0:
        if num > max_even_val:
            max_even_val = num
            max_even_index = i

if max_even_index != -1:
    print(f"Max even value is {max_even_val} at index: {max_even_index}")
else:
    print("No even numbers found in the list.")

# --- Create List 2 (Elements from List 1 divisible by 3) ---
list_2 = []
for num in list_1:
    if num % 3 == 0:
        list_2.append(num)

print(f"List 2 (Divisible by 3): {list_2}")

# --- Sum of List 2 ---
sum_list_2 = 0
for num in list_2:
    sum_list_2 += num

print(f"Sum of List 2: {sum_list_2}")

# --- Delete elements with Odd Indices from List 2 ---
final_list = []
for i in range(len(list_2)):
    if i % 2 == 0:
        final_list.append(list_2[i])

list_2 = final_list

print(f"List 2 after removing odd indices: {list_2}")