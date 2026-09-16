from ursina import *


class Key(Entity):

    def __init__(self, position):

        super().__init__(
            model="cube",
            color=color.yellow,
            scale=0.25,
            position=position,
            collider="box"
        )

        self.collected = False

    def collect(self):

        self.disable()
        self.collected = True


def create_keys():

    positions = [

        (-12, 1, 0),

        (12, 1, 0),

        (0, 1, -12),

        (0, 1, 12),

        (-12, 1, -24)

    ]

    return [
        Key(position)
        for position in positions
    ]
