phonebook = {'Anirach': '777-1111', 'Tanawat': '777-2222', 'Danai': '777-3333'}
print(phonebook)

print(phonebook['Anirach'])
print(phonebook.get('Daniai'))

key = 'Pluto'
if key in phonebook:
    print(phonebook['Pluto'])
else:
    print(key + ' not in phonebook')
phonebook['Simpson'] = '777-4567'
phonebook['Pluto'] = '777-4444'
phonebook['Tanawat'] = '777-2122'
print(phonebook)

del phonebook['Simpson']
print(phonebook)