print("Стоимость билетов:"
      "\n\t990 рублей (для посетителей от 18 до 24 лет)"
      "\n\t1390 рублей (для посетителей от 25 лет)"
      "\n\tдля посетителей до 18 лет билеты бесплатны"
      "\n\nПри покупке от трёх билетов действует скидка 10%\n")


tickets = int(input("Введите цифрами количество билетов: "))

print("Введите ниже возраст посетителя для каждого билета")

price = 0   # счётчик суммы оплаты

for i in range(tickets):   # подсчет суммы оплаты с учётом цены для каждой возрастной группы
    age = int(input("Возраст посетителя: "))

    if age < 18:
        i = 0
    elif 18 <= age <= 24:
        i = 990
    else:
        i = 1390

    price += i   # суммирование каждой суммы со следующей

if tickets >= 3:   # применение скижки 10% при покупке от 3 билетов
    price *= 0.9

print("\nСумма к оплате: ", int(price))