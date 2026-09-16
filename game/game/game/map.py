from ursina import *


WALL = color.rgb(55, 55, 60)
FLOOR = color.rgb(30, 30, 35)


def room(x, z, width, depth):

    Entity(
        model="cube",
        scale=(width, 0.2, depth),
        position=(x, 0, z),
        color=FLOOR
    )

    # Parede norte
    Entity(
        model="cube",
        scale=(width, 3, 0.2),
        position=(x, 1.5, z + depth / 2),
        color=WALL,
        collider="box"
    )

    # Parede sul
    Entity(
        model="cube",
        scale=(width, 3, 0.2),
        position=(x, 1.5, z - depth / 2),
        color=WALL,
        collider="box"
    )

    # Parede leste
    Entity(
        model="cube",
        scale=(0.2, 3, depth),
        position=(x + width / 2, 1.5, z),
        color=WALL,
        collider="box"
    )

    # Parede oeste
    Entity(
        model="cube",
        scale=(0.2, 3, depth),
        position=(x - width / 2, 1.5, z),
        color=WALL,
        collider="box"
    )


def create_map():

    # Corredor central
    room(0, 0, 10, 8)

    # Quarto
    room(-12, 0, 10, 8)

    # Biblioteca
    room(12, 0, 10, 8)

    # Cozinha
    room(0, -12, 10, 8)

    # Porão
    room(0, -24, 10, 8)

    # Garagem
    room(-12, -24, 10, 8)

    # Sala da saída
    room(12, -24, 10, 8)

    # Sótão
    room(0, 12, 10, 8)
