### Choice starts here ###
label mod_accepts:
    mc "Yeah.."
    mc "I mean it could be fun, right?"
    mc "Sharing our poems to each other..."
    show monika 1d at f33 zorder 3
    "Monika looks at me quizzically"
    m "Wait, [player]?"
    mc "Yes?"
    $ config.keymap['dismiss'] = []
    $ renpy.display.behavior.clear_keymap_cache()
    "She stares into my eyes for a good 3 seconds long{w=2.0}{nw}"
    $ config.keymap['dismiss'] = dismiss_keys
    $ renpy.display.behavior.clear_keymap_cache()
    mc "Eh, you mean..."
    mc "You know...."
    m "You do?"
    m 1b "Oh my goodness!"
    m 5a "You really mean it, don't you?"
    "Monika smiles sweetly."
    "Ugh, I guess I need to endure it anyway."
    show monika at t33 zorder 2
    mc "Yeah, I decided to join your club anyway."
    mc "I guess literature isn't really that bad for me."
    show monika at f33 zorder 3
    m "[player], I'm so happy..."
    m 1k "We can become an official club now!"
    m 1e "Thank you so much for this. You're really amazing."
    show monika at t33 zorder 2
    show natsuki 5w at f31 zorder 3
    n "Hmph. I really thought you didn't want to join our club."
    n 5e "Then you would be a complete jerk if you did that."
    mc "Yeah, yeah."
    show natsuki 5a at t31 zorder 2
    show yuri 1a at f32 zorder 3
    y "That is a wise decision."
    y 3m "I am so happy that you joined our club before the festival..."
    show yuri at t32 zorder 2
    mc "Ah, thank you."
    mc "It was my own choice after all"
    "I hope she's okay with me here."
    "Though I'm kind of worried that she might be her next target."
    #which is true, by the way
    return

label mod_rejects:
    if persistent.ggwp_monika == 3:
        "Oh wait, what?"
        "What's that supposed to be?"
    mc "Hold on...there's still one problem."
    show monika at f33 zorder 3
    m 1d "Eh? What's that?"
    if persistent.ggwp_monika == 3:
        "I've been forced to reject their invitation."
        "I thought I can just..."
        "Maybe because of the mashup just now?"
        "Did Monika do this on purpose?"
    else:
        "Guess I'll try to be natural then, if the game wants me to do this."
        "{i}I hope I didn't raise her suspicion level on me.{/i}"
    show monika at t33 zorder 2
    mc "I never said I would join this club!"
    mc "Monika may have convinced me to stop by, but I never made any decision."
    mc "I still have other clubs to look at, and...um..."
    show monika 1g
    show natsuki 4g
    show yuri 2e
    #"I lose my train of thought."
    #"All three girls stare back at me with dejected eyes."
    if persistent.ggwp_monika != 3:
        "I don't know why, but I felt kind of guilty after seeing their dejected eyes."
        "I feel bad for them."
    show monika at s33
    m 1p "B-But..."
    show yuri at s32
    y 2v "I'm sorry, I thought..."
    show natsuki at s31
    n 5s "Hmph."
    mc "Eh...?"
    "The girls exchange glances before Monika turns back to me."
    show monika at f33 zorder 3
    m 1m "I...guess I need to tell you the truth, [player]."
    m "The thing is..."
    m 1p "...We don't have enough members yet to form an official club."
    m "We need four..."
    m "And I've been trying really, really hard to find new members."
    m "And if we don't find one more before the festival..."
    show monika at t33 zorder 2
    mc "..."
    mc "I, uh..."
    mc "*Sigh*"
    if persistent.ggwp_monika == 3:
        "I feel like I'm defenseless against these girls, because I was forced to reject their invitation."
    else:
        "I feel like I'm defenseless against these girls."
    "Why am I being an asshole this whole time?"
    "Not to mention my best friend..."
    #"I...I'm defenseless against these girls."
    #"How am I supposed to make a clear-headed decision when it's like this?"
    #"I would feel terrible for letting everyone down in this situation..."
    #"So, if writing poems is the price I need to pay in order to spend every day with these beautiful girls..."
    mc "...Right."
    mc "Okay, I've decided, then."
    mc "I'll join the Literature Club."
    show monika 1e at t33 zorder 2
    show yuri 3f at t32 zorder 2
    show natsuki 1k at t31 zorder 2
    "One by one, the girls' eyes light up."
    show monika at f33 zorder 3
    m "Oh my goodness, really?"
    m "Do you really mean that, [player]?"
    show monika at t33 zorder 2
    mc "Yeah..."
    "\"Yeah...{fast}, right...\""
    mc "It could be fun, right?"
    show yuri at f32 zorder 3
    y 1m "You really did scare me for a moment..."
    if persistent.poster_seen:
        "Umm, yeah, Yuri."
        "The poster that I saw in my classroom is even scarier than me."
        if renpy.showing("bg spoopy", layer='master'):
            "Not to mention the one in the back of this classroom."
            "Haven't they even noticed?"
    elif renpy.showing("bg spoopy", layer='master'):
        "Yeah, the back of the classroom is even scarier than me."
        "Haven't they even noticed?"
    show yuri at t32 zorder 2
    show natsuki at f31 zorder 3
    n 5q "I mean, if you really just left after all this, I would be super pissed."
    mc "Yeah, yeah..."
    show natsuki at t31 zorder 2
    show monika at f33 zorder 3
    m "[player], I'm so happy..."
    m 1k "We can become an official club now!"
    m 1e "Thank you so much for this. You're really amazing."
    return    

label hello_neighbor:
    stop music fadeout 2.0
    scene bg house
    with wipeleft_scene
    "I'm kind of curious what is going on with my neighbor next door."
    "Since I was cockblocked{nw}"
    $ _history_list.pop()
    "Since{fast} Monika blocked me from entering that house."
    "Sorry, I didn't want to say something weird in this cute game."
    "I'm sure Monika wasn't supposed to be around here."
    "I know that this world is not like a sandbox, where you can go around anywhere..."
    #remember yandere simulator?
    "But that doesn't mean I can't do whatever I want in this game, {w}right?"
    "I take a closer look at the door."
    ####### There will be a locked version of the same door. I wanted to implement
    ####### a suspicion level system to Monika. If she is too suspicious to you, she
    ####### will lock the door. Same thing will happened like this in the future. :)
    ####### Or I could use persistent.ggwp_monika instead.
    ####### I don't know if this is too much, but let see how my mood coding goes.
    "The door is unlocked. Just like what I expected."
    mc "Ah, screw it!"
    mc "I'm going in!"
    
    scene black
    with wipeleft_scene
    play music mend
    
    "I look around on the first floor. The vibe that I get is something familiar..."
    "Back in the day when I lived with my best friend, Sayori."
    "I proceed to go upstairs, where Sayori's bedroom was."
    pause 1.0
    "I stand in front of Sayori's bedroom door."
    "This actually reminds me of the last moment when she ha{nw}"
    $ _history_list.pop()
    mc "No, I don't want to remember it anymore."
    "My anxiety is welling up inside my head even more."
    "I don't know if I can do this..."
    "I roughly remember what I told her."
    menu:
        mc "Sayori..."
        "\"I love you.\"":
            "I loved her."
            "I loved her so much."
            "I told her everything will be okay.."
        "\"You'll always be my dearest friend.\"":
            "I turned down her confession."
            "I thought that's what Sayori wants out of our relationship."
    "But no matter what I did, it always ended up in the same way..."
    "What kind of cruel game is this?"
    "It ruined my life..."
    "I don't know what to say anymore."
    stop music fadeout 2.0
    "Holding my tears, I grab the door knob."
    mc "Here goes nothing..."
    "I slowly open the door."
    pause 2.0
    mc "{cps=30}...Sayo-{/cps}{nw}"
    $ _history_list.pop()
    window hide(None)
    window auto
    show screen tear(8, offtimeMult=1, ontimeMult=10)
    play music g2
    pause 2.0
    hide screen tear

    scene bg bedroom
    show screen tear(8, offtimeMult=1, ontimeMult=10)
    pause 1.0
    hide screen tear
    stop music
    # scene bg bedroom_dawn
    # coming soon

    mc "Huh?"
    "Wait, what?"
    "This isn't her room..."
    "This is my room!"
    "Where am I?"
    "Why am I here?"
    "..."
    pause 2.0
    "I proceed to look outside through my bedroom window."
    mc "Did I just get teleported?"
    "Confused, I glance around."
    "My head is spinning like crazy."
    "Is this some kind of a trap?"
    "I don't know..."
    mc "I need to clear my head first. I'm so tired right now."
    mc "I need some rest..."
    "Maybe I'll do something tomorrow.."
    $ persistent.ggwp_monika = 4
    # 4 means he forgot to write poems, coming soon for chapter 3 i guess
    jump mod_end_demo

##### Start chapter here ######
label chapter_mod_2:
    if not monika_seen:
        # I give you a big warning. I'm just tired.
        stop music fadeout 2.0
        scene black
        with dissolve_scene_full
        $ fl = "FL13"
        fl "Damn, [player]..."
        fl "Why are you even playing this mod?"
        fl "Please play the game more carefully."
        fl "You wanted to know what happened if you visit Sayori's house, right? {w}Or not?"
        fl "You chose to go to school instead. {w}That was a wise choice."
        fl "Then that would be a normal gameplay."
        fl "Sorry, I don't take plots from original DDLC. It wasn't fun at all, since you already know what's gonna happen."
        fl "I don't even want to copy paste original DDLC script one by one into my mod."
        fl "It would be pain in the ass.."
        fl "Then, next time, I'll force you to go to Sayori's house."
        #fl "No butts. But {w}T {w}H {w}I {w}C {w}C{nw}"
        #$ persistent.playthrough = 2
        $ delete_all_saves()
        $ persistent.nice_try = 0
        $ persistent.ggwp_monika = 0
        $ monika_seen = False
        $ persistent.parfait_girls = False
        $ persistent.poster_seen = False
        $ persistent.tea_set = False
        $ persistent.mc_violent = False
        $ persistent.force_play = True
        $ persistent.warning_seen = True
        $ renpy.quit(relaunch=False, status=0)

    #haha i did it again~
    $ delete_all_saves()
    stop music fadeout 2.0

    scene bg corridor
    with wipeleft_scene

    "And thus, today marks the day I sold my soul to Monika and her irresistible smile."
    "Not really, I'm just saying it for the sake of the game script."
    if persistent.force_play:
        "Also, FL13 is really mad right now... I think"
        $ _history_list.pop()
        "Oh well..."
        $ _history_list.pop()
    "I timidly follow Monika across the school and upstairs - a section of the school I rarely visit, being generally used for third-year classes and activities."
    "Monika, full of energy, swings open the classroom door."

    if renpy.random.randint(0, 5) == 0:
        scene bg spoopy
    else:
        scene bg club_day
    with wipeleft
    play music t3

    #oh yeah? i'm already self-aware ya know that!?
    if renpy.random.randint(0, 2) == 0:
        show monika g1 at l31
        $ monika_glitch = True
    else:
        show monika 3b at l31
        $ monika_glitch = False
    m "I'm back~!"
    m "And I brought a guest with me!"
    #Show time
    if monika_glitch:
        "Monika, please don't let your true nature show..."
        if persistent.poster_seen:
            "I've already seen that horrible poster in my classroom..."
            if renpy.showing("bg spoopy", layer='master'):
                "And I see it again..."
                "Please help me."
    elif renpy.showing("bg spoopy", layer='master'):
        "What's that poster on the back wall of the classroom?"
    show yuri 2t at t33 zorder 2
    if not config.skipping:
        show screen invert(0.15, 0.3)
    $ y_name = "Girl 1"
    y "Eh?"
    y "A...a guest?"
    "What's this? A jumpscare?{nw}"
    $ _history_list.pop()
    show natsuki 4c at t32 zorder 2
    $ n_name = "Girl 2"
    n "Seriously? You brought a boy?"
    n "Way to kill the atmosphere."
    "Umm, yeah Natsuki... About that, she already killed the atmosphere in my classroom just now."
    "Wait, how do I know her name?{nw}"
    show monika 3m at f31 zorder 3
    m "Don't be mean, Natsuki..."
    m 3b "...But anyway, welcome to the club, [player]!"
    show monika 3a at t31 zorder 2
    mc "..."
    "All words escape me in this situation."
    "This club..."
    "{i}...is full of incredibly cute girls!!{/i}"

    "Again, {w}for the sake of the game scr{nw}"
    $ _history_list.pop()
    show natsuki at f32 zorder 3
    n 5c "So, let me guess..."
    if n_name == "Girl 2": # Just incase if user quits and run again because of script.rpy
        "Didn't Monika mention her name just now?"
        "Why is her name still \"Girl 2\"?!"
    n "You're Monika's boyfriend, right?"
    show natsuki at t32 zorder 2
    mc "Wha--"
    mc "No, I'm not!"
    "Huh?! Who gives you that idea?"
    show yuri at f33 zorder 3
    y 2l "Natsuki..."
    $ n_name = 'Natsuki'
    "The girl with the sour attitude, whose name is apparently Natsuki,{nw}"
    $ style.say_dialogue = style.edited
    "{cps=*2}The girl with the sour attitude, whose name is apparently Natsuki,{fast} is one I don't recognize.{/cps}{nw}"
    "{cps=*2}Her small figure makes me think she's probably a first-year.{/cps}{nw}"
    window hide(None)
    show screen tear(8, offtimeMult=1, ontimeMult=10)
    pause 2.0
    hide screen tear
    window show(None)
    $ style.say_dialogue = style.normal
    "Okay, I already know that."
    
    show yuri at t33 zorder 2
    show monika at f31 zorder 3
    m 2l "A-Anyway, this is Natsuki, energetic as usual..."
    m 2b "And this is Yuri, the Vice President!"
    $ y_name = 'Yuri'
    show monika 2a at t31 zorder 2
    show yuri at f33 zorder 3
    y 4 "I-It's nice to meet you..."
    #"Yuri, who appears comparably more mature and timid, seems to have a hard time keeping up with someone like Natsuki."
    pause 1.0 #we already know this...
    show yuri at t33 zorder 2
    mc "Yeah... It's nice to meet both of you."
    show monika at f31 zorder 3
    m 1a "So, I ran into [player] in a classroom, and he decided to come check out the club."
    m "Isn't that great?"
    "What's so great about me?"
    if persistent.poster_seen:
        "You just ruined my life back there."
    if persistent.mc_violent:
        "I just did something crazy back there."
    show monika at t31 zorder 2
    show natsuki at f32 zorder 3
    n 4e "Wait! Monika!"
    n "Didn't I tell you to let me know in advance before bringing anyone new?"
    n 4q "I was going to...well, you know..."
    "Make cupcakes?{nw}"
    show natsuki at t32 zorder 2
    show monika at f31 zorder 3
    m 1e "Sorry, sorry!"
    m "I didn't forget that, but I just happened to run into him."
    show monika at t31 zorder 2
    show yuri at f33 zorder 3
    y 1a "In that case, I should at least make some tea, right?"
    show yuri at t33 zorder 2
    show monika at f31 zorder 3
    mc "Ah, thanks?"
    m 1b "Yeah, that would be great!"
    m "Why don't you come sit down, [player]?"
    mc "Sure..."
    hide monika
    hide natsuki
    hide yuri
    with wipeleft

    "The girls have a few desks arranged to form a table."
    "Yuri walks to the corner of the room and opens the closet."
    "Meanwhile, Monika and Natsuki sit across from each other."
    "Well it looks like I have to play along, so I take a seat next to Monika."
    show monika 1a at t11 zorder 2
    m "So, I know you didn't really plan on coming here..."
    m "But we'll make sure you feel right at home, okay?"
    m 1j "As president of the Literature Club, it's my duty to make the club fun and exciting for everyone!"
    "Right..."
    "What should I say at this point?"
    mc "I'm surprised there aren't more people in the club yet."
    mc "It must be hard to start a new club."
    m 3b "You could put it that way."
    m "Not many people are very interested in putting out all the effort to start something brand new..."
    m "Especially when it's something that doesn't grab your attention, like literature."
    m "You have to work hard to convince people that you're both fun and worthwhile."
    m "But it makes school events, like the festival, that much more important."
    "Festival? I don't know much about what a literature club supposed to do in the festival."
    "As I don't see how well it goes, yet..?"
    if closet_checked and persistent.ggwp_monika != 3:
        "Speaking of festival..."
        mc "Hey, Monika?"
        show monika at f11 zorder 2
        m 1d "Yes, [player]?"
        mc "Here."
        "I take out markers and construction papers from my bag."
        "I took them from my classroom's closet just now."
        mc "I thought you need these for the festival, right?"
        $ currentpos = get_pos()
        stop music
        show monika 1n at t11 zorder 2
        "Monika looks sweaty."
        if persistent.ggwp_monika == 2:
            "The way her face looks... I know she did something horrible since I was there in the classroom."
            "Is she aware that I've changed?"
        m "A-ah, yeah..."
        m 1m "I-I see..."
        "The way she acts is really obvious..."
        "I hand the things in to Monika"
        m "Thanks..."
        show monika at t22 zorder 2
        show natsuki 5m at f21 zorder 3
        n 5m "Monika? Is there something wrong?"
        show natsuki at t21 zorder 2
        m 1l "I-It's nothing.."
        m "Ahaha.."
        "What's going on here?"
        "For some reason, the situation is getting intense."
        mc "Monika?"
        show monika 1o
        "It looks like she's in panic."
        m 1r "I'm just feeling a little bit dizzy lately, that's all..."
        "Her expression changed drastically."
        "I wonder for how long she can hold from hiding her true natu{nw}"
        $ persistent.temp_ggwp = persistent.ggwp_monika
        $ persistent.ggwp_monika = 3
        window hide(None)
        show screen tear(8, offtimeMult=1, ontimeMult=10)
        play music g2
        pause 2.0
        hide screen tear
        stop music
        scene white
        play music t1
        show intro with Dissolve(0.5, alpha=True)
        pause 2.5
        hide intro with Dissolve(0.5, alpha=True)
        show splash_warning "What are you doing?" with Dissolve(0.5, alpha=True)
        pause 1.0
        scene bg club_day
        $ audio.t3 = "<from " + str(currentpos) + " loop 4.499>bgm/3.ogg"
        play music t3
        window show(None)
        show monika 2k at i22 zorder 2
        show natsuki 4q at i21 zorder 2
        $ del _history_list[-24:]
    else:
        if persistent.ggwp_monika == 3:
            "I recognise these conversations from before."
            "It would be better if I didn't hand in the \"stuff\" to Monika."
            "At least not to raise her suspicion level on me."
            $ persistent.ggwp_monika = persistent.temp_ggwp
        m 2k "I'm confident that we can all really grow this club before we graduate!"
        m "Right, Natsuki?"
        show monika at t22 zorder 2
        show natsuki 4q at t21 zorder 2
        n "Well..."
        n "...I guess."
        "Natsuki reluctantly agrees."
        #"Such different girls, all interested in the same goal..."
        if persistent.ggwp_monika != 3:
            "Well, I guess literature isn't really that hard."
            "Despite it being kind of dull, it was worth making a poem, sharing with your friends and finding inspiration from other people."
            "The basic fundamental of literature is to express yourself."
            "Wow, I sound just like Monika..."
            "I don't know, I feel like I've done this before."
        #"Monika must have worked really hard just to find these two."
    "Yuri returns to the table, carrying a tea set."
    if persistent.tea_set:
        "Hm... I've seen this tea set before."
        "Weird..."
    "She carefully places a teacup in front of each of us before setting down the teapot in the middle."
    show natsuki at thide zorder 1
    show monika at thide zorder 1
    hide natsuki
    hide monika
    show yuri 1a at t21 zorder 2
    mc "You keep a whole tea set in this classroom?"
    y "Don't worry, the teachers gave us permission."
    if persistent.tea_set:
        "Really? I have an extra tea set in my classroom."
        "This school isn't that rich to buy a tea set for each classroom...."
    y "After all, doesn't a hot cup of tea help you enjoy a good book?"
    mc "Ah... I guess you're right, Yuri."
    show monika 4a at f22 zorder 3
    m "Ehehe, don't let yourself get intimidated, Yuri's just trying to impress you."
    show monika at t22 zorder 2
    show yuri at hf21
    y 3n "Eh?! T-That's not..."
    #"Insulted, Yuri looks away."
    "Really, Monika? You put me in a trap here..."
    y 4b "I meant that, you know..."
    show yuri at t21 zorder 2
    mc "I believe you."
    mc "Well, tea and reading might not be a pastime for me, but I at least enjoy tea."
    show yuri at f21 zorder 3
    y 2u "I'm glad..."
    show yuri at t21 zorder 2
    "Yuri faintly smiles to herself in relief."
    show monika at thide zorder 1
    hide monika
    show yuri 1a at t32 zorder 2
    y "So, [player], what kinds of things do you like to read?"
    mc "Well... Ah..."
    "I think I read a book before."
    "My memory is getting hazy, so I thought giving a rough answer is better than nothing."
    #"Considering how little I've read these past few years, I don't really have a good way of answering that."
    mc "...Manga..."
    #"I mutter quietly to myself, half-joking."
    if persistent.parfait_girls:
        "Though I want to read Parfait Girls later."
        "It looks interesting from the synopsis at the back of the book that I found."
        "Well, I'm a boy, so please don't think this is a weird thing to do."
        "Huh?"
    show natsuki 1c at t41 zorder 2
    "Natsuki's head suddenly perks up for some reason."
    #"It looks like she wants to say something, but she keeps quiet."
    "I bet she wants to say something about manga. I wonder if she..."
    show natsuki at thide zorder 1
    hide natsuki
    y 3u "N-Not much of a reader, I guess..."
    mc "Ah..."
    mc "Don't say that, you made it sound like a big deal or something"
    "I said that because of Yuri's sad smile."
    "It's up to me to save this situation."
    mc "I do like reading sometimes."
    mc "If there's any book that promotes interesting story, then I might enjoy reading it."
    y 3v "I see..."
    "Somehow I made her relieved a little bit."
    mc "Anyway, what about you, Yuri?"
    y 1l "Well, let's see..."
    "Yuri traces the rim of her teacup with her finger."
    y 1a "My favorites are usually novels that build deep and complex fantasy worlds."
    y "The level of creativity and craftsmanship behind them is amazing to me."
    y 1f "And telling a good story in such a foreign world is equally impressive."
    "I already knew that she is clearly passionate about her reading."
    "Even though she has an exquisite appearance, I could tell that she finds her comfort in the world of books, not people."
    "I would think she is not really into social-interaction, or maybe she is."
    #"Yuri goes on, clearly passionate about her reading."
    #"She seemed so reserved and timid since the moment I walked in, but it's obvious by the way her eyes light up that she finds her comfort in the world of books, not people."
    y 2m "But you know, I like a lot of things."
    y "Stories with deep psychological elements usually immerse me as well."
    y 2a "Isn't it amazing how a writer can so deliberately take advantage of your own lack of imagination to completely throw you for a loop?"
    "Really? I would think the same way in this current situation."
    y "Anyway, I've been reading a lot of horror lately..."
    mc "Really? I read a horror book once."
    "Or twice."
    "At this point, Yuri might as well be having a conversation with a rock."
    #"I desperately grasp something I can relate to at the minimal level."
    #"At this rate, Yuri might as well be having a conversation with a rock."
    show monika 1j at f33 zorder 3
    m "Ahaha. I'd expect that from you, Yuri."
    m 1a "It suits your personality."
    "I don't know why, but something's fishy about this conversation."
    show monika at t33 zorder 2
    show yuri at f32 zorder 3
    y 1a "Oh, is that so?"
    y "Really, if a story makes me think, or takes me to another world, then I really can't put it down."
    y "Surreal horror is often very successful at changing the way you look at the world, if only for a brief moment."
    show yuri at t32 zorder 2
    show natsuki 5q at f31 zorder 3
    n "Ugh, I hate horror..."
    show natsuki at t31 zorder 2
    show yuri at f32 zorder 3
    y 1f "Oh? Why's that?"
    "She likes cute things, maybe?"
    show yuri at t32 zorder 2
    show natsuki at f31 zorder 3
    n 5c "Well, I just..."
    "Natsuki's eyes dart over to me for a split second."
    n 5q "Never mind."
    show natsuki at t31 zorder 2
    show monika at f33 zorder 3
    m 1a "That's right, you usually like to write about cute things, don't you, Natsuki?"
    "Ah, I knew it."
    show monika at t33 zorder 2
    show natsuki 1o at f31 zorder 3
    n "W-What?"
    n "What gives you that idea?"
    show natsuki at t31 zorder 2
    show monika at f33 zorder 3
    m 3b "You left a piece of scrap paper behind last club meeting."
    m "It looked like you were working on a poem called--"
    show monika at t33 zorder 2
    show natsuki 1p at f31 zorder 3
    n "Don't say it out loud!!"
    n "And give that back!"
    show natsuki at t31 zorder 2
    show monika at f33 zorder 3
    m 1j "Fine, fine~"
    show monika 1a at t33 zorder 2
    mc "Natsuki, you write your own poems?"
    "I think everyone does writing their own poems at least once or twice."
    "I may have also written poems before."
    "I wonder whats her last poem anyway?"
    show natsuki at f31 zorder 3
    n 1c "Eh? Well, I guess sometimes."
    n "Why do you care?"
    show natsuki at t31 zorder 2
    mc "I think that's impressive."
    mc "Why don't you share them sometime?"
    show natsuki at f31 zorder 3
    n 5q "N-No!"
    "Natsuki averts her eyes."
    n "You wouldn't...like them..."
    show natsuki at t31 zorder 2
    mc "Ah.. You shouldn't worry about that."
    mc "I guess you need more confidence to share with someone.."
    #mc "Ah...not a very confident writer yet?"
    show yuri at f32 zorder 3
    y 2f "I understand how Natsuki feels."
    y "Sharing that level of writing takes more than just confidence."
    y 2k "The truest form of writing is writing to oneself."
    "Damn Yuri, you're so poetic."
    y "You must be willing to open up to your readers, exposing your vulnerabilities and showing even the deepest reaches of your heart."
    mc "So, you're basically saying that language itself is very important for making poems?"
    y 1b "Yes. It's like an artist painting beautiful pictures for everyone to see."
    y "People value the artist more than just a picture."
    "Huh? I didn't know Yuri likes pictures."
    "I thought I've heard that before from Sayori.."
    mc "I see.."
    show yuri at t32 zorder 2
    show monika 2a at f33 zorder 3
    m "Do you have writing experience too, Yuri?"
    m "Maybe if you share some of your work, you can set an example and help Natsuki feel comfortable enough to share hers."
    show yuri at s32
    y 3o "..."
    mc "Well, I guess it's the same for Yuri..."
    "I knew that from the start."
    "We all sit in silence for a moment."
    "What should I do at this point?"
    show monika at f33 zorder 3
    m 5a "Hey, I just got an idea!"
    m "How about this?"
    show monika at t33 zorder 2
    show natsuki 2k at f31 zorder 3
    show yuri 3e at f32 zorder 3
    ny "...?"
    "Natsuki and Yuri look quizzically at Monika."
    show natsuki at t31 zorder 2
    show yuri at t32 zorder 2
    show monika at f33 zorder 3
    m 2b "Let's all go home and write a poem of our own!"
    m "Then, next time we meet, we'll all share them with each other."
    m "That way, everyone is even!"
    "Didn't I hear this idea before?"
    show monika 2a at t33 zorder 2
    show natsuki at f31 zorder 3
    n 5q "U-Um..."
    show natsuki at t31 zorder 2
    show yuri 3v at f32 zorder 3
    y "..."
    show yuri at t32 zorder 2
    "I guess Yuri and Natsuki are having problems with accepting her idea."
    show monika 2m at f33 zorder 3
    m "Ah..."
    m "I mean, I thought it was a good idea..."
    show monika at t33 zorder 2
    show yuri at f32 zorder 3
    y 2l "Well..."
    y "...I think you're right, Monika."
    "Nevermind. I take back what I said before."
    y 2f "We should probably start finding activities for all of us to participate in together."
    y 2h "I did decide to take on the responsibility of Vice President, after all..."
    y "I need to do my best to nurture the club as well as its members."
    y 2a "Besides, now that we have a new member..."
    y "It seems like a good step for us to take."
    y "Do you agree as well, [player]?"
    show yuri at t32 zorder 2

    ####Time to choose
    mc "Well, uh...?"
    "Joining this club is not really a problem, but this game wants me to reject their invitation."
    "I don't know why, but accepting this club is not really a problem too."
    "Even if I say no, it won't change anything."
    "But, it's up to you."
    "You have your own will. Atleast we can avenge our best friend."
    menu:
        "So, what are you going to do, [player]?"
        "Accept their invitation":
            if persistent.ggwp_monika == 3:
                # u fked up boi
                $ currentpos = get_pos()
                stop music
                window hide(None)
                show screen tear(8, offtimeMult=1, ontimeMult=10)
                play music g2
                pause 3.0
                hide screen tear
                stop music
                window hide(None)
                $ audio.t3 = "<from " + str(currentpos) + " loop 4.618>bgm/3.ogg"
                play music t3
                $ persistent.accepts_invite = False
                call mod_rejects from _call_mod_rejects
            else:
                $ persistent.accepts_invite = True
                call mod_accepts from _call_mod_accepts
        "Reject their invitation":
            $ persistent.accepts_invite = False
            call mod_rejects from _call_mod_rejects_1

    ####End of Choice
    show monika at f33 zorder 3
    m "I'll do everything I can to give you a great time, okay?"
    mc "Ah. Alright then..."
    "Of course, I feel something's off"
    "Something bad is going to happen tomorrow."
    show yuri at thide zorder 1
    show natsuki at thide zorder 1
    show monika at t11 zorder 2
    hide yuri
    hide natsuki
    m 3b "Okay, everyone!"
    m "I think with that, we can officially end today's meeting on a good note."
    m "Everyone remember tonight's assignment:"
    m "Write a poem to bring to the next meeting, so we can all share!"
    "Monika looks over at me once more."
    if persistent.accepts_invite:
        "She looks even happier than before."
        "The fact that I joined her club without any hesitation."
        "I guess I'll smile back?"
    m 1a "[player], I look forward to seeing how you express yourself."
    show monika 5 at hop
    m "Ehehe~"
    "Did she just jump?"
    if persistent.accepts_invite:
        mc "Yeah, sure. Looking forward to it."
    else:
        if persistent.ggwp_monika == 3:
            "I just keep my mouth shut."
            "I think I messed up \"that\" part."
        if persistent.mc_violent:
            "I thought Monika would know that I broke the game."
        mc "Y-Yeah..."
    show monika at thide zorder 1
    hide monika
    #"Can I really impress the class star Monika with my mediocre writing skills?"
    #"I already feel the anxiety welling up inside me."
    "Wow, how far am I going to tag along with her?"
    if persistent.mc_violent:
        "I need a plan... {w}Maybe I can do something {i}epic{/i} after school."
        "Throwing a chair is not enough I guess."
    else:
        "I need a plan... {w}I'll do some thinking after school."
    if persistent.poster_seen:
        "I just don't want to see that poster again..."
    "In that case, I'll use your 'save n load game' power to achieve this!"
    if persistent.ggwp_monika == 3:
        "Also, I should try not to make things even more obvious when I mess things up."
    "Meanwhile, the girls continue to chit-chat as Yuri cleans up the tea set."
    if persistent.accepts_invite:
        mc "Alright, Monika."
        mc "See you tomorrow."
    else:
        mc "I guess I'll be on my way, then..."
    show monika 5a at t11 zorder 2
    m "Okay!"
    if persistent.accepts_invite:
        m "I'll see you tomorrow too, then."
    else:
        m "I'll see you tomorrow, then."
    m "I can't wait!"
    if persistent.ggwp_monika == 3:
        "..."

    scene bg residential_day
    with wipeleft_scene

    "With that, I depart the clubroom and make my way home."
    "The whole way, my mind wanders back and forth between the three girls:"
    show natsuki 4a at t31 zorder 2
    "Natsuki,"
    show yuri 1a at t32 zorder 2
    "Yuri,"
    show monika 1a at t33 zorder 2
    "and, of course, Monika."
    "Will I really be happy spending every day after school in a literature club?"
    hide natsuki
    hide yuri
    hide monika
    with wipeleft
    stop music
    "Probably not, but I said it anyway."
    #"I'll just need to make the most of my circumstances, and I'm sure good fortune will find me."
    #"And I guess that starts with writing a poem tonight..."
    "Thats enough. Its time to stop pretending to be an asshole."
    "Now it's time to act."
    
    ### Another choice won't hurt ###
    menu:
        "What should I do?"
        # This actually reminds me of Hello Neighbor
        "Say hello to my neighbor":
            jump hello_neighbor
        "Go home and read PG" if persistent.parfait_girls:
            "Hmm. I guess I can read Parfait Girls."
            "It looks kind of interesting.."
            "I guess I could share this to Natsuki later."
            "I wonder if this suits her..."
            if persistent.mc_violent:
                "Ugh, I thought I wanted to be hero once in a while."
            "In the meantime, I should write my poem tonight."
            "I'm already used to it, so I think I can handle this."
            "Okay, let's do this!"
            jump mod_end_demo
        "Go home" if not persistent.parfait_girls:
            if persistent.mc_violent:
                "Ugh, I thought I wanted to be hero once in a while."
            "I guess I'll go home and do nothing."
            "I mean technically I should write my poem tonight."
            "I'm already used to it, so I think I can handle this."
            "Okay, let's do this!"
            jump mod_end_demo
