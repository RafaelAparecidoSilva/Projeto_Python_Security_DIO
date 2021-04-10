import itertools


resultado = itertools.permutations('Python', 3)

with open('gerador_wordlists.txt', 'w') as file:
    for i in resultado:
        file.writelines(f"{''.join(i)}\n")
