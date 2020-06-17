"""
(a, b, c) = (1, 2, 3)
print(c)  # 3
print(b)  # 2

"""

frutas = dict()
frutas['Laranjas'] = 4
frutas['Banana'] = 6

for (k, v) in frutas.items():
    print(k, v)

tups = frutas.items()
print(tups)  # Nos da uma tupla
print (('d', 'c') > ('b', 'c'))
