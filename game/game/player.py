from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from config import *


class Player(FirstPersonController):

    def __init__(self):
        super().__init__()

        self.speed = PLAYER_WALK_SPEED
        self.run_speed = PLAYER_RUN_SPEED

        self.stamina = MAX_STAMINA

        self.height = PLAYER_HEIGHT
        self.gravity = 1

        self.create_hud()

    def create_hud(self):

        self.stamina_bg = Entity(
            parent=camera.ui,
            model="quad",
            color=color.dark_gray,
            scale=(0.3, 0.035),
            position=(-0.3, -0.44)
        )

        self.stamina_bar = Entity(
            parent=camera.ui,
            model="quad",
            color=color.lime,
            scale=(0.3, 0.035),
            position=(-0.3, -0.44)
        )

    def update(self):

        sprinting = held_keys["shift"]

        if sprinting and self.stamina > 0:

            self.speed = self.run_speed

            self.stamina -= (
                STAMINA_DRAIN * time.dt
            )

        else:

            self.speed = PLAYER_WALK_SPEED

            self.stamina += (
                STAMINA_REGEN * time.dt
            )

        self.stamina = clamp(
            self.stamina,
            0,
            MAX_STAMINA
        )

        self.stamina_bar.scale_x = (
            0.3 *
            self.stamina /
            MAX_STAMINA
        )
