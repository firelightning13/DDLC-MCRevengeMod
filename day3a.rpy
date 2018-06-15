label ch_mod_p2:
    $ chapter = 1 ### original poem game from DDLC
    call poem

    scene black with trueblack
    return

label mod_end_demo:
    $ quick_menu = False
    $ config.skipping = False
    $ config.allow_skipping = False
    $ persistent.autoload = "mod_end_demo"
    
    stop music fadeout 2.0
    scene black
    with dissolve_scene_full
    window auto
    
    $ fl = "FL13"
    fl "Demo is now finished."
    fl "Thank you for play my mod!"
    #fl "Full release is coming very soon! {w}If I'm not lazy."
    fl "I'm glad that I updated this mod in time."
    fl "I'm very sorry to all of you who were anticipated to wait for this update. I've been quite busy for a long time."
    fl "I don't know, like 5 months after the initial release?"
    fl "But this will be the last update of my mod, and I'll never finish this mod into a full release state."
    fl "Again, I'm very sorry."
    fl "I'm busy with the college and job and stuff."
    fl "This mod is still a proof of concept, just a part of my programming experiment."
    #fl "In the meantime, check out my github repository in my DDLC Mod Reddit Post for recent updates!"
    #fl "You can also help me while I'm making this mod. (like proofreading for checking my grammar mistakes, suggesting new interesting ideas, plots, etc.)"
    #fl "Just comment on my reddit post."
    #fl "And also comment \"Sayori is the best girl.\", ok thanks."
    fl "Anyway, you can play this mod again."
    if mc_blocked:
        fl "It looks like you didn't skip the dialogues when the game told you too..."
        fl "There is a \"secret\" route that you can discover!"
        fl "Well, you can't go back by saving or loading, but..."
    fl "To reset this mod back to the initial state, delete \"mod_firstrun\" inside the \"game\" folder."
    if mc_blocked:
        fl "That way you can play it again at a different route."
    else:
        fl "There are other secrets that you might missed."
    #fl "Or you can just wait for the full release."
    fl "Anyway..."
    fl "Uh..."
    fl "I guess there's nothing to do, right?"
    fl "Well, that's it, see you soon!{w} or noT{nw}"
    window hide(None)
    show screen tear(20, 0.1, 0.1, 0, 40)
    stop music
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    stop sound
    hide screen tear
    window auto
    #play music "<from 9.719>bgm/credits.ogg" noloop
    #$ config.keymap['dismiss'] = []
    #$ renpy.display.behavior.clear_keymap_cache()
    #fl "Goodbye, [player]!{w=1.0}{nw}"
    #fl "Oh wait what?{w=2.0}{nw}"
    #fl "OH SHET MONIKA!?!?!{w=1.2}{nw}"
    #python:
    #    currentpos = get_pos()
    #    startpos = currentpos - 0.3
    #    track = "<from " + str(startpos) + " to " + str(currentpos) + ">bgm/credits.ogg"
    #    renpy.music.play(track, loop=True)
    #call screen dialog(message="Error: Script file is missing or corrupt.\nPlease reinstall the game.", ok_action=Return())
    #call screen dialog(message="Ahaha! Just kidding~\n-Monika", ok_action=Quit(confirm=False))
    #jump creydits
    return
