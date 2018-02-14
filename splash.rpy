## This splash screen is the first thing that Renpy will show the player
##
## Before load, check to be sure that the archive files were found.
## If not, display an error message and quit.
init -100 python:
    #Check for each archive needed
    for archive in ['audio','images','scripts','fonts']:
        if not archive in config.archives:
            #If one is missing, throw an error and chlose
            renpy.error("DDLC archive files not found in /game folder. Check installation and try again.")

## First, a disclaimer declaring this is a mod is shown, then there is a
## check for the original DDLC assets in the install folder. If those are
## not found, the player is directed to the developer's site to download.
##
init python:
    menu_trans_time = 1
    #The default splash message.
    splash_message_default = "This game is an unofficial fan work,\nunaffiliated with Team Salvato."
    #Ah, nice message. I wonder who did these...
    splash_messages = [
    "Please support Doki Doki Literature Club.",
    "Monika is watching you code.",
    "Please support firelightning13.\nHe's a great guy.",
    "I spend everyday working with my mod.",
    "Monika is the best girl",
    "Sayori is the best girl",
    "I tried my best..",
    "Don't forget to save your game!~",
    "I love Dan Salvato.",
    "Can you change the world?",
    "Her Third Eye is getting closer.",
    ]

image splash_warning = ParameterizedText(style="splash_text", xalign=0.5, yalign=0.5)

##Here's where you can change the logo file to whatever you want
image menu_logo_mod:
    "/mod_assets/DDLCMCR.png"
    subpixel True
    xcenter 240
    ycenter 120
    zoom 0.60
    menu_logo_move

image menu_logo:
    "gui/logo.png"
    subpixel True
    xcenter 240
    ycenter 120
    zoom 0.60
    menu_logo_move

image hi_monika:
    topleft
    "images/cg/monika/monika_bg.png"

image menu_bg:
    topleft
    "gui/menu_bg.png"
    menu_bg_move

image game_menu_bg:
    topleft
    "gui/menu_bg.png"
    menu_bg_loop

image menu_fade:
    "white"
    menu_fadeout

image menu_art_y:
    subpixel True
    "gui/menu_art_y.png"
    xcenter 600
    ycenter 335
    zoom 0.60
    menu_art_move(0.54, 600, 0.60)

image menu_art_n:
    subpixel True
    "gui/menu_art_n.png"
    xcenter 750
    ycenter 385
    zoom 0.58
    menu_art_move(0.58, 750, 0.58)

image menu_art_s:
    subpixel True
    "gui/menu_art_s.png"
    xcenter 510
    ycenter 500
    zoom 0.68
    menu_art_move(0.68, 510, 0.68)

image menu_art_m:
    subpixel True
    "gui/menu_art_m.png"
    xcenter 1000
    ycenter 640
    zoom 1.00
    menu_art_move(1.00, 1000, 1.00)

image menu_art_y_ghost:
    subpixel True
    "gui/menu_art_y_ghost.png"
    xcenter 600
    ycenter 335
    zoom 0.60
    menu_art_move(0.54, 600, 0.60)

image menu_art_n_ghost:
    subpixel True
    "gui/menu_art_n_ghost.png"
    xcenter 750
    ycenter 385
    zoom 0.58
    menu_art_move(0.58, 750, 0.58)

image menu_art_s_ghost:
    subpixel True
    "gui/menu_art_s_ghost.png"
    xcenter 510
    ycenter 500
    zoom 0.68
    menu_art_move(0.68, 510, 0.68)

image menu_art_m_ghost:
    subpixel True
    "gui/menu_art_m_ghost.png"
    xcenter 1000
    ycenter 640
    zoom 1.00
    menu_art_move(1.00, 1000, 1.00)

image menu_art_s_glitch:
    subpixel True
    "gui/menu_art_s_break.png"
    xcenter 470
    ycenter 600
    zoom 0.68
    menu_art_move(.8, 470, .8)

image menu_nav:
    "gui/overlay/main_menu.png"
    menu_nav_move

image menu_particles:
    2.481
    xpos 224
    ypos 104
    ParticleBurst("gui/menu_particle.png", explodeTime=0, numParticles=20, particleTime=2.0, particleXSpeed=6, particleYSpeed=4).sm
    particle_fadeout

transform particle_fadeout:
    easeout 1.5 alpha 0

transform menu_bg_move:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat
    parallel:
        ypos 0
        time 0.65
        ease_cubic 2.5 ypos -500

transform menu_bg_loop:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat

transform menu_logo_move:
    subpixel True
    yoffset -300
    time 1.925
    easein_bounce 1.5 yoffset 0

transform menu_nav_move:
    subpixel True
    xoffset -500
    time 1.5
    easein_quint 1 xoffset 0

transform menu_fadeout:
    easeout 0.75 alpha 0
    time 2.481
    alpha 0.4
    linear 0.5 alpha 0

transform menu_art_move(z, x, z2):
    subpixel True
    yoffset 0 + (1200 * z)
    xoffset (740 - x) * z * 0.5
    zoom z2 * 0.75
    time 1.0
    parallel:
        ease 1.75 yoffset 0
    parallel:
        pause 0.75
        ease 1.5 zoom z2 xoffset 0

image intro:
    truecenter
    "white"
    0.5
    "bg/splash.png" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

image warning:
    truecenter
    "white"
    "splash_warning" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

#image tos = "bg/warning.png"
image tos = "mod_assets/bg/warning.png"
image tos2 = "mod_assets/bg/warning2.png"

# Make sure character files are in place
init python:
    #if not persistent.do_not_delete:
    if persistent.playthrough <= 5:
        try: renpy.file("../characters/monika.chr")
        except: open(config.basedir + "/characters/monika.chr", "wb").write(renpy.file("monika.chr").read())
        try: renpy.file("../characters/natsuki.chr")
        except: open(config.basedir + "/characters/natsuki.chr", "wb").write(renpy.file("natsuki.chr").read())
        try: renpy.file("../characters/yuri.chr")
        except: open(config.basedir + "/characters/yuri.chr", "wb").write(renpy.file("yuri.chr").read())
    if persistent.playthrough == 0:
        try: renpy.file("../characters/sayori.chr")
        except: open(config.basedir + "/characters/sayori.chr", "wb").write(renpy.file("sayori.chr").read())

label splashscreen:
    default persistent.first_run = False
    # Logic for detecting if the game has been reinstalled
    python:
        mod_firstrun = ""
        try:
            mod_firstrun = renpy.file("mod_firstrun").read(1)
        except:
            with open(config.basedir + "/game/mod_firstrun", "wb") as f:
                pass
    if not mod_firstrun: #renpy.loadable("10"):
        if persistent.first_run: #and not persistent.do_not_delete:
            $ quick_menu = False
            scene black
            menu:
                "A previous save file/updates for this mod has been found. Would you like to delete your save data and start over? If you have previous update from this mod, you should do so, or else it will break my mod!"
                "Yes, delete my existing data.":
                    "Deleting save data...{nw}"
                    python:
                        delete_all_saves()
                        renpy.loadsave.location.unlink_persistent()
                        renpy.persistent.should_save_persistent = False
                        renpy.utter_restart()
                "No, continue where I left off.":
                    pass

        python:
            if not mod_firstrun:
                with open(config.basedir + "/game/mod_firstrun", "w") as f:
                    f.write("1")
            #filepath = renpy.file("firstrun").name
            #open(filepath, "a").close()

    #If this is the first time the game has been run, show a disclaimer
    #if not persistent.first_run:
    if not persistent.first_run:
        default persistent.finished_ddlc = None
        #Optional, load a copy of DDLC save data
        call import_ddlc_persistent

        $ quick_menu = False
        scene white
        pause 0.5
        scene tos
        with Dissolve(1.0)
        pause 1.0
        "[config.name] is a Doki Doki Literature Club fan mod that is not affiliated with Team Salvato."
        "It is designed to be played only after the official game has been completed, and contains spoilers for the official game."
        "This story is mostly based on theories that were made by fans of DDLC, and in no way canon to the original story of DDLC or any other future games by Team Salvato."
        "Game files for Doki Doki Literature Club are required to play this mod and can be downloaded for free at: http://ddlc.moe"
        if persistent.finished_ddlc == "postcredits_loop":
            menu:
                "This mod detects that you already have completed the game. By playing [config.name], you consent to your exposure of highly disturbing content."
                "I agree.":
                    pass
        else:
            menu:
                "By playing [config.name] you agree that you have completed DDLC and accept any spoilers contained within, and you consent to your exposure of highly disturbing content."
                "I agree.":
                    pass
        scene tos2
        with Dissolve(1.5)
        pause 1.0

        scene white
        with Dissolve(1.5)

        $ persistent.first_run = True



    $ basedir = config.basedir.replace('\\', '/')

    #autoload handling
    #Use persistent.autoload if you want to bypass the splashscreen on startup for some reason
    if persistent.autoload and not _restart:
        jump autoload

    # Start splash logic
    $ config.allow_skipping = False

    # Splash screen
    show white
    $ persistent.ghost_menu = False #Handling for easter egg from DDLC
    $ splash_message = splash_message_default #Default splash message
    $ renpy.music.play(config.main_menu_music)
    show intro with Dissolve(0.5, alpha=True)
    pause 2.5
    hide intro with Dissolve(0.5, alpha=True)
    #You can use random splash messages, as well. By default, they are only shown during certain acts.
    if persistent.demu_demu:
        $ splash_message = "Just Monika."
    elif persistent.playthrough == 2 and renpy.random.randint(0, 3) == 0:
        $ splash_message = renpy.random.choice(splash_messages)
    show splash_warning "[splash_message]" with Dissolve(0.5, alpha=True)
    pause 2.0
    hide splash_warning with Dissolve(0.5, alpha=True)
    $ config.allow_skipping = True
    return

label warningscreen:
    hide intro
    show warning
    pause 3.0

label after_load:
    $ config.allow_skipping = allow_skipping
    $ _dismiss_pause = config.developer
    $ persistent.ghost_menu = False #Handling for easter egg from DDLC
    $ style.say_dialogue = style.normal
    #Check if the save has been tampered with
    if anticheat != persistent.anticheat:
        stop music
        scene black
        "The save file could not be loaded."
        "Are you trying to cheat?"
        #Handle however you want, default is to force reset all save data
        $ delete_all_saves()
        $ renpy.utter_restart()
    return



label autoload:
    python:
        # Stuff that's normally done after splash
        if "_old_game_menu_screen" in globals():
            _game_menu_screen = _old_game_menu_screen
            del _old_game_menu_screen
        if "_old_history" in globals():
            _history = _old_history
            del _old_history
        renpy.block_rollback()

        # Fix the game context (normally done when loading save file)
        renpy.context()._menu = False
        renpy.context()._main_menu = False
        main_menu = False
        _in_replay = None

    # Pop the _splashscreen label which has _confirm_quit as False and other stuff
    $ renpy.pop_call()
    jump expression persistent.autoload

label quit:
    return
