import random as rnd
from enum import Enum
import numpy as np
from enumeraciones import *


class Deck:
    def __init__(self, cartas):
        self.cartas = cartas



#pruebalo    tamo jodidos si...

    def CreacionDeck(self, arch1):
        arch=open(arch1 + ".txt","r")
        cartas_M=[] 
        cartas_T=[] 
        cartas_Ma=[]
                
        for linea in arch.readlines():
            l = linea.replace("\n", "")            
            l=l.split(", ")
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
        arch.close()
        deck = []
        for i in range(20):
            deck.append(rnd.choice(cartas_M))
        for i in range(5):
            deck.append(rnd.choice(cartas_T))
            deck.append(rnd.choice(cartas_Ma))
        print(deck)

#    def CreacionDeck(self, cartas_M, cartas_T, cartas_Ma):
 #       deck = []
  #      for i in range(20):
   #         deck.append(rnd.choice(cartas_M))
    #    for i in range(5):
     #       deck.append(rnd.choice(cartas_T))
      #      deck.append(rnd.choice(cartas_Ma))
       # return Deck(deck)

    def EliminarAgregarCarta(self, carta, agregar):
        if carta in self.cartas:
            agregar.append(carta)
            self.cartas.remove(carta)
        else:
            print("La carta no está en el deck.")

    def DeckStr(self):
        return [carta.nombre for carta in self.cartas]

    def __str__(self):
        return str(self.DeckStr())


class Jugador:
    def __init__(self, nombre, deck):
        self.nombre = nombre
        self.deck = deck
        self.hp = 4000
        self.cartas_mano = []  
        self.cartas_mano_str = []  

    def Atacado(self, carta):
        self.hp -= carta.ataque

    def PrimeraMano(self):
        for _ in range(5):
            if self.deck.cartas:
                carta = rnd.choice(self.deck.cartas)
                self.deck.EliminarAgregarCarta(carta, self.cartas_mano)
                self.cartas_mano_str.append(carta.nombre)
                carta.area = CartaUbicacion.MANO
            else:
                print("El deck está vacío, no puedes robar más cartas.")

    def jugadorDerrotado(self):
        return self.hp <= 0

    def TomarCarta(self):
        if self.deck.cartas:
            carta = self.deck.cartas[0]
            self.deck.EliminarAgregarCarta(carta, self.cartas_mano)
            print(f"{self.nombre} ha robado una carta.")
        else:
            print("El deck está vacío, no puedes robar más cartas.")


    

    def Atacar(self, tablero_oponente, tablero, carta_atacante):
        objetivos = [(i, carta) for i, carta in enumerate(tablero_oponente.esp_monster) if not isinstance(carta, Espacio)]

        if objetivos:
            idx_objetivo, objetivo = min(objetivos, key=lambda x: x[1].defensa)
            idx_atk = tablero.esp_monster.tolist().index(carta_atacante)
            print(f"{self.nombre} ataca a {objetivo.nombre} con {carta_atacante.nombre}.")
            if carta_atacante.ataque > objetivo.defensa:
                tablero_oponente.esp_monster[idx_objetivo] = Espacio("Monstruo")
                print(f"{objetivo.nombre} ha sido destruido.")
            elif carta_atacante.ataque < objetivo.defensa:
                print(f"{carta_atacante.nombre} no tiene suficiente ataque y es destruido.")
                tablero.esp_monster[idx_objetivo] = Espacio("Monstruo")
            elif carta_atacante.ataque == objetivo.defensa:
                tablero_oponente.esp_monster[idx_objetivo] = Espacio("Monstruo")
                tablero.esp_monster[idx_atk] = Espacio("Monstruo")
                print(f"{carta_atacante.nombre} tiene igual ataque que la defensa de {objetivo.nombre}, ambos son destruidos")

        else:
            print(f"{self.nombre} ataca directamente al oponente con {carta_atacante.nombre}.")
            return carta_atacante.ataque  
        return 0  



class Carta:
    def __init__(self, tipo, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.area = CartaUbicacion.INDECK


class CartaMonstruo(Carta):
    def __init__(self, nombre, descripcion, ataque, defensa, tipo_M, tipo_A):
        super().__init__("MONSTRUO", nombre, descripcion)
        self.ataque = int(ataque)
        self.defensa = int(defensa)
        self.tipo_M = TipoMonstruo(tipo_M)
        self.tipo_A = Atributo(tipo_A)


class CartaMagica(Carta):
    def __init__(self, nombre, descripcion, incremento, tipo_afectado, atk_def):
        super().__init__("TRAMPA", nombre, descripcion)
        self.tipo_afectado = TipoMonstruo(tipo_afectado)
        self.incremento = incremento
        self.atk_def = atk_def

    def usoMag(self, carta):
        if self.tipo_afectado == carta.tipo_M:
            if self.atk_def == "atk":
                carta.ataque += self.incremento
            elif self.atk_def == "def":
                carta.defensa += self.incremento
        else:
            print("La carta mágica no es compatible.")


class CartaTrampa(Carta):
    def __init__(self,  nombre, descripcion, atributo_afectado):
        super().__init__("TRAMPA", nombre, descripcion)
        self.atributo_afectado = atributo_afectado


class Espacio(Carta):
    def __init__(self, tipo):
        super().__init__("EspacioCarta","ESPACIO", tipo)


class Tablero:
    def __init__(self):
        self.esp_monster = np.array([Espacio("Monstruo") for _ in range(3)], dtype=Carta)
        self.esp_magtrp = np.array([Espacio("Trampa-Magica") for _ in range(3)], dtype=Carta)
        self.gy = []

    def AgregarAtk(self, carta, posicion):
        if isinstance(self.esp_monster[posicion - 1], Espacio):
            self.esp_monster[posicion - 1] = self.clonar_carta(carta)
            carta.area = CartaUbicacion.BUP

    def AgregarDef(self, carta, posicion):
        if isinstance(self.esp_monster[posicion - 1], Espacio):
            self.esp_monster[posicion - 1] = self.clonar_carta(carta)
            carta.area = CartaUbicacion.BDOWN

    def AgregarTrap(self, carta, posicion):
        if isinstance(self.esp_magtrp[posicion - 1], Espacio):
            self.esp_magtrp[posicion - 1] = self.clonar_carta(carta)
            carta.area = CartaUbicacion.BDOWN

    def AgregarMag(self, carta, posicion):
        if isinstance(self.esp_magtrp[posicion - 1], Espacio):
            self.esp_magtrp[posicion - 1] = self.clonar_carta(carta)
            carta.area = CartaUbicacion.BUP

    @staticmethod
    def clonar_carta(carta):
        """Clona una carta para evitar referencias compartidas."""
        if isinstance(carta, CartaMonstruo):
            return CartaMonstruo(carta.nombre, carta.descripcion, carta.ataque, carta.defensa, carta.tipo_M.value, carta.tipo_A.value)
        elif isinstance(carta, CartaMagica):
            return CartaMagica(carta.nombre, carta.descripcion, carta.incremento, carta.tipo_afectado.value, carta.atk_def)
        elif isinstance(carta, CartaTrampa):
            return CartaTrampa(carta.nombre, carta.descripcion, carta.atributo_afectado)
        else:
            return carta


class Bot(Jugador):
    def __init__(self, deck):
        super().__init__("Bot", deck)

    def turnoBot(self, tablero_bot, oponente, turno, atq):
        print("\n--- Turno del Bot ---")
        
        self.TomarCarta()

        self.jugarCartas(tablero_bot)

        if turno != 1 and atq!=0:  
            self.atacarConMonstruos(tablero_bot, oponente,atq)

            atq += 1

    def jugarCartas(self, tablero_bot):
        max_acciones = 3
        acciones_realizadas = 0

        for carta in list(self.cartas_mano):  
            if acciones_realizadas < max_acciones:
                if isinstance(carta, CartaMonstruo):
                    if self.invocarMonstruo(carta, tablero_bot):
                        acciones_realizadas += 1
                elif isinstance(carta, CartaMagica):
                    if self.usarCartaMagica(carta, tablero_bot):
                        acciones_realizadas += 1

    def invocarMonstruo(self, carta, tablero_bot):
        for i, espacio in enumerate(tablero_bot.esp_monster):
            if isinstance(espacio, Espacio):
                if carta.ataque > carta.defensa:
                    tablero_bot.AgregarAtk(carta, i + 1)
                    print(f"Bot invoca {carta.nombre} en modo ataque.")
                else:
                    tablero_bot.AgregarDef(carta, i + 1)
                    print(f"Bot invoca {carta.nombre} en modo defensa.")
                self.cartas_mano.remove(carta)
                return True  
        return False  

    def usarCartaMagica(self, carta, tablero_bot):
        for espacio in tablero_bot.esp_monster:
            if not isinstance(espacio, Espacio) and carta.tipo_afectado == espacio.tipo_M:
                carta.usoMag(espacio)
                print(f"Bot usa {carta.nombre} en {espacio.nombre}.")
                self.cartas_mano.remove(carta)
                return True  
        return False  

    def atacarConMonstruos(self, tablero_bot, oponente, ataque):
        i=0
        while i==0:
            carta_atacante=rnd.choice(tablero_bot.esp_monster)
            if not isinstance(carta_atacante, Espacio):
                objetivos = [(i, carta) for i, carta in enumerate(oponente.tablero.esp_monster) if not isinstance(carta, Espacio)]
                
                if objetivos:
                    idx_objetivo, objetivo = min(objetivos, key=lambda x: x[1].defensa)
                    print(f"Bot ataca a {objetivo.nombre} con {carta_atacante.nombre}.")
                    if carta_atacante.ataque > objetivo.defensa:
                        oponente.tablero.esp_monster[idx_objetivo] = Espacio("Monstruo")
                        print(f"{objetivo.nombre} ha sido destruido.")
                        ataque+=1
                        
                    else:
                        print(f"{carta_atacante.nombre} no tiene suficiente ataque para destruir {objetivo.nombre}, {carta_atacante.nombre} es destruido.")
                        tablero_bot.esp_monster[tablero_bot.esp_monster.tolist().index(carta_atacante)] = Espacio("Monstruo")
                        ataque+=1
                    

                else:
                    print(f"Bot ataca directamente a {oponente.nombre} con {carta_atacante.nombre}.")
                    oponente.hp -= carta_atacante.ataque
                    print(f"{oponente.nombre} recibe {carta_atacante.ataque} puntos de daño.")
                    ataque+=1
                    i+=1
    def botDerrotado(self):
        return self.hp <= 0

