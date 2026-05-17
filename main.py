# ------------------------------------------------------------
#  Micro:bit Game – Flappy‑Style Bird Catching Food
#  Author: <your name here>
#  Description:
#     - Move the bird (A = up, B = down)
#     - Food moves from right to left
#     - Catch food to gain points
#     - Miss food to lose life
#     - Logo button pauses/resumes the game
#     - Pin P0 shows life and score while paused
# ------------------------------------------------------------

# -----------------------------
#  Pin P0 → Show life + score
# -----------------------------
def on_pin_pressed_p0():
    if game.is_paused():
        basic.show_number(life)
        basic.pause(500)
        basic.clear_screen()
        basic.show_number(game.score())
        basic.pause(500)
        basic.clear_screen()
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

# -----------------------------
#  Button A → Move up (running)
#           → Add life/score (paused)
# -----------------------------
def on_button_pressed_a():
    global life
    if game.is_running():
        if bird.get(LedSpriteProperty.Y) > 0:
            bird.change(LedSpriteProperty.Y, -1)
    else:
        game.add_score(-6)
        game.add_life(1)
        life += 1
input.on_button_pressed(Button.A, on_button_pressed_a)

# -----------------------------
#  Button B → Move down (running)
#           → Add more life/score (paused)
# -----------------------------
def on_button_pressed_b():
    global life
    if game.is_running():
        if bird.get(LedSpriteProperty.Y) < 4:
            bird.change(LedSpriteProperty.Y, 1)
    else:
        game.add_score(-12)
        game.add_life(3)
        life += 3
input.on_button_pressed(Button.B, on_button_pressed_b)

# -----------------------------
#  Logo → Pause / Resume
# -----------------------------
def on_logo_pressed():
    if game.is_running():
        game.pause()
        basic.show_string("S")
        basic.pause(500)
        basic.clear_screen()
    else:
        game.resume()
        game.add_life(1)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

# -----------------------------
#  Game Setup
# -----------------------------
life = 0
bird: game.LedSprite = None
bird = game.create_sprite(0, 2)
game.set_life(3)
life = 3
food = game.create_sprite(4, randint(0, 4))

# -----------------------------
#  Main Food Movement Loop
# -----------------------------
def on_forever():
    global life
    # Move food left while game is running
    while food.get(LedSpriteProperty.X) > 0 and game.is_running():
        food.change(LedSpriteProperty.X, -0.2)
        basic.pause(100)

    # Check collision when food reaches X = 0
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

    # Reset food position
    food.set(LedSpriteProperty.X, 4)
    food.set(LedSpriteProperty.Y, randint(0, 4))
basic.forever(on_forever)

# -----------------------------
#  Gravity Effect (bird falls)
# -----------------------------
def on_forever2():
    while bird.get(LedSpriteProperty.Y) < 4 and game.is_running():
        bird.change(LedSpriteProperty.Y, 1)
        basic.pause(500)
basic.forever(on_forever2)
