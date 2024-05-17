def on_button_pressed_a():
    item1.change(LedSpriteProperty.Y, -3)
    item2.change(LedSpriteProperty.Y, -3)
    item3.change(LedSpriteProperty.Y, -3)
    item4.change(LedSpriteProperty.Y, -3)
    basic.pause(1000)
    item1.change(LedSpriteProperty.Y, 3)
    item2.change(LedSpriteProperty.Y, 3)
    item3.change(LedSpriteProperty.Y, 3)
    item4.change(LedSpriteProperty.Y, 3)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    game.pause()
input.on_button_pressed(Button.B, on_button_pressed_b)

item4: game.LedSprite = None
item3: game.LedSprite = None
item2: game.LedSprite = None
item1: game.LedSprite = None
item1 = game.create_sprite(0, 4)
item2 = game.create_sprite(1, 4)
item3 = game.create_sprite(0, 3)
item4 = game.create_sprite(1, 3)
obstacle1 = game.create_sprite(3, 2)
obstacle2 = game.create_sprite(3, 3)
obstacle3 = game.create_sprite(4, 3)
obstacle4 = game.create_sprite(3, 4)

def on_forever():
    for index in range(6):
        basic.pause(500)
        obstacle1.change(LedSpriteProperty.X, -1)
        obstacle2.change(LedSpriteProperty.X, -1)
        obstacle3.change(LedSpriteProperty.X, -1)
        obstacle4.change(LedSpriteProperty.X, -1)
        basic.pause(500)
        if obstacle2.get(LedSpriteProperty.Y) == item3.get(LedSpriteProperty.Y):
            basic.show_icon(IconNames.NO)
            basic.pause(1000)
            basic.show_icon(IconNames.SAD)
            break
        if index == 4:
            obstacle1.change(LedSpriteProperty.X, 3)
            obstacle2.change(LedSpriteProperty.X, 3)
            obstacle3.change(LedSpriteProperty.X, 4)
            obstacle4.change(LedSpriteProperty.X, 3)
            basic.pause(500)
basic.forever(on_forever)
