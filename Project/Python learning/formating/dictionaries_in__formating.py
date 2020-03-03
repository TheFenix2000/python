#używacjąc pozycji
print('The capital of {:s} is {:s}'.format('Ontario', 'Toronto'))

#używając parametru
print('The capital of {province} is {capital}'.format(province='Ontario', capital='Toronto'))

#używając słownika
data = {'Province': 'Ontario', 'Capital': 'Toronto'}
print('The capital of {Province} is {Capital}'.format(**data))  #'**data' -> (Province='Ontario', Capital='Toronto')

#przykład 1 metoda dłuższa trochę
capital_country = {"United States" : "Washington",
                   "US" : "Washington",
                   "Canada" : "Ottawa",
                   "Germany": "Berlin",
                   "France" : "Paris",
                   "England" : "London",
                   "UK" : "London",
                   "Switzerland" : "Bern",
                   "Austria" : "Vienna",
                   "Netherlands" : "Amsterdam"}
print('\nCountries and their capitals: ')
for c in capital_country:
    #iteracyjne 'c' to nazwa kraju a 'Capital' to słownikowa wartość od '[c]' czyli nazwy 'key' w danej iteracji
    print('{Country}: {Capital}'.format(Country=c, Capital=capital_country[c]))

#przykład 2 metoda szybsza
capital_country = {"United States" : "Washington",
                   "US" : "Washington",
                   "Canada" : "Ottawa",
                   "Germany": "Berlin",
                   "France" : "Paris",
                   "England" : "London",
                   "UK" : "London",
                   "Switzerland" : "Bern",
                   "Austria" : "Vienna",
                   "Netherlands" : "Amsterdam"}

print("\nCountries and their capitals:")
for c in capital_country:
    format_string = c + ": {" + c + "}"
    print(format_string.format(**capital_country))