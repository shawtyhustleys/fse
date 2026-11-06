previous = int(input("предыдущее показание счетчика: "))
current = int(input("текущее показание счетчика: "))
if current >= previous:
    bill = current - previous
else:
    bill = (10000 - previous) + current
if bill <= 300:
    cost = 21.0
elif bill <= 600:
    cost = 21.0 + (bill - 300) * 0.06
elif bill <= 800:
    cost = 21.0 + (600 - 300) * 0.06 + (bill - 600) * 0.04
else:
    cost = 21.0 + (600 - 300) * 0.06 + (800 - 600) * 0.04 + (bill - 800) * 0.025
medium = cost / bill if bill > 0 else 0.0
print(f"Использовано: {bill}")
print(f"Средняя за кубометр: {medium:.2f} $")
print(f"К оплате: {cost:.2f} $")
