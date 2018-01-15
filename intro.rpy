label ch_mod_intro:
    $ persistent.playthrough = 1
    $ delete_character("sayori")
    $ quick_menu = False
    $ config.allow_skipping = False
    stop music
    play music g2
    window hide(None)
    show screen tear(8, offtimeMult=1, ontimeMult=10)
    pause 3.0
    hide screen tear
    stop music
    scene white

    play music t1g
    show intro with Dissolve(0.5, alpha=True)
    #pause 2.5
    pause 2.0
    hide intro
    show splash_gl
    pause 0.01
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    stop sound
    hide screen tear
    hide splash_gl
    show splash_n
    pause 0.25
    hide splash_n with Dissolve(0.5, alpha=True)
    show splash_warning "WARNING: Flashing colours in 3 seconds ahead!\n-firelightning13" with Dissolve(0.5, alpha=True)
    pause 1.0
    hide splash_warning
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    stop sound
    hide screen tear
    stop music
    scene black with trueblack
    window auto

    $ renpy.call_screen("dialog", "Error: Script file is missing or corrupt.\nPlease reinstall the game.", ok_action=Return())
    scene black with trueblack
    pause 1.0
    show intro_rendered
    # Laggy af
    #show noise at noisefade(5) zorder 3
    play music spoopy
    $ config.keymap['dismiss'] = []
    $ renpy.display.behavior.clear_keymap_cache()

    $ gtext = glitchtext(renpy.random.randint(12, 80))
    mc "[gtext]{nw}"
    $ consolehistory = []
    if renpy.loadable("inject.rpyc"):
        pass
    else:
        jump mod_intro_reject
    call updateconsole("renpy.start(\"inject.rpyc\")", "Custom mod is ready to inject into \nscripts.rpa")
    pause 1.0
    $ gtext = glitchtext(renpy.random.randint(12, 80))
    mc "[gtext]{nw}"
    call updateconsole("renpy.inject(\"core.rpyc\")", "core.rpyc injected successfully.")
    pause 1.0

    $ gtext = glitchtext(renpy.random.randint(12, 80))
    mc "[gtext]{nw}"
    pause 0.5
    "Initiating \"DDLC: MC's Revenge\" mod{w=0.5}{nw}"
    "Initiating \"DDLC: MC's Revenge\" mod{fast}.{w=0.5}{nw}"
    "Initiating \"DDLC: MC's Revenge\" mod.{fast}.{w=0.5}{nw}"
    "Initiating \"DDLC: MC's Revenge\" mod..{fast}.{w=0.5}{nw}"
    "Initiating \"DDLC: MC's Revenge\" mod{fast}{w=0.5}{nw}"
    "Initiating \"DDLC: MC's Revenge\" mod{fast}.{w=0.5}{nw}"
    "Initiating \"DDLC: MC's Revenge\" mod.{fast}.{w=0.5}{nw}"
    call hideconsole
    $ config.keymap['dismiss'] = dismiss_keys
    $ renpy.display.behavior.clear_keymap_cache()

    $ currentpos = get_pos()
    stop music
    window hide(None)
    hide intro_rendered
    show screen tear(8, offtimeMult=1, ontimeMult=10)
    play music g2
    pause 3.0
    hide screen tear
    stop music
    $ audio.spoopy = "<from " + str(currentpos) + " loop 105.51>mod_assets/sfx/spoopy_glitch.ogg"
    play music spoopy

    mc "Argh...."
    mc "What's this?"
    "I glance around."
    mc "It's really dark here..."
    mc "Where am I?"
    "Where are these noises coming from?!"
    "Ah-"
    mc "What is happening to me...?"
    show intro_rendered
    $ gtext = glitchtext(renpy.random.randint(12, 80))
    mc "{cps=*0.5}Hell{/cps}{nw}"
    $ style.say_dialogue = style.edited
    mc "{cps=*2}Hell{fast}l111o000o who[gtext]{/cps}{nw}"

    play sound "sfx/s_kill_glitch1.ogg"
    hide intro_rendered
    scene bg sayori_bedroom
    window hide(None)
    pause 0.25
    scene black
    pause 0.75
    scene bg s_hang
    pause 0.01
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/glitch3.ogg"
    pause 0.25
    stop sound
    hide screen tear
    scene black
    pause 1.5
    play sound "sfx/s_kill_glitch1.ogg"
    scene bg s_hang_glitch
    pause 0.2
    stop sound
    scene black
    window show(None)
    $ style.say_dialogue = style.normal

    mc "What... {w}the heck?!"
    mc "What is this?!"
    "I suddenly remember what had happened before."
    "My head is spinning like crazy."
    mc "Arghh....!{nw}"
    mc "Why are you showing me that?!{nw}"
    mc "Who's that girl?!{nw}"
    mc "Who are you!?{nw}"
    mc "Who is she?!?!?!{nw}"
    pause 3.0

    mc "..."
    "I roughly remember that day.."
    "The day when..."
    "That girl, was.."
    mc "Ugh... I barely could remember what had happened before..."
    stop music fadeout 2.0
    $ renpy.music.play(audio.ghostmenu, channel="trans", fadein=2.0, tight=True)
    show noise at noisefade(2) zorder 3
    "This room..."
    "It's getting closer.."
    "I can't move."
    "I can't go anywhere.."
    "Please help me..."
    "Help me, [player]..."
    $ renpy.call_screen("dialog", "Please help me.", ok_action=Return())

    $ renpy.music.stop(channel='trans', fadeout=None)
    play music g2
    window hide(None)
    show screen tear(8, offtimeMult=1, ontimeMult=10)
    pause 1.5
    $ renpy.utter_restart()
    return

label mod_intro_reject:
    $ m.display_args["callback"] = monika_showed_up
    call updateconsole("renpy.start(\"inject.rpyc\")", "inject.rpyc does not exist.")
    show monika 1h at t11 zorder 2
    m "{cps=*0.5}Eh...?{/cps}"
    m 2i "{cps=*0.5}What's this?{/cps}"
    call updateconsole("renpy.start(\"inject.rpyc\")", "inject.rpyc does not exist.")
    m "{cps=*0.5}Is this actually a mod?{/cps}"
    m "{cps=*0.5}What are you doing, [player]?{/cps}"
    m 5b "{cps=*0.5}Are you trying to cheat?{/cps}"
    call updateconsole("renpy.start(\"inject.rpyc\")", "inject.rpyc does not exist.")
    m 1q "{cps=*0.5}{i}*Sigh*{/i}{/cps}"
    m 1i "{cps=*0.5}I guess I have no choice....{/cps}"
    call updateconsole("renpy.start(\"just_monika.rpy\")", "Running just_monika.rpy code \nfrom scripts.rpa...")
    $ persistent.ggwp_monika = -1
    pause 1.0
    m 5b "{cps=*0.5}Don't ever do that again, [player]!{/cps}"
    m 5a "{cps=*0.5}Okay, sweetheart~?{/cps}"
    window hide(None)
    hide intro_rendered
    show screen tear(8, offtimeMult=1, ontimeMult=10)
    play music g2
    pause 3.0
    $ m.display_args["callback"] = None
    $ renpy.quit(relaunch=False, status=0)
    return

label mod_crash:
    if renpy.loadable("inject.rpyc"):
        $ persistent.ggwp_monika = 0
    else:
        $ persistent.ggwp_monika = -1
    $ quick_menu = False
    window hide(None)
    stop music fadeout 2.0
    play music ghostmenu
    scene black
    show end
    with dissolve_scene_full
    pause 4.0
    "IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII{nw}"
    show screen tear(8, offtimeMult=1, ontimeMult=10)
    pause 3.0
    hide screen tear
    if renpy.loadable("inject.rpyc"):
        $ renpy.call_screen("dialog", "The file \"inject.rpyc\" has been found.", ok_action=Return())
        $ renpy.call_screen("dialog", "Restarting the game...", ok_action=Return())
        $ renpy.utter_restart()
    else:
        call screen dialog(message="Error: Script file is missing or corrupt.\nPlease reinstall the game.", ok_action=Quit(confirm=False))
    return
