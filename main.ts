input.onButtonPressed(Button.A, function on_button_pressed_a() {
    item1.change(LedSpriteProperty.Y, -3)
    item2.change(LedSpriteProperty.Y, -3)
    item3.change(LedSpriteProperty.Y, -3)
    item4.change(LedSpriteProperty.Y, -3)
    basic.pause(1000)
    item1.change(LedSpriteProperty.Y, 3)
    item2.change(LedSpriteProperty.Y, 3)
    item3.change(LedSpriteProperty.Y, 3)
    item4.change(LedSpriteProperty.Y, 3)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    game.pause()
})
let item4 : game.LedSprite = null
let item3 : game.LedSprite = null
let item2 : game.LedSprite = null
let item1 : game.LedSprite = null
item1 = game.createSprite(0, 4)
item2 = game.createSprite(1, 4)
item3 = game.createSprite(0, 3)
item4 = game.createSprite(1, 3)
let obstacle1 = game.createSprite(3, 2)
let obstacle2 = game.createSprite(3, 3)
let obstacle3 = game.createSprite(4, 3)
let obstacle4 = game.createSprite(3, 4)
basic.forever(function on_forever() {
    for (let index = 0; index < 6; index++) {
        basic.pause(500)
        obstacle1.change(LedSpriteProperty.X, -1)
        obstacle2.change(LedSpriteProperty.X, -1)
        obstacle3.change(LedSpriteProperty.X, -1)
        obstacle4.change(LedSpriteProperty.X, -1)
        basic.pause(500)
        if (obstacle2.get(LedSpriteProperty.Y) == item3.get(LedSpriteProperty.Y)) {
            basic.showIcon(IconNames.No)
            basic.pause(1000)
            basic.showIcon(IconNames.Sad)
            break
        }
        
        if (index == 4) {
            obstacle1.change(LedSpriteProperty.X, 3)
            obstacle2.change(LedSpriteProperty.X, 3)
            obstacle3.change(LedSpriteProperty.X, 4)
            obstacle4.change(LedSpriteProperty.X, 3)
            basic.pause(500)
        }
        
    }
})
