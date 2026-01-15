#Зад. 1

first_list = []
n = 0
while n < 20:
    num = int(input(f"Въведи число - {n+1}:"))
    first_list.append(num)
    n += 1
print("Елементи в first_list:", first_list)

sum_list_1 = min(first_list) + max(first_list)
print("Сума на минималната и максималната стойнист в first_list:", sum_list_1)

odd_c = 0
for i in first_list:
    if i % 2 != 0:
        odd_c +=1
print("Броят нечетни числа в fisrt_list:", odd_c)


second_list = []
for i in first_list:
    if i % 5 == 0:
        second_list.append(i)
print("second_list с елементи от first_list, които са кратни на 5:", second_list)

average = sum(second_list) / len(second_list)
sum_list_2 = max(second_list) - average

print(f"Разликата на максималната и ср. аритметичната стойнист в second_list: {sum_list_2:.2f}")

new_n_s_l = second_list[0] + second_list[-1]
second_list.append(new_n_s_l)
print("second_list с нов елемент, сумата на първия и последния елемент от този списък:", second_list)