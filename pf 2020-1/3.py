#dictionary to count damage
#calcula_dano

dict = {
    'nome': 'hero',
    'força': 18,
    'vida': 42,
    'equipamentos': [
        {'nome': 'sword', 'força': 5},
        {'nome': 'shield', 'força': 1}
        ],
}

def calcula_dano(dict):
    i = 0
    while i != (len(dict['equipamentos'])):
        dmg = dict['força']+dict['equipamentos'[i][['força']]]
        i += 1
    return dmg

print(calcula_dano(dict))