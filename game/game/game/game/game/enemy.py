from ursina import *
from config import *


class Enemy(Entity):

    def __init__(self, player):

        super().__init__(
            model="cube",
            color=color.rgb(120, 20, 20),
            scale=(1, 2, 1),
            position=(12, 1, 10),
            collider="box"
        )

        self.player = player

        self.state = "patrol"

        self.points = [

            Vec3(12, 1, 0),

            Vec3(0, 1, 0),

            Vec3(-12, 1, 0),

            Vec3(0, 1, -12),

            Vec3(0, 1, -24),

            Vec3(12, 1, -24)

        ]

        self.current_point = 0

    def can_see_player(self):

        player_distance = distance(
            self.position,
            self.player.position
        )

        if player_distance > 17:
            return False

        direction = (
            self.player.position -
            self.position
        ).normalized()

        hit = raycast(
            self.position + Vec3(0, 1, 0),
            direction,
            distance=player_distance,
            ignore=[self]
        )

        return hit.entity == self.player

    def update(self):

        if self.can_see_player():

            self.state = "chase"

        if self.state == "chase":

            direction = (
                self.player.position -
                self.position
            )

            direction.y = 0

            if direction.length() > 0:

                direction.normalize()

                self.position += (
                    direction *
                    ENEMY_CHASE_SPEED *
                    time.dt
                )

        else:

            target = self.points[
                self.current_point
            ]

            direction = (
                target -
                self.position
            )

            direction.y = 0

            if direction.length() < 1.5:

                self.current_point += 1

                if self.current_point >= len(self.points):
                    self.current_point = 0

            else:

                direction.normalize()

                self.position += (
                    direction *
                    ENEMY_PATROL_SPEED *
                    time.dt
                )
