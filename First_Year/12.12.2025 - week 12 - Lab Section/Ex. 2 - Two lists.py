# Ex. 2
'''
Напишете програма, в която потребителя въвежда неограничен брой цели числа от клавнатурата 
(за край на въвеждането се приема "#").
Да се създадат два списъка:

В първият списък да се запишат числара, които са кратни на 3 и са четни. 
Намерете сумата на елементите от списъка на нечетен индекс.

Във вторият списък да се запишат тези числа от въведените от
потребителя, конто са кратни на 7 и са нечетни. 
Сортирайте списъка в низходящ ред. 
Намерете произведението на елемента с минимална и елемента с максимална стойност от този списък.
'''

list_1 = [] 
list_2 = []

print("Enter integers (type '#' to stop):")

while True:
    user_input = input()
    
    if user_input == "#":
        break
    
    try:
        number = int(user_input)
    except ValueError:
        print("Please enter a valid number.")
        continue

    # List 1: Divisible by 3 AND Even
    if number % 3 == 0 and number % 2 == 0:
        list_1.append(number)

    # List 2: Divisible by 7 AND Odd
    if number % 7 == 0 and number % 2 != 0:
        list_2.append(number)

# Sum of elements at odd INDICES (index 1, 3, 5...)
sum_odd_indices = 0
# Start at index 1, go to end, step by 2
for i in range(1, len(list_1), 2): 
    sum_odd_indices += list_1[i]

print(f"List 1: {list_1}")
print(f"Sum of elements at odd indices in List 1: {sum_odd_indices}")

# Sort descending
list_2.sort(reverse=True)

# Product of Min and Max element
if len(list_2) > 0:
    max_val = list_2[0]  # Since it is sorted descending, first is max
    min_val = list_2[-1] # Last is min
    product_min_max = max_val * min_val
    
    print(f"List 2 (Sorted Descending): {list_2}")
    print(f"Product of Min and Max in List 2: {product_min_max}")
else:
    print("List 2 is empty.")