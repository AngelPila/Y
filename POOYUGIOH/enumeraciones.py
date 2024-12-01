from enum import Enum


class TipoMonstruo(Enum):
    LANZADOR_DE_CONJUROS = "Lanzador de Conjuros"
    DRAGON = "Dragón"
    ZOMBI = "Zombi"
    GUERRERO = "Guerrero"
    BESTIA = "Bestia"
    DEMONIO = "Demonio"
class CartaUbicacion(Enum):
    INDECK = "Carta en el Deck"
    BUP = "Carta en campo Boca Arriba"
    BDOWN = "Carta en campo Boca Abajo"
    GY = "Cementerio"
    MANO = "Carta en Mano"


class Atributo(Enum):
    OSCURIDAD = "OSCURIDAD"
    LUZ = "LUZ"
    TIERRA = "TIERRA"
    AGUA = "AGUA"
    FUEGO = "FUEGO"
    VIENTO = "VIENTO"