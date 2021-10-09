money = float(input("Введите сумму вклада"))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = []
for key in per_cent:
    deposit.append(round(per_cent[key] / 100 * money, 2))
print(deposit)
max_deposit = max(deposit)
print('Максимальная сумма, которую вы можете заработать — ', max_deposit)
