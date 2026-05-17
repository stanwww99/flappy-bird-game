input.onPinPressed(TouchPin.P0, function () {
    if (game.isPaused()) {
        basic.showNumber(life)
        basic.pause(500)
        basic.clearScreen()
        basic.showNumber(game.score())
        basic.pause(500)
        basic.clearScreen()
    }
})
input.onButtonPressed(Button.A, function () {
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
input.onButtonPressed(Button.B, function () {
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
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
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
let life = 0
let bird: game.LedSprite = null
bird = game.createSprite(0, 2)
game.setLife(3)
life = 3
let food = game.createSprite(4, randint(0, 4))
basic.forever(function () {
    while (food.get(LedSpriteProperty.X) > 0 && game.isRunning()) {
        food.change(LedSpriteProperty.X, -0.2)
        basic.pause(100)
    }
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
    food.set(LedSpriteProperty.X, 4)
    food.set(LedSpriteProperty.Y, randint(0, 4))
})
basic.forever(function () {
    while (bird.get(LedSpriteProperty.Y) < 4 && game.isRunning()) {
        bird.change(LedSpriteProperty.Y, 1)
        basic.pause(500)
    }
})
