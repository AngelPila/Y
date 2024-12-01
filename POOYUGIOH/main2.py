import random
from CLASES import *
import colored

def mostrar_tableros(tablero_jugador, tablero_bot):
    print("\n" + colored("--- TABLERO ---", "yellow", attrs=["bold"]))
    
    # Mostrar tablero del bot
    print(colored("\nTablero del Bot:", "cyan", attrs=["bold"]))
    
    print(colored("Monstruos:", "magenta", attrs=["bold"]))
    i = 1
    for carta in tablero_bot.esp_monster:
        if carta.area.value == CartaUbicacion.BDOWN:   
            print(colored(f"{i}. La carta no es visible", "red"))
        else:
            if not isinstance(carta, Espacio):
                print(f"{i}. Nombre: {carta.nombre} | ATK: {carta.ataque} | DEF: {carta.defensa} | Tipo: {carta.tipo_M}")
                print("_"*100)
            else:
                print(f"{i}. {colored('Vacio', 'red')}")
                print("_"*100)
        i += 1
    
    print("\n" + colored("Magia/Trampa:", "blue", attrs=["bold"]))
    i = 1
    for carta in tablero_bot.esp_magtrp:
        if carta.area.value == CartaUbicacion.BDOWN:   
            print(colored(f"{i}. La carta no es visible", "red"))
        else:
            if not isinstance(carta, Espacio):
                print(f"{i}. Nombre: {carta.nombre}")
                print("_"*100)
            else:
                print(f"{i}. {colored('Vacio', 'red')}")
                print("_"*100)
        i += 1
    
    print("\n" + "-"*100 + "\n")  # Línea separadora

    # Mostrar tablero del jugador
    print(colored("Tablero del Jugador:", "green", attrs=["bold"]))
    
    print(colored("Monstruos:", "magenta", attrs=["bold"]))
    i = 1
    for carta in tablero_jugador.esp_monster:
        if carta.area.value == CartaUbicacion.BDOWN:   
            print(colored(f"{i}. La carta no es visible", "red"))
        else:
            if not isinstance(carta, Espacio):
                print(f"{i}. Nombre: {carta.nombre} | ATK: {carta.ataque} | DEF: {carta.defensa} | Tipo: {carta.tipo_M}")
                print("_"*100)
            else:
                print(f"{i}. {colored('Vacio', 'red')}")
                print("_"*100)
        i += 1
    
    print("\n" + colored("Magia/Trampa:", "blue", attrs=["bold"]))
    i = 1
    for carta in tablero_jugador.esp_magtrp:
        if carta.area.value == CartaUbicacion.BDOWN:   
            print(colored(f"{i}. La carta no es visible", "red"))
        else:
            if not isinstance(carta, Espacio):
                print(f"{i}. Nombre: {carta.nombre}")
                print("-"*100)
            else:
                print(f"{i}. {colored('Vacio', 'red')}")
                print("_"*100)
        i += 1

    print("\n" + "-"*100 + "\n")
def main(): 
    cartas_monstruo = [
    # Lanzadores de Conjuros (L)
    CartaMonstruo("Hechicero de la Tormenta", "Controla relámpagos.", 2000, 1500, TipoMonstruo.LANZADOR_DE_CONJUROS, Atributo.LUZ),
    CartaMonstruo("Mago de la Oscuridad", "Maestro de las artes oscuras.", 2200, 1700, TipoMonstruo.LANZADOR_DE_CONJUROS, Atributo.OSCURIDAD),
    CartaMonstruo("Maga del Alba", "Utiliza magia luminosa.", 1800, 1400, TipoMonstruo.LANZADOR_DE_CONJUROS, Atributo.LUZ),
    CartaMonstruo("Ilusionista Sombrío", "Engaña con ilusiones.", 1900, 1200, TipoMonstruo.LANZADOR_DE_CONJUROS, Atributo.OSCURIDAD),
    CartaMonstruo("Arquimago Ancestral", "Posee conocimientos milenarios.", 2400, 2000, TipoMonstruo.LANZADOR_DE_CONJUROS, Atributo.LUZ),
    CartaMonstruo("Encantador de Espíritus", "Controla entidades etéreas.", 1700, 1500, TipoMonstruo.LANZADOR_DE_CONJUROS, Atributo.OSCURIDAD),
    CartaMonstruo("Maga de las Estrellas", "Convoca poderes cósmicos.", 2000, 1600, TipoMonstruo.LANZADOR_DE_CONJUROS, Atributo.LUZ),
    CartaMonstruo("Maestro de Portales", "Crea portales entre dimensiones.", 2300, 1800, TipoMonstruo.LANZADOR_DE_CONJUROS, Atributo.OSCURIDAD),
    CartaMonstruo("Adivino Arcano", "Predice movimientos enemigos.", 1500, 1300, TipoMonstruo.LANZADOR_DE_CONJUROS, Atributo.LUZ),
    CartaMonstruo("Mago del Vacío", "Manipula energías del vacío.", 2100, 2000, TipoMonstruo.LANZADOR_DE_CONJUROS, Atributo.OSCURIDAD),
    # Dragones (D)
    CartaMonstruo("Dragón de la Eternidad", "Dragón inmortal.", 3000, 2500, TipoMonstruo.DRAGON, Atributo.OSCURIDAD),
    CartaMonstruo("Dragón del Sol Ardiente", "Alimentado por el sol.", 2800, 2000, TipoMonstruo.DRAGON, Atributo.FUEGO),
    CartaMonstruo("Dragón de la Aurora", "Dragón de energía pura.", 2600, 2100, TipoMonstruo.DRAGON, Atributo.LUZ),
    CartaMonstruo("Serpiente Alada", "Un dragón que domina los cielos.", 2400, 1900, TipoMonstruo.DRAGON, Atributo.FUEGO),
    CartaMonstruo("Dragón de Hielo", "Respira un aliento gélido.", 2500, 2200, TipoMonstruo.DRAGON, Atributo.AGUA),
    CartaMonstruo("Tirano de las Llamas", "Causa incendios devastadores.", 3000, 2000, TipoMonstruo.DRAGON, Atributo.FUEGO),
    CartaMonstruo("Dragón de Roca", "Fuerte como una montaña.", 2600, 2400, TipoMonstruo.DRAGON, Atributo.TIERRA),
    CartaMonstruo("Dragón Espectral", "Inmaterial y misterioso.", 2000, 2000, TipoMonstruo.DRAGON, Atributo.OSCURIDAD),
    CartaMonstruo("Dragón Eléctrico", "Controla tormentas eléctricas.", 2700, 1800, TipoMonstruo.DRAGON, Atributo.LUZ),
    CartaMonstruo("Dragón Marino", "Reina en los océanos.", 2800, 2200, TipoMonstruo.DRAGON, Atributo.AGUA),
    # Zombis (Z)
    CartaMonstruo("Zombi Errante", "Busca almas sin descanso.", 1500, 1000, TipoMonstruo.ZOMBI, Atributo.OSCURIDAD),
    CartaMonstruo("Lich Oscuro", "Poderes necrománticos.", 2500, 2100, TipoMonstruo.ZOMBI, Atributo.OSCURIDAD),
    CartaMonstruo("Esqueleto Furioso", "Implacable en batalla.", 1600, 1200, TipoMonstruo.ZOMBI, Atributo.TIERRA),
    CartaMonstruo("Necrófago Hambriento", "Devorador de carne.", 1800, 1400, TipoMonstruo.ZOMBI, Atributo.OSCURIDAD),
    CartaMonstruo("Zombi de la Ciénaga", "Surgido de un pantano.", 1400, 1100, TipoMonstruo.ZOMBI, Atributo.AGUA),
    CartaMonstruo("General No-Muerto", "Lidera hordas zombis.", 2100, 1900, TipoMonstruo.ZOMBI, Atributo.OSCURIDAD),
    CartaMonstruo("Sombras Errantes", "Entes oscuros e intangibles.", 2000, 1700, TipoMonstruo.ZOMBI, Atributo.OSCURIDAD),
    CartaMonstruo("Guardián del Cementerio", "Protege los muertos.", 1900, 1800, TipoMonstruo.ZOMBI, Atributo.TIERRA),
    CartaMonstruo("Rey Zombi", "Monarca inmortal.", 2500, 2200, TipoMonstruo.ZOMBI, Atributo.OSCURIDAD),
    CartaMonstruo("Sirviente de las Tinieblas", "Zombi con poderes menores.", 1700, 1500, TipoMonstruo.ZOMBI, Atributo.OSCURIDAD),
    # Guerreros (G)
    CartaMonstruo("Guerrero Valiente", "Nunca retrocede.", 1800, 1600, TipoMonstruo.GUERRERO, Atributo.TIERRA),
    CartaMonstruo("Caballero de la Aurora", "Armado con luz.", 2000, 1800, TipoMonstruo.GUERRERO, Atributo.LUZ),
    CartaMonstruo("Espadachín Oscuro", "Maestro de la espada.", 1900, 1400, TipoMonstruo.GUERRERO, Atributo.OSCURIDAD),
    CartaMonstruo("Paladín del Rey", "Protector del reino.", 2100, 2000, TipoMonstruo.GUERRERO, Atributo.TIERRA),
    CartaMonstruo("Berseker de la Montaña", "Lucha sin descanso.", 2500, 1500, TipoMonstruo.GUERRERO, Atributo.TIERRA),
    CartaMonstruo("Caballero de Acero", "Blindado con metal puro.", 2300, 1900, TipoMonstruo.GUERRERO, Atributo.TIERRA),
    CartaMonstruo("Samurái Errante", "Busca su destino.", 1800, 1600, TipoMonstruo.GUERRERO, Atributo.LUZ),
    CartaMonstruo("Lancero Divino", "Guerrero con lanza celestial.", 2400, 1800, TipoMonstruo.GUERRERO, Atributo.LUZ),
    CartaMonstruo("Soldado de Élite", "Disciplina impecable.", 2000, 1700, TipoMonstruo.GUERRERO, Atributo.TIERRA),
    CartaMonstruo("Espadachín Legendario", "Conocido por su habilidad.", 2200, 2000, TipoMonstruo.GUERRERO, Atributo.TIERRA),
    # Bestias (B)
    CartaMonstruo("Bestia del Bosque", "Protege secretos del bosque.", 1700, 1200, TipoMonstruo.BESTIA, Atributo.TIERRA),
    CartaMonstruo("León Salvaje", "Feroz y poderoso.", 2300, 1400, TipoMonstruo.BESTIA, Atributo.TIERRA),
    CartaMonstruo("Tigre Espectral", "Acecha en las sombras.", 1900, 1600, TipoMonstruo.BESTIA, Atributo.OSCURIDAD),
    CartaMonstruo("Lobo Lunar", "Aúlla bajo la luna.", 1800, 1500, TipoMonstruo.BESTIA, Atributo.LUZ),
    CartaMonstruo("Serpiente Gigante", "Reptil venenoso.", 1500, 2000, TipoMonstruo.BESTIA, Atributo.TIERRA),
    CartaMonstruo("Águila Majestuosa", "Domina los cielos.", 2000, 1300, TipoMonstruo.BESTIA, Atributo.FUEGO),
    CartaMonstruo("Bestia Infernal", "Criatura salvaje.", 2500, 1700, TipoMonstruo.BESTIA, Atributo.OSCURIDAD),
    CartaMonstruo("Oso de la Montaña", "Fuerza bruta de la naturaleza.", 2400, 2000, TipoMonstruo.BESTIA, Atributo.TIERRA),
    CartaMonstruo("Ciervo Protector", "Cuida los bosques sagrados.", 1600, 1900, TipoMonstruo.BESTIA, Atributo.TIERRA),
    CartaMonstruo("Pantera Negra", "Acechadora silenciosa.", 2100, 1800, TipoMonstruo.BESTIA, Atributo.OSCURIDAD),
    # Demonios (O)
    CartaMonstruo("Demonio de las Sombras", "Nacido del odio.", 2500, 2000, TipoMonstruo.DEMONIO, Atributo.OSCURIDAD),
    CartaMonstruo("Archidemonio del Abismo", "Reina en el abismo.", 2800, 2400, TipoMonstruo.DEMONIO, Atributo.OSCURIDAD),
    CartaMonstruo("Súcubo Nocturna", "Seduce y destruye.", 1900, 1400, TipoMonstruo.DEMONIO, Atributo.OSCURIDAD),
    CartaMonstruo("Señor del Terror", "Genera miedo a sus enemigos.", 2700, 2100, TipoMonstruo.DEMONIO, Atributo.OSCURIDAD),
    CartaMonstruo("Guardián del Inframundo", "Protege las puertas del infierno.", 2400, 2000, TipoMonstruo.DEMONIO, Atributo.OSCURIDAD),
    CartaMonstruo("Demonio Esclavizador", "Domina mentes débiles.", 2200, 1800, TipoMonstruo.DEMONIO, Atributo.OSCURIDAD),
    CartaMonstruo("Incubo Sombrío", "Se alimenta de la desesperación.", 2000, 1600, TipoMonstruo.DEMONIO, Atributo.OSCURIDAD),
    CartaMonstruo("Bestia Infernal", "Criatura salvaje del abismo.", 2500, 1700, TipoMonstruo.DEMONIO, Atributo.OSCURIDAD),
    CartaMonstruo("Destructor de Almas", "Destruye todo a su paso.", 3000, 2500, TipoMonstruo.DEMONIO, Atributo.OSCURIDAD),
    CartaMonstruo("Tirano Oscuro", "Rey de los demonios.", 2800, 2400, TipoMonstruo.DEMONIO, Atributo.OSCURIDAD),
]
    cartas_magicas = [
    # Para Lanzadores de Conjuros (L)
    CartaMagica("Libro de Magia Antigua", "Incrementa el ataque de un Lanzador de Conjuros.", 600, TipoMonstruo.LANZADOR_DE_CONJUROS, "atk"),
    CartaMagica("Esfera de Energía", "Incrementa la defensa de un Lanzador de Conjuros.", 500, TipoMonstruo.LANZADOR_DE_CONJUROS, "def"),
    CartaMagica("Runa Arcana", "Aumenta el ataque de un Lanzador de Conjuros.", 700, TipoMonstruo.LANZADOR_DE_CONJUROS, "atk"),
    CartaMagica("Báculo de Sabiduría", "Aumenta tanto el ataque como la defensa de un Lanzador de Conjuros.", 500, TipoMonstruo.LANZADOR_DE_CONJUROS, "atk"),
    CartaMagica("Escudo Místico", "Incrementa la defensa de un Lanzador de Conjuros.", 400, TipoMonstruo.LANZADOR_DE_CONJUROS, "def"),
    CartaMagica("Capa del Ilusionista", "Mejora la defensa contra ataques directos.", 300, TipoMonstruo.LANZADOR_DE_CONJUROS, "def"),
    CartaMagica("Cristal de Poder", "Duplica el ataque de un Lanzador de Conjuros.", 800, TipoMonstruo.LANZADOR_DE_CONJUROS, "atk"),
    CartaMagica("Poción Mágica", "Recupera puntos de vida y mejora la defensa de un Lanzador de Conjuros.", 400, TipoMonstruo.LANZADOR_DE_CONJUROS, "def"),
    CartaMagica("Rayo de Luz", "Aumenta el ataque si el atributo es Luz.", 600, TipoMonstruo.LANZADOR_DE_CONJUROS, "atk"),
    CartaMagica("Oscuridad Arcana", "Incrementa el ataque si el atributo es Oscuridad.", 700, TipoMonstruo.LANZADOR_DE_CONJUROS, "atk"),

    # Para Dragones (D)
    CartaMagica("Rugido del Dragón", "Incrementa el ataque de un Dragón.", 800, TipoMonstruo.DRAGON, "atk"),
    CartaMagica("Alas de Dragón", "Incrementa tanto el ataque como la defensa de un Dragón.", 700, TipoMonstruo.DRAGON, "atk"),
    CartaMagica("Llama Eterna", "Incrementa el ataque de Dragones con atributo Fuego.", 900, TipoMonstruo.DRAGON, "atk"),
    CartaMagica("Escamas de Diamante", "Aumenta la defensa de un Dragón.", 600, TipoMonstruo.DRAGON, "def"),
    CartaMagica("Colmillos Gigantes", "Incrementa el ataque de un Dragón.", 500, TipoMonstruo.DRAGON, "atk"),
    CartaMagica("Gema del Dragón", "Otorga inmunidad contra una trampa.", 0, TipoMonstruo.DRAGON, "atk"),
    CartaMagica("Resonancia Dracónica", "Aumenta tanto ataque como defensa de todos los Dragones.", 300, TipoMonstruo.DRAGON, "atk"),
    CartaMagica("Aura de Fuego", "Aumenta el ataque de Dragones de atributo Fuego.", 400, TipoMonstruo.DRAGON, "atk"),
    CartaMagica("Rugido Devastador", "El ataque de Dragones no puede ser bloqueado este turno.", 0, TipoMonstruo.DRAGON, "atk"),
    CartaMagica("Corazón de Dragón", "Aumenta 500 puntos de ataque por turno mientras esté en el campo.", 500, TipoMonstruo.DRAGON, "atk"),

    # Para Zombis (Z)
    CartaMagica("Amuleto Zombi", "Incrementa la defensa de un Zombi.", 500, TipoMonstruo.ZOMBI, "def"),
    CartaMagica("Piedra de la Resurrección", "Incrementa el ataque de un Zombi.", 400, TipoMonstruo.ZOMBI, "atk"),
    CartaMagica("Fuerza Necrótica", "Aumenta ataque y defensa de un Zombi.", 700, TipoMonstruo.ZOMBI, "atk"),
    CartaMagica("Cuerpo Reforzado", "Aumenta la defensa de un Zombi.", 600, TipoMonstruo.ZOMBI, "def"),

    CartaMagica("Máscara Macabra", "Incrementa el ataque si el atributo es Oscuridad.", 800, TipoMonstruo.ZOMBI, "atk"),
    CartaMagica("Polvo de Huesos", "Aumenta la defensa en 300 puntos por turno.", 300, TipoMonstruo.ZOMBI, "def"),
    CartaMagica("Llamada de las Sombras", "Aumenta tanto ataque como defensa de todos los Zombis.", 500, TipoMonstruo.ZOMBI, "atk"),
    CartaMagica("Veneno Mortal", "Reduce la defensa del monstruo enemigo y aumenta el ataque del Zombi.", 500, TipoMonstruo.ZOMBI, "atk"),
    CartaMagica("Poder de la Oscuridad", "Incrementa el ataque de un Zombi con atributo Oscuridad.", 600, TipoMonstruo.ZOMBI, "atk"),

    # Para Guerreros (G)
    CartaMagica("Espada del Honor", "Incrementa el ataque de un Guerrero.", 700, TipoMonstruo.GUERRERO, "atk"),
    CartaMagica("Escudo Sagrado", "Incrementa la defensa de un Guerrero.", 600, TipoMonstruo.GUERRERO, "def"),
    CartaMagica("Armadura de Acero", "Aumenta tanto ataque como defensa de un Guerrero.", 400, TipoMonstruo.GUERRERO, "atk"),
    CartaMagica("Lanza de Fuego", "Incrementa el ataque de un Guerrero.", 800, TipoMonstruo.GUERRERO, "atk"),

    CartaMagica("Tácticas de Batalla", "Aumenta ataque de todos los Guerreros en el campo.", 500, TipoMonstruo.GUERRERO, "atk"),
    CartaMagica("Fuerza de los Antiguos", "Aumenta el ataque por cada carta en el cementerio.", 100, TipoMonstruo.GUERRERO, "atk"),
    
    CartaMagica("Estandarte de Guerra", "Aumenta tanto ataque como defensa de todos los Guerreros.", 300, TipoMonstruo.GUERRERO, "atk"),
    CartaMagica("Espada Sagrada", "Incrementa ataque si el atributo es Luz.", 800, TipoMonstruo.GUERRERO, "atk"),

    # Para Demonios (O) y Bestias (B) – Similares a las anteriores.
]
    cartas_trampa = [
    CartaTrampa("Trampa del Dragón Celestial", "Impide ataques de monstruos con atributo Luz.", Atributo.LUZ),
    CartaTrampa("Trampa Volcánica", "Bloquea ataques de monstruos con atributo Fuego.", Atributo.FUEGO),
    CartaTrampa("Corte de Tierra", "Anula ataques de monstruos con atributo Tierra.", Atributo.TIERRA),
    CartaTrampa("Barrera Viento", "Bloquea ataques de monstruos con atributo Viento.", Atributo.VIENTO),
    CartaTrampa("Murallas de Agua", "Impide ataques de monstruos con atributo Agua.", Atributo.AGUA),
    
    CartaTrampa("Giro del Viento", "Bloquea ataques de monstruos con atributo Viento.", Atributo.VIENTO),
    CartaTrampa("Escudo Aéreo", "Impide ataques de monstruos con atributo Viento.", Atributo.VIENTO),
    CartaTrampa("Contrataque Mortal", "Anula ataques de monstruos con atributo Oscuridad.", Atributo.OSCURIDAD),
    CartaTrampa("Trampa del Fénix", "Destruye monstruos con atributo Fuego cuando atacan.", Atributo.FUEGO),
    CartaTrampa("Manto de Hielo", "Bloquea ataques de monstruos con atributo Agua.", Atributo.AGUA),
    
    CartaTrampa("Emboscada Subterránea", "Anula ataques de monstruos con atributo Tierra.", Atributo.TIERRA),
    CartaTrampa("Rayo Solar", "Bloquea ataques de monstruos con atributo Luz.", Atributo.LUZ),
    CartaTrampa("Niebla Mortal", "Evita ataques de monstruos con atributo Oscuridad.", Atributo.OSCURIDAD),
    CartaTrampa("Red Volcánica", "Destruye monstruos con atributo Fuego cuando atacan.", Atributo.FUEGO),
    CartaTrampa("Barrera Acuática", "Impide ataques de monstruos con atributo Agua.", Atributo.AGUA),
    
    CartaTrampa("Vórtice Aéreo", "Bloquea ataques de monstruos con atributo Viento.", Atributo.VIENTO),
    CartaTrampa("Tumba Sellada", "Anula ataques de monstruos con atributo Oscuridad.", Atributo.OSCURIDAD),
    CartaTrampa("Tormenta Celestial", "Anula ataques de monstruos con atributo Luz.", Atributo.LUZ),
    CartaTrampa("Red de Fuego", "Bloquea ataques de monstruos con atributo Fuego.", Atributo.FUEGO),
    CartaTrampa("Escudo de Tierra", "Evita ataques de monstruos con atributo Tierra.", Atributo.TIERRA),
    
    CartaTrampa("Trampa Absorbente", "Absorbe ataques de monstruos con atributo Agua.", Atributo.AGUA),
    CartaTrampa("Destrucción de Llamas", "Anula ataques de monstruos con atributo Fuego.", Atributo.FUEGO),
    CartaTrampa("Tempestad Oscura", "Bloquea ataques de monstruos con atributo Oscuridad.", Atributo.OSCURIDAD),
    CartaTrampa("Danza de Lluvia", "Impide ataques de monstruos con atributo Agua.", Atributo.AGUA),
    CartaTrampa("Camuflaje de Tierra", "Anula ataques de monstruos con atributo Tierra.", Atributo.TIERRA),
    
    CartaTrampa("Poder Luminoso", "Bloquea ataques de monstruos con atributo Luz.", Atributo.LUZ),
    CartaTrampa("Golpe Aéreo", "Anula ataques de monstruos con atributo Viento.", Atributo.VIENTO),
    CartaTrampa("Cementerio Oscuro", "Evita ataques de monstruos con atributo Oscuridad.", Atributo.OSCURIDAD),
    CartaTrampa("Barrera Flameante", "Destruye monstruos con atributo Fuego que atacan.", Atributo.FUEGO),
    CartaTrampa("Explosión Subterránea", "Bloquea ataques de monstruos con atributo Tierra.", Atributo.TIERRA),
    
    CartaTrampa("Reflejo Lunar", "Anula ataques de monstruos con atributo Luz.", Atributo.LUZ),
    CartaTrampa("Trampa Nebulosa", "Impide ataques de monstruos con atributo Viento.", Atributo.VIENTO),
    CartaTrampa("Maldición Acuática", "Destruye monstruos con atributo Agua.", Atributo.AGUA),
    CartaTrampa("Trampa de Lavas", "Evita ataques de monstruos con atributo Fuego.", Atributo.FUEGO),
    CartaTrampa("Golpe Subterráneo", "Bloquea ataques de monstruos con atributo Tierra.", Atributo.TIERRA),
    
    CartaTrampa("Noche Silenciosa", "Anula ataques de monstruos con atributo Oscuridad.", Atributo.OSCURIDAD),
    CartaTrampa("Tornado Viento", "Destruye monstruos con atributo Viento cuando atacan.", Atributo.VIENTO),
    CartaTrampa("Escudo de Agua", "Bloquea ataques de monstruos con atributo Agua.", Atributo.AGUA),
    CartaTrampa("Destructor Solar", "Anula ataques de monstruos con atributo Luz.", Atributo.LUZ),
    CartaTrampa("Llamarada Infernal", "Evita ataques de monstruos con atributo Fuego.", Atributo.FUEGO),
    
    CartaTrampa("Trampa de Arena", "Bloquea ataques de monstruos con atributo Tierra.", Atributo.TIERRA),
    CartaTrampa("Demonio de la Oscuridad", "Destruye monstruos con atributo Oscuridad que atacan.", Atributo.OSCURIDAD),
    CartaTrampa("Trampa del Relámpago", "Bloquea ataques de monstruos con atributo Luz.", Atributo.LUZ),
    CartaTrampa("Tierra Sagrada", "Anula ataques de monstruos con atributo Tierra.", Atributo.TIERRA),
    CartaTrampa("Escudo Acuático", "Impide ataques de monstruos con atributo Agua.", Atributo.AGUA),
]



    
    deck_usuario = Deck(cartas_monstruo + cartas_magicas + cartas_trampa)
    deck_bot = Deck(cartas_monstruo + cartas_magicas + cartas_trampa)

    jugador = Jugador("Usuario", deck_usuario)
    bot = Bot(deck_bot)

    tablero_jugador = Tablero()
    tablero_bot = Tablero()
    jugador.tablero = tablero_jugador
    bot.tablero = tablero_bot

    print(f"¡Bienvenido al duelo, {jugador.nombre}!")
    jugador.PrimeraMano()
    bot.PrimeraMano()

    turno_jugador = rnd.choice([True, False])
    print("\nSorteo de inicio...")
    if turno_jugador:
        print(f"{jugador.nombre} comienza primero.")
    else:
        print(f"{bot.nombre} comienza primero.")

    turno = 1
    ataque = 0
    while not jugador.jugadorDerrotado() and not bot.botDerrotado():
        
        print(f"\n--- Turno {turno} ---")
        print(f"HP {jugador.nombre}: {jugador.hp} | HP {bot.nombre}: {bot.hp}")
        if turno_jugador:
            while ataque == 0:
                mostrar_tableros(tablero_jugador, tablero_bot)


                
                print("\nTurno del Jugador:")
                print("Tus cartas en mano:")
                for idx, carta in enumerate(jugador.cartas_mano):
                    print(f"{idx + 1}. {carta.nombre} ({carta.descripcion})")

                accion = input("Elige una acción: (1) Invocar carta, (2) Usar carta mágica, (3) Atacar, (4) Pasar turno: ")

                if accion == "1":
                    idx = int(input("Elige el índice de la carta a invocar: ")) - 1
                    carta = jugador.cartas_mano[idx]
                    if isinstance(carta, CartaMonstruo):
                        posicion = int(input("Elige posición (1-3): "))
                        modo = input("Modo de invocación: (1) Ataque, (2) Defensa: ")
                        if modo == "1":
                            tablero_jugador.AgregarAtk(carta, posicion)
                        elif modo == "2":
                            tablero_jugador.AgregarDef(carta, posicion)
                        jugador.cartas_mano.remove(carta)
                    else:
                        print("Solo puedes invocar monstruos.")
                elif accion == "2":
                    idx = int(input("Elige el índice de la carta mágica a usar: ")) - 1
                    carta = jugador.cartas_mano[idx]
                    if isinstance(carta, CartaMagica):
                        for m in tablero_jugador.esp_monster:
                            if not isinstance(m, Espacio) and carta.tipo_afectado == m.tipo_M:
                                carta.usoMag(m)
                                jugador.cartas_mano.remove(carta)
                                
                    else:
                        print("Selecciona una carta mágica válida.")
                elif accion == "3":
                    # Atacar
                    posicion = int(input("Elige el espacio desde donde atacar (1-3): "))
                    carta_atacante = tablero_jugador.esp_monster[posicion - 1]
                    if not isinstance(carta_atacante, Espacio):
                        daño = jugador.Atacar(bot.tablero, tablero_jugador, carta_atacante)
                        if daño > 0:
                            print(f"{bot.nombre} recibe {daño} puntos de daño.")
                            bot.hp -= daño
                        ataque+=1
                    else:
                        print("No hay monstruo en esa posición.")
                elif accion == "4":
                    print("Pasas tu turno.")
                    ataque+=1
                else:
                    print("Opción no válida.")

        else:
            bot.turnoBot(tablero_bot, jugador, turno, ataque )

        turno_jugador = not turno_jugador
        
        turno += 1

    print("\n--- Fin del Juego ---")
    if jugador.jugadorDerrotado():
        print("¡Has perdido! El bot te ha derrotado.")
    elif bot.botDerrotado():
        print("¡Felicidades! Has derrotado al bot.")


if __name__ == "__main__":
    main()