from CLASES import *
deck = []
print(deck)
arch=open("lol.txt","r")
cartas_M=[] 
cartas_T=[] 
cartas_Ma=[]
           
for linea in arch.readlines():
    print(linea) 
    l = linea.replace("\n", "")            
    l=l.split(", ")
    print(l)
    l_m= ["LANZADOR_DE_CONJUROS","DRAGON","ZOMBI","GUERRERO","BESTIA","DEMONIO"]
    l_a= ["OSCURIDAD","LUZ","TIERRA","AGUA","FUEGO","VIENTO"]
    if l[-1] == "MAGICA" :
                    
        if l_m[0]==l[3]:
            cartas_Ma.append(CartaMagica(l[0],l[1],int(l[2]),TipoMonstruo.LANZADOR_DE_CONJUROS,l[4]))
        elif l_m[1]==l[3]:
            cartas_Ma.append(CartaMagica(l[0],l[1],int(l[2]),TipoMonstruo.DRAGON,l[4]))
        elif l_m[2]==l[3]:
            cartas_Ma.append(CartaMagica(l[0],l[1],int(l[2]),TipoMonstruo.ZOMBI,l[4]))
        elif l_m[3]==l[3]:
            cartas_Ma.append(CartaMagica(l[0],l[1],int(l[2]),TipoMonstruo.GUERRERO,l[4]))
        elif l_m[4]==l[3]:
            cartas_Ma.append(CartaMagica(l[0],l[1],int(l[2]),TipoMonstruo.BESTIA,l[4]))
        else:
            cartas_Ma.append(CartaMagica(l[0],l[1],int(l[2]),TipoMonstruo.DEMONIO,l[4]))
    elif l[-1] == "MONSTRUO":
                    
        if l_m[0]==l[4]:
            x=TipoMonstruo.LANZADOR_DE_CONJUROS
        elif l_m[1]==l[4]:
            x=TipoMonstruo.DRAGON
        elif l_m[2]==l[4]:
            x=TipoMonstruo.ZOMBI
        elif l_m[3]==l[4]:
            x=TipoMonstruo.GUERRERO
        elif l_m[4]==l[4]:
            x=TipoMonstruo.BESTIA
        else:
            x=TipoMonstruo.DEMONIO
                   
        if l_a[0]==l[5]:
            cartas_M.append(CartaMonstruo(l[0],l[1],int(l[2]),int(l[3]),x,Atributo.OSCURIDAD))
        elif l_a[1]==l[5]:
            cartas_M.append(CartaMonstruo(l[0],l[1],int(l[2]),int(l[3]),x,Atributo.LUZ))
        elif l_a[2]==l[5]:
            cartas_M.append(CartaMonstruo(l[0],l[1],int(l[2]),int(l[3]),x,Atributo.TIERRA))
        elif l_a[3]==l[5]:
            cartas_M.append(CartaMonstruo(l[0],l[1],int(l[2]),int(l[3]),x,Atributo.AGUA))
        elif l_a[4]==l[5]:
            cartas_M.append(CartaMonstruo(l[0],l[1],int(l[2]),int(l[3]),x,Atributo.FUEGO))
        else:
            cartas_M.append(CartaMonstruo(l[0],l[1],int(l[2]),int(l[3]),x,Atributo.VIENTO))
    else:
        if l_a[0]==l[2]:
            cartas_T.append(CartaTrampa(l[0],l[1],Atributo.OSCURIDAD))
        elif l_a[1]==l[2]:
            cartas_T.append(CartaTrampa(l[0],l[1],Atributo.LUZ))
        elif l_a[2]==l[2]:
            cartas_T.append(CartaTrampa(l[0],l[1],Atributo.TIERRA))
        elif l_a[3]==l[2]:
            cartas_T.append(CartaTrampa(l[0],l[1],Atributo.AGUA))
        elif l_a[4]==l[2]:
            cartas_T.append(CartaTrampa(l[0],l[1],Atributo.FUEGO))
        else:
            cartas_T.append(CartaTrampa(l[0],l[1],Atributo.VIENTO))
print(cartas_M)
arch.close()
deck = []
for i in range(20):
    deck.append(rnd.choice(cartas_M))
for i in range(5):
    deck.append(rnd.choice(cartas_T))
    deck.append(rnd.choice(cartas_Ma))
print(deck)