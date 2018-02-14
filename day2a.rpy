label ch_mod_p1:
    scene black 
    pause 1.0
    show p1 zorder 1
    pause 0.01
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    stop sound
    hide screen tear
    play music ap1
    pause 0.33
    hide p1
    show p1a zorder 1
    pause 0.4
    hide p1a
    show p1b zorder 1
    show m_sticker at m_pos zorder 2
    pause 2.58
    show screen tear(20, 0.1, 0.1, 0, 40)
    pause 0.59
    #3.9
    hide screen tear
    hide p1b
    show p1 zorder 1
    pause 1.55
    show m_sticker hop
    pause 0.04
    hide m_sticker
    hide m_sticker hop
    hide pl
    show screen tear(8, offtimeMult=1, ontimeMult=10)
    pause 2.0
    hide screen tear
    stop music
    scene black with trueblack
    scene bg notebook
    show screen quick_menu
    show n_sticker at sticker_mid
    show y_sticker at sticker_right
    with dissolve_scene_full
    play music t4
    $ config.skipping = False
    $ config.allow_skipping = False
    $ allow_skipping = False
    call screen dialog("It's time to write a poem!\n\nPick words you think your favorite club member\nwill like. Something good might happen with\nwhoever likes your poem the most!", ok_action=Return())
    stop music
    # Of course, I'm a lazy bastard, I was trying not to modify Dan Salvato's poem game mechanics.
    hide screen quick_menu
    hide n_sticker
    hide y_sticker
    show screen tear(8, offtimeMult=1, ontimeMult=10)
    play music aglitch2
    pause 2.0
    stop music
    hide screen tear
    scene white
    pause 2.0
    show noise:
        alpha 0.1
    $ gtext = glitchtext(80)
    "[gtext]"
    $ gtext = glitchtext(22)
    menu:
        "ŴHaŧ ĸIñd øF ¶o3m shoųlÐ ¡ mÆke¿"
        "Something cute":
            $ poetappeal = "cute"
        "Something bittersweet":
            $ poetappeal = "bs" # lol
        "Something metaphorical":
            $ poetappeal = "mp"
        "[gtext]":
            $ poetappeal = "abs" # abstract
    hide noise
    scene black
    $ config.allow_skipping = True
    $ allow_skipping = True

    return

###### There's a lot of anti-cheat system that i implemented, trying to prevent abusive save/load mechanics by players
###### (you are probably confused if you see some weird things below, sry you had to see my horrendous codes)

label dftsy_game:
    if not renpy.can_load("1-1", test=False)and not persistent.warning_seen and not (persistent.ggwp_monika > 0):
        $ renpy.save("1-6", extra_info='') # incase if player forgot to save
    return

label dftsy_game2:
    if not renpy.can_load("1-1", test=False) and not persistent.warning_seen and persistent.ggwp_monika > 0:
        $ renpy.call_screen("dialog", "I just saved your life.", ok_action=Return())
        $ renpy.call_screen("dialog", "If you want to be safe, please always save your game.\n-firelightning13", ok_action=Return())
        $ persistent.warning_seen = True
    return

label ch_mod_2:
    $ narrator.display_args["callback"] = player_pls_skip ### use this if player tends to load again after showing up in the clubroom
    $ del _history_list[0:]
    pause 1.0
    scene bg bedroom
    with wipeleft_scene

    if config.developer: # for testing purposes
        $ persistent.ggwp_monika = 0
        $ parfait_girls = False
        $ persistent.tea_set = False
        $ persistent.mc_violent = False
        $ persistent.poster_seen = False
        $ persistent.cheat_mod = 0
        $ poster_checked = False
        $ closet_checked = False
    if persistent.protecc: # refresh curse words list
        $ fword = "***"
        $ fgword = "******"
        $ bword = "****"
        $ aword = "******"
        $ sword = "***"
    else:
        $ fword = "uck"
        $ fgword = "ucking"
        $ bword = "itch"
        $ aword = "sshole"
        $ sword = "hit"
    "Argh.."
    "I had a bad dream..."
    "...Someone screaming my name."
    "I wonder who {i}she{/i} was?"
    "She said something like \"save me\"..."
    default persistent.warning_seen = False
    call dftsy_game
    "Or something like \"Don't forget to save your game\"...?"
    call dftsy_game2
    "That was weird..."
    if poetappeal != "abs" or persistent.ggwp_monika == 1:
        # if player chooses other than abstract
        "Anyway, it's pretty late right now."
        "I have to go to school quickly!"
    else:
        # if player chooses abstract poem
        "Anyway, I still have time to go to school."
        "I need to get ready!"

    scene bg residential_day
    with wipeleft_scene
    show screen tear(20, 0.1, 0.1, 0, 40)
    play music aglitch2
    pause 0.25
    stop music
    hide screen tear
    scene bg res_gl2
    play music t2l
    #$ style.say_window = style.window
    $ style.say_window = style.window_lq

    "It's an ordinary school day, like any other."
    #"Mornings are usually the worst, being surrounded by couples and friend groups walking to school together."
    if poetappeal != "abs" or persistent.ggwp_monika == 1:
        "Mornings are usually the worst, being surrounded by couples{nw}"
        $ _history_list.pop()
        "It looks like there are only a few people running around.. they must be late, just like me."
        #"Meanwhile, I've always walked to school alone."
        "Meanwhile, I've always walked{nw}"
        $ _history_list.pop()
        "Meanwhile, I am trying to run as fast as possible so that I can catch up with them."
        window auto
        "My class could start any minute now!"
        if persistent.ggwp_monika > 0:
            label mc_realise:
                # going back in time when you load at the start of the game
                $ currentpos = get_pos()
                stop music
                window hide(None)
                show screen tear(20, 0.1, 0.1, 0, 40)
                play sound "sfx/s_kill_glitch1.ogg"
                pause 0.25
                stop sound
                hide screen tear
                window show(None)
                scene bg residential_day
                $ style.say_window = style.window
                $ audio.t2 = "<from " + str(currentpos) + " loop 4.499>bgm/2.ogg"
                play music t2

                mc "Ah, what just happened?!"
                mc "Did I just..."
                mc "What's going on right now?"
                "Confused, I glance around."
                "Did I just go back in time?"
                if persistent.ggwp_monika == 1:# post going to sayori's house
                    mc "That screaming girl back there.."
                    mc "Argh!"
                elif persistent.ggwp_monika == 2:# going back in time after seeing poster/throwing a chair
                    mc "Did I do something in my classroom just now?"
                    mc "Argh!"
                "What am I saying?!"
                "I'm really late right now!"
                window auto
                "Forget this, I'm going to school!"
                if persistent.ggwp_monika == 2:
                    jump skip_2_2a
    else:
        "Mornings are usually the worst, being surrounded by couples and friend groups walking to school together."
        "I mean, I still have time to go to school, so..."
        window hide(None)
        pause 0.5
        window show(None)
        $ gtext = glitchtext(8)
        $ stext = glitchtext(80)
        $ s_name = "[gtext]"
        s "{cps=*2}[stext]{/cps}{nw}" # spooky
        $ _history_list.pop()
        $ currentpos = get_pos()
        stop music
        window hide(None)
        show screen tear(20, 0.1, 0.1, 0, 40)
        play music s_gl
        pause 0.25
        stop music
        hide screen tear
        window show(None)
        mc "Eh?"
        "What was that?"
        window auto
        "I hear someone screaming in the distance..."
        "The same voice that I heard in my dream."
        "It's coming from my neighbor's house."
        $ style.say_window = style.window

        scene bg house
        with wipeleft
        stop music
        $ audio.t2 = "<from " + str(currentpos) + " loop 4.499>bgm/2.ogg"
        play music t2

        "This house..."
        "...looks familiar to me..."
        "My memory's been a little bit hazy lately."
        "I proceed to knock the door."
        mc "H-Hello? Is anyone there?"
        "The house looks empty to me, {w}the door is strangely unlocked..."
        "Has something happened in this house?"
        #mc "I'm coming over..." basically how to deal with robbery situation
        "{cps=30}I silently open the front door...{/cps}{nw}"
        python:
            currentpos = get_pos()
            startpos = currentpos - 0.3
            if startpos < 0: startpos = 0
            track = "<from " + str(startpos) + " to " + str(currentpos) + ">bgm/2.ogg"
            renpy.music.play(track, loop=True)
        if persistent.ggwp_monika == 0:
            $ persistent.ggwp_monika = 1
            show screen tear(8, offtimeMult=1, ontimeMult=10)
            pause 1.0
            $ renpy.utter_restart()
        elif persistent.ggwp_monika == 2:
            jump mc_realise
        else:
            window hide(None)
            show screen tear(20, 0.1, 0.1, 0, 40)
            play sound "sfx/s_kill_glitch1.ogg"
            pause 0.25
            stop sound
            hide screen tear
            window show(None)

            # going back in time when you load in front of sayori's house
            mc "Wait, I thought I tried opening this door before."
            mc "Ah, what just happened?!"
            mc "Did I just..."
            mc "What's going on right now?"
            "Confused, I glance around once again."
            "Did I just go back in time?"
            "My gut says that I shouldn't be here."
            "I don't want to get in trouble again."
            "What am I saying?!"
            window auto
            "Screw this, I'm going to school!"

    if poetappeal != "abs" and not persistent.ggwp_monika == 1:
        scene bg cr_gl # glitched bg when choosing other than abstract
    else:
        scene bg class_day # normal bg when choosing abstract poem
    with wipeleft_scene

    "The school day is as ordinary as ever, and it's over before I know it."
    "After I pack up my things, I stare blankly at the wall{nw}"
    $ _history_list.pop()
    "After I pack up my things, I should get going."
    if persistent.ggwp_monika != 1:# or config.developer:
        # this stuff happens when player not choose abstract poem
        "Literature club{nw}"
        $ _history_list.pop()
        $ style.say_dialogue = style.edited
        "Literature club{fast}, here I go...{nw}"
        window hide(None)
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound aglitch2
        pause 0.25
        stop sound
        hide screen tear
        window show(None)
        $ style.say_dialogue = style.normal
        "Argh!{nw}"
        "What?! {w}Oh...."
        "I just noticed..."
        "This classroom seems a little bit off..."
        "I feel like something is not right..."
        window hide(None)
        window auto
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound s_gl
        pause 0.25
        stop sound
        hide screen tear
        window auto
        if persistent.ggwp_monika == 2:
            label mc_realise_2:
                # going back in time after seeing poster/throwing a chair
                window show(None)
                $ gtext = glitchtext(50)
                mc "[gtext]{nw}"
                window hide(None)
                show screen tear(20, 0.1, 0.1, 0, 40)
                play sound aglitch2
                pause 0.25
                stop sound
                hide screen tear
                window show(None)
                scene bg class_day
                $ style.say_window = style.window
                mc "Ah, what just happened?!"
                mc "Did I just..."
                mc "What's going on right now?"
                "I'm so confused."
                "What was all that about?"
                mc "Did I do something weird just now?"
                mc "Argh!"
                "What am I saying?!"
                "I'm really late now!"
                "Screw it, I'm going to the litera{nw}"
                jump skip_2_2a
        elif parfait_girls or persistent.tea_set or persistent.ggwp_monika == 1:
            $ gtext = glitchtext(50) # prevent anti-cheat
            mc "[gtext]{nw}"
            play sound aglitch1
            pause 1.0
            stop sound
            jump skip_2_2a
        if not config.skipping:#or config.developer:
            label mc_choice:
                $ gtext = glitchtext(12)
                menu:
                    " "
                    "Check the closet" if not closet_checked:
                        if persistent.ggwp_monika == 2:
                            jump mc_realise_2
                        jump check_closet
                    "Do something violent": # release your anger, don't be like a green hulk/ogre
                        if persistent.ggwp_monika == 2:
                            jump mc_realise_2
                        if persistent.protecc:
                            # praise to god
                            $ renpy.call_screen("dialog", "WARNING: Profanity filter is enabled.", ok_action=Return())
                            $ renpy.call_screen("dialog", "Something terrible is going to happen.\nProceed with caution.", ok_action=Return())
                        jump throw_chair
                    "[gtext]" if not poster_checked: # check poster
                        if persistent.ggwp_monika == 2:
                            jump mc_realise_2
                        if persistent.protecc:
                            $ renpy.call_screen("dialog", "WARNING: Profanity filter is enabled.", ok_action=Return())
                            $ renpy.call_screen("dialog", "Something terrible is going to happen.\nProceed with caution.", ok_action=Return())
                        jump check_poster
        else:
            $ config.skipping = False
            jump skip_2_2a
    else:
        # skip over those stuff if player choose abstract poem
        window auto
        "Literature club, here I go..."
        stop music fadeout 1.0
        scene bg corridor
        with wipeleft_scene
        jump ch_mod_2a

label check_closet:
    scene bg closet
    with wipeleft_scene
    window auto
    $ style.say_window = style.window
    "Just curious to see what's inside that closet."
    "I'm expecting the contents of that closet to simply be classroom stuff like books, files or markers."
    "But you'll never know what is actually inside it until you look."
    "Well, here goes nothing."
    play sound closet_open
    "I open the closet."
    show noise at noisefade(5) zorder 3
    mc "..."
    mc "I found markers."
    "Construction paper, too.."
    "Wasn't Monika trying to find this stuff yesterday?"
    $ half_chance = renpy.random.randint(0, 1)
    if half_chance == 0:# or config.developer:
        $ another_chance = renpy.random.randint(0, 3) # Make it fair
        if another_chance == 0:# or config.developer:
            ### 12.5% chance
            "Well, I guess I could give them to Monika after all."
        else:
            ### 37.5% chance
            mc "What's this?"
            "There's a lone volume of manga amidst a stack of various books on the side of one of the shelves."
            "Curious, I pull the book out."
            mc "Parfait Girls...? {w}Part one?"
            "I stare at the cover."
            "It features four girls in colorful attire striking animated feminine poses."
            "Have I heard of this manga before?"
            "My memory is a little bit hazy, so I don't know if I read it before."
            "I wonder why it's here in the classroom?"
            "Has it been here the entire time?"
            mc "I guess I could keep it, though..."
            "I put it inside my bag, just in case."
            "I kind of want to read it though, in my spare time."
            "Well, about the markers and construction paper..."
            "I guess I could give them to Monika after all."
            $ parfait_girls = True
            $ closet_checked = True
            #it's possible to get both parfait girls and tea set, for smart gamers; so i just gonna leave it here
    else:
        ### 50% chance, i think yuri like this idea
        "Huh? There is a tea set as well."
        "Who put in this closet anyway?"
        "Maybe one of my teachers needs it?"
        "Eh, whatever."
        "I just grab the markers and construction paper instead."
        "Well, I guess I could give this stuff to Monika after all."
        $ persistent.tea_set = True
    play sound closet_close
    "I proceed to close the closet."
    "Hmm... what else should I do...?"
    $ closet_checked = True
    if persistent.tea_set or parfait_girls:
        # oops, you ran out of time
        window hide(None)
        window auto
        play sound aglitch1
        pause 1.0
        hide noise
        stop sound
        jump skip_2_2a
    else:
        window auto
        hide noise
        jump mc_choice

label throw_chair:
    show noise at noisefade(5) zorder 3
    "Hmm..."
    "I feel like doing something crazy..."
    "Well, here goes nothing..."
    mc "May God have mercy on me...{nw}"
    $ _history_list.pop()
    play sound aglitch1
    $ style.say_dialogue = style.edited
    "{cps=*2}LOAD ME{/cps}{nw}"
    $ _history_list.pop()
    $ style.say_dialogue = style.normal
    stop sound
    mc "May God have mercy on me...{fast}"
    "I grab the nearest chair."
    if persistent.mc_violent:
        play sound gb_gl
        pause 1.5
        stop sound
        jump skip_2_2a # anti-cheat
    "Then... I throw the chair as hard as I can{nw}"
    play sound throw
    "Then... I throw the chair as hard as I can{fast} at one of the classroom windows{nw}"
    $ persistent.mc_violent = True
    $ persistent.ggwp_monika = 2
    hide noise
    window hide(None)
    stop music
    show screen tear(8, offtimeMult=1, ontimeMult=10)
    play sound gb_gl
    pause 1.5
    $ renpy.error("cg_glass_break.png not found. Oops... I'm too lazy to add custom arts in my mod. Click \"Ignore\" to restart the game.")
    stop sound
    $ renpy.utter_restart()

label check_poster:
    $ gtext = glitchtext(50)
    mc "[gtext]{nw}"
    window hide(None)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    stop sound
    hide screen tear
    $ style.say_window = style.window
    window show(None)
    scene bg class_day

    "I guess I could just look around..."
    pause 1.0
    $ counter = 5 # i dont want to play longer
    ### initiating terrible "look-around" engine, can bypassed by skipping
    ### again, this is by intention
    if not config.skipping:
        while counter > 0:
            $ direction = renpy.random.randint(0, 4)
            if direction == 0:
                if counter == 5: # make sure you don't look behind first ehehehe
                    pass
                else:
                    $ counter = 0
            elif direction == 1:
                "I look right."
            elif direction == 2:
                "I look up."
            elif direction == 3:
                "I look down."
            elif direction == 4:
                "I look left."
            $ counter -= 1
        "I look behind me..."

    $ half_chance = renpy.random.randint(0, 2)
    if half_chance == 0:# or config.developer:
        # 33.33% chance
        "Nothing is happening around here..."
        "Maybe I should do something else?"
        "Well..."
        $ poster_checked = True
        window auto
        jump mc_choice
    else:
        # 66.66% chance
        "I see..."
        "A girl..."
        "In the poster."
        mc "Uh..."
        mc "What is this picture?!"
        $ currentpos = get_pos()
        stop music
        scene black
        window hide(None)
        pause 1.0
        scene bg s_hang # picture of sayori hanging, uh
        pause 0.01
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound aglitch2
        pause 0.25
        stop sound
        hide screen tear
        window show(None)
        $ audio.t2l = "<from " + str(currentpos) + " loop 4.499>mod_assets/sfx/2l.ogg"
        play music t2l
        scene bg class_day
        
        mc "What is this picture?!{fast}"
        $ _history_list.pop()
        "I quickly look away."
        "My head start to feel dizzy again."
        if seen_day == 1: ### 11.11% chance
            "That's.... what I saw yesterday..." # if you see sayori poster yesterday
        mc "I wish I didn't see that..."
        stop music
        "I suppress the urge to vomit."
        "I think... {w}I just want to go outside."
        "I need some air."
        scene bg cord_gl
        with wipeleft_scene
        show noise at noisefade(5) zorder 3
        "{i}What the hell was that?!?!{/i}"
        "What did I just see??"
        "God! Please, I don't want to do this anymore!"
        "Don't do this to me!"
        "I'm not a program! I'm a f[fgword] human!"
        "I DONT WANT TO DO THIS ANYMORE!!"
        $ style.say_dialogue = style.edited
        "DO YOU UNDERSTAND ME!??!{nw}" # MC gone rogue
        $ style.say_dialogue = style.normal
        window hide(None)
        hide noise
        show screen tear(8, offtimeMult=1, ontimeMult=10)
        pause 1.5
        $ persistent.ggwp_monika = 2
        $ persistent.poster_seen = True
        $ renpy.error("Ren'py is unable to suppress player's unstable emotion... Click \"Ignore\" to restart the game.")
        $ renpy.utter_restart()

label skip_2_2a:
    $ narrator.display_args["callback"] = None
    stop music
    window hide(None)
    window auto
    scene black with trueblack
    pause 1.0
    scene bg corridor
    with wipeleft_scene
    jump ch_mod_2a
