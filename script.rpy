# This is used for top-level game strucutre.
# Should not include any actual events or scripting; only logic and calling other labels.
# define config.developer = True

label start:

    # Set the ID of this playthrough
    $ anticheat = persistent.anticheat

    # We'll keep track of the chapter we're on for poem response logic and other stuff
    $ chapter = 0

    #If they quit during a pause, we have to set _dismiss_pause to false again (I hate this hack)
    $ _dismiss_pause = config.developer

    # Each of the girls' names before the MC learns their name throughout ch0.
    $ s_name = "Sayori"
    $ m_name = "Monika"
    $ n_name = "Natsuki"
    $ y_name = "Yuri"

    $ quick_menu = True
    $ style.say_dialogue = style.normal
    $ allow_skipping = True
    $ config.allow_skipping = True

    if persistent.ggwp_monika == -1:
        jump mod_crash

    elif persistent.playthrough == 0:
        call ch_mod_intro
    
    elif persistent.playthrough == 1:
        call ch_mod_1a
        jump mod_continue

    elif persistent.playthrough == 2:
        call ch_mod_1b
        label mod_continue:
            call ch_mod_p1
            call ch_mod_2

label endgame(pause_length=4.0):
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    show end
    with dissolve_scene_full
    pause pause_length
    $ quick_menu = True
    return
