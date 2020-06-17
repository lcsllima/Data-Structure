aurelio = {'a': 10, 'b': 1, 'c': 22}
tmp = list()
for key, valor in aurelio.items():
    tmp.append((valor, key))

print(tmp)

tmp = sorted(tmp, reverse=True)
print(tmp)
