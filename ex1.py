total_price = float(input('Введите общую стоимость часов: '))
s_watch = 96
g_watch = s_watch / 16
s_price = 48
g_price = (total_price - (s_watch * s_price)) / g_watch

print(int(g_price))