"""import random
isk_chislo=random.randint(0,100)
def zapros(chislo):
    ret=int(input('Предпологаемое число-'))

    if ret < chislo:
        print('more please')
    elif ret > chislo:
        print('less please')
    else:
        return True
check=False
while(check!=True):
    try:
        check=zapros(isk_chislo)
    except Exception:
        pass"""
import random
mas8=[
    [' ',' ','_','_','_',' ',' '],
    [' ',' ','*',' ',' ','|',' '],
    [' ','/','|',' ',' ','|',' '],
    [' ','/',' ',' ',' ','|','_']
]
mas1=[
    [' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ','_']
]
mas2=[
    [' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ','|',' '],
    [' ',' ',' ',' ',' ','|',' '],
    [' ',' ',' ',' ',' ','|','_']
]
mas3=[
    [' ',' ','_','_','_',' ',' '],
    [' ',' ',' ',' ',' ','|',' '],
    [' ',' ',' ',' ',' ','|',' '],
    [' ',' ',' ',' ',' ','|','_']
]
mas4=[
    [' ',' ','_','_','_',' ',' '],
    [' ',' ','*',' ',' ','|',' '],
    [' ',' ',' ',' ',' ','|',' '],
    [' ',' ',' ',' ',' ','|','_']
]
mas5=[
    [' ',' ','_','_','_',' ',' '],
    [' ',' ','*',' ',' ','|',' '],
    [' ',' ','|',' ',' ','|',' '],
    [' ',' ',' ',' ',' ','|','_']
]
mas6=[
    [' ',' ','_','_','_',' ',' '],
    [' ',' ','*',' ',' ','|',' '],
    [' ','/','|',' ',' ','|',' '],
    [' ',' ',' ',' ',' ','|','_']
]
mas7=[
    [' ',' ','_','_','_',' ',' '],
    [' ',' ','*',' ',' ','|',' '],
    [' ','/','|',' ',' ','|',' '],
    [' ','/',' ',' ',' ','|','_']
]
massivs=[mas1,mas2,mas3,mas4,mas5,mas6,mas7,mas8]
slova=['school','brawl','car','cat']
def vyvod_slova(slovo,number=0,miss=0):
    print_number=number
    vyvod=''
    for i in range(0,len(slovo)):
        if print_number>0:
            vyvod+=slovo[i]+' '
            print_number-=1
        else:
            vyvod+='_ '
    print(vyvod)
    if miss>0 and miss<9:
        for i in massivs[miss-1]:
            for j in i:
                print(j,end='')
            print('')
    elif miss==9:
        print('you loh')
        return False
def game_pusk(slovo):
    
    num_ot=0
    num_mis=0
    while(True):
        otvet='12'
        while(len(otvet)!=1):    
            otvet=input('Input bykvy-')
        otvet=otvet.lower()
        if otvet ==slovo[num_ot]:
            num_ot+=1
            
        else:
            num_mis+=1
        a=vyvod_slova(slovo,num_ot,num_mis)
        if num_ot==len(slovo):
            print('ygadal no vse ravno loh')
            break
        if a==False:
            break

#game_pusk(random.choice(slova))

game_slovo=input('Введите слово ')
game_pusk(game_slovo.lower())