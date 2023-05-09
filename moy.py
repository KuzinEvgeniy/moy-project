soldier_count = int(input("Сколько солдат в шеренге? "))
rules_count = 1
push_ups_count = 0
for soldier in range(soldier_count, 0, -4):
    rules_count = (rules_count + soldier * 3) % soldier_count  # изменять количество правил можно любой формулой, это не единственный
    # вариант
    soldier_var = int(input("Сколько правил? "))
    if soldier_var != rules_count:
        push_ups_count += soldier * 10
        print("упал-отжался", soldier * 10, "раз")

print("Всего отжиманий", push_ups_count)

soldier_count = int(input("Сколько солдат в шеренге? "))
rules_count = 1
push_ups_count = 0
for soldier in range(soldier_count - 4, 0, -4):
    rules_count = (rules_count + soldier * 3) % soldier_count
    soldier_var = int(input("Сколько правил? "))
    if soldier_var != rules_count:
        push_ups_count += soldier * 10
        print("упал-отжался", soldier * 10, "раз")

print("Всего отжиманий", push_ups_count)