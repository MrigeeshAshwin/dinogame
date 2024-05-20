#restarts the game
def restart_game():
    global item1, item3, item4, item2, obstacle1, obstacle2, obstacle3, obstacle4
    # clear existing sprites
    item1.delete()
    item2.delete()
    item3.delete()
    item4.delete()
    obstacle1.delete()
    obstacle2.delete()
    obstacle3.delete()
    obstacle4.delete()
    # recreate sprites at starting positions
    item1 = game.create_sprite(0, 4)
    item3 = game.create_sprite(1, 4)
    item4 = game.create_sprite(0, 3)
    item2 = game.create_sprite(1, 3)
    obstacle1 = game.create_sprite(3, 2)
    obstacle2 = game.create_sprite(3, 3)
    obstacle3 = game.create_sprite(4, 3)
    obstacle4 = game.create_sprite(3, 4)

#jumps when A is pressed
def on_button_pressed_a():
    jump()
input.on_button_pressed(Button.A, on_button_pressed_a)

#restarts when B is pressed
def on_button_pressed_b():
    restart_game()
input.on_button_pressed(Button.B, on_button_pressed_b)

#infinite loop
def on_forever():
    for index in range(5):
        #checking for collision condition
        if obstacle2.is_touching(item4) or (obstacle2.is_touching(item2) or obstacle3.is_touching(item3) or obstacle4.is_touching(item4) or obstacle1.is_touching(item1) or obstacle4.is_touching(item1)):
            basic.show_icon(IconNames.NO)
            basic.show_icon(IconNames.SAD)
            basic.pause(1000)
            basic.clear_screen()
            restart_game()
            break
        #ensuring that the ostacle scrolls by changing it back to its starting pos
        elif index == 3:
            obstacle1.change(LedSpriteProperty.X, 3)
            obstacle2.change(LedSpriteProperty.X, 3)
            obstacle3.change(LedSpriteProperty.X, 4)
            obstacle4.change(LedSpriteProperty.X, 3)
            break
        if index == 0:
            basic.pause(150)
        #moving the obstacle to the left
        obstacle1.change(LedSpriteProperty.X, -1) 
        obstacle2.change(LedSpriteProperty.X, -1)
        obstacle3.change(LedSpriteProperty.X, -1)
        obstacle4.change(LedSpriteProperty.X, -1)
        basic.pause(150)

#the jump function moves the block up and down on a being pressed
def jump():
    #moving each led up by 3 units
    item1.change(LedSpriteProperty.Y, -3)
    item2.change(LedSpriteProperty.Y, -3)
    item3.change(LedSpriteProperty.Y, -3)
    item4.change(LedSpriteProperty.Y, -3)
    basic.pause(300)
    #bring them back down to their actual position
    item1.change(LedSpriteProperty.Y, 3)
    item2.change(LedSpriteProperty.Y, 3)
    item3.change(LedSpriteProperty.Y, 3)
    item4.change(LedSpriteProperty.Y, 3)

#creating the block
item1 = game.create_sprite(0, 4)
item3 = game.create_sprite(1, 4)
item4 = game.create_sprite(0, 3)
item2 = game.create_sprite(1, 3)
#creating the obstacle
obstacle1 = game.create_sprite(3, 2)
obstacle2 = game.create_sprite(3, 3)
obstacle3 = game.create_sprite(4, 3)
obstacle4 = game.create_sprite(3, 4)


basic.forever(on_forever)
