//  ------------------------------------------------------------
//   Micro:bit Game – Flappy‑Style Bird Catching Food
//   Author: <your name here>
//   Description:
//      - Move the bird (A = up, B = down)
//      - Food moves from right to left
//      - Catch food to gain points
//      - Miss food to lose life
//      - Logo button pauses/resumes the game
//      - Pin P0 shows life and score while paused
//  ------------------------------------------------------------
//  -----------------------------
//   Pin P0 → Show life + score
//  -----------------------------
input.onPinPressed(TouchPin.P0, function on_pin_pressed_p0() {
    if (game.isPaused()) {
        basic.showNumber(life)
        basic.pause(500)
        basic.clearScreen()
        basic.showNumber(game.score())
        basic.pause(500)
        basic.clearScreen()
    }
    
})
//  -----------------------------
//   Button A → Move up (running)
//            → Add life/score (paused)
//  -----------------------------
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    if (game.isRunning()) {
        if (bird.get(LedSpriteProperty.Y) > 0) {
            bird.change(LedSpriteProperty.Y, -1)
        }
        
    } else {
        game.addScore(-6)
        game.addLife(1)
        life += 1
    }
    
})
//  -----------------------------
//   Button B → Move down (running)
//            → Add more life/score (paused)
//  -----------------------------
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    if (game.isRunning()) {
        if (bird.get(LedSpriteProperty.Y) < 4) {
            bird.change(LedSpriteProperty.Y, 1)
        }
        
    } else {
        game.addScore(-12)
        game.addLife(3)
        life += 3
    }
    
})
//  -----------------------------
//   Logo → Pause / Resume
//  -----------------------------
input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_pressed() {
    if (game.isRunning()) {
        game.pause()
        basic.showString("S")
        basic.pause(500)
        basic.clearScreen()
    } else {
        game.resume()
        game.addLife(1)
    }
    
})
//  -----------------------------
//   Game Setup
//  -----------------------------
let life = 0
let bird : game.LedSprite = null
bird = game.createSprite(0, 2)
game.setLife(3)
life = 3
let food = game.createSprite(4, randint(0, 4))
//  -----------------------------
//   Main Food Movement Loop
//  -----------------------------
basic.forever(function on_forever() {
    
    //  Move food left while game is running
    while (food.get(LedSpriteProperty.X) > 0 && game.isRunning()) {
        food.change(LedSpriteProperty.X, -0.2)
        basic.pause(100)
    }
    //  Check collision when food reaches X = 0
    if (food.get(LedSpriteProperty.X) <= 0) {
        if (bird.get(LedSpriteProperty.Y) == food.get(LedSpriteProperty.Y)) {
            basic.showIcon(IconNames.Happy)
            game.addScore(1)
            music.play(music.builtinPlayableSoundEffect(soundExpression.giggle), music.PlaybackMode.UntilDone)
        } else {
            basic.showIcon(IconNames.No)
            game.removeLife(1)
            life += -1
            music.play(music.builtinPlayableSoundEffect(soundExpression.sad), music.PlaybackMode.UntilDone)
        }
        
    }
    
    //  Reset food position
    food.set(LedSpriteProperty.X, 4)
    food.set(LedSpriteProperty.Y, randint(0, 4))
})
//  -----------------------------
//   Gravity Effect (bird falls)
//  -----------------------------
basic.forever(function on_forever2() {
    while (bird.get(LedSpriteProperty.Y) < 4 && game.isRunning()) {
        bird.change(LedSpriteProperty.Y, 1)
        basic.pause(500)
    }
})
