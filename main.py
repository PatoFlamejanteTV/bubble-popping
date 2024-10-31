def on_a_pressed():
    print("A pressed")
    bubble.toss_bubble()
    print("Bubble toss")
    bubble.load_bubble()
    music.play(music.create_sound_effect(WaveShape.SQUARE,
            1600,
            1,
            255,
            0,
            300,
            SoundExpressionEffect.NONE,
            InterpolationCurve.CURVE),
        music.PlaybackMode.IN_BACKGROUND)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_right_repeated():
    bubble.tilt_angle(bubble.Choice.RIGHT)
controller.right.on_event(ControllerButtonEvent.REPEATED, on_right_repeated)

def on_hit_wall(sprite, location):
    bubble.stick_to_wall(sprite, location)
    print("Sticked my gyatt for the rizzler")
    music.play(music.create_sound_effect(WaveShape.SQUARE,
            200,
            1,
            255,
            0,
            100,
            SoundExpressionEffect.NONE,
            InterpolationCurve.CURVE),
        music.PlaybackMode.IN_BACKGROUND)
scene.on_hit_wall(SpriteKind.bubble, on_hit_wall)

def on_left_repeated():
    bubble.tilt_angle(bubble.Choice.LEFT)
controller.left.on_event(ControllerButtonEvent.REPEATED, on_left_repeated)

bubble.create_board()
bubble.load_bubble()
mySprite = sprites.create(img("""
        ..............ccccccccc........
            ............cc555555555cc......
            ...........c5555555555555c.....
            ..........c55555555555555dc....
            .........c555555555555b5bdc....
            .........555bc1555555555bdcccc.
            ........c555ccc55555555bbdccddc
            ........c555bcb5555555ccddcdddc
            .......c555555555551ccccddbdddc
            .......c555555b555c1cccbddbbdbc
            .......c5555555bbc33333ddddbcc.
            .......c555555555bc333555ddbc..
            .......c5555555555555555555c...
            .......cd555555555555cccc555c..
            .......cd55555555555c555c555c..
            .......cdd555555555b5555b555c..
            .......cddd55555ddbb555bb555c..
            .......cdddd55555555555b5555c..
            .......cddddd5555555ddb5555dc..
            c......cdddddd555555555555dcc..
            cc...ccddddddd555555555555dc...
            cdccccdddddd555555d55555ddcc...
            cdddddddddbd5555555ddddddccccc.
            ccdddddddbb55555555bddddccbddc.
            .ccddddddbd55555555bdddccdddc..
            ..cccddddbd5555555cddcccddbc...
            ....ccccccd555555bcccc.cccc....
            .........cc555555bc............
            .........cc55555555c...........
            ..........cccccccccc...........
    """),
    SpriteKind.player)
mySprite.top = 102