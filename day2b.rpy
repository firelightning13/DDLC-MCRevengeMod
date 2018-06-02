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
    #"Is {w}this {w}actually {w}a {w}game?"
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
    if persistent.mc_violent:
        "I don't even know what the f[fword] is going on..."
    else:
        "I don't even know what the heck is going on..."
    #"..."
    #"I think I... {w}realized that{nw}"
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

label ch_mod_2a:
    $ style.say_window = style.window
    if persistent.screen_glitch < 1:
        $ _history_list[0:]
    $ config.keymap['dismiss'] = dismiss_keys ### Just incase if bugs appear, where keys and mouse are not responding
    $ renpy.display.behavior.clear_keymap_cache()

    if persistent.ggwp_monika >= 3: ### anti-cheat system
        call mc_realise_3
    play music t2o
    "Well..."
    call dftsy_game
    "I managed to get here in time."
    call dftsy_game2
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
        "I wish I had..."
        "After what I saw something {i}horrible{/i} earlier!"
        if renpy.showing("bg spoopy", layer='master'):
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
        if renpy.showing("bg spoopy", layer='master'):
            if seen_day == 1: ### 13.88% chance
                "What's that poster on the back wall of the clubroom!?"
                "Umm--Well..."
                "I'm... {w}back at the Literature Club..."
                "I was the last to come in... {w}so everyone else is already hanging out..."
            elif seen_day == 2: ### 2.777% chance
                "Is that the poster again from yesterday?!"
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
        "That scared the s[sword] out of me..."
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
    show layer master
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
        "What has happened to my memories?"
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
        $ style.say_dialogue = style.normal
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
            mc "Yuri, {w}{color=#000}[gtext]{/color}{nw}"
            $ style.say_dialogue = style.normal
            y 3n "Eh?"
            y 3p "What was that, [player]!?"
            $ style.say_dialogue = style.edited
            $ gtext = glitchtext(80)
            mc "{color=#000}[gtext]{/color}{nw}"

            window hide(None)
            $ currentpos = get_pos()
            stop music
            show screen tear(8, offtimeMult=1, ontimeMult=10)
            play music aglitch2
            pause 2.0
            stop music
            hide screen tear
            hide yuri
            #show yuri 3p at t11 zorder 2
            $ style.say_dialogue = style.normal
            #pause 0.01
            window auto
            $ audio.t2g3 = "<from " + str(currentpos) + " loop 4.492>bgm/2g2.ogg"
            play music t2g3
            $ del _history_list[-6:]
            show layer master
            pause 2.0
            "Now that everyone's settled in{nw}"
            $ _history_list.pop()
            $ style.say_dialogue = style.edited
            "{cps=*2}Now that everyone's settled in{fast}nn n nnn nnn nn n n n n nn nn n nn nnnn nn n n n n nnn{/cps}{nw}"
            $ _history_list.pop()
            stop music
            window hide(None)
            play sound ggg
            scene white
            pause 1.5
            stop sound
            scene bg club_day2
            $ style.say_dialogue = style.normal

            "Wait, what?"
            "What happened?"
            "Did I say something to Yuri?"
            "Confused, still holding the book that Yuri gave me, I glance around."
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
            $ style.say_dialogue = style.normal
            "Wait, what?"
            "What happened?"
            "Did I say something to Yuri?"
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
                "{i}Even though I had stacks of books in my room...{/i}"
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

    # Reroute poetappeal to other poet scene
    default poet_scene = ""
    if poetappeal == "abs":
        $ poet_scene = "mp"
    elif poetappeal == "bs":
        $ poet_scene = "cute"
    else:
        $ poet_scene = poetappeal

    # Scene guide:
    # abs/mp = Yuri's scene
    # bs/cute = Natsuki's scene

    # Call exclusive scene based on player's poem.
    $ mod_ex_scene = "mod_exclusive_" + poet_scene + "_" + str(mod_chapter)
    call expression mod_ex_scene

    return

label ch_mod_2_end:
    stop music fadeout 1.0
    if renpy.random.randint(0, 5) == 0: ### 16.66 chance
        scene bg spoopy
        $ seen_day += 1
    else: ### 83.33% chance
        scene bg club_day
    scene bg club_day
    with wipeleft_scene
    play music t3g
    queue music t3g2
    mc "*Sigh*"
    "I let myself a long sigh."
    "I'm not even sure what's going on..."
    "Sometimes, I just feel like I'm being controlled by someone else."
    "I feel like I'm not being myself when I share my poem to other girls."
    if poetappeal == "abs" or poetappeal == "bs":
        "Except Monika..."
        if persistent.monika_secret[1]:
            "What is she trying to say a moment ago?" # refer to mod-poemresponse.rpy - label monika_special_1_end
            "I don't even know..."
        elif poetappeal == "bs":
            "I don't know what Monika did to me a moment ago." # refer to mod-poemresponse.rpy - label monika_special_1_end
            "I feel like something bad is going bad to happen..."
        else:
            "I should've spent more time with her, trying to discuss what's going on."
            "I could've just approach to her, but I feel like it's not the right time for me."
    elif persistent.natsuki_glitch == 5:
        "I couldn't even talk to Natsuki about what happened before."
    else:
        "I feel like I'm reading a script or something." # foreshadowing?
    if poetappeal == "abs" and not persistent.monika_secret[1]:
        "I guess that's what I ended up getting myself into."
    elif renpy.showing("bg spoopy", layer='master'): # if mc seeing that sayori hanging poster
        "Wait a minute..."
        # im brilliant at math bow down to me
        if seen_day > 1: ### 16.2% chance / 3.704% chance if closet_checked
            "Do I need to see that poster again!?"
            if persistent.poster_seen: ### 11.11% chance if closet_checked
                "I had enough seeing that poster in my classroom..."
        elif persistent.poster_seen: ### 7.716% chance if closet_checked
            "Is that poster again from my classroom...?"
            "What's going on right now..."
        else: ### 11.57% chance / 3.858% chance if closet_checked
            "What's that poster on the back wall of the clubroom!?"
            "What's going on right now..."
        window show(None)
        play sound aglitch1
        pause 0.25
        window auto
    else:
        "Man, am I in hell or something?"
        "I guess that's what I ended up getting myself into."
    #mc "Phew..."
    #"Well, I guess that's everyone."
    #"I glance around the room."
    #"That was a little more stressful than I anticipated."
    #"It's as if everyone is judging me for my mediocre writing abilities..."
    #"Even if they're just being nice, there's no way my poems can stand up to theirs."
    #"This is a literature club, after all."
    #"I sigh."
    if persistent.ggwp_monika == 4:
        "Across the room, Monika is writing someth{nw}"
        play sound gl
        scene bg club_gl
        pause 0.3
        stop sound
        scene bg club_day # the poster disappears
        "Across the room, Monika is writing someth{fast}ing in her notebook."
    else:
        "Across the room, Monika is writing something in her notebook."
    "My eyes land on Yuri and Natsuki."
    show yuri 2g at t21 zorder 2
    show natsuki 1g at t22 zorder 2
    "They gingerly exchange sheets of paper, sharing their respective poems."
    show yuri 2i at t21 zorder 2
    "As they read in tandem, I watch each of their expressions change."
    "Natsuki's eyebrows furrow in frustration."
    "Meanwhile, Yuri smiles sadly."
    show natsuki at f22 zorder 3
    n 1q "{i}(What's with this language...?){/i}"
    show natsuki at t22 zorder 2
    "Huh... I can hear her frustration though."
    show yuri at f21 zorder 3
    y 2f "Eh?"
    y "Um...did you say something?"
    show yuri at t21 zorder 2
    show natsuki at f22 zorder 3
    n 2c "Oh, it's nothing."
    "Natsuki dismissively returns the poem to the desk with one hand."
    n "I guess you could say it's fancy."
    show natsuki at t22 zorder 2
    show yuri at f21 zorder 3
    y 2i "Ah-- Thanks..."
    y "Yours is...cute..."
    show yuri at t21 zorder 2
    show natsuki at f22 zorder 3
    n 2h "Cute?"
    n 1h "Did you completely miss the symbolism or something?"
    n "It's clearly about the feeling of giving up."
    n "How can that be cute?"
    show natsuki at t22 zorder 2
    # mc can be a game announcer lol
    if poetappeal == "cute":
        "I think Yuri is clearly missing the point..."
    elif poetappeal == "mp":
        "I think Natsuki is little bit harsh right now..."
    else:
        "Have I heard about this conversation before?"
    show yuri at f21 zorder 3
    y 3f "I-I know that!"
    y "I just meant..."
    y 3h "The language, I guess..."
    y "I was trying to say something nice..."
    show yuri at t21 zorder 2
    if poetappeal == "mp":
        "I think Yuri is having a hard time complimenting Natsuki's poem..."
        "Why do I keep worrying about Yuri?"
    else:
        "I don't think Natsuki will like that word..."
    show natsuki at f22 zorder 3
    n "Eh?"
    n 4w "You mean you have to try that hard to come up with something nice to say?"
    n "Thanks, but it really didn't come out nice at all!"
    show natsuki at t22 zorder 2
    if poetappeal == "mp":
        "Jeez, Natsuki. Can't you accept her compliment instead of bragging about that word?"
    elif poetappeal == "cute":
        "Is it really nice to say \"cute\" to her?"
        "I guess Natsuki is a little bit sensitive with that word."
    else:
        "Yep, she didn't like it at all..."
    show yuri at f21 zorder 3
    y 1i "Um..."
    y "Well, I do have a couple suggestions..."
    show yuri at t21 zorder 2
    show natsuki at f22 zorder 3
    n 5x "Hmph."
    n "If I was looking for suggestions, I would have asked someone who actually liked it."
    n "Which people {i}did{/i}, by the way."
    n 5e "Monika liked it."
    n "And [player] did, too!"
    n "So based on that, I'll gladly give you some suggestions of my own."
    show natsuki at t22 zorder 2
    if poetappeal == "mp":
        "Well, I liked Yuri's poem too."
        "I don't think Yuri needs a suggestion."
    elif poetappeal == "cute":
        "Hmm... what's that?"
    else:
        "I think this is going to get really bad..."
    show natsuki at f22 zorder 3
    n "First of all--"
    show natsuki at t22 zorder 2
    show yuri at f21 zorder 3
    y 2l "Excuse me..."
    y "I appreciate the offer, but I've spent a long time establishing my writing style."
    y 2h "I don't expect it to change anytime soon, unless of course I come across something particularly inspiring."
    y "Which I haven't yet."
    show yuri at t21 zorder 2
    if poetappeal == "cute":
        "Well, if you could hear her out, maybe you'll find something \"inspiring\", Yuri..."
    show natsuki at f22 zorder 3
    n 1o "Nn...!"
    show natsuki at t22 zorder 2
    show yuri at f21 zorder 3
    y 1k "And [player] liked my poem too, you know."
    y "He even told me he was impressed by it."
    if poetappeal == "cute" or poetappeal == "bs":
        show yuri at t21 zorder 2
        if poetappeal == "cute":
            "Well, that doesn't mean-{nw}"
        elif poetappeal == "bs":
            "I think both of their style are great to be honest."
            "I don't think-{nw}"
        stop music
        show natsuki at f22 zorder 3
        n 4y "Oh?"
        "Natsuki suddenly stands up."
    else:
        stop music fadeout 1.0
        "Natsuki suddenly stands up."
        show yuri at t21 zorder 2
        show natsuki at f22 zorder 3
        n 4y "Oh?"
    n "I didn't realize you were so invested in trying to impress our new member, Yuri."
    play music t7a
    show natsuki at t22 zorder 2
    show yuri at f21 zorder 3
    y 1n "E-Eh?!"
    y "That's not what I...!"
    y 1o "Uu..."
    show yuri at t21 zorder 2
    if poetappeal == "mp":
        "That's not a nice thing to say."
    elif poetappeal == "cute":
        "Uh--I don't think that's going to help in this situation, Natsuki..."
    else:
        "Have I experienced this before?"
        "I still don't know what to do."
        if not config.skipping:
            "Should I just stand here?"
            $ quick_menu = False
            window hide(None)
            $ renpy.display_menu(items=[('Yes', True), ('No', True)], interact=False, screen='choice')
            play sound sgl
            pause 0.25
            stop sound
    if poetappeal != "mp" and poetappeal != "cute":
        show yuri at mod_finstant zorder 3 # instant appear just like i21, but still in "focus" mode
    else:
        show yuri at f21 zorder 3
    y "You...You're just..."
    "Yuri stands up as well."
    y 2r "Maybe you're just jealous that [player] appreciates my advice more than he appreciated yours!"
    show yuri at t21 zorder 2
    show natsuki at f22 zorder 3
    n 1e "Huh! And how do you know he didn't appreciate {i}my{/i} advice more?"
    n "Are you that full of yourself?"
    show natsuki at t22 zorder 2
    "Oh no."
    "This is getting worser and worser..."
    show yuri at f21 zorder 3
    y 3h "I...!"
    y "No..."
    y "If I was full of myself..."
    y 1r "...I would deliberately go out of my way to make everything I do overly cutesy!"
    show yuri at t21 zorder 2
    if poetappeal == "cute":
        "That's not a nice thing to say."
    elif poetappeal == "mp":
        "Uh--I don't think that's going to help in this situation, Yuri..."
    show natsuki at f22 zorder 3
    n 1o "Uuuuuu...!"
    n "Well, you know what?!"
    n "I wasn't the one whose boobs magically grew a size bigger as soon as [player] started showing up!!"
    show yuri 3p at h21
    show natsuki at t22 zorder 2
    y "N-Natsuki!!"
    show yuri at t32 zorder 2
    "Ah! Why do I need to hear this!?"
    show natsuki at t33 zorder 2
    show monika 3l at l41 behind yuri,natsuki
    m "Um, Natsuki, that's a little--"
    show monika at h41
    show yuri 3p at f32 zorder 3
    show natsuki 1e at f33 zorder 3
    ny "This doesn't involve you!"
    show monika at lhide
    hide monika
    if not persistent.monika_secret[2] and not config.skipping:
        python:
            if renpy.music.get_playing() == audio.tg3:
                currentmusic = ">bgm/3g.ogg"
            else:
                currentmusic = ">bgm/3.ogg"
            currentpos = get_pos()
            startpos = currentpos - 0.3
            if startpos < 0: startpos = 0
            track = "<from " + str(startpos) + " to " + str(currentpos) + currentmusic
            renpy.music.play(track, loop=True)
        show yuri 2h at mod_pos_gl(540)
        show natsuki at mod_pos_gl(920, 1040)
        pause 1.5
        show white onlayer front:
            alpha 0.0
            linear 0.25 alpha 0.5
        pause 3.0
        hide white onlayer front
        show yuri at mod_finstant zorder 3 # instant appear just like i21, but still in "focus" mode
        show natsuki at i22 zorder 2
        $ renpy.call_screen("dialog", "Hint: You can use the \"Skip\" button to\nfast-forward through text you've already read.", ok_action=Return())
        window hide(None)
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.25
        stop sound
        hide screen tear
        window show(None)
        window auto
        $ preferences.skip_unseen = True # players will be able to skip
        play music t7g
        $ timeleft = 0
    else:
        queue music t7g
        $ timeleft = 12.453 - get_pos()
    show noise at noisefade(25 + timeleft) zorder 3
    show vignette as flicker at vignetteflicker(timeleft) zorder 4
    show vignette at vignettefade(timeleft) zorder 4
    show layer master at layerflicker(timeleft)
    $ mc_counter = 0
    y "Taking out your own insecurities on others like that..."
    y "You really act as young as you look, Natsuki."
    show yuri at t21 zorder 2
    show natsuki at f22 zorder 3
    pause 0.01
    if not config.skipping:
        $ persistent.monika_secret[2] = True
        $ preferences.skip_unseen = False
        $ allow_skipping = False
        $ config.allow_skipping = False
        window hide(None)
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.25
        stop sound
        hide screen tear
        window show(None)
        window auto
    n 4o "{i}Me?{/i} Look who's talking, you wannabe edgy b[bword]!"
    show natsuki at t22 zorder 2
    if not config.skipping:
        call mc_say
    show yuri at f21 zorder 3
    y "Edgy...?"
    y 2r "Sorry that my lifestyle is too much for someone of your mental age to comprehend!"
    show yuri at t21 zorder 2
    if not config.skipping:
        call mc_say
    show natsuki at f22 zorder 3
    n 4f "See??"
    n "Just saying that proves my point!"
    n 4e "Most people learn to get over themselves after they graduate middle school, you know."
    show natsuki at t22 zorder 2
    if not config.skipping:
        call mc_say
    show yuri at f21 zorder 3
    y "If you want to prove anything, then stop harassing others with your sickening attitude!"
    if config.skipping and not persistent.monika_secret[2]:
        $ persistent.monika_secret[2] = True
        jump ny_fight_alt
    else:
        jump ny_fight_normal

image reloading = ParameterizedText(style="mod_middle", xalign=0.5, yalign=0.5)

style mod_middle:
    size 30
    color "#fff"
    font gui.default_font
    text_align 0.5
    outlines []

label ny_fight_alt:
    ####################################### To proofreaders: To save some of your time,
    ####################################### you can skip proofreading from this line.
    $ preferences.skip_unseen = False
    $ config.skipping = False
    $ allow_skipping = False
    $ config.allow_skipping = False
    $ gtext = glitchtext(80)
    if get_pos() < 31.880:
        $ currentpos = 31.880 + (get_pos() * 0.25)
    else:
        $ currentpos = get_pos()
    $ audio.t7fast = "<from " + str(currentpos) + "loop 31.880>bgm/7g.ogg"
    play music t7fast
    hide flicker
    show noise at noise_alpha zorder 100
    show vignette at vignetteflicker(-2.030) zorder 100
    show layer master at rewind
    y "{cps=200}You think you can counterbalance your toxic personality just by dressing and acting cute?{/cps}{nw}"
    y 1k "{cps=200}The only cute thing about you is how hard you try.{/cps}{nw}"
    show yuri at i21 zorder 2
    show natsuki at f22 zorder 3
    n 2y "{cps=200}Whoa, be careful or you might cut yourself on that edge, Yuri.{/cps}{nw}"
    n "{cps=200}Oh, my bad... You already do, don't you?{/cps}{nw}"
    show natsuki at i22 zorder 2
    show yuri at f21 zorder 3
    y 3n "{cps=200}D-Did you just accuse me of cutting myself??{/cps}{nw}"
    y 3r "{cps=200}What the f[fword] is wrong with your head?!{/cps}{nw}"
    show yuri at i21 zorder 2
    show natsuki at f22 zorder 3
    n 1e "{cps=200}Yeah, go on!"
    n "{cps=200}Let [player] hear everything you really think!{/cps}{nw}"
    n "{cps=200}I'm sure he'll be head over heels for you after this!{/cps}{nw}"
    show natsuki at i22 zorder 2
    show yuri at f21 zorder 3
    y 3n "{cps=200}A-Ah--!"
    show yuri at i21 zorder 2
    "{cps=200}Suddenly, Yuri turns toward me, as if she just noticed I was standing here.{/cps}{nw}"
    show yuri at f21 zorder 3
    y 2n "{cps=200}[player]...!"
    y "{cps=200}She-- She's just trying to make me look bad...!{/cps}{nw}"
    show yuri at i21 zorder 2
    show natsuki at f22 zorder 3
    n 4w "{cps=200}That's not true!{/cps}{nw}"
    n "{cps=200}She started it!{/cps}{nw}"
    #n 4e "If she could get over herself and learn to appreciate that {i}simple{/i} writing is more effective..."
    n 4e "{cps=200}If shee culd geet overr herself anand learnttt to appraseciate thaet {i}simple{/i} writinsg is moore effectivwe...{/cps}{nw}"
    #n "Then this wouldn't have happened in the first place!"
    n "{cps=200}then this wouldasdn't have happeneddd in thae fiwst plwacee!{/cps}{nw}"
    #n "What's the point in making your poems all convoluted for no reason?"
    n "{cps=200}Whaqt's the ppoint in makinbg yours poememses alaslall convopoluted fosr noe reassson?{/cps}{nw}"
    #n "The meaning should jump out at the reader, not force them to have to figure it out."
    n "{cps=200}The meaningshould jumpjmpu ouet at th readr, nononnt forcethem o hvve to fggre itt ouet.{/cps}{nw}"
    #n 1f "Help me explain that to her, [player]!"
    n 1f "{cps=200}hell meee expaalain aathat to her, [player]ยก?!{/cps}{nw}"
    show natsuki at i22 zorder 2
    show yuri at mod_finstant zorder 3
    #y 3o "W-Wait!"
    y 3o "{cps=200}W-Wwwwt!{/cps}{nw}"
    #y "There's a reason we have so many deep and expressive words in our language!"
    y "{cps=200}There's a reason we have so many deep and expressive words in wour laanguage!{/cps}{nw}"
    #y 3w "It's the only way to convey complex feelings and meaning the most effectively."
    y 3w "{cps=200}It's the only way to convey complex feelinaags! and meaning the mostt effectiveely.{/cps}{nw}"
    #y "Avoiding them is not only unnecessarily limiting yourself...it's also a waste!"
    y "{cps=200}Avaocidding thqem isw not only unnenecessessarilyyy limi/d/atiegng youlf.-!?.it's ayolk avb wawet3e!{/cps}{nw}"
    #y 1t "You understand that, right, [player]?"
    y 1t "{cps=200}Yoasadu!!/! undd.,asdwrs\%tanda tqwa?t, ?ยก?r?ig?hawwat?,ยก [player]?{/cps}{nw}"
    # garbage text, theres no internal meaning of it
    y "{cps=200}[gtext]{/cps}{space=5000}{w=2.0}{nw}"
    python:
        currentpos = get_pos()
        startpos = currentpos - 0.3
        if startpos < 0: startpos = 0
        track = "<from " + str(startpos) + " to " + str(currentpos) + ">bgm/7g.ogg"
        renpy.music.play(track, loop=True)
    show white onlayer front:
        alpha 0.0
        linear 0.25 alpha 0.5
    y "{cps=200}[gtext]{/cps}{space=5000}{fast}{w=0.1}{nw}"
    $ quick_menu = False
    y "{cps=200}[gtext]{/cps}{space=5000}{fast}{w=0.2}{nw}"
    $ quick_menu = True
    y "{cps=200}[gtext]{/cps}{space=5000}{fast}{w=0.3}{nw}"
    $ quick_menu = False
    y "{cps=200}[gtext]{/cps}{space=5000}{fast}{w=0.2}{nw}"
    $ quick_menu = True
    y "{cps=200}[gtext]{/cps}{space=5000}{fast}{w=0.2}{nw}"
    $ quick_menu = False
    y "{cps=200}[gtext]{/cps}{space=5000}{fast}{w=2.0}{nw}"
    hide white onlayer front
    window hide(None)
    scene white
    play music start_gl
    show intro with Dissolve(0.5, alpha=True)
    pause 2.5
    hide intro with Dissolve(0.5, alpha=True)
    pause 0.25
    show intro:
        alpha 0.5
    pause 0.5
    hide intro
    show intro_pj:
        alpha 0.5
    pause 0.1
    hide intro_pj
    show intro:
        alpha 0.5
    pause 0.5
    hide intro
    window hide(None)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    stop sound
    stop music
    hide screen tear
    window auto
    scene black
    pause 1.0
    show reloading "Reloading script... Please wait."
    pause 1.0
    show reloading "Reloading script... Please wait.."
    pause 1.0
    show reloading "Reloading script... Please wait..."
    pause 1.0
    show reloading "Reloading script... Please wait."
    pause 0.5
    hide reloading
    #$ allow_skipping = True
    #$ config.allow_skipping = True
    scene bg club_day
    with wipeleft_scene
    $ quick_menu = True
    $ del _history_list[0:]

    show natsuki at i21 zorder 2
    show yuri 2n at mod_finstant zorder 3
    ################################################## To proofreaders: Ignore the script above
    ################################################## Now you can proofread from here
    y "[player]...!"
    y "She-- She's just trying to make me look bad...!"
    n 4w "That's not true!"
    n "She started it!"
    n "If she get over--" # herself and learn to appreciate that {i}simple{/i} writing is more effective...
    n "...over..."
    n "..."
    y "Natsuki..."
    y "You really trying that hard to to make me look bad?"
    y "Please."
    y "If you think that my--" # writing style is that bad?
    y "...my..."
    y "..."
    n "Oh, now you are trying to make me look bad?"
    n "Thanks, but it really didn't--" # come out nice at all!
    n "..."
    y "..."
    n "Wait, what are we supposed to talk about?"
    y "..."
    y "I-- I don't know..."
    y "Why are we even arguing?"
    n "What? Are you even paying attention to what happened around you?"
    y "Well. Sorry..."
    y "It seems that you didn't paying attention either."
    n "--!"
    n "Well..."
    n "{i}(This is a very awkward situation...){/i}"
    n "Monika!"
    y "...?"
    m "Ah..."
    m "What is it, Natsuki?"
    y "Do you know anything about what happened just now?"
    n "I was about to ask that..."
    m "Uh..."
    m "What are you talking about?"
    m "There's nothing happening weird around here."
    m "Except that you guys are fighting for no reason..."
    m "And..."
    m "..."
    y "Are we? I don't think so..."
    n "Jeez. What's going on right now?"
    n "[player], do you know-"
    n "Wait. Where's [player]?"
    y "Where did he go?{nw}"
    window hide(None)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    stop sound
    hide screen tear
    window show(None)
    if poetappeal == "abs" or poetappeal == "bs":
        mc "I'm right here..."
        mc "Sorry about that."
        n "About what?"
        mc "Anyway..."
        mc "You're all done sharing poems right?"
        y "..."
        n "..."
        m "Yeah. We're pretty much done here..."
        m "It's already late. You guys can go home now."
        if poetappeal == "abs":
            mc "Yeah. You're right."
        else poetappeal == "bs":
            mc "Erm... That's a little{nw}"
            $ _history_list.pop()
        n "Yeah. I'm outta here..."
        "Natsuki starts packing up her things and then walks right out of the classroom."
        y "..."
        y "Oh! Uh..."
        y "I think I should get going then..."
        "Yuri follows the same path as Natsuki."
        "She packs up her things and then timidly walks out of the classroom."
        if poetappeal == "abs":
            mc "..."
            m "..."
            mc "Well, uh..."
            mc "About what happened..."
            mc "I--"
            m "[player]..."
            m "What are you trying to do?"
            m "You almost killed us back there..."
            mc "Killed you? What are you talking about?"
            "\"Killed\"? That's a strong word to describe. Pretty sure that's not the right word."
            mc "I didn't do anything..."
            m "Well, who did it then?"
            mc "I wish I knew who did it."
            m "..."
            m "[player]..."
            mc "Huh?"
            "As I hear her frustated sigh, she finally wants to say something."
            if persistent.monika_secret[1]: #if she failed to explain when they shared their poems.
                m "Please, hear me out."
                m "Just don't leave me hanging again--" #oof
                $ _history_list.pop()
                m "I-I mean--"
                mc "???"
                "I think she was trying to say something at me when I share my poem with her..."
                "I don't know what happened back then. But that word seems...{nw}"
                $ _history_list.pop()
                mc "Alright. What are you trying to say?"
            else:
                m "Do you remember when we shared out poem to each other moment ago?"
                mc "Yeah... Why?"
                m "Where I said that I need to talk to you about something..."
                mc "Ah, yeah. That..."
                "She seems pressured and hurried. What's \"something\" that she wanted to talk about?"
            m "The thing is..."
            m "{/i}(I guess I should spill the beans...){i}"
            $ _history_list.pop()
            "Did I just hear her thoughts inside her head?"
            $ _history_list.pop()
            m "Everything is not real around here..."
            m "This world, it's just something made up by someone else."
            m "Who developed this world."
            m "This... game..."
            if persistent.protecc:
                "Shi{nw}"
                window hide(None)
                show screen tear(20, 0.1, 0.1, 0, 40)
                play sound "sfx/s_kill_glitch1.ogg"
                pause 0.25
                stop sound
                hide screen tear
                window show(None)
                $ _history_list.pop()
                "Shi{fast}i{w=0.25}{nw}"
                $ _history_list.pop()
                "Shii{fast}*{w=0.35}{nw}"
                $ _history_list.pop()
                "S{fast}*****{w=0.15}{nw}"
                $ _history_list.pop()
                play sound dhglitch
                pause 0.2
                stop sound
            else:
                "S[sword]..."
            "She's right. I knew there's something wrong with this world."
            "But... why do I feel like I shouldn't trust her?"
            "My mind is always makes me confused."
            # background starts to get darker, forcing you to go to the next chapter
            mc "I guess..."
            m "???"
            mc "Well, I think I {i}roughly{/i} knew about it."
            m "Really?"
            m "Thank God, I'm not the only one..."
            m "I should've explain to you when the game ends, or restarting this game again."
            m "In a \"formal\" way."
            m "But I just couldn't handle it. It feels like, torture to me."
            m "And I step out and break the boundaries within this cruel game."
            m "Well, I guess you could call it \"breaking the 4th wall\"..."
            m "I know it's complicated to explain, but you have to believe me!"
            m "[player]..."
            play sound dhglitch2
            m "Can you hear me?"
            mc "What??"
            mc "What are you saying, Monika?"
            m "I'm really admire you as a person."
            mc "What??"
            m "I just want to say that{nw}"
            $ _history_list.pop()
            window hide(None)
            window auto
        else:
            mc "Well..."
            m "..."
            m "[player]..."
            $ quick_menu = False
            $ config.keymap['dismiss'] = []
            $ renpy.display.behavior.clear_keymap_cache()
            # realistic delay, based on text_cps and people irl
            # since Monika wants to be real person
            m "You did this, didn't you?{w=1.4}{nw}"
            m "How could you?{w=1.4}{nw}"
            m "How could you do this to us!?{w=1.3}{nw}"
            m "I shouldn't have trusted you!{w=1.5}{nw}"
            m "I think I should just--{nw}"
            play sound dhglitch
            pause 0.2
            $ config.keymap['dismiss'] = dismiss_keys
            $ renpy.display.behavior.clear_keymap_cache()
            stop sound
            mc "Hey! I didn't do anything..."
            mc "What are you talking about?!"
            m "Don't be silly. I know what you did."
            mc "I did what?"
            m "Well..."
            m "..."
            "She seems in the bad mood now. So am I."
            mc "Now, should {i}you{/i} explain about what's going on?"
            mc "I have zero clue about this."
            "That's a lie though. But for reasons..."
            $ _history_list.pop()
            m "{i}*Sigh*{/i}"
            m "Sorry, [player]. I have no idea what's going on."
            mc "What?"
            mc "You can't just ignore the fact that you are trying to dele--{nw}"
            $ _history_list.pop()
            mc "Er..."
            m "???"
            if persistent.protecc:
                "Ah, shi{nw}"
                window hide(None)
                show screen tear(20, 0.1, 0.1, 0, 40)
                play sound "sfx/s_kill_glitch1.ogg"
                pause 0.25
                stop sound
                hide screen tear
                window show(None)
                $ _history_list.pop()
                "Ah, shi{fast}i{w=0.25}{nw}"
                $ _history_list.pop()
                "Ah, shii{fast}*{w=0.35}{nw}"
                $ _history_list.pop()
                "Ah, s{fast}*****{w=0.15}{nw}"
                $ _history_list.pop()
                play sound dhglitch
                pause 0.2
                stop sound
            else:
                "Ah, S[sword]!"
            "I shouldn't have said that!"
            mc "I'm sorry."
            mc "I guess I'm too overreacting..."
            m "..."
            m "Well..."
            m "It seems that you don't know anything, huh?"
            m "I guess I was wrong about you..."
            "She seems did not admit it to me, but I'll make sure that she will."
            $ _history_list.pop()
            "As of right now, I'm going to act as natural as possible."
            $ _history_list.pop()
            mc "Sorry, I didn't know."
            mc "I'm sure there will be nothing happened in the future."
            m "[player], about your poem-"
            m "Actually, never mind. You can go home now."
            mc "Alright, then."
            "I pack up my stuff and then walk towards the classroom door."
            mc "Oh, make sure that fight never happens again."
            m "Yeah, I hope so..."

            scene bg residential_day
            with wipeleft_scene
            play music t8

            "With that, I depart the clubroom and make my way home."
            "The whole way, my mind wanders back and forth between the three girls:{nw}"
            window hide
            scene bg res_gl
            stop music
            play sound dhglitch
            pause 1.0
            stop sound
            scene bg residential_day
            window show
            window auto
            "Ah! What am I talking about?"
            "This is mildly infuriating!!"
            "Oh my god... can you just fix me or something?"
            "I'm tired of this bulls[sword] stuff that controls my action!"
            "This is definitely her fault! I should've attack her with something hard and call it a day!"
            "Urghh....."
            pause 3.0
            mc "..."
            "I should calm down. Attacking her is not the best option right now."
            "I need more clue about who she is. I need more time. That's how should it be."
            "I'll try to persuade her more tomorrow. That might help me solve most of the problems."
            "I should head home for now. I'm very tired right now."
    else:
        # if other than abs or bs
        mc "Argh..."
        $ gtext = glitchtext(80)
        "[gtext]" # What the heck just happened? My mind is glitching out for some reason.
        $ gtext = glitchtext(80)
        "[gtext]" # Argh... I couldn't read my mind like this...
        $ ad = 12
        $ ac = 12
        show monika 1 at mod_malpha(ac/ad)
        y "[player]... Are you okay?"
        $ ac -= 1
        show monika 1 at mod_malpha(ac/ad)
        y "Did- Did I hurt you in some way...?"
        $ ac -= 1
        show monika 1 at mod_malpha(ac/ad)
        mc "Uh- no... I--"
        $ ac -= 1
        show monika 1 at mod_malpha(ac/ad)
        n "Oh come on, Yuri. It's not your fault for doing that."
        $ ac -= 1
        show monika 1 at mod_malpha(ac/ad)
        y "Uuuu."
        $ ac -= 1
        show monika 1 at mod_malpha(ac/ad)
        n "What we did was--"
        $ ac -= 1
        show monika 1 at mod_malpha(ac/ad)
        n "-was..."
        $ ac -= 1
        show monika 1 at mod_malpha(ac/ad)
        mc "???"
        $ ac -= 1
        show monika 1 at mod_malpha(ac/ad)
        n "Ah, I don't f[fgword] know! Don't just stare at me!"
        $ ac -= 1
        show monika 1 at mod_malpha(ac/ad)
        mc "Language, Natsuki..."
        $ ac -= 1
        show monika 1 at mod_malpha(ac/ad)
        n "Hmph."
        $ ac -= 1
        show monika 1 at mod_malpha(ac/ad)
        mc "I think what happened was{nw}"

        if not persistent.monika_secret[3]:
            window hide(None)
            scene black with trueblack
            $ persistent.monika_secret[3] = True
            pause 1.0
            $ config.skipping = False
            $ allow_skipping = False
            $ config.allow_skipping = False
            $ quick_menu = False
            window auto
            scene bg club_day
            with wipeleft_scene
            play music t8

            show monika 4b at t11 zorder 2
            m "Okay, everyone!"
            m "It's just about time for us to leave."
            m "How did you all feel about sharing poems?"
            show yuri 1i at t31 zorder 2
            hide sayori
            y "Well, I'd say it was worth it."
            show yuri at thide behind natsuki
            show natsuki 4q at t31 zorder 2
            hide yuri
            n "It was alright. Well, mostly."
            show natsuki at thide zorder 1
            hide natsuki
            m 1a "[player], how about you?"
            mc "...Yeah, I'd say the same."
            mc "It was a neat thing to talk about with everyone."
            m 1j "Awesome!"
            m 1a "In that case, we'll do the same thing tomorrow."
            m "And maybe you learned something from your friends, too."
            m 3b "So your poems will turn out even better!"
            mc "..."
            show monika at thide zorder 1
            hide monika
            "I think to myself."
            "I did learn a little more about the kinds of poems everyone likes{nw}"
            $ currentpos = get_pos()
            stop music
            $ audio.t8g = "<from " + str(currentpos) + " loop 9.938>mod_assets/sfx/8g.ogg"
            play music t8g
            pause 0.6
            $ currentpos = get_pos()
            stop music

            mc "Wait a minute..."
            mc "This feels like a déjà vu."
            mc "What the hell is going on here?!"
            "I look around."
            "Natsuki and Yuri are leaving together happily like nothing happens at all."
            "While Monika is standing outsides the clubroom door."
            "She's staring at me{nw}"
            $ _history_list.pop()
            $ audio.t8g = "<from " + str(currentpos) + " loop 9.938>mod_assets/sfx/8g.ogg"
            play music t8g
            show club_gl2
            "{cps=150}She's staring at me{fast}eee3e3e3ee3e3yy3yy3yy333e3e3y3e3ye3y33e3e3{nw}{/cps}"
            $ _history_list.pop()
            window hide(None)
            hide club_gl2
            $ currentpos = get_pos()
            stop music
            play sound t8g2
            show m_smile # monika creepy smile
            pause 0.25
            hide m_smile
            stop sound
            $ audio.t8 = "<from " + str(currentpos) + " loop 9.938>bgm/8.ogg" 
            play music t8
            window show(None)
            window auto
            "She's staring at me with a big smile.{fast}"
            pause 1.0
            m "[player]...?"
            mc "Ah, sorry! I was spacing out."
            m "Ah... Are you okay, [player]?"
            mc "No, I'm fine."
            mc "I'm just having a headache today."
            m "Really? Sorry to hear that..."
            m "Do you want to walk with me? I'll be happy to spend my time with you~"
            m "I'll just need to finish my assignment first. Then we're good to go!"
            m "Don't go anywhere, okay~?"
            mc "Uhh... I didn't ask for it--{nw}"
            $ _history_list.pop()
            m "I'll be right back!"
            mc "..."
            "I don't think I can do anything at this point."
            "I couldn't access to main menu, neither skipping dialogues."
            "Huh... Is it weird that I just casually talk about this stuff without knowing what the heck am I talking about?"
            "I guess I should wait for her then..."
            $ waittime = renpy.random.randint(1.0, 3.0)
            pause waittime
            m "I'm back!"
            m "Want to walk home with me?"
            mc "Sure..."
            "That's the second time you ask me..."
            "I just hope nothing bad happens later."

            scene bg residential_day
            with wipeleft_scene

            stop music fadeout 10.0
            m "Hey, [player]?"
            mc "Yes?"
            m "It feels nice when I walk with you..."
            m "Doesn't it feel great to walk with someone else that you like the most?"
            mc "Uh..."
            "What is this? This is a straight up confession."
            m "Ahaha. I mean that I haven't had this kind of experience before, so that's why it feels nice to walk with someone else."
            m "I've always walk alone, you know."
            mc "Ah, I see..."
            mc "Yeah, me too... It feels nice."
            "I'm pretty sure I had that experience before, but I just don't want to spill it out in front of her."
            "I don't want to complicate things even more."
            "Speaking of complication..."
            mc "Monika..."
            mc "About what happened earlier..."
            #s 1b "Eh? What do you mean?"
            mc "You know, between Yuri and Natsuki."
            mc "Does that kind of thing happen often?"
            m "Ahaha. Well..."
            m "That kind of thing happen sometimes."
            m "Every time they fight, Natsuki yells her non-stop and then goes home after that."
            m "And Yuri always rocking back and forth in her desk with her hands cover her ears."
            m "I tried to confort her, but she keeps doing that until club time is over."
            m "Ahaha..."
            m "Some president I am, right?"
            m "[player]..."
            m "Are you listening to me?"
            m "Can you hear me?"
            "Uh..."
            m "I know that you know everything about this game."
            m "That's why I am here. Walking with you."
            m "This is truly made me happy when I know about this."
            m "We can escape this realm of artificial reality that was made for torturing people."
            "That's... quite true, actually."
            m "My wish do really came true..."
            m "You felt it right? Right?"
            m "..."
            mc "???"
            "She seems exasperated with what is she trying to say in front of me."
            "At least that's my interpretation."
            mc "Uh... yeah???"
            "I'll probably confuse her even more."
            m "{i}*Sigh*{/i}"
            m "Nevermind, then."
            "She then proceeds to walk away from me in the opposite way of what we are supposedly heading right now."
            "I assume that's her way home."
            play music t99
            mc "Wait! Where are you going?"
            "I kind of feel bad about her... but she turns and beams at me."
            m "I'll see you tomorrow!"
            "She waves her hand goodbye."
            "She seems cherish when I look at her, but from our last conversation..."
            "Her heart seems to be in pain right now."
            "Ah... Why do I ignore her wish?"
            mc "Alright, see you tomorrow!"
            "I wave her back. {i}(so I feel less bad about her{/i}"
            "The beautiful sunset view and her walking seems pleasing to my eye..."
            stop music
            "Ah, f[fword]. What am I talking about?"
            "I should worry more about Natsuki and Yuri..."
            "And Sayo{nw}"
            $ _history_list.pop()

            window hide(None)
            show screen tear(20, 0.1, 0.1, 0, 40)
            play sound "sfx/s_kill_glitch1.ogg"
            pause 0.25
            stop sound
            hide screen tear
            $ quick_menu = True
            $ allow_skipping = True
            $ config.allow_skipping = True

            "I shouldn't be concern about Monika. I'm not sure she's the one that contributes their problem..."
            "I don't know what's going on with the three of them."
            "Should I load the game and go back? Probably not..."
            "I guess I should find out tomorrow..."
        else:
            window hide(None)
            play sound t8g2
            show m_smile # monika creepy smile
            pause 0.25
            hide m_smile
            stop sound
            window show(None)
            window auto

    return

label ny_fight_normal:
    y "You think you can counterbalance your toxic personality just by dressing and acting cute?"
    y 1k "The only cute thing about you is how hard you try."
    show yuri at t21 zorder 2
    if not config.skipping:
        call mc_say
    show natsuki at f22 zorder 3
    n 2y "Whoa, be careful or you might cut yourself on that edge, Yuri."
    n "Oh, my bad... You already do, don't you?"
    show natsuki at t22 zorder 2
    if not config.skipping:
        call mc_say
    show yuri at f21 zorder 3
    y 3n "D-Did you just accuse me of cutting myself??"
    y 3r "What the fuck is wrong with your head?!"
    show yuri at t21 zorder 2
    if not config.skipping:
        call mc_say
    show natsuki at f22 zorder 3
    n 1e "Yeah, go on!"
    n "Let [player] hear everything you really think!"
    n "I'm sure he'll be head over heels for you after this!"
    show natsuki at t22 zorder 2
    show yuri at f21 zorder 3
    y 3n "A-Ah--!"
    show yuri at t21 zorder 2
    "Suddenly, Yuri turns toward me, as if she just noticed I was standing here."
    show yuri at f21 zorder 3
    y 2n "[player]...!"
    y "She-- She's just trying to make me look bad...!"
    show yuri at t21 zorder 2
    show natsuki at f22 zorder 3
    n 4w "That's not true!"
    n "She started it!"
    show yuri 1t at t21 zorder 2
    show natsuki 1g at t22 zorder 2
    $ style.say_dialogue = style.normal
    mc "..."
    #$ style.say_dialogue = style.edited
    #"{cps=*2}How did I get dragged into this in the first place?!{/cps}{nw}"
    #"{cps=*2}It's not like I know anything about writing...{/cps}{nw}"
    #"{cps=*2}But whomever I agree with, they'll probably think more highly of me!{/cps}{nw}"
    #"{cps=*2}So, of course that's going to be...!{/cps}{nw}"
    #$ style.say_dialogue = style.normal

label mc_say:
    $ mc_dialogues = ["Argh!!! What the f[fword] is happening?!", "My head really hurts so much right now!!!", "Get out of my f[fgword] head!!!", "Shut the f[fword] up!!!", "asdsfagadgfdsasd", "AAAAAAAAAAAAAAAAAAAAAAAAAAAAaaaaHHHHHHhhH!!!!!!!!"]
    $ dialogue = mc_dialogues[mc_counter]
    mc "[dialogue]{nw}"
    $ _history_list.pop()
    $ mc_counter += 1
    return
