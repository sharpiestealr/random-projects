def mais_medalhas(placar):
    size = len(placar)
    for i in range (size):
        placar[i]['total']: placar[i][sum(list(tuple([placar[i]['ouro']]+[placar[i]['prata']]+[placar[i]['bronze']])))]
    
    ranking = [{'nacionalidade', 0}]*size
    
    for i in range (size):
        if (placar[i]['nacionalidade'] == placar[i+1]['nacionalidade']):
            ranking[i] = [{(placar[i]['nacionalidade']): (sum(list(tuple([placar[i]['total']]+[placar[i+1]['total']]))))}]
    
    ranking = list.sort(ranking)
    
    return ranking[0]

#to test
placar = [{
    'nome': ' Michael Phelps',
    'nacionalidade': 'Norte Americano',
    'ouro': 23, 'prata': 3, 'bronze': 2,
},
{
    'nome': 'Larisa Latynina',
    'nacionalidade': 'Russo',
    'ouro': 9, 'prata': 5, 'bronze': 4,
},
{
    'nome': 'Nikolai Andrianov',
    'nacionalidade': 'Russo',
    'ouro': 7, 'prata': 5, 'bronze': 3,
},
{
    'nome': 'Boris Shakhlin',
    'nacionalidade': 'Russo',
    'ouro': 7, 'prata': 4, 'bronze': 2,
},
{
    'nome': 'Jenny Thompson',
    'nacionalidade': 'Norte Americano',
    'ouro': 8, 'prata': 3, 'bronze': 1,
}]

print(mais_medalhas(placar))