string1 = "Mar" 
string2 = "Mark"

if string1 == string2:
    print(f'"{string1}" is equal to "{string2}"')
else:
    print(f'"{string1}" is not equal to "{string2}"')

if string1 < string2:
    print(f'" {string1}" comes before " {string2}" in lexicographical order')
else:
    print(f'" {string1}" does not come before " {string2}" in lexicographical order')


if string1.lower() == string2.lower():
    print(f'"{string1}" is equal to "{string2}" are equal when case is ignored')
else:
    print(f'"{string1}" is not equal to "{string2}" are not equal when case is ignored')
