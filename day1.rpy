label ch_mod_1a:
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

    $ s_name = glitchtext(12)
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
    $ persistent.anticheat = renpy.random.randint(100000, 999999) # why not
    $ anticheat = persistent.anticheat

    $ del _history_list[0:]
    scene bg residential_day
    with dissolve_scene_half
    play music t2
    jump ch_mod_1

label ch_mod_1b:
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full
    play music t2
    jump ch_mod_1

label ch_mod_1:
    "It's an ordinary school day, like any other."
    "Mornings are usually the worst, being surrounded by couples and friend groups walking to school together."
    "Meanwhile, I've always walked to school alone.{nw}"
    $ currentpos = get_pos()
    stop music
    window hide(None)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    stop sound
    hide screen tear
    window show(None)
    mc "Argh...!"
    mc "What the he-{nw}"
    mc "Eh?"
    "What the heck?"
    "I felt, weird... just now."
    "What's going on?"
    mc "I feel... {w}uncomfortable.."
    mc "I feel like my body just woke up for some reason..."
    mc "Huh..."
    $ del _history_list[-9:]
    "Probably nothing, I guess.."
    "Well, "
    $ _history_list.pop()
    $ audio.t2 = "<from " + str(currentpos) + " loop 4.499>bgm/2.ogg"
    play music t2
    "Well, {fast}going to school isn't really bad at all."
    "I always tell myself it's about time I meet some girls or something like that..."
    "But I have no motivation to join any clubs."
    "After all, I'm perfectly content just getting by on the average while spending my free time on games and anime."
    window auto

    scene bg class_day
    with wipeleft_scene

    "The school day is as ordinary as ever, and it's over before I know it."
    "After I pack up my things, I stare blankly at the wall, looking for an ounce of motivation."
    mc "Clubs..."
    "There really aren't any that interest me."
    "Besides, most of them would probably be way too demanding for me to want to deal with."
    "I guess I have no choice but to start with the anime club..."
    if not config.skipping: # oops... skipping this dialogue is the safest way to heaven
        $ currentpos = get_pos()
        stop music
        $ quick_menu = False
        $ config.keymap['dismiss'] = []
        $ renpy.display.behavior.clear_keymap_cache()
        #$ config.allow_skipping = False
        $ mcrp = player # temp fix
        mcrp "\"What the hell is that?!\"{w=1.0}{nw}"
        "{cps=*1.5}The \"thing\" started to approach me.{/cps}{w=0.5}{nw}"
        "{cps=*1.5}I didn't recognize that distorted mess of an entity.{/cps}{w=0.5}{nw}"
        "{cps=*1.5}It's getting closer and closer now...{/cps}{w=0.5}{nw}"
        "{cps=*1.5}Ah, what is happening to this world?!!?!{/cps}{w=0.2}{nw}"
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
        $ config.keymap['dismiss'] = dismiss_keys
        $ renpy.display.behavior.clear_keymap_cache()
        $ quick_menu = True
        $ style.say_dialogue = style.normal
        $ del _history_list [-7:]
        $ audio.t2 = "<from " + str(currentpos) + " loop 4.499>bgm/2.ogg"
        play music t2
        $ gg_skip = False
    if config.skipping:
        $ config.skipping = False
        $ allow_skipping = False
        $ config.allow_skipping = False
        $ gg_skip = True
    $ m_name = "???"
    show monika 1a at t11 zorder 2
    m "...[player]?"
    $ m_name= "Monika"
    m 1b "Oh my goodness, I totally didn't expect to see you here!"
    m 5 "It's been a while, right?"
    mc "Ah..."
    if not gg_skip:
        "What did I just witness?"
    else:
        # suprise motherfcker
        "Can I skip over this stuff at this point?"
        "It infuriates me."
        $ del _history_list [-2:]
        "Wait, what am I talking about?"
        $ config.allow_skipping = True
        $ allow_skipping = True
    $ _history_list.pop()
    mc "Yeah, it has."
    "Monika smiles sweetly."
    "We do know each other - well, we rarely talked, but we were in the same class last year."
    #"Monika was probably the most popular girl in class - smart, beautiful, athletic."
    #"Basically, completely out of my league."
    #"So, having her smile at me so genuinely feels a little..."
    "Wait, what?"
    "I feel like I met her here not long ago..."
    "What is happening to my head right now?"
    mc "What did you come in here for, anyway?"
    m 1a "Oh, I've just been looking for some supplies to use for my club."
    m 1d "Do you know if there's any construction paper in here?"
    m "Or markers?"
    mc "I guess you could check the closet."
    mc "...You're in the literature {nw}"
    $ _history_list.pop()
    $ style.say_dialogue = style.edited
    mc "...You're in the literature {fast}club, right?{nw}"
    $ _history_list.pop()
    window hide(None)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    stop sound
    hide screen tear
    window show(None)
    $ style.say_dialogue = style.normal
    mc "...You're in the debate club, right?{fast}"
    "Ah, what did I just say?"
    m 5 "Ahaha, about that..."
    m "I actually quit the debate club."
    mc "Really? You quit...?"
    m "Yeah..."
    m 2e "To be honest, I can't stand all of the politics around the major clubs."
    m "It feels like nothing but arguing about the budget and publicity and how to prepare for events..."
    m "I'd much rather take something I personally enjoy and make something special out of it."
    mc "In that case, what club did you decide to join?"
    m 1b "Actually, I'm starting a new one!"
    m "A literature club!"
    mc "Literature...?"
    pause 1.0
    mc "How many members do you have so far?"
    m "Ahaha..."
    m "It's kind of embarrassing, but there are only three of us so far."
    m "It's really hard to find new members for something that sounds so boring..."
    mc "Well, I can see that..."
    "Why do I feel like my wrath has been growing since Monika showed up?"
    $ _history_list.pop()
    m 3d "But it's really not boring at all, you know!"
    m "Literature can be anything. Reading, writing, poetry.."
    m 3e "I mean, one of my members even keeps her manga collection in the clubroom..."
    "Have I heard this conversation before?"
    mc "Wait...really?"
    m 2k "Yeah, it's funny, right?"
    m 2e "She always insists that manga is literature, too."
    m "I mean, she's not wrong, I guess..."
    m "And besides, a member's a member, right?"
    #"...Did Monika say \"she\"?"
    #"Hmm..."
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
    "Well, I guess I have no reason to ref-{nw}"
    $ _history_list.pop()
    window hide(None)
    menu:
        "Visit her club":
            pass
        "Don't visit her club":
            pass
    window show(None)
    "Well, I guess I have no reason to ref{fast}use."
    "Eh? What was that?"
    mc "Sure, I guess I could check it out."
    m 1k "Aah, awesome!"
    m 1b "You're really sweet, [player], you know that?"
    m 1a "Shall we go, then?"
    m "I'll look for the materials another time - you're more important."
    show monika at thide zorder 1
    hide monika
    "I'm more important?"
    "Why do I feel like I'm being betrayed instead?"
    "For some reason, it actually infuriates me."
    "I can't even understand my own feelings right now..."
    "I wonder if this is how Sayori felt..."
    "Wait, who is Sayo{nw}"
    $ del _history_list [-6:]
    stop music
    window hide(None)
    window auto
    scene black with trueblack
    pause 1.0

    scene bg corridor
    with wipeleft_scene

    "And thus, today marks the day I {i}sold my soul{/i} to Monika and her irresistible smile."
    "I timidly follow Monika across the school and upstairs - a section of the school I rarely visit, being generally used for third-year classes and activities."
    "Monika, full of energy, swings open the classroom door."

    if renpy.random.randint(0, 5) == 0: ### 16.66% chance 
        scene bg spoopy
        $ seen_day += 1
    else:
        scene bg club_day
    with wipeleft
    play music t3

    if renpy.random.randint(0, 2) == 0: ### 33.33% chance
        show monika g1 at l31
        $ monika_glitch = True
    else:
        show monika 3b at l31
        $ monika_glitch = False

    m "I'm back~!"
    m "And I brought a guest with me!"
    if monika_glitch:
        "What the heck did I just see?"
        if renpy.showing("bg spoopy", layer='master'):
            "And what's with the poster on the back wall of the clubroom!?"
            "Why do I feel like something terrible is going to happen...?"
    elif renpy.showing("bg spoopy", layer='master'):
        "What's that poster on the back wall of the clubroom!?"
        "Why do I feel like something terrible is going to happen...?"
    show yuri 2t at t33 zorder 2
    if not config.skipping:
        show screen invert(0.15, 0.3)
    $ y_name = "Girl 1"
    y "Eh?"
    y "A...a guest?"
    show natsuki 4c at t32 zorder 2
    $ n_name = "Girl 2"
    n "Seriously? You brought a boy?"
    n "Way to kill the atmosphere."
    mc "Excuse me!?"
    show monika 3m at f31 zorder 3
    m "Don't be mean, Natsuki..."
    m 3b "...But anyway, welcome to the club, [player]!"
    show monika 3a at t31 zorder 2
    mc "..."
    #"All words escape me in this situation."
    #"This club..."
    #"{i}...is full of incredibly cute girls!!{/i}"
    "Hmm..."
    "I guess this club is alright..."
    "Why do I feel empty seeing their cute faces?"
    "I don't even understand my own feelings."
    show natsuki at f32 zorder 3
    n 5c "So, let me guess..."
    n "You're Monika's boyfriend, right?"
    mc "W-What?"
    mc "What gives you that idea?"
    show natsuki at t32 zorder 2
    show yuri at f33 zorder 3
    y 2l "Natsuki..."
    show yuri at t33 zorder 2
    $ n_name = 'Natsuki'
    "The girl with the sour attitude, whose name is apparently Natsuki, is one I don't recognize."
    "Her small figure makes me think she's probably a first-year."
    "Wait, I should've introduced you when Monika said \"Don't be mean, Natsuki...\""
    $ _history_list.pop()
    "What am I talking about?"
    $ _history_list.pop()
    show monika at f31 zorder 3
    m 2l "A-Anyway, this is Natsuki, energetic as usual..."
    m 2b "And this is Yuri, the Vice President!"
    $ y_name = 'Yuri'
    show monika 2a at t31 zorder 2
    show yuri at f33 zorder 3
    y 4 "I-It's nice to meet you..."
    "Yuri, who appears comparably more mature and timid, seems to have a hard time keeping up with someone like Natsuki."
    show monika at t31 zorder 2
    show natsuki at f32 zorder 3
    n 4e "Wait! Monika!"
    n "Didn't I tell you to let me know in advance before bringing anyone new?"
    n 4q "I was going to...well, you know..."
    show natsuki at t32 zorder 2
    show monika at f31 zorder 3
    m 1e "Sorry, sorry!"
    m "I didn't forget that, but I just happened to run into him."
    show monika at t31 zorder 2
    show yuri at f33 zorder 3
    y 1a "In that case, I should at least make some tea, right?"
    show yuri at t33 zorder 2
    mc "Ah, thanks?"
    show monika at f31 zorder 3
    m 1b "Yeah, that would be great!"
    m "Why don't you come sit down, [player]?"
    mc "Sure..."
    hide monika
    hide natsuki
    hide yuri
    with wipeleft

    "The girls have a few desks arranged to form a table."
    "Yuri walks to the corner of the room and opens the closet."
    "Meanwhile, Monika and Natsuki sit across {nw}"
    $ _history_list.pop()
    window hide(None)
    menu:
        "Sit next to Monika":
            $ isit = False
        "Sit next to Natsuki":
            $ isit = True
    window show(None)
    "Meanwhile, Monika and Natsuki sit across {fast}from each other."
    "I take a seat next to Monika."
    if isit:
        "I don't know why, but I feel like I should sit next to Natsuki instead..."
    show monika 1a at t11 zorder 2
    m "So, I know you didn't really plan on coming here..."
    m "But we'll make sure you feel right at home, okay?"
    m 1j "As president of the Literature Club, it's my duty to make the club fun and exciting for everyone!"
    mc "I'm surprised there aren't more people in the club yet."
    mc "It must be hard to start a new club."
    m 3b "You could put it that way."
    m "Not many people are very interested in putting out all the effort to start something brand new..."
    m "Especially when it's something that doesn't grab your attention, like literature."
    m "You have to work hard to convince people that you're both fun and worthwhile."
    m "But it makes school events, like the festival, that much more important."
    "The festival? I don't really know much about what a literature club is supposed to do in the festival."
    "And I don't see how well it could go, either..."
    m 2k "We'll figure that out soon enough, I'm confident that we can all really grow this club before we graduate!"
    m "Right, Natsuki?"
    show monika at t22 zorder 2
    show natsuki 4q at t21 zorder 2
    n "Well..."
    n "...I guess."
    "Natsuki reluctantly agrees."
    #"Such different girls, all interested in the same goal..."
    "Well, I guess literature isn't really that hard."
    "Despite it being kind of dull, it's worth it to make a poem, share it with your friends and to find inspiration from other people."
    "The basic fundamentals of literature is to express yourself."
    "I don't know, I feel like I've done this before."
    "Yuri returns to the table, carrying a tea set."
    "She carefully places a teacup in front of each of us before setting down the teapot in the middle."
    show natsuki at thide zorder 1
    show monika at thide zorder 1
    hide natsuki
    hide monika
    show yuri 1a at t21 zorder 2
    mc "You keep a whole tea set in this classroom?"
    y "Don't worry, the teachers gave us permission."
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
    "Considering how little I've read these past few years, I don't really have a good way of answering that."
    window hide(None)
    menu:
        "Manga":
            $ ihorror = False
        "Horror":
            window show(None)
            $ ihorror = True
            y 1e "Oh?"
            "Yuri looks at me with a suprised expression."
            y 1a "What did you say?"
            mc "Uh..."
            window hide(None)
            $ del _history_list[-4:]
    $ currentpos = get_pos()
    stop music
    play sound aglitch1
    pause 0.5
    stop sound
    $ audio.t3 = "<from " + str(currentpos) + " loop 4.618>bgm/3.ogg"
    play music t3
    #mc "...Manga..."
    #"I mutter quietly to myself, half-joking."
    #"Natsuki's head suddenly perks up for some reason."
    #"It looks like she wants to say something, but she keeps quiet."
    #show natsuki at thide zorder 1
    #hide natsuki
    window show(None)
    y 3u "N-Not much of a reader, I guess..."
    "What was that about?"
    mc "Ah..."
    mc "Don't say that, you're making it sound like a big deal or something."
    "I say that because of Yuri's sad smile."
    "It's up to me to save this situation."
    mc "I do like reading sometimes."
    mc "If there's any book that promotes an interesting stories, then I usually enjoy reading it."
    y 3v "I see..."
    "Somehow I relieved her a little bit."
    mc "Anyway, what about you, Yuri?"
    "I'm confused when I say \"you\" and \"Yuri\" at the same time."
    $ _history_list.pop()
    "What kind of language am I speaking right now?"
    $ _history_list.pop()
    y 1l "Well, let's see..."
    #"Yuri traces the rim of her teacup with her finger."
    y 1a "My favorites are usually novels that build deep and complex fantasy worlds."
    y "The level of creativity and craftsmanship behind them is amazing to me."
    y 1f "And telling a good story in such a foreign world is equally impressive."
    "She is clearly passionate about her reading."
    "Even though she has an exquisite appearance, I can already tell that she's most comfortable in the fantasy worlds that books bring, not with regular people."
    "I would think she is not really into social-interaction, but maybe she is?"
    #"Yuri goes on, clearly passionate about her reading."
    #"She seemed so reserved and timid since the moment I walked in, but it's obvious by the way her eyes light up that she finds her comfort in the world of books as I imagined, not people."
    y 2m "But you know, I like a lot of things."
    y "Stories with deep psychological elements usually immerse me as well."
    y 2a "Isn't it amazing how a writer can so deliberately take advantage of your own lack of imagination to completely throw you for a loop?"
    if monika_glitch or renpy.showing("bg spoopy", layer='master'):
        "Ah... I would think the same way in this current situation."
    y "Anyway, I've been reading a lot of horror lately..."
    mc "Really? I read a horror book once."
    if ihorror:
        "I thought I said before that I like horror...?"
        "What is happening right now?!"
    else:
        "Or twice..."
        "Either way, horror can be interesting..."
    #"I desperately grasp something I can relate to at the minimal level."
    #"At this rate, Yuri might as well be having a conversation with a rock."
    show monika 1j at f33 zorder 3
    m "Ahaha. I'd expect that from you, Yuri."
    m 1a "It suits your personality."
    "Something seems fishy about this conversation."
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
    show yuri at t32 zorder 2
    show natsuki at f31 zorder 3
    n 5c "Well, I just..."
    "Natsuki's eyes dart over to me for a split second."
    mc "Huh?"
    n 5q "Never mind."
    show natsuki at t31 zorder 2
    show monika at f33 zorder 3
    m 1a "That's right, you usually like to write about cute things, don't you, Natsuki?"
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
    "I think everyone writes their own poems at least once or twice."
    "I may have also written poems before."
    "I wonder what her latest poem is..."
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
    mc "I guess you just need more confidence to share with someone.."
    #mc "Ah...not a very confident writer yet?"
    show yuri at f32 zorder 3
    y 2f "I understand how Natsuki feels."
    y "Sharing that level of writing takes more than just confidence."
    y 2k "The truest form of writing is writing to oneself."
    y "You must be willing to open up to your readers, exposing your vulnerabilities and showing even the deepest reaches of your heart."
    mc "So you're basically saying that language itself is very important for making poems?"
    y 1b "Yes. It's like an artist painting beautiful pictures for everyone to see."
    y "People value the artist because of more than just a picture that they paint."
    "Huh? I didn't know Yuri likes pictures."
    "I thought I've heard that before from Sayo-{nw}"
    $ _history_list.pop()
    window hide(None)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    stop sound
    hide screen tear
    window show(None)
    mc "I see.."
    show yuri at t32 zorder 2
    show monika 2a at f33 zorder 3
    m "Do you have writing experience too, Yuri?"
    m "Maybe if you share some of your work, you can set an example and help Natsuki feel comfortable enough to share hers."
    show yuri at s32
    y 3o "..."
    mc "Well, I guess it's the same for Yuri..."
    "We all sit in silence for a moment."
    "I stare at the desk, trying to understand the painful thoughts inside my head."
    "I feel like I should admit it to everyone, but my anxious feelings and fear stop me from speaking my mind about it."
    show monika at f33 zorder 3
    m 5a "Hey, I just got an idea!"
    m "How about this?"
    show monika at t33 zorder 2
    show natsuki 2k at f31 zorder 3
    show yuri 3e at f32 zorder 3
    ny "...?"
    "Natsuki and Yuri look quizzically at Monika."
    "I guess I should look at Monika, too."
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
    show monika 2m at f33 zorder 3
    m "Ah..."
    m "I mean, I thought it was a good idea..."
    show monika at t33 zorder 2
    show yuri at f32 zorder 3
    y 2l "Well..."
    y "...I think you're right, Monika."
    y 2f "We should probably start finding activities for all of us to participate in together."
    y 2h "I did decide to take on the responsibility of Vice President, after all..."
    y "I need to do my best to nurture the club as well as its members."
    y 2a "Besides, now that we have a new member..."
    y "It seems like a good step for us to take."
    y "Do you agree as well, [player]?"
    show yuri at t32 zorder 2
    if monika_glitch or renpy.showing("bg spoopy", layer='master'):
        "What the heck is going on!? My head is getting crazy!"
        "Things are getting weirder and weirder."
    $ mcrp = player # temp fix
    mc "Well, uh...?"
    $ _history_list.pop()
    menu:
        mcrp "\"Well, uh...?\"{fast}"
        "Accept their invitation":
            $ accepts_invite = True
            call mod_ch1_accepts
        "Reject their invitation":
            $ accepts_invite = False
            call mod_ch1_rejects
    show monika at f33 zorder 3
    m "I'll do everything I can to give you a great time, okay?"
    if accepts_invite:
        mc "Ah. Alright then..."
    else:
        mc "Ah...thanks, I guess...?"
    if monika_glitch or renpy.showing("bg spoopy", layer='master'):
        "I feel like something's off."
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
    if accepts_invite:
        "She looks even happier than before."
        "The fact that I joined her club without any hesitation."
        "I guess I'll smile back?"
    m 1a "[player], I look forward to seeing how you express yourself."
    show monika 5 at hop
    m "Ehehe~"
    "Did she just jump?"
    "Her ecstatic seems to be overflowing inside her head."
    if accepts_invite:
        "But I begin to understand that it is hard to get a new member. So..."
        mc "Yeah, sure. Looking forward to it."
    else:
        "I don't know what makes her do that..."
        mc "Y-Yeah..."
    show monika at thide zorder 1
    hide monika
    #"Can I really impress the class star Monika with my mediocre writing skills?"
    #"I already feel the anxiety welling up inside me."
    "Should I really impress the class star Monika my mediocre writing skills?"
    "I feel my wrath is growing even faster than before..."
    "What's going on?"
    "Meanwhile, the girls continue to chit-chat as Yuri cleans up the tea set."
    if accepts_invite:
        mc "Alright, Monika."
        mc "See you tomorrow."
    else:
        mc "I guess I'll be on my way, then..."
    show monika 5a at t11 zorder 2
    m "Okay!"
    if accepts_invite:
        m "I'll see you tomorrow too, then~!"
    else:
        m "I'll see you tomorrow."
    m "I can't wait~!"
    
    scene bg residential_day
    with wipeleft_scene
    window auto

    "With that, I depart the clubroom and make my way home."
    "The whole way, my mind wanders{nw}"
    window show(None)
    $ currentpos = get_pos()
    stop music
    $ audio.t3 = "<from " + str(currentpos) + " loop 4.618>bgm/3.ogg"
    $ audio.t3l = "<from " + str(currentpos) + " loop 4.618>mod_assets/sfx/3l.ogg" 
    play music t3l
    scene bg res_gl
    "The whole way, my mind wanders{fast} back and forth between the three girls:"
    window auto
    show natsuki 4a at t31 zorder 2
    "Natsuki,"
    show yuri 1a at t32 zorder 2
    "Yuri,"
    show monika 1a at t33 zorder 2
    "and, of course, {w}Monika.{nw}"
    scene bg residential_day
    "Will I really be hap{nw}"
    $ style.say_dialogue = style.edited
    "Will I really be hap{fast}py spending every day after school in a literature club?"
    "Perhaps I'll have the chance to grow closer to one of these girls..."
    hide natsuki
    hide yuri
    hide monika
    with wipeleft
    $ style.say_dialogue = style.normal
    stop music
    play music t3
    "Alright!"
    "I'll just need to make the most of my circumstances, and I'm sure good fortune will find me."
    "And I guess that starts with writing a poem tonight..."

    stop music fadeout 2.0
    scene black with dissolve_scene_full
    $ config.skipping = False
    $ config.allow_skipping = False
    $ allow_skipping = False

    # its a joke, pls dont kill me
    $ gtext = glitchtext(31)
    call screen confirm("This mod has profanity filter mode.\nDo you want to enable it?", Return(True), Return(False))
    if _return:
        $ persistent.protecc = True
        $ renpy.call_screen("dialog", "Profanity filter is enabled.", ok_action=Return())
    else:
        $ persistent.protecc = False
        $ renpy.call_screen("dialog", "[gtext]", ok_action=Return())
    return

label mod_ch1_accepts:
    mc "Yeah.."
    mc "I mean it could be fun, right?"
    mc "Sharing our poems with each other..."
    show monika 1d at f33 zorder 3
    "Monika looks at me quizzically"
    m "Wait, [player]?"
    mc "Yes?"
    $ quick_menu = False
    $ config.keymap['dismiss'] = []
    $ renpy.display.behavior.clear_keymap_cache()
    "She stares into my eyes for a good 3 seconds long{w=1.5}{nw}"
    $ config.keymap['dismiss'] = dismiss_keys
    $ renpy.display.behavior.clear_keymap_cache()
    $ quick_menu = True
    mc "Eh, I mean..."
    mc "You know...."
    m "You do?"
    m 1b "Oh my goodness!"
    m 5a "You really mean it, don't you?"
    "Monika smiles sweetly."
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
    n 5e "You would be a complete jerk if you did that. Not join, that is."
    mc "Yeah, yeah."
    show natsuki 5a at t31 zorder 2
    show yuri 1a at f32 zorder 3
    y "That is a wise decision."
    y 3m "I am so happy that you joined our club before the festival..."
    show yuri at t32 zorder 2
    mc "Ah, thank you."
    mc "It was my own choice after all"
    "I hope she's okay with me here."
    "Though I'm kind of worried that she might be {i}her{/i} next target."
    "Wait, what am I talking about?"
    $ del _history_list[-2:]
    return

label mod_ch1_rejects:
    mc "Hold on...there's still one problem."
    show monika at f33 zorder 3
    m 1d "Eh? What's that?"
    show monika at t33 zorder 2
    mc "I never said I would join this club!"
    mc "Monika may have convinced me to stop by, but I never made any decision."
    mc "I still have other clubs to look at, and...um..."
    show monika 1g
    show natsuki 4g
    show yuri 2e
    #"I lose my train of thought."
    #"All three girls stare back at me with dejected eyes."
    "I don't know why, but I feel kind of guilty after seeing their dejected eyes."
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
    "I feel like I'm defenseless against these girls."
    "Why am I being indecisive all the time?"
    "Not to mention my best friend..."
    $ _history_list.pop()
    "Wait, who is my best friend?"
    $ _history_list.pop()
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
    if renpy.showing("bg spoopy", layer='master'):
        "Yeah, the back of the classroom is even scarier than me."
        "Haven't they even noticed? {i}How{/i}?"
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
