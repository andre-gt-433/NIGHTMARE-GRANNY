from ursina import *
from game.player import Player
from game.enemy import Enemy
from game.map import create_map
from game.items import create_keys
from game.game_manager import GameManager

app = Ursina()

window.title = "Nightmare: Pesadelo"
window.borderless = False
window.fps_counter.enabled = True

create_map()

player = Player()

keys = create_keys()

enemy = Enemy(player)

game_manager = GameManager(
    player,
    enemy,
    keys
)


def update():
    game_manager.update()


def input(key):

    if key == "escape":
        application.quit()


app.run()
