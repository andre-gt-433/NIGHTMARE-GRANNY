from ursina import *
from config import TOTAL_KEYS


class GameManager:

    def __init__(
        self,
        player,
        enemy,
        keys
    ):

        self.player = player
        self.enemy = enemy
        self.keys = keys

        self.collected = 0
        self.finished = False

        self.text = Text(
            text="Chaves: 0 / 5",
            position=(-0.85, 0.45),
            scale=1.2
        )

        self.message = Text(
            text="Encontre todas as chaves.",
            origin=(0, 0),
            y=0.35,
            scale=1.5
        )

        self.exit = Entity(
            model="cube",
            color=color.red,
            scale=(3, 3, 0.4),
            position=(12, 1.5, -28),
            collider="box"
        )

    def update(self):

        if self.finished:
            return

        self.collect_keys()

        self.check_enemy()

        self.check_exit()

    def collect_keys(self):

        for key in self.keys:

            if not key.collected:

                if distance(
                    self.player.position,
                    key.position
                ) < 1.5:

                    key.collect()

                    self.collected += 1

                    self.text.text = (
                        f"Chaves: "
                        f"{self.collected} / "
                        f"{TOTAL_KEYS}"
                    )

    def check_enemy(self):

        if distance(
            self.player.position,
            self.enemy.position
        ) < 1.5:

            self.finished = True

            self.message.text = (
                "VOCÊ FOI ENCONTRADO!"
            )

            self.player.enabled = False

    def check_exit(self):

        if distance(
            self.player.position,
            self.exit.position
        ) < 2:

            if self.collected >= TOTAL_KEYS:

                self.finished = True

                self.message.text = (
                    "VOCÊ ESCAPOU!"
                )

                self.player.enabled = False

            else:

                faltam = (
                    TOTAL_KEYS -
                    self.collected
                )

                self.message.text = (
                    f"Faltam {faltam} chaves."
                )
