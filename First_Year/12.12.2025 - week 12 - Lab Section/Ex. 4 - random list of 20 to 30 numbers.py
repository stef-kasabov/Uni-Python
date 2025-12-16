#Ex. 4
'''
Зад. 4. Напишете програма, в която се създава числов списък с n на
брой елементи, като n се въвежда от потребителя и n е цяло число
между 20 и 30 (20<n<30). 
Да се провери входа (дали условнето "20<n<30" е изпълнено). 

Списъкът се запълва със случайни числа в интервала [ -100 .. 100]. 

Намерете сумата на елементите от списъка чинто индекси са нечетни. 

Да се намери броят на елементите от списъка, чиято цифра на единиците е кратна на 2. 
Намерете произведението на елементите с отрицателна стойност, които са четни. 

Списъкът да се сортира в низходяш ред и да се принтира.


Да се създаде втори списък и в него да се включват тези числа от първия списък, 
които са по-големи от n. 
Да се намери разликата между елемента с максимална и елемента с минимална стойност в списъка.
Да се принтират нечетните числа от този списък и техния брой. 
Да се изтрие елемента с минимална стойност от списъка.
'''

import random

# 1. Input n (must be between 20 and 30)
n = 0
while True:
    try:
        n = int(input("Enter number of elements n (20 < n < 30): "))
        if 20 < n < 30:
            break
        else:
            print("Condition 20 < n < 30 is not met. Try again.")
    except ValueError:
        print("Please enter an integer.")

# 2. Fill list with random numbers [-100 to 100]
num_list = []
for _ in range(n):
    num_list.append(random.randint(-100, 100))

print(f"\nOriginal List: {num_list}")

# 3. Sum of elements at odd indices
sum_odd_idx = 0
for i in range(1, len(num_list), 2):
    sum_odd_idx += num_list[i]
print(f"Sum of elements at odd indices: {sum_odd_idx}")

# 4. Count elements where 'unit digit' is divisible by 2 (Even numbers)
even_count = 0
for num in num_list:
    if num % 2 == 0:
        even_count += 1
print(f"Count of elements with even unit digit: {even_count}")

# 5. Product of negative elements that are even
prod_neg_even = None 

for num in num_list:
    if num < 0 and num % 2 == 0:
        if prod_neg_even is None:
            prod_neg_even = num  # Set the first number
        else:
            prod_neg_even *= num # Multiply

if prod_neg_even is None:
    prod_neg_even = 0

print(f"Product of negative even numbers: {prod_neg_even}")

# 6. Sort descending and print
num_list.sort(reverse=True)
print(f"Sorted List: {num_list}")

# --- Create Second List ---
# Elements from first list greater than n
second_list = []
for num in num_list:
    if num > n:
        second_list.append(num)

print(f"\nSecond List (elements > {n}): {second_list}")

if len(second_list) > 0:
   max_val = second_list[0]
   min_val = second_list[0]

   for num in second_list:
        if num > max_val:
            max_val = num 
        if num < min_val:
            min_val = num

   diff = max_val - min_val
   print(f"Difference between Max and Min: {diff}")

    # Print odd numbers from this list and their count
   odd_nums = []
   for num in second_list:
        if num % 2 != 0:
            odd_nums.append(num)
    
   print(f"Odd numbers in second list: {odd_nums}")
   print(f"Count of odd numbers: {len(odd_nums)}")

    # Delete element with minimal value
   second_list.remove(min_val)
   print(f"Second list after deleting min value ({min_val}): {second_list}")
else:
    print("Second list is empty.")