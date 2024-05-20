// restarts the game
function restart_game() {
    
    //  clear existing sprites
    item1.delete()
    item2.delete()
    item3.delete()
    item4.delete()
    obstacle1.delete()
    obstacle2.delete()
    obstacle3.delete()
    obstacle4.delete()
    //  recreate sprites at starting positions
    item1 = game.createSprite(0, 4)
    item3 = game.createSprite(1, 4)
    item4 = game.createSprite(0, 3)
    item2 = game.createSprite(1, 3)
    obstacle1 = game.createSprite(3, 2)
    obstacle2 = game.createSprite(3, 3)
    obstacle3 = game.createSprite(4, 3)
    obstacle4 = game.createSprite(3, 4)
}

// jumps when A is pressed
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    jump()
})
// restarts when B is pressed
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    restart_game()
})
// infinite loop
// the jump function moves the block up and down on a being pressed
function jump() {
    // moving each led up by 3 units
    item1.change(LedSpriteProperty.Y, -3)
    item2.change(LedSpriteProperty.Y, -3)
    item3.change(LedSpriteProperty.Y, -3)
    item4.change(LedSpriteProperty.Y, -3)
    basic.pause(300)
    // bring them back down to their actual position
    item1.change(LedSpriteProperty.Y, 3)
    item2.change(LedSpriteProperty.Y, 3)
    item3.change(LedSpriteProperty.Y, 3)
    item4.change(LedSpriteProperty.Y, 3)
}

// creating the block
let item1 = game.createSprite(0, 4)
let item3 = game.createSprite(1, 4)
let item4 = game.createSprite(0, 3)
let item2 = game.createSprite(1, 3)
// creating the obstacle
let obstacle1 = game.createSprite(3, 2)
let obstacle2 = game.createSprite(3, 3)
let obstacle3 = game.createSprite(4, 3)
let obstacle4 = game.createSprite(3, 4)
basic.forever(function on_forever() {
    for (let index = 0; index < 5; index++) {
        // checking for collision condition
        if (obstacle2.isTouching(item4) || (obstacle2.isTouching(item2) || obstacle3.isTouching(item3) || obstacle4.isTouching(item4) || obstacle1.isTouching(item1) || obstacle4.isTouching(item1))) {
            basic.showIcon(IconNames.No)
            basic.showIcon(IconNames.Sad)
            basic.pause(1000)
            basic.clearScreen()
            restart_game()
            break
        } else if (index == 3) {
            // ensuring that the ostacle scrolls by changing it back to its starting pos
            obstacle1.change(LedSpriteProperty.X, 3)
            obstacle2.change(LedSpriteProperty.X, 3)
            obstacle3.change(LedSpriteProperty.X, 4)
            obstacle4.change(LedSpriteProperty.X, 3)
            break
        }
        
        if (index == 0) {
            basic.pause(150)
        }
        
        // moving the obstacle to the left
        obstacle1.change(LedSpriteProperty.X, -1)
        obstacle2.change(LedSpriteProperty.X, -1)
        obstacle3.change(LedSpriteProperty.X, -1)
        obstacle4.change(LedSpriteProperty.X, -1)
        basic.pause(150)
    }
})
