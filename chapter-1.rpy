init python:
    #ya boy cant skip when monika dialogue shows up
    #seems more realistic actually
    #just monika
    def monika_showed_up(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "begin":
           config.keymap['dismiss'] = []
           renpy.display.behavior.clear_keymap_cache()
        elif event == "slow_done":
           config.keymap['dismiss'] = dismiss_keys
           renpy.display.behavior.clear_keymap_cache()

label intro_mod_2:
    $ delete_all_saves()
    $ persistent.deleted_saves = True
    $ gtext = glitchtext(48)
    stop music
    $ config.window_hide_transition = None
    scene black with trueblack
    pause 0.01
    scene bg residential_day
    with dissolve_scene_half
    $ config.window_hide_transition = Dissolve(.2)
    play music t2g
    queue music t2g2

    $ s_name = glitchtext(8)
    $ gtext = glitchtext(80)
    s "[gtext]"
    "I see an annoying girl running toward me from the distance, waving her arms in the air like she's totally oblivious to any attention she might draw to herself."
    "That girl is [s_name], my neighbor and good friend since we were children."
    "You know, the kind of friend you'd never see yourself making today, but it just kind of works out because you've known each other for so long?"
    "We used to walk to school together on days like this, but starting around high school she would oversleep more and more frequently, and I would get tired of waiting up."
    "But if she's going to chase after me like this, I almost feel better off running away."
    "However, I just sigh and idle in front of the crosswalk and let [s_name] catch up to me."

    show sayori glitch at t11 zorder 2
    python:
        currentpos = get_pos()
        startpos = currentpos - 0.3
        if startpos < 0: startpos = 0
        track = "<from " + str(startpos) + " to " + str(currentpos) + ">bgm/2.ogg"
        renpy.music.play(track, loop=True)
    pause 1.0
    $ gtext = glitchtext(48)
    s "{cps=60}[gtext]{/cps}{nw}"
    pause 1.0
    $ gtext = glitchtext(48)
    s "{cps=60}[gtext]{/cps}{nw}"
    show screen tear(8, offtimeMult=1, ontimeMult=10)
    pause 1.5
    hide screen tear
    window hide(None)
    window auto
    scene black with trueblack
    $ delete_all_saves()
    $ persistent.playthrough = 2
    #$ persistent.anticheat = renpy.random.randint(100000, 999999)
    #$ anticheat = persistent.anticheat

    scene bg residential_day
    with dissolve_scene_half
    play music t2
    jump intro_mod_2_2
    
label intro_mod_2_1:
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full
    play music t2
    jump intro_mod_2_2

default persistent.nice_try = 0

label intro_mod_2_2:
    $ delete_all_saves()
    $ persistent.ggwp_monika = 0
    $ monika_seen = False
    $ persistent.parfait_girls = False
    $ persistent.poster_seen = False
    $ persistent.mc_violent = False
    $ persistent.tea_set = False
    $ persistent.demu_demu = False
    $ _history_list = []
    "It's an ordinary school day, like any other."
    "Mornings are usually the worst, being surrounded by couples and friend groups walking to school together."
    "Meanwhile, I've always walked to school alone."

    $ currentpos = get_pos()
    stop music
    "..."
    "Alone...{w} I'm alone, huh?"
    "I feel like I'm not supposed to be alone, right?"
    "I felt, some kind of déjà vu."
    "Well...."
    $ s_name = glitchtext(8)
    menu:
        "What should I to do right now?"
        "Visit [s_name]'s house.":
            pass
        "Just go to school.":
            if not persistent.force_play:
                jump intro_mod_2_3
            else:
                $ renpy.call_screen("dialog", "Ah, c'mon!", ok_action=Return())
                $ renpy.call_screen("dialog", "Really, [player]? Please don't do this again..", ok_action=Return())
    "Maybe I should check out my \"neighbor\" next door, since I'm very curious about it."
    "Wait, is it \"neighbor\" or \"neighbour\"?"
    "Whatever..."
    "Hope that I'll find something interesting."
    "Oh, I might want to save my game before I continue."
    "If there's something wrong, I can load the game again, trying to play safe."
    if persistent.ggwp_monika == 1:
        jump load_g
    else:
        jump its_time_boys
    
label intro_mod_2_3:
    $ audio.t2 = "<from " + str(currentpos) + " loop 4.499>bgm/2.ogg"
    play music t2
    "Well, going to school isn't really bad at all."
    "I always tell myself it's about time I meet some girls or something like that..."
    "But I have no motivation to join any clubs."
    "After all, I'm perfectly content just getting by on the average while spending my free time on games and anime."
    $ monika_seen = False
    jump chapter_mod_1
    
label its_time_boys:
    scene bg house
    with wipeleft_scene
    "This house..."
    if persistent.ggwp_monika == 1:
        jump load_g
    "...looks familiar to me..."
    "I wonder why, though..."
    "My memory's been a little bit hazy lately."
    if persistent.ggwp_monika == 1:
        jump load_g
    "I proceed myself to knock the door."
    if persistent.ggwp_monika == 1:
        jump load_g
    mc "Hello? Is anyone there?"
    "The house looks empty to me, {w}the door is strangely unlocked... {w}Weird..."
    mc "I'm coming over..."
    if persistent.ggwp_monika == 1:
        jump load_g
    "I open the front door...{nw}"
    
    scene black
    with dissolve_scene_half
    play music ghostmenu
    $ m.display_args["callback"] = monika_showed_up
    m "{cps=*0.5}Hey, [player]!{/cps}{nw}"
    $ persistent.ggwp_monika = 1
    show screen tear(20, 0.1, 0.1, 0, 40)
    window hide(None)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    stop sound
    hide screen tear
    window show(None)
    show bg glitch:
        yoffset 480 ytile 2
        linear 0.25 yoffset 0
        repeat
    show monika 2h at t11 zorder 2
    m "{cps=*0.5}What are you doing here?{/cps}"
    m 4i "{cps=*0.5}You shouldn't be here.{/cps}"
    m 1r "{cps=*0.5}Are you trying to cheat?{/cps}"
    m 5b "{cps=*0.5}Shame on you.{/cps}"
    m 5a "{cps=*0.5}You better not do that again, ok sweetheart?{/cps}"
    if persistent.nice_try == 0:
        $ renpy.call_screen("dialog", "Don't play with my heart~", ok_action=Return())
    $ persistent.nice_try = 1
    play music g2
    show sayori glitch at t11 zorder 2
    pause 0.5
    show screen tear(8, offtimeMult=1, ontimeMult=10)
    pause 1.5
    $ renpy.utter_restart()

label load_g:
    "Ah, what happened....?"
    "Just now..."
    "I saw..."
    "I saw her true form."
    "She was there all along."
    "She set up some kind of trap just to trick me?!"
    "I just couldn't stand this."
    "If thats what she wants from me..."
    "Then should I get along? {w}Act normally like the game would be?"
    "I guess I have no choice but to move on..."
    "But she will pay for it!"
    "Just you wait, Moni-{nw}"
    $ monika_seen = True
    $ _history_list = []
    stop music
    scene black with trueblack
    pause 1.0
    $ audio.t2 = "<from " + str(currentpos) + " loop 4.499>bgm/2.ogg"
    play music t2
    jump chapter_mod_1


#### Main chapter flag ####
label chapter_mod_1:
    #haha you cant save this game forever ~Monika
    $ delete_all_saves()
    scene bg class_day
    with wipeleft_scene
    "The school day is as ordinary as ever, and it's over before I know it."
    if monika_seen:
        "I stare blankly at the wall, looking for an ounce of motivation."
    else:
        "After I pack up my things, I stare blankly at the wall, looking for an ounce of motivation."
    mc "Clubs..."
    "There really aren't any that interest me."
    "Besides, most of them would probably be way too demanding for me to want to deal with."
    if monika_seen:
        "Except for one club that I recognise from before..."
        $ currentpos = get_pos()
        stop music
        mc "What the hell is that?!{w=1.0}{nw}"
        "{cps=*1.5}The \"thing\" started to approach me.{/cps}{w=1.0}{nw}"
        "{cps=*1.5}I didn't recognise that distorted mess of an entity.{/cps}{w=1.0}{nw}"
        "{cps=*1.5}It's getting closer and closer now...{/cps}{w=1.0}{nw}"
        "{cps=*1.5}Ah, what is happening to this world?!!?!{/cps}{w=0.5}{nw}"
        mc "{cps=*1.5}WHAT THE F{/cps}{nw}"
        show monika g2 at t11 zorder 2
        $ style.say_dialogue = style.edited
        $ gtext = glitchtext(80)
        mc "{cps=*1.5}WHAT THE F{fast}[gtext]{/cps}{nw}"
        window hide(None)
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.25
        stop sound
        hide screen tear
        hide monika
        window show(None)
        $ style.say_dialogue = style.normal
        $ del _history_list [-8:]
        $ m.display_args["callback"] = None
        $ audio.t2 = "<from " + str(currentpos) + " loop 4.499>bgm/2.ogg"
        play music t2
        $ m_name = "???"
        show monika 1a at t11 zorder 2
        m "...[player]?"
    else:
        "I guess I have no choice but to start with the anime club..."
        $ m_name = "???"
        m "...[player]?"
        window hide(None)
        show monika g2 at t11 zorder 2
        pause 0.75
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.25
        stop sound
        hide screen tear
        window show(None)
        show monika 1 at t11 zorder 2
    mc "...Monika?"
    $ m_name = "Monika"
    m 1b "Oh my goodness, I totally didn't expect to see you here!"
    m 5 "It's been a while, right?"
    mc "Ah..."
    mc "Yeah, it has."
    if monika_seen:
        "Oh, yeah? After what I saw {i}just now???{/i}"
        "I literally want to die just by looking at her."
        "Having her smile at me so genuinely feels a little... {w}suspicious..."
    else:
        "Monika smiles sweetly."
        "We do know each other - well, we rarely talked, but we were in the same class last year."
        "Monika was probably the most popular girl in class - smart, beautiful, athletic."
        "Basically, completely out of my league."
        "So, having her smile at me so genuinely feels a little..."
    mc "What did you come in here for, anyway?"
    m 1a "Oh, I've just been looking for some supplies to use for my club."
    m 1d "Do you know if there's any construction paper in here?"
    m "Or markers?"
    if monika_seen:
        "I bet she didn't come to look for them in the first place."
    mc "I guess you could check the closet."
    mc "...You're in the debate club, right?"
    m 5 "Ahaha, about that..."
    m "I actually quit the debate club."
    mc "Really? You quit?"
    m "Yeah..."
    m 2e "To be honest, I can't stand all of the politics around the major clubs."
    m "It feels like nothing but arguing about the budget and publicity and how to prepare for events..."
    m "I'd much rather take something I personally enjoy and make something special out of it."
    mc "In that case, what club did you decide to join?"
    m 1b "Actually, I'm starting a new one!"
    m "A literature club!{nw}"
    $ _history_list.pop()
    show screen tear(20, 0.1, 0.1, 0, 40)
    window hide(None)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    stop sound
    hide screen tear
    window show(None)
    m "A literature club!{fast}"
    window auto
    if monika_seen:
        "That scared the shit out of me."
        $ _history_list.pop()
    mc "Literature...?"
    if not monika_seen:
        "That sounds kind of...dull?"
    mc "How many members do you have so far?"
    m 5 "Um..."
    m "Ahaha..."
    m "It's kind of embarrassing, but there are only three of us so far."
    m "It's really hard to find new members for something that sounds so boring..."
    mc "Well, I can see that..."
    if monika_seen:
        "...that fact that you had another member as well..."
    m 3d "But it's really not boring at all, you know!"
    m "Literature can be anything. Reading, writing, poetry..."
    m 3e "I mean, one of my members even keeps her manga collection in the clubroom..."
    "Have I heard this before?"
    mc "Wait...really?"
    m 2k "Yeah, it's funny, right?"
    m 2e "She always insists that manga is literature, too."
    m "I mean, she's not wrong, I guess..."
    m "And besides, a member's a member, right?"
    if not monika_seen:
        "...Did Monika say \"she\"?"
        "Hmm..."
    else:
        pause 1.0
    m 1a "Hey, [player]..."
    m "By any chance...are you still looking for a club to join?"
    mc "Ah--"
    mc "I mean, I guess so, but..."
    m "In that case..."
    m 5 "Is there any chance you could do me a big favor?"
    m "I won't ask you to join, but..."
    m "If you could at the very least visit my club, it would make me really happy."
    m "Please?"
    mc "Um..."
    if monika_seen:
        "Well, I guess I have no reason to refu-{nw}"
        $ _history_list.pop()
        "Wait, why did I say that?!"
        "I cant' just go head over heels for her just yet."
        "I need a plan to take out on her."
        "I need to do something rather than playing along."
        "This game... there must be some kind of a weak spot, or a plot hole."
        "Ah, you might want to save the game later..."
        "You know that something might happened in the future..."
        "If I could--{nw}"
        $ _history_list.pop()
        m 1g "[player]?"
        mc "Oh! Uh..."
    else:
        "Well, I guess I have no reason to refuse..."
        "Besides, how could I ever refuse someone like Monika?"
    mc "Sure, I guess I could check it out."
    m 1k "Aah, awesome!"
    m 1b "You're really sweet, [player], you know that?"
    mc "I-It's nothing, really..."
    if monika_seen:
        "I let my guard down."
        "God damn it!"
    m 1a "Shall we go, then?"
    m "I'll look for the materials another time - you're more important."

    if monika_seen:
        jump chapter_mod_1a
    else:
        show monika at thide zorder 1
        hide monika
    jump chapter_mod_2

label end_ch_mod:
    "Wait, didn't I hear about this conversation before?"
    "What I did just now..."
    "You... {w}You {i}saved{/i} me!"
    "Well, this will make it easier for me to know what's going on with Monika."
    "I think I can pull this thing one by one."
    "[player], you are a fucking genius!"
    m "[player], huurry up!"
    "Ah, I found her weak spot."
    "She doesn't remember anything!"
    "This might be my chance to beat her!"
    mc "Yes! I'm coming...!"
    jump chapter_mod_2

#choice flag
label chapter_mod_1a:
    "I knew it..."
    mc "Ah, before that..."
    mc "I need to pack my things up."
    mc "Also, I'm on duty today to clean my classroom."
    "I am actually supposed to be on duty today by the way."
    mc "Can you wait outside a little bit?"
    m 1c "Hm???"
    "Monika looks at me."
    "I swallow, trying not to spill the beans."
    m 5a "Okay, [player]. Just hurry up okay~?"
    mc "A-Ah, I sure will."
    show monika at thide zorder 1
    hide monika

    "Okay, [player]... What should I do?"
    jump i_do_1
    
label i_do_1:
    menu:
        "I guess I should..."
        "Do something violent" if persistent.ggwp_monika != 2:
            jump throw_chair
        "Check the closet" if persistent.ggwp_monika != 2:
            $ _history_list.pop()
            "I guess I should... {fast}check the classroom closet."
            jump check_closet
        "Check the poster" if (not poster_checked) and (persistent.ggwp_monika == 1):
            $ _history_list.pop()
            "I guess I should... {fast}check the poster on the wall, at the back of the classroom."
            jump check_poster
        "What did I just..." if persistent.ggwp_monika == 2:
            jump end_ch_mod
        "Nevermind..." if persistent.ggwp_monika != 2:
            "Ah, never mind..."
            "There's no point for me to do anything here."
            "After all, she is waiting for me."
            "I guess getting along is fine, for now."
            "I can do something about this later on."
            jump chapter_mod_2

label throw_chair:
    "Hmm..."
    "I think of doing something crazy..."
    "Well, here goes nothing..."
    mc "May God save me.{nw}"
    $ _history_list.pop()
    $ style.say_dialogue = style.edited
    "{cps=*2}LOAD ME{/cps}{nw}"
    $ _history_list.pop()
    $ style.say_dialogue = style.normal
    mc "May God save me.{fast}"
    "I grab a chair."
    "Then... I throw the chair with my full power{nw}"
    play sound throw
    "Then... I throw the chair with my full power{fast} at one of the classroom window{nw}"
    play sound gb_mod
    $ persistent.mc_violent = True
    $ quick_menu = False
    stop music
    scene black
    window hide(None)
    window auto
    pause 1.0
    $ persistent.ggwp_monika = 2
    play music ghostmenu
    show end
    with dissolve_scene_full
    pause 1.0
    "What?"
    "What am I seeing right now?"
    "Did I break the game?"
    "What?!"
    pause 2.0
    "Huh..."
    pause 2.0
    "Well..."
    pause 2.0
    "What do I do right now..."
    "I can't even go to main menu."
    "There must be another way!"
    pause 10.0
    "What happens if I quit the game?"
    "Will my memories stay intact after this?"
    "I'll guess we're about to find out."
    pause 30.0
    "I found something strange..."
    "What is this?"
    "Is that a switch?"
    "What if I try to pull it?"
    $ consolehistory = []
    call updateconsole("renpy.utter_restart()", "Restarting...") from _call_updateconsole
    pause 1.0
    "Oh."
    "Well, I guess that wor{nw}"
    stop music
    window hide(None)
    show screen tear(8, offtimeMult=1, ontimeMult=10)
    pause 1.5
    $ renpy.utter_restart()

label check_closet:
    "Just curious to see what's inside that closet."
    "I expect the contents of that closet to be classroom stuffs like books, files or markers."
    "But you'll never know what is actually inside it."
    scene bg closet
    with wipeleft_scene
    "Well, here goes nothing."
    "I open the closet."
    play sound closet_open
    mc "..."
    mc "I found markers."
    "Construction papers too.."
    "Wasn't Monika trying to find these stuff before?"
    #half chance isnt really half of a chance ~Monika
    menu:
        "Look at the side of the shelf":
            $ chance_sel = 0
        "Look at the center of the shelf":
            $ chance_sel = 1
        "Grab construction paper and markers":
            $ chance_sel = 2
    if chance_sel == 0:# or config.developer:
        mc "What's this?"
        "There's a lone volume of manga amidst a stack of various books on the side of one of the shelves."
        "Curious, I pull the book out."
        mc "Parfait Girls...? {w}Part one?"
        "Have I heard of this manga before?"
        "My memory is a little bit hazy, so I don't know if I read it before."
        "I wonder why it was there in my classroom."
        "Was it there for the entire time?"
        mc "I guess I could keep it though..."
        "I put it inside my bag, just incase."
        "I kind of want to read it though, in my spare time."
        "Well, about the markers and construction paper..."
        "I guess I could give them to Monika after all."
        $ persistent.parfait_girls = True
    elif chance_sel == 1:
        "Huh? There is a tea set as well."
        "Who put in this closet anyway?"
        "Maybe one of my teachers needs it?"
        "Well, whatever."
        "I just grab the markers and construction papers instead."
        $ persistent.tea_set = True
        $ persistent.parfait_girls = True
        # Oops, you just slipped that book.
        "Well, I guess I could give them to Monika after all."
    play sound closet_close
    "I proceed to close the closet."
    m "[player], are you done already?"
    "I saw Monika, eagerly waiting for me outside."
    "I guess I have no choice."
    mc "Alright, I'm coming..."
    $ closet_checked = True
    jump chapter_mod_2

label check_poster:
    "..."
    #half chance isnt really half of a chance ~Monika
    $ half_chance = renpy.random.randint(0, 2)
    if half_chance == 0:# or config.developer:
        "I see..."
        "A girl..."
        "In the poster."
        mc "Uh..."
        mc "What is this picture?"
        $ currentpos = get_pos()
        stop music
        scene black
        pause 1.0
        scene bg s_hang
        pause 0.1
        show screen tear(20, 0.1, 0.1, 0, 40)
        window hide(None)
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.25
        stop sound
        hide screen tear
        window show(None)
        $ audio.t2 = "<from " + str(currentpos) + " loop 4.499>bgm/2.ogg"
        play music t2
        scene bg class_day
        mc "What is this picture?{fast}"
        $ _history_list.pop()
        "My head started to feel dizzy again."
        "I wish I didn't see that."
        stop music
        "I think... {w}I just want to go outside."
        "I need some air."
        scene bg corridor
        with wipeleft_scene
        show monika 1d at t11 zorder 2
        m "[player], what happened?"
        mc "Ugh.."
        mc "Uh..."
        mc "I..." 
        show monika at thide
        hide monika
        "I feel like I couldn't speak anymore."
        "I sit down at the corridor, against the wall."
        m "[player]..."
        show monika 1d at t11 zorder 2
        m "What just happened..."
        mc "I..."
        "I can't explain it to her, or else she might know about my self-awareness."
        m 1h "[player]... {w}You've seen it have you not?"
        m 1k "Ahaha~ Sorry you had to witness that \"thing\"."
        "What?"
        "I'm screwed..."
        m 5a "Don't do it ever again, ok sweetheart?~"
        "What did she just sa{nw}"
        $ persistent.ggwp_monika = 2
        $ persistent.poster_seen = True
        show screen tear(8, offtimeMult=1, ontimeMult=10)
        pause 1.5
        $ persistent.new_game = True
        $ renpy.utter_restart()
    else:
        $ persistent.poster_seen = False
        "Just a calendar."
        "Nothing interesting around here."
        "Maybe I should do something else?"
        "Well..."
        $ poster_checked = True
        jump i_do_1
