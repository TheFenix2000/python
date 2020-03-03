en_de = {'red': 'rot', 'yellow': 'gelb', 'blue': 'blau'}
de_fr = {'rot': 'rouge', 'gelb': 'jaune', 'blau': 'bleu'}

#z z angieskiego wuszukujemy "red" i to jako key w de_fr() daje nam value niemiecką, wyszukuje odpowiadającej jesj francuskiej
print('The French word for red is: {}'.format(de_fr[en_de['red']]))

#ze słownika de_fr wyszukujemy pozycję odpowiadającą niemieckiemu "żółty"
dictionaries = {'en_de': en_de, "de_fr": de_fr}
print('The French word for yellow is: {}'.format(dictionaries['de_fr']['gelb']))