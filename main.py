import Graphics.Graphics as Graphics
win = Graphics.Graphics()

import EntityContainer
game = EntityContainer.EntityContainer()

while True:
    if game.is_enemies_dead():
        game.start_level()
    game.update()
    print(game.level)