tup = [('1', 'Hi there', 'Sunny', 'Not me'), ('2', 'Hello there', 'Cloudy', 'Its you'), ('3', 'Willkommen', 'Windy', 'Ok, It was me')]
excl = [1]
lista = []
for item in tup:
    selected = item[2]
    selected1 = item[0]
    selected2 = item[3]
    if selected1 not in str(excl):
        lista.append((selected, selected2))