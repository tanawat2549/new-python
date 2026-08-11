heroes = ['Ironman', 'Thor','Hulk','Superman','Spiderman']
h2 = ['Dr.Strange','Cpt.america','Black Panther','Antman']

heroes.insert(0, h2[0])
print(heroes.index('Thor'))
heroes.insert(heroes.index('Thor')+1, h2[1])
print(heroes)
heroes.remove('Superman')
heroes.append('Antman')
print(heroes)
heroes.sort()
print(heroes)
heroes.reverse()
print(heroes)
new_heroes = heroes
new_heroes[0] = 'Wonder Woman'
print(heroes)
copy_heroes = []+ heroes
print(copy_heroes)
copy_heroes[0] = 'Hanuman'
print(heroes)
print(copy_heroes)