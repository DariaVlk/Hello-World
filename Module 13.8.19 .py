tickets = int(input("Количество билетов > "))
prices = []
for i in range(tickets):
    message = 'Возраст посетителя ' + str(i+1) + ' > '
    age = int(input(message))
    price = 1390
    if age < 18:
        price = 0
    elif 18 <= age <=25:
        price = 990
    prices.append(price)
total_price = sum(prices)
total_price *= 0.9 if tickets > 3 else 1
print("К оплате: " + str(total_price))

