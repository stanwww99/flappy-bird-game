def on_pin_pressed_p0():
    if game.is_running():
        game.pause()
    else:
        game.resume()
        game.add_life(1)
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def on_button_pressed_a():
    if bird.get(LedSpriteProperty.Y) > 0 and game.is_running():
        bird.change(LedSpriteProperty.Y, -1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_pin_pressed_p2():
    if game.is_paused():
        basic.show_number(life)
    elif game.score() >= 6:
        game.add_score(-6)
        game.add_life(1)
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

def on_button_pressed_b():
    if bird.get(LedSpriteProperty.Y) < 4 and game.is_running():
        bird.change(LedSpriteProperty.Y, 1)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_pin_pressed_p1():
    if game.is_paused():
        basic.show_number(game.score())
    elif game.score() >= 12:
        game.add_score(-12)
        game.set_life(3)
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

life = 0
bird: game.LedSprite = None
bird = game.create_sprite(0, 2)
game.set_score(0)
game.set_life(3)
life = 3
food = game.create_sprite(4, randint(0, 4))

def on_forever():
    if input.light_level() >= 128:
        led.set_brightness(input.light_level())
    else:
        led.set_brightness(255 - input.light_level())
basic.forever(on_forever)

def on_forever2():
    global life
    while food.get(LedSpriteProperty.X) > 0 and game.is_running():
        food.change(LedSpriteProperty.X, -0.2)
        basic.pause(100)
    if food.get(LedSpriteProperty.X) <= 0:
        if bird.get(LedSpriteProperty.Y) == food.get(LedSpriteProperty.Y):
            basic.show_icon(IconNames.HAPPY)
            game.add_score(1)
            music.play(music.builtin_playable_sound_effect(soundExpression.giggle),
                music.PlaybackMode.UNTIL_DONE)
        else:
            basic.show_icon(IconNames.NO)
            game.remove_life(1)
            life += -1
            music.play(music.builtin_playable_sound_effect(soundExpression.sad),
                music.PlaybackMode.UNTIL_DONE)
    food.set(LedSpriteProperty.X, 4)
    food.set(LedSpriteProperty.Y, randint(0, 4))
basic.forever(on_forever2)

def on_forever3():
    while game.is_paused():
        basic.show_string("Stopped")
basic.forever(on_forever3)

def on_forever4():
    while bird.get(LedSpriteProperty.Y) < 4 and game.is_running():
        bird.change(LedSpriteProperty.Y, 1)
        basic.pause(500)
basic.forever(on_forever4)
