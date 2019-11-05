# /usr/bin/env python3

# Created by: Marwan Mashaly
# Created on: September 2019
# This programs shows a sprite and makes a sound

import ugame
import stage
import constants


def menu_scene():
    # setting text
    NEW_PALETTE = (b'\xff\xaf\x00\x22\xcey\x22\xab\xff\xff\xff\xba\x22\
                      \xff\xff\xff'
                   b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\
                       \xff\xff\xff\xff')
    # image bank
    image_bank_1 = stage.Bank.from_bmp16("space_aliens.bmp")
    # set background
    background = stage.Grid(image_bank_1, constants.SCREEN_X,
                            constants.SCREEN_Y)
    # sprite bank
    sprites = []
    # text objects
    text = []
    text1 = stage.Text(width=29, height=12, font=None,
                       palette=NEW_PALETTE, buffer=None)
    text1.move(20, 10)
    text1.text("MT Game Studio")
    text.append(text1)

    text2 = stage.Text(width=29, height=12, font=None,
                       palette=NEW_PALETTE, buffer=None)
    text2.move(40, 110)
    text2.text("Press START")
    text.append(text2)

    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = text + sprites + [background]
    game.render_block()

    while True:

        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_START != 0:
            main()

        game.tick()


def main():
    # This function shows a sprite and makes a sound
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    # an image bank for circuitpython
    image_bank_1 = stage.Bank.from_bmp16("space_aliens.bmp")
    # a list of sprites that will be updated every frame
    sprites = []
    # get sound ready
    pew_sound = open("pew.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    # sprites in the scene
    ship = stage.Sprite(image_bank_1, 5, int(constants.SCREEN_X / 2
                        - constants.SPRITE_SIZE / 2),
                        int(constants.SCREEN_Y - constants.SPRITE_SIZE
                        + constants.SPRITE_SIZE / 2))
    sprites.append(ship)  # insert at the top of the sprite list

    # sets the background to image 0 in the bank
    # backgrounds do not have magents as a transparent color
    background = stage.Grid(image_bank_1, 10, 8)
    # create a sprite
    # parameters (image_bank, image # in bank, x, y)
    alien = stage.Sprite(image_bank_1, 8, 64, 56)
    sprites.append(alien)

    # create a stage for the background to show up on
    #  and set the frame rate to 60
    game = stage.Stage(ugame.display, constants.FPS)
    # set the layers, items show up in order
    game.layers = sprites + [background]
    # render the background and initial location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

    # repeat forever, or you turn it off
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()
        if keys & ugame.K_X != 0:  # a button (fire)
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]
        if keys & ugame.K_X:
            # print("A")
            pass
        if keys & ugame.K_O:
            # print("B")
            pass
        if keys & ugame.K_START:
            # print("K_START")
            pass
        if keys & ugame.K_SELECT:
            # print("K_SELECT")
            pass
        # update_game_logic
        # move ship to the right and the left
        if keys & ugame.K_RIGHT != 0:
            if ship.x > constants.SCREEN_X - constants.SPRITE_SIZE:
                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)
            else:
                ship.move(ship.x + 1, ship.y)

        if keys & ugame.K_LEFT != 0:
            if ship.x < 0:
                ship.move(0, ship.y)
            else:
                ship.move(ship.x - 1, ship.y)
            pass
        # move ship up and down
        if keys & ugame.K_UP:
            ship.move(ship.x, ship.y - 1)
        elif keys & ugame.K_DOWN:
            ship.move(ship.x, ship.y + 1)
            pass
        if a_button == constants.button_state["button_just_pressed"]:
            sound.play(pew_sound)

        # redraw sprite list
        game.render_sprites(sprites)
        game.tick()  # wait until refresh rate finishes


if __name__ == "__main__":
    menu_scene()
