def porcentagem(valor):
    rep=valor*100/total
    return rep
SP=67836.43 
RJ=36678.66 
MG=29229.88 
ES=27165.48 
Outros=19849.53
total=SP+RJ+MG+ES+Outros
print(f'SP:{porcentagem(SP)}')
print(f'RJ:{porcentagem(RJ)}')
print(f'MG:{porcentagem(MG)}')
print(f'ES:{porcentagem(ES)}')
print(f'Outros:{porcentagem(Outros)}')