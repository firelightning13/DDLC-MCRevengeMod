label ch_mod_2a:
    $ style.say_window = style.window
    $ _history_list = []
    $ config.keymap['dismiss'] = dismiss_keys ### Just incase if bugs appear, where keys and mouse are not responding
    $ renpy.display.behavior.clear_keymap_cache()

    if persistent.ggwp_monika >= 3: ### anti-cheat system
        $ persistent.cheat_mod += 1
        label mc_realise_3:
            if renpy.showing("bg spoopy", layer='master'):
                $ temp_scene = 1
            elif renpy.showing("bg club_day", layer='master'):
                $ temp_scene = 2
            elif renpy.showing("bg corridor", layer='master'):
                $ temp_scene = 3
            "Ah, what happened?"
            "Did I do something weird again?"
            "Maybe there's something wrong with me..."
            "Is {w}this {w}actually {w}a {w}game?"
            scene black
            play music ap1
            window hide(None)
            pause 0.35
            show m_sticker at m_pos zorder 5
            show p1b zorder 4
            pause 0.08
            stop music
            hide m_sticker
            hide p1b
            if temp_scene == 1:
                scene bg spoopy
            elif temp_scene == 2:
                scene bg club_day
            elif temp_scene == 3:
                scene bg corridor
            "..."
            "I think I... realized that..."
            window hide(None)
            show screen tear(20, 0.1, 0.1, 0, 40)
            play sound "sfx/s_kill_glitch1.ogg"
            pause 0.25
            stop sound
            hide screen tear
            pause 1.0
            window show(None)
            $ persistent.mc_realise = True
            $ persistent.ggwp_monika = 2
            $ del _history_list[-6:]
            return
    play music t2o
    "Well..."
    "I managed to get here in time."
    "Even though I'm a little bit late. I hope they don't mind..."
    "I timidly open the front door."

    if renpy.random.randint(0, 5) == 0:
        scene bg spoopy
        $ seen_day += 1
    else:
        scene bg club_day
    with wipeleft
    $ currentpos = get_pos()
    stop music
    $ audio.t2g3 = "<from " + str(currentpos) + " loop 4.492>bgm/2g2.ogg"
    play music t2g3

    show monika 5 at t11 zorder 2
    show layer master:
        subpixel True
        truecenter
        linear 240 rotate 8 zoom 1.30
    m "Hi again, [player]!"
    m "Glad to see you didn't run away on us. Hahaha!"
    ####################################### MC's REACTIONS FLAG #############################################
    if persistent.poster_seen:
        "I wish I was..."
        "After what I saw something {i}horrible{/i} earlier!"
        if seen_day == 1: ### 18.52% chance
            "I saw it again..."
            "What the hell is wrong with this world..."
        elif seen_day == 2: ### 1.851% chance, wow that's too little actually, i should set up achievement system for this
            "That's three in a row..."
            "What..."
        else: ### 46.29% chance
            "What's up with that anyway?"
        mc "Ah... well..."
    elif persistent.mc_violent: # mc's personality changed a little bit.?
        "Oh wait... I should've done that earlier..."
        "Throwing a chair is not enough I guess."
        "Well, apparently I can't go back. I'm not a super hero that can change and manipulate time and space."
        # unironically, you can't because i don't want to compromise my anti-cheat system
        "That would've been cool.."
        mc "Nah, don't worry."
    elif poster_checked or closet_checked: ### 41.66% chance
        # late if mc checked the closet/not seeing the poster when looked behind
        mc "Ah, sorry. I'm a bit late."
    else: ### 0% chance, unless they cheat
        mc "Nah, don't worry."
    mc "This might be a little strange for me, but I at least keep my word."
    show monika at thide zorder 1
    hide monika
    if persistent.ggwp_monika > 0: # 66.66% chance if != abs
        # post going to sayori's house/game crash (caused by throwing chair/seeing poster)
        "I don't think I can go anywhere at this point."
        if seen_day == 1 and not persistent.poster_seen: ### 13.88% chance
            "Wait..."
            "What's that poster on the back wall of the clubroom!?"
            "Is this even reality?"
        elif seen_day == 2 and not persistent.poster_seen: ### 2.777% chance, 2low4me
            "I can tell by the poster on the back wall of the clubroom"
            "..."
        else: ### 69.44% chance
            "Is this even reality?"
    else:
        # normal playthrough (no game crash, no saving/reloading)
        if seen_day == 1: ### 13.88% chance
            "What's that poster on the back wall of the clubroom!?"
            "Umm--Well..."
            "I'm... {w}back at the Literature Club..."
            "I was the last to come in... {w}so everyone else is already hanging out..."
        elif seen_day == 2: ### 2.777% chance
            "Is that poster again from yesterday?!"
            "What is going on in this world..."
        else: ### 69.44% chance
            "Well, I'm back at the Literature Club."
            "I was the last to come in, so everyone else is already hanging out."
    ########################################### END FLAG ##################################################################
    show yuri glitch2 at t32 zorder 2
    y "Thanks for keeping your promise, [player]."
    y 1a "I hope this isn't too overwhelming of a commitment for you."
    y 1u "Making you dive headfirst into literature when you're not accustomed to it..."
    if persistent.poster_seen:
        "I don't think that's my real problem right now..."
    else:
        "I don't know about that, as I think literature is not really bad for me"
        mc "Well, that's true..."
        mc "It wouldn't be a problem. I would like to try out new things for sure..."
    show natsuki glitch1 at i33 zorder 2
    n "Oh, come on! Like he deserves any slack."
    # mc saw glitching natsuki
    if persistent.mc_violent:
        "That scare the s[sword] out of me..."
        if not persistent.protecc: # if profanity filter disabled
            "Oops, did I swear?"
            $ del _history_list[-2:]
    else:
        "Natsuki... you're scaring me a little..."
    n 4e "You already had to be dragged here by Monika."
    n "I don't know if you plan to just come here and hang out, or what..."
    if persistent.mc_violent:
        "And throw a chair? Sounds good to me."
        $ _history_list.pop()
        "Sorry, that was taken out of context."
    elif persistent.ggwp_monika > 0:
        "I completely disagree."
    n "But if you don't take us seriously, then you won't see the end of it."
    if persistent.mc_violent:
        mc "Well, I am here now. So...{w=1.0}{nw}"
    show monika 2b at l41 onlayer front
    m "Natsuki, you certainly have a big{nw}"
    $ _history_list.pop()
    hide monika onlayer front
    window hide(None)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    stop sound
    hide screen tear
    window show(None)
    show monika 2b at i41 zorder 3
    m "Natsuki, you certainly have a big{fast} mouth for someone who keeps her manga collection in the clubroom."
    n 4o "M-M-M...!!"
    show monika at lhide zorder 3
    hide monika
    "Natsuki finds herself stuck between saying \"Monika\" and \"Manga\"."
    show natsuki at h33
    n 1v "Manga is literature!!"
    show natsuki at thide zorder 1
    hide natsuki
    "Swiftly defeated, Natsuki plops back into her seat."
    if parfait_girls: # 33.33% chance
        "Well, I mean I had the book that I found in my classroom."
        if poetappeal == "cute":
            # if u make cute poem and found parfait girls
            "Though I might want to share with her later.."
        else:
            # if u only found parfait girls
            "Maybe I should share with her..."
    show yuri 2s at t11 zorder 2
    y "I'm sorry, [player]..."
    y "We'll make sure to put your comfort first, okay?"
    show yuri 2g
    "Yuri shoots Natsuki with a disappointed glance."
    if poetappeal == "mp":
        "I feel awkward already..."
    elif poetappeal == "cute" or poetappeal == "bs":
        "I mean technically manga is literature, right?"
    y 1a "Um, anyway..."
    y "Now that you're in the club and all..."
    y "...Perhaps you might have interest in picking up a book to read?"
    if poetappeal == "mp" or ihorror:
        mc "Oh, well..."
        mc "I thought about it when I wrote my poem last night."
        mc "I think I should start reading something."
        "I don't know... but I feel like I've done something like this before..."
        "What is happening with my memory?"
        y 1b "Well... I was thinking that..."
        y 2u "...as Vice President, I might help you with that."
        mc "Oh, alright. What should I read, then?"
        y 1a "Well..."
    else:
        #mc "Well..."
        mc "Ah, well..."
        mc "I can't really say no either way."
        mc "Like you said, I'm in this club now."
        mc "So it only feels right for me to do something like that, if you ask."
        y 4b "W-Wait..."
        y "I didn't mean it like that!"
        y "Uu..."
        y "If you don't really want to, then forget I said anything, I guess..."
        mc "Ah--No, it's not that, Yuri."
        mc "I want to try to be a part of this club."
        mc "So even if I don't read often, I'd be happy to pick up a book if you wanted me to."
        y 3t "A-Are you sure...?"
        y "I just felt like..."
        y 3u "...Well, as Vice President and all..."
        y "...That I should help you get started on something you might like."
    "Yuri reaches into her bag and pulls out a book."
    y 1s "I didn't want you to feel left out..."
    y "So I picked out a book that I thought you might enjoy."
    y "It's a short read, so it should keep your attention, even if you don't usually read."
    y "And we could, you know..."
    show yuri at sink
    y 4b "Discuss it...if you wanted..."
    #"Th-This is..."
    if persistent.ggwp_monika >= 3: ### if player reloads again after mc glitches out when yuri "gave" him a book
        $ currentpos = get_pos()
        stop music
        call mc_realise_3
        $ audio.t2g3 = "<from " + str(currentpos) + " loop 4.492>bgm/2g2.ogg"
        play music t2g3
        y 1t "[player]?"
        mc "A-Ah..."
        mc "Yuri, thank you! I'll definitely read this!"
        "My hands shiver all of sudden, but I'm trying to clench my fist to make it stop."
        "Then, I slowly take the book."
        show yuri 1f at t11 zorder 2
        y "[player]? Are you okay? You look pale..."
        mc "I'm fine..."
        mc "Don't worry about it."
        y 2m "Phew..."
        y 2a "Well, you can read it at your own pace."

        show yuri at thide zorder 1
        hide yuri
        show layer master
        $ currentpos = get_pos()
        stop music
        $ audio.t2gl = "<from " + str(currentpos) + " loop 4.492>mod_assets/sfx/2gl.ogg"
        play music t2gl

        "My heart pounds really fast..."
        "What's going on?"
        $ config.keymap['dismiss'] = []
        $ renpy.display.behavior.clear_keymap_cache()
        "I take a deep breath for 3 seconds long.{w=1.5}{nw}"
        $ config.keymap['dismiss'] = dismiss_keys
        $ renpy.display.behavior.clear_keymap_cache()
        "My quivering hands finally stop."
        "I don't know why it happens, my mind seems to be confused about it..."
        "I glance around."
        "Yuri's face is already buried in a book."
        "Meanwhile, Natsuki is rummaging around in the closet."
    elif (poetappeal == "abs" or poetappeal == "bs") and not persistent.mc_realise: ### glitch happens when choosing abstract/bittersweet poem
        "Th-This is..."
        if not config.skipping: ### mc glitched out, can be avoided by skipping
            "How is this girl accidentally being so {nw}"
            $ _history_list.pop()
            $ persistent.ggwp_monika = 3
            $ style.say_dialogue = style.edited
            $ currentpos = get_pos()
            stop music
            $ audio.t2gl = "<from " + str(currentpos) + " loop 4.492>mod_assets/sfx/2gl.ogg"
            play music t2gl
            "How is this girl accidentally being so {fast}cute?"
            "She even picked out a book she thinks I'll like, despite me not reading much..."
            $ gtext = glitchtext(80)
            mc "Yuri, {w}{color=#000}[gtext]{/color}"
            $ style.say_dialogue = style.normal
            y 3n "Eh?"
            y 3p "What was that, [player]!?"
            $ style.say_dialogue = style.edited
            $ gtext = glitchtext(80)
            mc "{color=#000}[gtext]{/color}"

            window hide(None)
            $ currentpos = get_pos()
            stop music
            show screen tear(8, offtimeMult=1, ontimeMult=10)
            play music aglitch2
            pause 2.0
            stop music
            hide screen tear
            show yuri 3p at t11 zorder 2
            $ style.say_dialogue = style.normal
            pause 0.01
            window auto
            $ audio.t2g3 = "<from " + str(currentpos) + " loop 4.492>bgm/2g2.ogg"
            play music t2g3
            $ del _history_list[-6:]
            show yuri at thide zorder 1
            hide yuri
            show layer master
            pause 2.0
            "Now that everyone's settled in{nw}"
            $ _history_list.pop()
            $ style.say_dialogue = style.edited
            "{cps=*2}Now that everyone's settled in{fast}nn n nnn nnn nn n n n n nn nn n nn nnnn nn n n n n nnn{/cps}{nw}"
            $ _history_list.pop()
            stop music
            window hide(None)
            play sound sgl
            scene white
            pause 1.5
            scene bg club_day2

            "Wait, what?"
            "What happened?"
            "Did I said something to Yuri?"
            "Confused, still holding a book that Yuri gave me, I glance around."
            play music t2g3
            "Yuri's face is already buried in a book."
            "Meanwhile, Natsuki is rummaging around in the closet."
            "It looks like everything is normal here..."
        else: ### if player skipped the glitch stuff
            $ currentpos = get_pos()
            stop music
            $ config.skipping = False
            $ allow_skipping = False
            $ config.allow_skipping = False
            show yuri at thide zorder 1
            hide yuri
            "Wait, what?"
            "What happened?"
            "Did I said something to Yuri?"
            "I can't see what she said to me. It was {i}too fast{/i}." # 4th wall breaking?
            "..."
            "What am I doing right now?"
            "I glance around."
            $ allow_skipping = True
            $ config.allow_skipping = True
            $ audio.t2g3 = "<from " + str(currentpos) + " loop 4.492>bgm/2g2.ogg"
            play music t2g3
            "Yuri's face is already buried in a book."
            "Meanwhile, Natsuki is rummaging around in the closet."
            "It looks like everything is normal here..."
    else: ### Normal playthrough
        mc "Ah..."
        "Well..."
        if parfait_girls:
            "I guess there's nothing wrong with having two books in my bag."
            "After all, she's trying to help me, right?"
        else:
            "She's trying to help me, right?"
            "After all, I don't have other things to read, so..."
            if not ihorror: ### choose manga over horror from day one
                "{i}Even though I had loads of stacks of books in my room...{/i}"
                "I'm not trying to be an a[aword] here..."
                if persistent.protecc:
                    $ _history_list.pop()
        #"How is this girl accidentally being so cute?"
        #"She even picked out a book she thinks I'll like, despite me not reading much..."
        mc "Yuri, thank you! I'll definitely read this!"
        "I enthusiastically take the book."
        show yuri 2m at t11 zorder 2
        y "Phew..."
        y 2a "Well, you can read it at your own pace."
        mc "Alright."

        show yuri at thide zorder 1
        hide yuri
        show layer master
        $ currentpos = get_pos()
        stop music
        $ audio.t2gl = "<from " + str(currentpos) + " loop 4.492>mod_assets/sfx/2gl.ogg"
        play music t2gl

        #"Now that everyone's settled in, I expected Monika to kick off some scheduled activities for the club."
        "Now that everyone's settled in, it seems that everything is normal around here."
        #"But that doesn't seem to be the case."
        "Yuri's face is already buried in a book."
        "I can't help but notice her intense expression, like she was waiting for this chance."
        "Meanwhile, Natsuki is rummaging around in the closet."

    # Reroute scene to other poet
    default poet_scene = "mp"
    if poetappeal == "abs":
        $ poet_scene = "mp"
    elif poetappeal = "bs":
        $ poet_scene = "cute"
    else:
        $ poet_scene = poetappeal

    # Scene guide:
    # abs/mp = Yuri's scene
    # bs/cute = Natsuki's scene

    # Call exclusive scene based on player's poem.
    # Also, anti-cheat is not yet implemented in the exclusive scene or any further scene, as im too lazy rn...
    # So, I'll probably expect bugs or something bad happening to players who want to cheat the system through
    # saving/loading many times or making different save point.
    # Might be fixed in the next v0.3
    $ mod_ex_scene = "mod_exclusive_" + poet_scene + "_" + str(mod_chapter)
    ### temporary "mod_chapter" variable, cg logic doesnt apply yet, maybe in the next v0.3
    call expression mod_ex_scene
    return
