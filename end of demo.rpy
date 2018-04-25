label mod_end_demo:
    $ quick_menu = False
    $ config.skipping = False
    $ config.allow_skipping = False
    
    stop music fadeout 2.0
    scene black
    with dissolve_scene_full
    
    $ fl = "FL13"
    fl "Demo is now finished."
    fl "Thanks for playing!"
    if persistent.force_play:
        fl "I know, sorry for forcing you to play on that route"
        fl "I wish I could handle it more tactfully."
        fl "Anyways..."
    fl "Full release is coming very soon! {w}If I'm not lazy."
    fl "In the meantime, check out my github repository in my DDLC Mod Reddit Post for recent updates!"
    fl "You can also help me while I'm making this mod. (like proofreading for checking my grammar mistakes, suggesting new interesting ideas, plots, etc.)"
    fl "Just comment on my reddit post."
    fl "And also comment \"Sayori is the best girl.\", ok thanks."
    fl "Or you can play this mod again."
    fl "There are other secrets that you might missed."
    fl "Or you can just wait for the full release."
    fl "Anyway..."
    fl "Uh..."
    fl "I guess there's nothing to do, right?"
    fl "Well, that's it, see you soon!"
    play music "<from 9.719>bgm/credits.ogg" noloop
    $ config.keymap['dismiss'] = []
    $ renpy.display.behavior.clear_keymap_cache()
    fl "Goodbye, [player]!{w=1.0}{nw}"
    fl "Oh wait what?{w=2.0}{nw}"
    fl "OH SHET MONIKA!?!?!{w=1.2}{nw}"
    python:
        currentpos = get_pos()
        startpos = currentpos - 0.3
        track = "<from " + str(startpos) + " to " + str(currentpos) + ">bgm/credits.ogg"
        renpy.music.play(track, loop=True)
    $ config.keymap['dismiss'] = dismiss_keys
    $ renpy.display.behavior.clear_keymap_cache()
    $ persistent.playthrough = 2
    $ delete_all_saves()
    $ persistent.deleted_saves = False
    $ persistent.nice_try = 0
    $ persistent.ggwp_monika = 0
    $ monika_seen = False
    $ persistent.parfait_girls = False
    $ persistent.poster_seen = False
    $ persistent.tea_set = False
    $ persistent.mc_violent = False
    $ persistent.force_play = False
    $ poster_checked = False
    $ closet_checked = False
    $ persistent.demu_demu = True
    call screen dialog(message="Error: Script file is missing or corrupt.\nPlease reinstall the game.", ok_action=Return())
    call screen dialog(message="Ahaha! Just kidding~\n-Monika", ok_action=Quit(confirm=False))
    return
