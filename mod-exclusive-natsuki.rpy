label mod_exclusive_cute_1:
    ### Guide of some sort:
    # persistent.ggwp_monika = 3;post-glitched yuri when choosing "bs" poem in day2b.rpy
    # persistent.ggwp_monika = 2;post-crashed game when seen poster/throws chair in day2a.rpy
    # persistent.ggwp_monika = 4;game crashed when mc breaks the system (in the label special_cute_1)
    # persitent.poster_seen = seen poster in day2a.rpy (66.66% chance)
    # persistent.mc_violent = throws chair incident in day2a.rpy- might changed mc's personality
    # parfait_girls = mc found a volume one of parfait girls series from his classroom from day2a.rpy
    # poetapeal = "cute", if player chooses "something cute"; "bs", if player chooses "something bittersweet"
    # config.skipping = if players use "Skip" button
    ### persistent.natsuki_glitch:
    # 1-4 = generally makes all glitch happen once and never seen again after saving/loading
    # 5 = when players realised that they need to skip in order to get "special route" when going to normal route by saving/loading again
    # 6 = if player skips in the first place and get special route without going to normal one; normal route for special_cute_1 if players load again

    scene bg club_day
    with wipeleft_scene
    if not persistent.ggwp_monika == 3:
        if persistent.poster_seen: # self-explanatory
            "I need to clear my head first."
            "After I saw it in my classroom..."
            "I don't even know that I should use the word \"saw\" in this situation."
            pause 2.0
            $ currentpos = get_pos()
            $ audio.t2g3 = "<from " + str(currentpos) + " loop 4.492>bgm/2g2.ogg"
            play music t2g3
            "Anyways..."
    else: # post-glitched yuri
        if persistent.ggwp_monika == 4:
            $ currentpos = get_pos()
            $ audio.t2g3 = "<from " + str(currentpos) + " loop 4.492>bgm/2g2.ogg"
            play music t2g3
        "I'm not sure what happened just a minute ago, between me and Yuri."
        "Ugh--My head hurts..."
        "Well think I should--"
    n "Ugh...!"
    "I hear Natsuki utter an exasperated sigh from within the closet."
    "She seems to be annoyed by something."
    "I approach her, in case she needs a hand."
    play music t6 fadeout 1
    scene bg closet
    show natsuki 4r at t11 zorder 2
    with wipeleft_scene
    window auto
    #mc "You looking for something in there?"
    mc "Natsuki, are you looking for something in there?"
    $ style.say_dialogue = style.edited
    if persistent.natsuki_glitch < 1 and not config.skipping: # glitch doesn't happen when skipping
        if poetappeal == "cute" and persistent.protecc: # if players chooses "cute" poem and enables profanity filter
            n 4x "f[fgword] monikammmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm{nw}"
            pause 1.0
            n "f[fgword] monikammmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm{nw}"
            pause 1.0
            n "f[fgword] monik{nw}"
            $ del _history_list[-3:]
            window hide(None)
            show screen tear(20, 0.1, 0.1, 0, 40)
            play sound aglitch1
            pause 0.25
            stop sound
            hide screen tear
            window show(None)
            $ style.say_dialogue = style.normal
            $ persistent.natsuki_glitch = 1
            n "Freaking Monika...{fast}"
            "Eh, what just happen?"
        else: # if players chooses "bittersweet" poem (or still "cute" but players didn't enable profanity filter)
            n 4x "f[fgword] monikammmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm"
            $ _history_list[-1].what = "Freaking Monika..."
            $ style.say_dialogue = style.normal
            $ persistent.natsuki_glitch = 1
            if persistent.mc_violent:
                "What the f[fword] was that?"
            else:
                "What the heck was that?"
    else:
        n "Freaking Monika..."
    n "She never puts my stuff back in the right spot!"
    n "What's the point in keeping your collection organized if someone else is just gonna mess it up?" # gonna? wtf natsuki
    "Natsuki slides a bunch of stacked books and boxes across the shelf."
    mc "Manga..."
    if ihorror: # if players chose horror in day one
        "Wait, why did I say that?"
    n 2c "You read manga, right?"
    mc "Ah--"
    #mc "...Sometimes..."
    mc "Well, sometimes I do."
    mc "How did you know, anyway?"
    #"Manga is one of those things where you can't admit you're really into it until you figure out where the other person stands." -meh
    #mc "...How did you know, anyway?"
    n 2k "I heard you bring it up at some point."
    n "Besides, it's kind of written on your face."
    #"What's that supposed to mean...?"
    #mc "I-I see..."
    if not ihorror: # self-explanatory
        mc "Oh-Yeah..."
        mc "I talked about it yesterday when Yuri{nw}"
        $ _history_list.pop()
        mc "I talked about it yesterday{fast}..."
    else:
        mc "Wait, what's that supposed to mean?"
        $ _history_list[-1].who = None
        $ _history_list[-1].what = "What's that supposed to mean?"
        mc "I didn't say \"manga\" befor{nw}"
        $ _history_list[-1].what = "I-I see..."
        window hide(None)
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.25
        stop sound
        hide screen tear
        window show(None)
    mc "Eh? What's this?"
    "There's a lone volume of manga amidst a stack of various books on the side of one of the shelves."
    if parfait_girls: # self-explanatory
        "Wait, isn't that the same book that I found recently?"
    "Curious, I pull it out of the stack."
    n 1b "{i}There{/i} it is!"
    "Natsuki snatches it out of my hand."
    "She then turns to a box of manga and slips the volume right into the middle of the rest."
    n 4d "Aah, much better!"
    n "Seeing a box set with one book missing is probably the most irritating sight in the world."
    if parfait_girls:
        mc "I-I see..."
    else:
        mc "I know that feel..."
    "I get a closer look at the box set she's admiring."
    if parfait_girls:
        "Wait, it is the same book that I had in my classroom!"
        "Is this a coincidence?"
    else:
        mc "Parfait Girls...?"
        #"It's a series I've never heard of in my life."
        "I think I heard about this series before."
        #"That probably means it's either way out of my demographic, or it's simply terrible."
        "Wait, I think I've read it before, or haven't I...?"
    n 5g "If you're gonna judge, you can go do it through the glass on that door."
    "She points to the classroom door."
    if parfait_girls or persistent.ggwp_monika == 2:
        mc "Ah-No!"
        mc "I didn't judge anything!"
        mc "What's wrong with you?"
        n 4e "Yeah... right!"
    else:
        #mc "H-Hey, I wasn't judging anything...!"
        #mc "I didn't even say anything."
        mc "Woah--Hey, I didn't even say anything..."
        n 5c "It was the tone of your voice."
    n "But I'll tell you one thing, [player]."
    if persistent.natsuki_glitch < 2 and not config.skipping:
        n 4l "Consider this a lesson straight from the Literature Club:{nw}"
        $ _history_list.pop()
        #$ _history_list[-1].what = "Consider this a lesson straight from the Literature Club: Don't judge a book by its cover!"
        #n "don't judge a bookkkkkkkkkkkkkkkkk kkkkk kk{space=20}k{space=40}k{space=120}k{space=160}k{space=200}k"
        #$ _history_list.pop()
        $ style.say_dialogue = style.edited
        n "{cps=*1.5}don't judge a bookkkkkkkkkkkkkkkkk kkkkk kk{/cps}{nw}"
        $ _history_list.pop()
        pause 1.0
        n "{cps=*1.5}don't judge a boo{/cps}{nw}"
        $ _history_list.pop()
        window hide(None)
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.25
        stop sound
        hide screen tear
        window show(None)
        $ style.say_dialogue = style.normal
        $ persistent.natsuki_glitch = 2
        n "Consider this a lesson straight from the Literature Club: Don't judge a book by its cover!{fast}"
    else:
        n 4l "Consider this a lesson straight from the Literature Club: Don't judge a book by its cover!"
    n "In fact--"
    "Natsuki pulls out the first volume of Parfait Girls from the box."
    n "I'm gonna show you exactly why!"
    "She shoves the book right into my hands."
    mc "Ah..."
    if not parfait_girls:
        "I stare at the cover."
        "It features four girls in colorful attire striking animated feminine poses."
        "I somehow feel like those girls are kind of reminiscent of this whole club members..."
    else:
        mc "Umm, Natsuki...?"
        mc "What I want to say that I already have th-{nw}"
    n 4b "Don't just stand there!"
    mc "Uwa--"
    show natsuki at thide zorder 1
    hide natsuki
    "Natsuki grabs my arm and pulls me out of the closet."
    "She then takes a seat against the wall, beneath the windowsills."
    "She pats on the ground next to her, signaling me to sit there."
    show bg club_day
    show natsuki 2a at t11 zorder 2
    with wipeleft
    if parfait_girls: # extra thicc for mc
        mc "Umm... Natsuki, I think-{nw}"
        n 1e "Just sit down already!"
        mc "Okay, okay!"
        "I take my seat."
        n 2i "Man, you're denser than a brick!"
        "Huh, I guess that's true..."
        "My whole life is such a mess after I had some kind of epiphany."
        n 5h "I mean, c'mon. You look like you never had a chance when you're reading with someone else for the first time in your life."
        n "Well, I wanted to have that chance when you join--"
        n 5o "...!"
        mc "...this club?"
        n 5u "..."
        mc "Yeah, I you're right, I haven't socialize to anyone in my entire life..."
        "That's not entirely true, I feel like I had a friend before."
        mc "After all--"
        "I quickly retrieve the same book that Natsuki admires in my bag, which I found it from my classroom an hour ago."
        "I grab both of them, which is mine and hers, and show them to Natsuki just so that I can prove to her." # pls fix this im tired of this english bs
        mc "See? I already have it. You don't need to worry about yours getting bent or smudges on the pages."
        mc "I only have volume one, so I thought I'd like to share this with you sometimes."
        mc "But it seems that we already had the same book, and--"
        n "..."
        n 5n "D-Did you already read that whole thing?"
        mc "Ah--No."
        mc "I just--"
        $ _history_list.pop()
        "I don't think I should tell her the truth."
        "I'm already afraid that something terrible is going to happened to her."
        "I don't even know why I'm feeling this way."
        # a fake story by mc, nice one eh
        mc "I just{fast} bought a stack of it a few months ago for my older sister's birthday present."
        mc "But she forgot this one as she left my house because of her college." # again, pls fix this, this is so wrong :(
        mc "I didn't want to read it though since I'm not into it, so I thought I just wanted to share it with you."
        mc "I don't want this book going to be wasted and left alone in my house."
        "Wow, this is one hell of a story."
        n 5q "I-I see..."
        n "Well, I can't argue with that, since you already had one."
        n 5n "I guess I can do is to reread some of it."
        n 5u "I-Is that okay?"
        mc "Alright, you asked for it."
        "I return her book by slipping it back into the box of manga."
        "Then, I open the book and start the prologue."
    else:
        #mc "Wouldn't chairs be more comfortable...?"
        #"I take my seat."
        mc "Why don't we just use chairs instead?"
        "I timidly take my seat."
        n 2k "Chairs wouldn't work."
        n "We can't read at the same time like that."
        #mc "Eh? Why's that?"
        #mc "Ah...I guess it's easier to be close together like this..."
        mc "Eh? Why's that-{nw}"
        mc "Ah, I guess we can read like this way."
        "I think I am too close with her, our shoulder are almost touching..."
        n 2o "--!"
        n 5r "D-Don't just stare at me...!"
        #n 5r "D-Don't just say that!"
        n "You'll make me feel weird about it!"
        "Natsuki crosses her arms and scootches an inch away from me."
        mc "Sorry, I didn't realise..."
        show natsuki 5g
        #"I didn't exactly expect to be sitting this close to her, either..."
        #"Not that I can say it's a particularly bad thing."
        mc "I guess we can get started."
        "I open the book."
        "It's only a few seconds before Natsuki once again inches closer, reclaiming the additional space while she hopes I won't notice."
    "I can feel her peering over my shoulder, much more eager to begin reading than I am."
    n 1k "Wow, how long has it been since I read the beginning...?"
    mc "Huh?"
    mc "You don't go back and flip through the older volumes every now and then?"
    n 2k "Not really."
    n "Maybe sometimes after I've already finished the series."
    if persistent.natsuki_glitch < 3 and not config.skipping:
        mc "Ah... It's just like starting a game all over ag-{nw}"
        if persistent.ggwp_monika == 2:
            "Oh, s[sword]!"
        else:
            "Oh, shoot!"
        "Why the hell did I say that...?"
        "Let me do something real quick..."
        $ del _history_list[-4:]
        $ persistent.natsuki_glitch = 3
    n 2c "Hey, are you paying attention?"
    mc "Uh..."
    mc "I am, but nothing's happened yet, so I can talk-"
    n 2e "Just keep reading it!"
    mc "Alright, alright..."
    #"I am, but nothing's really happened yet, so I can talk at the same time."
    if parfait_girls:
        "I was eager to read it since I found it.."
        "Well..."
    else:
        "I guess I have to read it then..."
    "It looks like it's about a bunch of friends in high school."
    "Typical slice-of-life affair."
    #"I kind of grew out of these, since it's rare for the writing to be entertaining enough to make up for the lack of plot."
    "I kind of relate out of these with my whole life. Well, it's not that I am self-reflecting. It's what I had in my mind the whole time."
    scene n_cg1_bg
    show n_cg1_base
    with dissolve_cg
    if not parfait_girls:
        mc "...Are you sure this isn't boring for you?"
        n "It's not!"
        mc "Even though you're just watching me read?"
    else:
        mc "Is it really okay if we're reading like this?"
        mc "Even if it's not yours?"
        mc "Well, I know you're already finished the first volume."
    n "Well...!"
    n "I'm...fine with that."
    mc "If you say so..."
    mc "...I guess it's fun sharing something you like with someone else."
    mc "I always get excited when I convince any of my friends to pick up a series I enjoy."
    mc "You know what I mean?"
    n "...?"
    mc "Hm?"
    mc "You don't?"
    show n_cg1_exp2 at cgfade
    n "Um..."
    n "That's not..."
    n "Well, I wouldn't really know."
    #mc "...What do you mean?"
    #mc "Don't you share your manga with your friends?"
    mc "Ah, I see..."
    "I'm kind of suprise how Natsuki was alone all the time. Not to mention about Yuri though..."
    hide n_cg1_exp2
    show n_cg1_exp3 at cgfade
    n "Could you not rub it in?"
    n "Jeez..."
    #mc "Ah... Sorry..."
    mc "Sorry, I didn't know about that."
    n "Hmph."
    n "Like I could ever get my friends to read this..."
    n "They just think manga is for kids."
    n "I can't even bring it up without them being all like..."
    n "'Eh? You still haven't grown out of that yet?'"
    n "Makes me want to punch them in the face..."
    mc "Urgh, I know those kinds of people..."
    mc "Honestly, it takes a lot of effort to find friends who don't judge, much less friends who are also into it..."
    mc "I'm already kind of a loser, so I guess I gravitated toward the other losers over time."
    mc "But it's probably harder for someone like you..."
    "I feel like doubting my own advice. I don't know if I can keep being like this the whole time!"
    hide n_cg1_exp3
    n "Hm."
    n "Yeah, that's pretty accurate."
    "{i}...Wait, which part?? {w}All of it??{/i}"
    n "I mean, I feel like I can't even keep it in my own room..."

    $ style.say_dialogue = style.edited
    if not config.skipping and poetappeal == "cute" and persistent.natsuki_glitch < 4: # if players choose "cute" poem, glitch happens (only seen once)
        $ currentpos = get_pos()
        $ audio.t666 = "<from " + str(currentpos) + " loop 10.893>mod_assets/sfx/666.ogg"
        play music t666
        show n_cg1b
        hide n_cg1_base
        n "{color=#000}My dad would beat the s[sword] out of me if he found this.{/color}"
        n "{color=#000}Then, my dad will not give me lunch money because of it...{/color}"
        n "{color=#000}I don't have lunch money.{/color}"
        n "{color=#000}I don't have friends.{/color}"
        n "{color=#000}I don't have free will.{/color}"
        n "{color=#000}I don't have self-confidence.{/color}"
        $ gtext = glitchtext(96)
        n "{cps=*1.5}{color=#000}[gtext]{/color}{/cps}{nw}"
        $ _history_list[-1].what = "{color=#000}Loathing. Judgement. Elytysmmm. Self-doubt.{/color}"
        window hide(None)
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound s_gl
        pause 0.25
        stop sound
        hide screen tear
        window show(None)
        python: ### same text as "CAN YOU HEAR ME?.txt" but different name file
            try: renpy.file(config.basedir + "/Loathing-Judgement-Elitism-Self-doubt.txt")
            except: open(config.basedir + "/Loathing-Judgement-Elitism-Self-doubt.txt", "wb").write(renpy.file("CAN YOU HEAR ME.txt").read())
        $ style.say_dialogue = style.normal
        mc "Nani?" # what?
        $ _history_list[-1].what = "What?"
        mc "Nani ga okotte iru?" # what is going on?
        $ _history_list[-1].what = "What's going on?"
        mc "Natsuki, daijōbudesuka?" # natsuki, are you okay?
        $ currentpos = get_pos()
        stop music
        window hide(None)
        show screen tear(8, offtimeMult=1, ontimeMult=10)
        play sound ggg
        pause 2.0
        stop sound
        hide screen tear
        window show(None)
        show n_cg1_base
        hide n_cg1b
        $ del _history_list[-3:]
        $ persistent.natsuki_glitch = 4
        $ audio.t6 = "<from " + str(currentpos) + " loop 10.893>bgm/6.ogg"
        play music t6
    elif persistent.natsuki_glitch >= 4 or config.skipping: # post-glitch natsuki after load previous save/start a new game/skipping dialogues
        n "I don't even know what my dad would do if he found this."
    else: # if players choose "bs" poem, minor glitch happens (only seen once)
        n "My dad would beat the s[sword] out of me if he found this."
        $ style.say_dialogue = style.normal
        $ _history_list[-1].what = "I don't even know what my dad would do if he found this."
        $ persistent.natsuki_glitch = 4
        if persistent.mc_violent:
            "What the f[fword] was that?"
        else:
            "What the heck was that?"
    $ preferences.skip_unseen = True # a hint
    n "At least it's safe here in the clubroom."
    show n_cg1_exp3 at cgfade
    n "'Cept Monika's kind of a jerk about it..."
    n "Ugh! I just can't win, can I?"
    if not config.skipping:
        $ preferences.skip_unseen = False
    "Wait, what did Monika do?"
    mc "Well, it paid off in the end, didn't it?"
    mc "Maybe..."
    if persistent.parfait_girls:
        mc "Even if it's mine though..."
    mc "But at least you're enjoying yourself, right?"
    hide n_cg1_exp3
    show n_cg1_exp2 at cgfade
    n "--"
    if persistent.parfait_girls:
        n "U-Urm..."
        n "Y-Yeah... so?"
    else:
        n "..."
        n "...So?"
    mc "Ahaha."
    hide n_cg1_exp2
    show n_cg1_exp3 at cgfade
    n "Jeez, that's enough!"
    n "Are you gonna keep reading, or what?"
    mc "Yeah, yeah..."
    "I flip the page."
    if config.skipping and persistent.natsuki_glitch < 6 and persistent.ggwp_monika != 4:
        call special_cute_1 # secrets scene
    elif persistent.natsuki_glitch == 6:
        call special_cute_1 # secrets scene converts to normal route when saving/loading again in their first playthrough (no glitch)
    else:
        call normal_cute_1 # glitch happens when not skipping
    window auto
    return

label special_cute_1:
    "Suddenly, Natsuki starts laughing."
    if persistent.natsuki_glitch < 6:
        $ preferences.skip_unseen = False
        $ config.skipping = False
        $ config.allow_skipping = False
        $ allow_skipping = False
        window hide(None)
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.25
        stop sound
        hide screen tear
        window show(None)
        "Argh. What the-{nw}"
        $ _history_list.pop()
    hide n_cg1_exp3
    show n_cg1_exp1 at cgfade
    n "Ahahaha!"
    n "I totally forgot that happens!"
    "Natsuki puts her finger on one of the panels."
    n "Minori is my favorite character."
    n "You always feel a little bad for her, since she's so unlucky."
    n "But it gets especially bad when--"
    hide n_cg1_exp1
    n "Uu..."
    n "I shouldn't be talking about that yet!"
    n "Just finish this chapter!"
    if persistent.natsuki_glitch < 6:
        "I felt weird just now..."
        if persistent.ggwp_monika == 2:
            "What the f[fword] was that?"
        else:
            "What the heck was that?"
    show black with dissolve_cg
    hide n_cg1_exp3
    show n_cg1_exp4 at cgfade behind black
    if persistent.natsuki_glitch < 6:
        "Anyway, Natsuki's voice sparkles with excitement."
    else:
        "Natsuki's voice sparkles with excitement."
    "It's a stark contrast to her usual bossy tone."
    "But if she's not used to sharing her favorite manga with her friends, I can understand why."
    "It's hard to express in words the feeling you get when connecting with someone like that."
    "And being able to provide that to Natsuki, for whom it's a rare experience..."
    "The thought makes me smile a little to myself."
    hide black with dissolve_cg
    stop music fadeout 10.0
    "But I notice that Natsuki is a little bit pale recently."
    mc "Natsuki, you seems tired all of sudden."
    mc "Are you okay?"
    hide n_cg1_exp4
    show n_cg1_exp5 at cgfade
    n "Nnnnn--"
    n "Y-Yeah..."
    n "I'm... fine."
    n "D-Don't worry about it."
    mc "A-Alright..."
    "Suddenly, Natsuki collapses straight into me."
    play sound fall
    mc "Woah--Hey--"
    "I catch her right before she falls onto the ground."
    "I grab her shoulders with both of my hands."
    "For some reason, we're like hugging together, in a weird way..."
    "My heart starts to go crazy. I don't know I'll be able to keep it up!"
    mc "Natsuki, are you okay?!"
    queue music t9
    n "..."
    "I presses my hand againts her forehead."
    "Natsuki seems having a serious fever..."
    mc "Don't worry, Natsuki."
    if persistent.natsuki_glitch == 5:
        mc "I'll help you the best I can."
        n "..."
        n "Your heart..."
        mc "...?"
        n "...is beating really fast..."
        mc "...!"
        "Ah, I didn't realise I was too close to her."
        "But I have no choice."
        "I need to help her!"
    else:
        mc "I'll call someone for help."
    mc "Just hold tight and you'll be fine."
    "Natsuki nods in agreement."
    scene bg club_day
    with dissolve_cg
    "Still holding her shoulder, I assist her to slowly get up."
    if persistent.natsuki_glitch == 5 and persistent.ggwp_monika != 4: # if player tends to reload again after normal route
        "I begin to walk with Natsuki through the door, as we are on our way to the infirmary."
        "I'll probably can find nurse there."
        stop music
        m "[player]!"
        "Ah, damn it! I can't just stop here..."
        show monika 2f at t11 zorder 2
        m "What are you doing, with Natsuki?"
        m 5b "Don't tell me you're going out with her!"
        show monika at t21 zorder 2
        show natsuki 12g at f22 zorder 2
        n "..."
        mc "W-What? No!"
        mc "That's ridiculous!"
        "That makes me feel bad about her, I mean she had no friend in the first place."
        "I'll probably ended up in the same way as before..."
        show monika 5a at t11 zorder 2
        show natsuki at thide zorder 1
        hide natsuki
        m "Ahaha, don't worry...I believe you, silly."
        m 1a "[player], I think I should handle this situation."
        m 2b "It's my job to take care of my member's well-being, as a club president."
        m 2e "You know what I mean...?"
        mc "Does this happens very often?"
        show monika 1l at s11 zorder 2
        m "Ahaha, well..."
        "There's something obvious going around here..."
        show monika 1l at t11 zorder 2
        m 1j "It just happens every now and then."
        m 1a "Don't worry about it."
        m "Now... [player], can you please let me accompany her to the infirmary instead?"
        m 2b "That would be appreciated~!"
        mc "Then, I might as well walk with you..."
        m 1n "N-No... I think you should stay away from this..."
        m "You're still new to this club, so let me handle this instea-{nw}"
        show monika at t21 zorder 2
        mc "You seem a little bit apprehensive, Monika..."
        m 1m "Ahaha--I mean..."
        m 1e "I am very concern about her health, so let me-{nw}"
        mc "That's enough, Monika."
        mc "I know you're hiding something from me."
        m 1o "..."
        n "..."
        m 2p "Well, [player]... I-I think that-"
        m 1o "Uhm..."
        "It looks like she fumbles with her words even more."
        "I don't know why, I thought I might as well break the system..."
        "Before she breaks it."
        if persistent.mc_violent:
            "Much like what I did before..."
        "Here goes nothing."
        mc "Hey, Monika..."
        mc "Sorry if I assume you doing something weird."
        mc "I think you're right, as club president."
        mc "You can have her now."
        m 2l "Ah-It's nothing to worry about, I mean you're deserve to accompany her."
        m 2n "But there's something that I need to talk to her about this problem."
        m 3a "I won't let this happen in the future, I promise. So-{nw}"
        mc "But there's one thing I need to do with you."
        m 2g "Eh? What do you mean?"
        "I approach her closer to her face."
        $ p_char_1 = player[:0]
        m 1n "[p_char_1]-[player]! W-What are you doing?"
        m 1o "..."
        m 1n "I-I think that's too early--"
        m "I mean I would loved to do that if I were you... Ahaha..." # turned on?
        m 1l "Oh my god. What's wrong with me?~"
        mc "I see..."
        "I apprehensively presses my hand against her forehea{nw}"
        if persistent.ggwp_monika != 4:
            $ audio.t29 = "<from 5.458 loop 5.458>mod_assets/sfx/p1.ogg"
            play music t29
            python:
                try: sys.modules['renpy.error'].report_exception("Panic mode failed to activate. Please send this error log to \"firelightning13\", either via DDMC official reddit page or DDMC official discord", False)
                except: pass
            scene bg club_gl
            pause 0.01
            show screen tear(8, offtimeMult=1, ontimeMult=10)
            pause 3.0
            hide screen tear
            window hide(None)
            $ persistent.ggwp_monika = 4
            $ renpy.quit(relaunch=False, status=0)
        else:
            hide monika
            scene black with trueblack
    elif persistent.ggwp_monika == 4:
        stop music
        scene black with trueblack
    else: # if players skip in the first playthrough (where mc didn't know about "protein bar" that monika had)
        mc "Monika!"
        "I think she can handle this, since she is the club president."
        show monika 1r at t11 zorder 2
        m "Oh jeez..."
        m 1d "Natsuki, are you okay?"
        show monika at t21 zorder 2
        show natsuki 12b at f22 zorder 3
        n "..."
        show natsuki at t22 zorder 2
        show monika 1f at f21 zorder 3
        m "Alright. Let me help her."
        mc "What are you going to do with her?"
        m 2i "I'm going to send her to the infirmary."
        m 2q "I hope she's okay..."
        show monika at t21 zorder 2
        show natsuki 12g at f22 zorder 3
        n "...--"
        show natsuki at t22 zorder 2
        "She looks like she wants to say something..."
        show natsuki at thide zorder 1
        show monika 3a at t11 zorder 2
        hide natsuki
        stop music fadeout 2.0
        m "Don't worry, she'll be fine."
        m "It just happens every now and then."
        mc "Really?"
        "There are things that I don't know much about them..."
        "Should I be worried about her?"
        "I sigh."
        mc "Alright. Make sure she's safe."
        m 5a "You can count on me, [player]!"
        show monika at thide zorder 1
        hide monika
        "Natsuki timidly follows Monika through the door, as they're on their way to the school's infirmary."
        if parfait_girls:
            "Then, I slip my book into my bag."
        else:
            mc "Guess I'll return this book back into its place."
            "I return her book by slipping it into her manga box."
        $ natsuki_out = True
        scene bg club_day
        with wipeleft_scene
        "..."
        "After a few minutes pass... Monika finally returns."
        show monika 4b at l11 zorder 2
        m "Alright, everyone! It's time to share poems!"
        $ config.allow_skipping = True
        $ allow_skipping = True
    return

label normal_cute_1:
    $ preferences.skip_unseen = False
    "Suddenly, Natsuki starts laugh{nw}."
    $ _history_list[-1].what = "Suddenly, Natsuki was tooo tired for {i}anythingg{/i}"
    $ currentpos = get_pos()
    stop music
    show black
    "..."
    "..."
    "....."
    "......."
    "........."
    "Time passes."
    hide n_cg1_exp3
    show n_cg1_exp4 at cgfade behind black
    "Natsuki is strangely quiet now."
    "I glance over at her."
    hide black with dissolve_cg
    "It looks like she's started to fall asleep."
    mc "Hey, Natsuki..."
    n "Y-Yeah...?"
    "Suddenly, Natsuki collapses straight into me."
    play sound fall
    mc "H-Hey... what the--"

    if persistent.natsuki_glitch == 5 or persistent.natsuki_glitch == 4:
        show n_cg1_exp5
        hide n_cg1_exp5

        show n_cg1b
        hide n_cg1_base

        $ audio.t6g = "<from " + str(currentpos) + " loop 10.893>bgm/6g.ogg"
        play music t6g
        if poetappeal == "cute":
            stop sound
            $ renpy.music.play(audio.fall_gl, channel="trans", tight=True)

        $ ntext = glitchtext(96)
        $ style.say_dialogue = style.edited
        n "{color=#000}[ntext]{/color}"
        $ ntext = glitchtext(96)
        n "{color=#000}[ntext]{/color}"
        $ style.say_dialogue = style.normal

        if poetappeal == "cute":
            $ renpy.music.stop(channel='trans', fadeout=None)
        stop music
    else:
        stop music
        show mod_one_eye
        play sound ggg
        pause 0.5
        stop sound
    window hide(None)
    window auto
    scene bg club_day

    show monika 1r at t11 zorder 2
    $ persistent.natsuki_glitch = 5
    m "Oh jeez..."
    m 1d "Natsuki, are you okay?"
    mc "Monika, what's going o-{nw}"
    $ _history_list.pop()
    call glitcher_n
    pause 0.25
    show monika at t21 zorder 2
    show natsuki 12b at f22 zorder 3
    n "..."
    show natsuki at t22 zorder 2
    show monika at f21 zorder 3
    m 1a "Here..."
    show monika at t21 zorder 2
    mc "What the f[fword] was tha-{nw}"
    $ _history_list.pop()
    call glitcher_n
    pause 0.25
    "Monika reaches into her bag and pulls out some kind of protein bar."
    "She throws it in Natsuki's direction."
    "Natsuki's eyes suddenly light up again."
    "She snatches the bar from the floor and immediately tears off the wrapper."
    show natsuki at f22 zorder 3
    n 1s "I told you not to give mmph..."
    show natsuki at t22 zorder 2
    mc "Natsuki???{nw}"
    $ _history_list.pop()
    call glitcher_n
    pause 0.25
    "She doesn't even finish her sentence before stuffing it into her mouth."
    show natsuki at thide zorder 1
    hide natsuki
    show monika 3b at t11 zorder 2
    m "Don't worry, [player]."
    m "She's fine."
    m "It just happens every now and then."
    m 1a "That's why I always keep a snack in my bag for her."
    mc "Why I can't say anyth-{nw}"
    $ _history_list.pop()
    call glitcher_n
    pause 0.25
    m 5a "Anyway...!"
    m "Why don't we all share poems now?"
    scene black with trueblack
    return

label glitcher_n:
    window hide(None)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound aglitch2
    pause 0.25
    stop sound
    hide screen tear
    window show(None)
    return
