previous = int(input("предыдущее показание счетчика:"))
current = int(input("текущее показание счетчика:"))
bill = current - previous
if current < previous:
    print("Текущие показатели меньше предыдущих!")
else:
    if bill <= 300:
        cost = int(21.0)
    elif bill <= 600:
            cost = int(21.0 + (bill - 300) * 0.06)
    elif bill <= 800:
        cost = int(21.0 + (600 - 300) * 0.06 + (bill - 600) * 0.04)
    else: 
        cost = int(21.0 + (600 - 300) * 0.06 + (800 - 600) * 0.04 + (bill - 800) * 0.025) #округление до 2 зн после зап
medium = cost/bill
print(f"Рaсход: {bill}")
print(f"Средняя за кубометр: {medium} $")
print(f"Итоговая стоимость: {cost} $")