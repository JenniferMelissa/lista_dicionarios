# #quando quer cadastrar os usuarios mas nao tem um banco dados uma base de dados na empresa para o cadastro

# #lista de dicionarios 
# usuarios = [
#     {
#         'Nome': 'Fulano',
#         'Idade':'20',
#         'Profissão':'Programador',
#     },
#     {
#         'Nome': 'Fulano',
#         'Idade':'20',
#         'Profissão':'Programador',
#     }
# ]

#ou
#MELHOR E MAIS USADO

#tupla
chaves = ('Nome','Idade','Profissão')

#lista de dicionarios
usuarios2 = [
    {
        chaves[0]: 'Fulano',
        chaves[1]: '20',
        chaves[2]: 'Programador',
    },
    {
        chaves[0]: 'Ciclano',
        chaves[1]: '20',
        chaves[2]: 'Jogador',
    },
    {
        chaves[0]: 'Jusara',
        chaves[1]: '60',
        chaves[2]: 'Diretor',
    }
]


#mostrar a lista de usuarios
print(f'\n{'='*10} LISTA DE USUARIOS {'='*10}\n')

for usuario in usuarios2:
#percorre a lista
    for chave in chaves:
        #percorre o dicionario
        print(f'{chave}: {usuario[chave]}')
    print(f'\n{'-'*10}\n')

#adicionar novo dicionario a lista
for i in (len(chaves)):
    usuario[chaves[i]] = input(f'Informe{chaves[i]}: ')

usuarios2.append(usuario)

print(f'\n{'='*10} LISTA DE USUARIOS {'='*10}\n')