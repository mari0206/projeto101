import random

sim = input(' você quer jogar o dado, sim ou não? ')

response = int(sim)

while response == sim:
    no = random.randint(1,6)
    if no == 1:
        print(['-----'])
        print(['     '])
        print(['  0  '])
        print(['     '])
        print(['-----'])

after = input(' aperte y para continuar e n para sair')
