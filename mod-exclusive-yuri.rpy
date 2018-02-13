label mod_exclusive_mp_1:
    scene bg club_day
    with wipeleft_scene
    if not persistent.ggwp_monika == 3:
        if persistent.poster_seen:
            "I need to clear my head first."
            "After I saw it in my classroom..."
            "I don't even know that I should use the word \"saw\" in this situation."
            pause 2.0
            $ currentpos = get_pos()
            stop music
            $ audio.t2g3 = "<from " + str(currentpos) + " loop 4.492>bgm/2g2.ogg"
            play music t2g3
            "Anyway, I'm really curious to talk to Yuri a little bit more..."
        else:
            "I'm really curious to talk to Yuri a little bit more..."
        "But at the same time, I would feel bad for distracting her from reading."
        "I catch a glimpse of the cover of her book."
        "It looks like the same book that she lent to me..."
        #"More than that, she seems to be on the first few pages."
        "I thought I've seen that book before..."
    elif persistent.ggwp_monika == 4 and not persistent.mc_realise: # if player tends to reload again after mc talked to yuri
        stop music
        call mc_realise_3
    else: # post glitching mc
        "I'm not sure what happened just a minute ago, between me and Yuri."
        "Ugh--My head hurts..."
        "I'm sure Yuri can explain to me what has happened to me, or her."
        "But I don't feel like asking her just yet, because I would feel bad for distracting her from reading..."
        "...as I watch her intense reading expression..."
        "..."
        $ del _history_list[-6:]
    play music t6 fadeout 1.0
    show yuri 4a at t11 zorder 2
    y "Ah..."
    if persistent.mc_violent:
        "S[sword]--"
    else:
        "Crap--"
    "I think she noticed me looking at her..."
    "She sneaks another glance at me, and our eyes meet for a split second."
    y 4b "..."
    "But that only makes her hide her face deeper in her book."
    if persistent.ggwp_monika == 2: # oof
        mc "Um..."
        "This is too awkward already..."
        "I need to stop worrying about what happened in my classroom. Just get over it!"
        mc "Sorry about that..."
    else:
        mc "S-Sorry..."
        mc "I was just spacing out..."
        "I mutter this, sensing I made her uncomfortable."
    y oneeye "Oh..."
    y "It's fine..."
    y "If I was focused, then I probably wouldn't have noticed in the first place."
    y "But I'm just re-reading a bit of this, so..."
    mc "That's the book that you gave me, right?"
    if persistent.ggwp_monika == 3:
        "Wait, what?"
        $ _history_list.pop()
    y "Mhm."
    y "I wanted to re-read some of it."
    y 2q "Not for any particular reason...!"
    mc "Ah. I wonder why..."
    mc "Also, just curious, how come you have two copies of the same book?"
    if persistent.ggwp_monika == 3:
        "I was about to ask what just happened."
        $ _history_list.pop()
        "Why did my inner thoughts doesn't show up in the history list!?"
        $ _history_list.pop()
    y "Ah..."
    y "Well, when I stopped at the bookstore yesterday--"
    y 3o "Ah, that's not what I meant..."
    y "I mean--"
    y 1w "I... just happened to buy two of them."
    if persistent.ggwp_monika == 3 and poetappeal == "abs": # mc talks to yuri about stuff
        #jump mod_exclusive_abs_1 # temporary idea
        call mod_exclusive_abs_1
        $ skip_counter = 0
        scene bg club_gl
        label stuck_loop: # stuck in infinite loop, can be avoided by skipping/loading previous save
            $ audio.t666 = "<from " + str(currentpos) + " loop 10.893>mod_assets/sfx/666.ogg"
            play music t666
            $ style.say_dialogue = style.edited
            $ gtext = glitchtext(renpy.random.randint(10,80))
            mc "[gtext]"
            $ _history_list.pop()
            if config.skipping:
                $ skip_counter += 1
                if skip_counter > 20:
                    $ config.skipping = False
                    $ currentpos = get_pos()
                    stop music
                    window hide(None)
                    show screen tear(8, offtimeMult=1, ontimeMult=10)
                    play music aglitch2
                    pause 2.0
                    stop music
                    hide screen tear
                    window show(None)
                    scene bg club_day
                    $ style.say_dialogue = style.normal
                    $ audio.t6 = "<from " + str(currentpos) + " loop 10.893>bgm/6.ogg"
                    play music t6
                    mc "Argh..."
                    "{i}What the hell was that?{/i}"
                    "My head... it hurts..."
                    show yuri 2f at t11 zorder 2
                    y "[player]?"
                    mc "Oh, yeah. Where was I?"
                    "I try to endure the pain that I'm experiencing, then I remember what we are suppose to talk about."
                    mc "Ah, I see."
                    "I look at the book that she holds with her right hand."
                else:
                    jump stuck_loop
            else:
                jump stuck_loop
    elif persistent.ggwp_monika == 4 and not persistent.mc_realise: # if player tends to reload again after mc talked to yuri
        $ currentpos = get_pos()
        stop music
        call mc_realise_3
        # jump mod_poemrp_1
        $ audio.t6 = "<from " + str(currentpos) + " loop 10.893>bgm/6.ogg"
        play music t6
        mc "Ah, I see."
        #"There's something fairly obvious here that Yuri isn't telling me, but I decide to let it go."
        #mc "I'll definitely start reading it soon!"
        "The way she act is really obvious, but I decide to let it go anyway."
        "Also, does the bookstore even exist? {w}What am I talking about right now?"
        $ _history_list.pop()
    else: # normal playthrough if choosing mp poem
        mc "Ah, I see."
        #"There's something fairly obvious here that Yuri isn't telling me, but I decide to let it go."
        #mc "I'll definitely start reading it soon!"
        "The way she act is really obvious, but I decide to let it go anyway."
        "Also, does the bookstore even exist? {w}What am I talking about right now?"
        $ _history_list.pop()
    mc I'll probably start reading it soon.
    if ihorror and persistent.ggwp_monika != 4:
        mc "I hope the story is interesting enough for me."
    y 2u "I'm glad to hear..."
    y "Once it starts to pick up, you might have a hard time putting it down."
    y 2c "It's a very engaging and relatable story."
    #mc "Is that so...?"
    mc "Oh, really?"
    mc "What's the story about, anyway?"
    y 1f "Well..."
    y "Mmm..."
    "I look at the cover of the book."
    "The book is titled \"Portrait of Markov\", with an ominous-looking eye symbol on the front cover."
    if persistent.ggwp_monika != 2:
        "This book seems familiar to me, for some reason..."
    y 1a "Basically, it's about this religious camp that was turned into a human experiment prison..."
    y "And the people trapped there have this trait that turns them into killing machines that lust for blood."
    y 1m "But the facility gets even worse, and they start selectively breeding people by cutting off their limbs and affixing them to--"
    y 1q "O-Oh, that might be a little bit of a spoiler..."
    y 3q "But anyway, I-I'm really into it!"
    y 3n "...The book, I mean!"
    y 3q "N-Not the thing about the limbs..."
    #mc "That's kind of--!"
    if ihorror:
        mc "Wow, that was unexpected synopsis."
        mc "Are you sure you didn't spoil anything?"
        y 2o "Uh... well..."
        y 2p "N-No...!"
        y 3q "I-I mean-{nw}"
        mc "No, what I mean is..."
        mc "...I can definitely enjoy those kinds of stories, so don't worry."
        y 2s "I-I see..."
        y 1l "Phew..."
    else:
        mc "Umm... that's kind of... {w}dark?"
        #"That's kind of dark, isn't it?"
        #"Yuri made it sound like it was going to be a nice story, so that dark turn came from nowhere."
        "Well, this is such an unexpected story, coming from that book..."
        y 1s "Ah..."
        y "Are you not a fan of that sort of thing, [player]?"
        mc "No, it's not that..."
        mc "I mean, I can definitely enjoy those kinds of stories, so don't worry."
        y 2u "I hope so..."
    #"Yeah... I totally forgot that Yuri is into those things."
    #"She's so shy and reclusive on the outside, but her mind seems to be completely different."
    "That was... intense..."
    "I wonder why she was so into it, with such a dark story. I can tell by her intense reading expression."
    "Is it really interesting?"
    y 1s "It's just that this kind of story..."
    y 1a "It's the kind that challenges you to look at life from a strange new perspective."
    y "When horrible things happen not just because someone wants to be evil..."
    $ style.say_dialogue = style.edited
    y "But because the world is full of horrible people, and we're all worthless anyway."
    #y "Then, suddenlyyyyyyyyyyyyyyyyyyyyyy yyyyyyyyyyyyyyyyyyyy{nw}"
    $ style.say_dialogue = style.normal
    $ gtext = glitchtext(40)
    "Huh? Why's that? [gtext]{nw}"
    $ _history_list.pop()
    $ style.say_dialogue = style.edited
    y "Then, suddenlyyyyyyyy{nw}"
    $ _history_list.pop()
    play sound aglitch1
    y "Then, suddenlyyyyyyyy{fast}yyyyyyyyyyyy yyyyyyyyyyyy{nw}"
    $ _history_list.pop()
    stop sound
    $ style.say_dialogue = style.normal
    y "Then suddenly{fast}, when you thought you related to the protagonist..."
    y "They're made out to be the naive one for letting their one-sided morals interfere with the villain's plans."
    y 3v "I'm...I'm rambling, aren't I...?"
    y "Not again..."
    y 4b "I'm sorry..."
    mc "Hey, don't apologize...!"
    mc "I haven't lost interest or anything."
    mc "I mean, I can relate that to my own life, what it is like to be a protagonist in my own story." # oh wow self-reflecting?
    mc "Being naive is another thing though..."
    y "Well..."
    y "I guess it's alright, then..."
    y 4a "But I feel like I should let you know that I have this problem..."
    y "When I let things like books and writing fill my thoughts..."
    y "I kind of forget to pay attention to other people..."
    y 3t "So I'm sorry if I end up saying something strange!"
    y "And please stop me if I start talking too much!"
    #mc "That's--"
    #mc "I really don't think you need to worry..."
    mc "Well... I don't see there's anything wrong when you talking about something."
    mc "That just means you're passionate about reading."
    mc "The least I can do is listen."
    mc "It's a literature club, after all..."
    y 4a "Ah--"
    y "That's..."
    y "Well, that's true..."
    mc "In fact..."
    mc "I might as well get started reading it, right?"
    #play sound "sfx/glitch3.ogg"
    #y dragon "Y-Yes!"
    play sound aglitch1
    pause 0.4
    stop sound
    y 3y1 "Y-Yes!{nw}"
    y 3n "I-I mean, you don't have to, but...!"
    mc "Ahaha, what are you saying?"
    y 3o "..."
    "I quickly retrieve the book that I had put into my bag."
    mc "Alright...it's fine if I sit here, right?"
    "I slip into the seat next to Yuri's."
    y 3n "Ah...!"
    y "Yeah..."
    pause 1.0
    mc "That's okay."
    mc "I know you're not used to reading in company with someone."
    mc "I mean, we're on the same boat right now."
    mc "I hope that we can socialize more, even though we're not that good at it."
    mc "Well, of course it takes time. I'm sure we'll get over this sort of barrier soon enough."
    "Wow, I sound just like Monika all of sudden."
    "But I'll make sure that Yuri is comfortable enough to be with me. I don't want Yuri to get in trouble or else..."
    y 2s "A-Alright then..."
    y "If you say so..."
    y 1s "Thank you, for reassuring me."
    mc "Let me know if you feel uncomfortable or something."
    y "A-Alright..."
    #mc "Are you sure?"
    #mc "You seem a little apprehensive..."
    #y "That's..."
    #y 4b "I'm sorry..."
    #y "It's not that I don't want you to!"
    #y "It's just something I'm not very used to..."
    #y "That is, reading in company with someone."
    #mc "I see..."
    #mc "Well, just tell me if I end up distracting you or anything."
    #y "A-Alright..."
    show yuri at thide zorder 1
    hide yuri
    "I open the book and start the prologue."
    if poetappeal == "mp": # glitch happens when choosing mp
        "..."
        "I don't know why, I'm too tired to read right now."
        "..."
        "As I look at the back of the book, I curiously read the synopsis of this book...."
        pause 1.0
        "The synopsis is pretty  different from what Yuri told me earlier..."
        "I mean... {w}it does kind of make sense, as she'd already finished reading-{nw}"
        "Wait, that doesn't make sense either... {w}she bought this book yesterday-{nw}"
        "No! This doesn't make sense either... {w}she probably has the old copy though-{nw}"
        "Ugh... {w}why am I overthinking this!{nw}" # over autocorrect mc's fake script (monika's plan)
        mc "What's this?"
        "I look at the small text printed at the bottom right corner of the back of the book."
        mc "\"Eye can see you\"?"
        $ currentpos = get_pos()
        stop music
        scene bg club_gl
        $ audio.t666 = "<from " + str(currentpos) + " loop 10.893>mod_assets/sfx/666.ogg"
        play music t666
        "Huh, what the-{nw}"
        ".my head is getting dizzy all of suddeN"
        ".i close the booK."
        $ gtext = glitchtext(5)
        y "{alpha=*0.5}[gtext]{/alpha}"
        mc "?huH"
        ".yu/U/ri is in the corner of my eYe"
        ".i realize that sHe's not actually looking at hEr own booK"
        ".i glance oveR{nw}"
        "{i}Argh, s[sword]...!{/i} My right eye hurts!"
        if persistent.protecc:
            $ _history_list.pop()
        "I quickly cover my right eye with my right hand."
        pause 1.0
        "Then, as I release my right hand from my right eye, I take a look at it..." # pls fix this sentence im bad at it
        window hide(None)
        show mod_one_eye # oof
        play sound s_gl
        pause 0.5
        hide mod_one_eye
        stop sound
        window show(None)
        mc "A... {w}blood?"
        "{cps=*0.5}What's happening right now...?{/cps}{nw}"
        $ currentpos = get_pos()
        stop music
        window hide(None)
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound s_gl
        pause 0.5
        stop sound
        hide screen tear
        window show(None)
        $ del _history_list[-25:]
        $ gtext = glitchtext(8)

        if not config.skipping and persistent.ggwp_monika != 4:
            #y "{alpha=*0.5}Hey, [player]...{/alpha}"
            #y "{alpha=*0.5}Don't mess with my power...{/alpha}"
            #y "{alpha=*0.5}Can you hear me, [player]?{/alpha}"
            #y "{alpha=*0.5}There's a devil inside all of us.{/alpha}"
            $ m.add_history(None, "", """Hey, [player]...\nDon't mess with my power...\nCan you hear me, [player]?\nThere's a devil inside all of us.""")
            $ persistent.ggwp_monika = 4

        $ audio.t6 = "<from " + str(currentpos) + " loop 10.893>bgm/6.ogg"
        play music t6
        scene bg club_day
        python: ### same text as "CAN YOU HEAR ME?.txt" but different name file
            try: renpy.file(config.basedir + "/EY3 CAN S33 Y0U.txt")
            except: open(config.basedir + "/EY3 CAN S33 Y0U.txt", "wb").write(renpy.file("CAN YOU HEAR ME.txt").read())
    else: # normal playthrough when choosing abs
        #"I soon understand what Yuri means about reading in company."
        "I kind of understand how hard it is for Yuri to be comfortable when reading with someone."
        "It's as if I can feel her presence over my shoulder as I read."
        #"It's not particularly bad thing."
        "I mean it's not particularly bad thing."
        #"Maybe a little distracting, but the feeling is somewhat comforting."
        "Well, to be honest, I haven't socialized with anyone for a long time now..."
        "Or have I?"
        "Yuri is in the corner of my eye."
        "I realize that she's not actually looking at her own book."
        "I glance over."
        "It looks like she's reading from my book instead--"
    show yuri 3n at t11 zorder 2
    y "S-Sorry!"
    if poetappeal == "mp": # glitch happens when choosing mp poem
        #y "I was just--!"
        y "I was just bathing in the feeling of your body--!{nw}"
        y 4c "Uuu... what am I saying that?!"
        mc "Wait, what?"
        "My eYe"
        $ _history_list.pop()
        "My eye{fast}s, my boOokkkkKKkkkkKKKkkkkKKK{nw}"
        $ _history_list.pop()
        window hide(None)
        hide yuri
        show mod_one_eye # oof
        play sound aglitch2
        pause 0.2
        hide mod_one_eye
        stop sound
        show yuri 4c at i11 zorder 2
        window show(None)
        pause 1.0
        "It looks like my book is still open, where it's just only first few pages."
        y 3n "I-I'm sorry...!"
    else: # glitch happens when choosing abs
        y "I was just--!{nw}"
        $ style.say_dialogue = style.edited
        y "I was just{fast} bathing in the feeling of your body heat tttttttttttttheat eattttttt{nw}"
        y "I was just{fast} bathing in the feeling of your body heat tttttttttttttheat eattttttt{nw}"
        y "I was just{fast} bathing in the feeling of your body heat tttttttttttttheat eattttttt{nw}"
        $ style.say_dialogue = style.normal
        $ del _history_list[-3:]
        python:
            try: sys.modules['renpy.error'].report_exception("List index out of rangeeYeeYe eYeeYeeYe... there's a deVil inSIde aLL oF US.", False)
            except: pass
        "What's that all about? {alpha=*0.5}Error: List index out of range{/alpha}"

    mc "Yuri, you really apologize a lot, don't you?"
    y "I...I do?"
    y 4a "I don't really mean to..."
    y "Sorry..."
    y 4c "I mean--!"
    #mc "Ahaha." - faggot
    mc "Oh, well..."
    mc "Here, this should work, right?"
    "I slide my desk until it's up against Yuri's, then hold my book more between the two of them."
    y 2v "Ah..."
    y "I-I suppose so..."
    "Yuri timidly closes her own copy."
    "Once we each lean in a little bit, our shoulders are almost touching."
    "It feels like my left arm is in the way, so instead I use my right hand to hold the book open."
    mc "Ah, I guess that makes it kind of difficult to turn the page..."
    y "Here..."
    scene y_cg1_base with dissolve_cg
    "Yuri takes her left arm and holds the left side of the book between her thumb and forefinger."
    #mc "Ah..."
    mc "Eh... okay then."
    "I do the same with my right arm, on the right side of the book."
    "That way, I turn a page, and Yuri slides it under her thumb after it flips to her side."
    if ihorror or poetappeal == "mp":
        pause 1.0
        "Hmm..."
        "This story feels a little bit dark though, and immersive as well..."
        " I guess Yuri is really good at finding these kinds of stories."
        "I wonder why..."
    else:
        "But in holding it like this..."
        "We're huddled even closer together than before."
        #"It's actually kind of distracting me...!"
        "It's kind of distracting me a little bit..."
        "It's as if I can feel the warmth of Yuri's face, and she's in the corner of my vision..."
    show y_cg1_exp1 at cgfade
    y "...Are you ready?"
    #mc "Eh?"
    mc "Ready? For what?"
    y "To turn the page..."
    #mc "Ah...sorry!" - dumb
    #mc "I think I got a bit distracted for a second..."
    mc "Ah--Uh..."
    "I glance over at Yuri's face again, and our eyes meet."
    if ihorror or poetappeal == "mp":
        mc "Well, it took me quite a while to read the whole page. So..."
    else:
        "I don't know how I'll be able to keep up with her..."
        mc "Sorry... I think I got a bit distracted for a second..."
    show y_cg1_exp2 at cgfade
    y "Ah..."
    y "That's okay."
    y "You're not as used to reading, right?"
    y "I don't mind being patient if it takes you a bit longer..."
    y "It's probably the least I can do..."
    y "Since you've been so patient with me..."
    #mc "Y-Yeah..."
    mc "Ah--Thanks."
    hide y_cg1_exp1
    hide y_cg1_exp2
    "We continue reading."
    "Yuri no longer asks me if I'm ready to turn the page."
    "Instead, I just assume that she finishes the page before me, so I turn it by my own volition."
    "We continue the first chapter in silence."
    pause 2.0
    #"Even so, turning each page almost feels like an intimate exchange..."
    #"My thumb gently letting go of the page, letting it flutter over to her side as she catches it under her own thumb."
    if poetappeal == "mp":
        window show(None)
        menu:
            "Let's talks about the main character of this story": # ironic af
                call normal_mp_1
            "Shut up and just read it" if not persistent.mc_violent and not persistent.poster_seen:
                call special_mp_1
            "Just shut the f[fword] up and just f[fgword] read it" if persistent.mc_violent or persistent.poster_seen:
                call special_mp_1
    else:
        call normal_mp_1
    return

label special_mp_1:
    "I was about to ask her about the main character of this story."
    "But for some reason, I feel like my mind doesn't allow me to talk about it..."
    "Well, I think it's better this way. I don't want to hurt her even further."
    "I mean, she could have mental problems or something that I might not know about. Maybe I should convince her to talk to a therapist."
    $ _history_list.pop()
    "Wait, what am I talking about?"
    "Oh, well..."
    pause 2.0
    stop music
    window hide(None)
    scene bg club_day
    window show(None)
    window auto
    show monika 2b at l21 zorder 2
    m "Alright, everyone! It's time to share poems!"
    m 2d "Would you kindly get the poem now? You two seems to get closer to each other, and..."
    show yuri 3n at t22 zorder 2
    y "...!"
    mc "..."
    mc "Alright, if you say so..."
    show monika 5a at f21 zorder 3
    m "Okay, [player]. You just need to hurry up. I can't wait to share my poems!"
    show yuri at t11 zorder 2
    show monika at lhide zorder 2
    hide monika
    mc "Right..."
    "Yuri releases her hand from the book, causing it to close on top of my thumb."
    mc "I guess we'll continue our reading tomorrow.."
    y 2s "A-Ah... that would be nice. I'm looking forward to it."
    show yuri at thide zorder 1
    hide yuri
    "I stand up."
    "I make a mental note of where I left off in the book, then slip it back into my bag."
    return

label normal_mp_1:
    mc "Hey, Yuri..."
    mc "This might be a silly thought, but..."
    mc "The main character kind of reminds me of you a little bit."
    show y_cg1_exp3 at cgfade
    y "E-Eh??"
    y "N-No, I don't relate to this character at all!"
    y "Definitely not!"
    "There's something obvious that Yuri didn't tell me..."
    mc "Really...?"
    mc "I was just thinking the way she second-guesses things she says, and all that..."
    show y_cg1_exp1 at cgfade
    y "A-Ah..."
    y "That's what you were talking about..."
    hide y_cg1_exp3
    hide y_cg1_exp1
    show y_cg1_exp2 at cgfade
    y "Sorry..."
    y "I thought you meant...something else about her."
    mc "Something else...?"
    hide y_cg1_exp2
    show y_cg1_exp3 at cgfade
    y "N-Never mind!"
    y "We didn't even get that far yet..."
    y "So I don't know why that came into my head..."
    y "Ahaha!"
    mc "Yuri, are you feeling alright?"
    hide y_cg1_exp3
    show y_cg1_exp1 at cgfade
    y "Eh--?"
    "Yuri's been a little fidgety ever since we started reading..."
    mc "You can rest if you're feeling sick or something."
    mc "Your breathing is a little..."
    y "My breathing...?"
    hide y_cg1_exp1
    "Yuri puts her hands on her chest, as if to feel her heartbeat."
    y "I-I didn't...even notice..."
    show y_cg1_exp3 at cgfade
    y "...Anyway, I'm fine!"
    y "I just need some water...!"
    mc "Alright...don't push yourself."
    scene bg club_day
    with dissolve_cg
    "Yuri stands up and practically rushes out of the classroom."
    mc "What on Earth was that about...?"
    show monika 1d at t11 zorder 2
    m "[player]?"
    m "Did something happen just now?"
    "I don't think I can say whatever I want..."
    "Or else she would be too suspicious of me."
    mc "Eh?"
    mc "I have no idea..."
    mc "Yuri was acting a little strange, I guess..."
    m 1r "So you don't know anything..."
    mc "Sorry, I can't say I do."
    mc "Are you worried about her?"
    m 1a "Oh...no, not really."
    m "I was just making sure that you didn't do anything to her."
    mc "N-No, nothing!"
    m 5a "Ahaha, don't worry...I believe you, silly."
    m "Yuri just does this sometimes, so it's nothing alarming."
    mc "Alright...if you say so."
    m 2b "Anyway, why don't we start with sharing our poems with each other?"
    mc "Eh?"
    mc "Shouldn't we wait for Yuri?"
    m 2a "Well, she might be out a while, so I just figured we'd get started without her."
    m "Is that okay?"
    #mc "Yeah, I was just asking..."
    mc "Yeah, sure. Why not?"
    show monika at thide zorder 1
    hide monika
    "I stand up."
    "I make a mental note of where I left off in the book, then slip it back into my bag."
    "I hope that Yuri comes back safely..."
    $ y_ranaway = True
    return

label mod_exclusive_abs_1:
    $ currentpos = get_pos()
    stop music
    window hide(None)
    show screen tear(8, offtimeMult=1, ontimeMult=10)
    play music aglitch1
    pause 0.25
    stop music
    hide screen tear
    window show(None)
    scene black
    # mc's doki-doki power charged up to 9000 bps
    show yuri 1w at i11 zorder 2
    mc "Umm... Yuri?"
    mc "Can I ask you one question?"
    y 3p "E-Eh?"
    y "W-What is happening right now?"
    mc "Don't worry, we're safe here"
    y 3o "Uuu..." # what?
    play music t9gl
    mc "Yuri..."
    "I honestly don't want to talk about this... but she leaves me no choice."
    mc "What is going on around here?"
    mc "What is happening to me?"
    mc "If you know everything, you can't just hide it from me!"
    y 4b "..."
    "She looks away from me."
    "I assume she knows everything."
    "It's very obvious that she might know everything."
    "It's only second da-{nw}"
    "No... it's been 6 days since I was here, right?"
    "My memories don't lie..."
    "But..."
    "I think I went too far."
    "I know her too well, so..."
    mc "Yuri."
    y 3p "W-What..?"
    mc "It's okay that you don't want to tell me anything."
    mc "But, if you want my help, just ask me anytime okay?"
    y 3o "..."
    mc "I'll help you no matter what."
    "I feel like I should be responsible, as a friend."
    "I'll help her! I'll help all of them!"
    y 3w "I..."
    y 2v "I... don't know..."
    y "I can't remember anything..."
    "Hmm... she didn't remember anything?"
    "She didn't look like she was lying..."
    "Maybe I underestimate her..."
    mc "Alright... don't push yourself, okay?"
    "I say that as I hold her right hand with my left hand, trying to make her comfortable."
    y 2s "[player]..."
    mc "What is it, Yuri?"
    "She holds my other hand with her right hand."
    show yuri 2s at face(y=600) with dissolve
    y "I kind of like that about you..."
    "Didn't I hear this phrase before?"
    hide yuri at face(y=600)
    stop music
    window hide(None)
    show s_hacker zorder 10
    play sound sgl
    pause 0.5
    stop sound
    hide s_hacker
    window show(None)
    show yuri 3p at i11 zorder 2
    y "S-Sayori--?"
    mc "Wait, what?"
    $ gtext = glitchtext(20)
    mc "How did you know her na{nw}"
    play music gl
    show yuri glitch at t11 zorder 2
    mc "How did you know her na{fast} [gtext] [gtext] [gtext]{nw}"
    window hide(None)
    window auto
    hide yuri
    stop music
    scene bg club_day
    pause 2.0
    #$ audio.t6 = "<from " + str(currentpos) + " loop 10.893>bgm/6.ogg"
    #play music t6
    $ del _history_list[-44:]
    $ persistent.ggwp_monika = 4
    #show yuri 1w at i11 zorder 2
    return

########################################################
#### Temporary idea, dont't change anything below! #####
###############################################################################################
#    y "[player]...?"
#    mc "A-Ah...!"
#    mc "What just happened?"
#    show yuri 2g at t11 zorder 2
#    y "Hmm..."
#    y 2f "Well, we were reading together just now, and..."
#    y 2n "I-I mean...!"
#    mc "Huh?"
#    "Apparently Yuri is sitting right next to me, and we're still holding my book."
#    "I don't remember what just happen..."
#    "What's going o{nw}"
#    $ _history_list.pop()
#    show yuri at t22 zorder 2
#    show monika 2b at l21 zorder 2
#    m "Alright, everyone! It's time to share poems!"
#    m "Would you kindly get the poem now? You two seems to get closer to each other, and..."
#    y 3n "...!"
#    mc "..."
#    mc "Alright, if you say so..."
#    m 5a "Okay, [player]. You just need to hurry up. I can't wait to share my poems!"
#    show yuri at t11 zorder 2
#    show monika at lhide zorder 1
#    hide monika
#    mc "Right..."
#    "Yuri releases her hand from the book, causing it to close on top of my thumb."
#    mc "I guess we'll continue our reading tomorrow.."
#    y 2s "A-Ah... that would be nice. I'm looking forward to it."
#    show yuri at thide zorder 1
#    hide yuri
#    "I stand up."
#    "I make a mental note of where I left off in the book, then..."
#    "Wait, that's stupid! I don't even know what I'm reading just now."
#    "Well, I think I can just ask Yuri about it."
#    "Anyway, I proceed to slip it back into my bag, and take out my poem."
#    return
###############################################################################################
