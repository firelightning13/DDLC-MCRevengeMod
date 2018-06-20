### possible outcomes after exclusive scene (my footnote):
# persistent.ggwp_monika = 4, secret message from yuri/natsuki's glitch; 3, post-glitched yuri when choosing "abs/bs" poem;
# persistent.ggwp_monika = 2, post-game crashed when seeing poster/throws chair/mc's realization; 0, nothing happens other than 1-4;
# persistent.tea_set, mc noticed tea set inside his classroom's closet
# persistent.parfait_girls, mc got parfait girls from his classroom's closet and didnt read(if yuri's route)/already read(if natsuki's route)
# persistent.natsuki_glitch = 5, natsuki shuts down and monika fed her; 6, natsuki seeks "health check" in infirmary.
# persistent.natsuki_glitch = 4, natsuki seeks "health check" in infirmary, if skipping once (not loading from previous saved point)
# persistent.protecc, if players enabled profanity filter
# isit, mc wants to sit with monika; ihorror, mc's interest in horror theme (both in day one)
# accepts_invite, mc indirectly accepted monika's invitation
# persistent.cheat_mod, how many times player cheats
# persistent.mc_realise, uses english(uk) instead of english(us), mc's realise after yuri's glitched out
# natsuki_out, if natsuki went to infirmary with monika, depends on persistent.natsuki_glitch
# persistent.screen_glitch = 1, if player load again from day one, either normal poem game if "cute"/"mp", or glitched out if "abs"/"bs"

label mod_poemresponse:
    #################################################### RESPONSE LOGIC/CALCULATION #########################################################
    ### basically how to calculate "like" points threshold for poem responses in lazy and dirty way (completely different from original game)
    ### this "like" points calculated based on choice that you make in day one and day two
    ### parfait_girls and persistent.tea_set doesn't affect any points by the way... (or else it would unfair for players)
    ### normal poem game doesn't have much of an affect on any points though... (if player tends to play "poem game" again on day one)
    ### will probably change when im working on day three/four scene in the next full/beta/demo/experimental release (which i havnt plan yet)

    # initialize point system
    # 0 = bad; 1 = med ; 2 or 3 = good
    # right now, mod_mpoints is unusable atm

    $ mod_ypoints = 0
    $ mod_npoints = 0
    $ mod_mpoints = 0

    if ihorror:
        $ mod_ypoints = 1
    else:
        $ mod_npoints = 1
    if isit:
        $ mod_npoints = 1
    else:
        $ mod_mpoints = 1
    if accepts_invite:
        $ mod_mpoints = 1

    if poetappeal == "cute":
        $ mod_npoints += 2
    elif poetappeal == "mp":
        $ mod_ypoints += 2
    elif poetappeal == "abs":
        $ mod_mpoints += 2
        $ mod_ypoints = 2
    elif poetappeal == "bs":
        $ mod_npoints = 2
        $ mod_mpoints = 2
        $ mod_ypoints = 1

    #########################################################################################################################################

    ### most codes here are from original scripts from DDLC, except a few tweaks for my mod to work
    $ poemsread = 0
    label mod_poemresponse_loop:
        $ skip_poem = False
        if renpy.music.get_playing() and not (renpy.music.get_playing() == audio.t5 or renpy.music.get_playing() == audio.t5c):
            $ renpy.music.play(audio.t5, fadeout=1.0, if_changed=True)
        scene bg club_day
        with wipeleft_scene
        if not renpy.music.get_playing():
            play music t5
        if poemsread == 0:
            $ menutext = "Whom should I show my poem to first?"
        else:
            $ menutext = "Whom should I show my poem to next?"

        menu:
            "[menutext]"

            "Natsuki" if not n_readpoem and not natsuki_out:
                $ n_readpoem = True
                if mod_chapter == 1 and poemsread == 0: #Show a special comment if picked for very first poem
                    if persistent.natsuki_glitch >= 5: # from natsuki exclusive scene
                        "I'm not sure what had happened before between Natsuki and Monika..."
                        "This game is pretty much broken at this p{nw}"
                        $ _history_list.pop()
                        scene black
                        pause 0.1
                    elif persistent.ggwp_monika == 4 and poetappeal == "mp": # from yuri exclusive scene (oof Natsuki)
                        "{cps=50}dskfgsfjgsdkfjsg{nw}{/cps}"
                        $ _history_list[-1].what = "I told Natsuki I was interested in her poems yesterday."
                        "{cps=50}oiasdhosdiasdisadaodk{nw}{/cps}"
                        $ _history_list[-1].what = "It's probably only fair if I shared mine with her first."
                        "{cps=100}mosadiondeyyeyeeyeyeeyeyeeyeyeyeyyeyeyey{/cps}{nw}"
                        $ _history_list[-1].what = "eye  can   c    u   .. / .-.. --- ...- . / -.-- --- ..-" # it's a morse code, feel free to translate it
                    elif persistent.ggwp_monika > 0: # if none of the above happened
                        "I'm not sure what is happening in this world..."
                        "I hope that sharing with Natsuki would ease my mind from such a messy world that I'm in."
                    else: # which never happens, hypothetically
                        "I told Natsuki I was interested in her poems yesterday."
                        "It's probably only fair if I shared mine with her first."
                call mod_poemresponse_natsuki
            "Yuri" if not y_readpoem and not y_ranaway:
                $ y_readpoem = True
                if mod_chapter == 1 and poemsread == 0: #Show a special comment if picked for very first poem
                    if poetappeal == "mp" or poetappeal == "abs": # from yuri exclusive scene
                        "Not sure why my mind is racing when I decided to share my poems with her..."
                        "Is it because that I'm afraid that something terrible will happened to her?"
                    elif persistent.ggwp_monika == 3 and poetappeal == "bs": # from "before" natsuki exclusive scene shows up
                        "I still don't know what's up between me and Yuri recently..."
                        "I think I should ask her about it-{nw}"
                        $ _history_list.pop()
                        scene black
                        pause 0.1
                    elif persistent.ggwp_monika > 0: # if none of the above happened
                        "I'm not sure what is happening in this world..."
                        "I hope that sharing with Yuri would ease my mind from such a messy world that I'm in."
                    else: # which never happens, hypothetically
                        "Yuri seems the most experienced, so I should start with her."
                        "I can trust her opinion to be fair."
                call mod_poemresponse_yuri
            "Monika" if not m_readpoem:
                $ m_readpoem = True
                if mod_chapter == 1 and poemsread == 0: #Show a special comment if picked for very first poem
                    if persistent.natsuki_glitch == 6 and not natsuki_out: # if glitch happens after mc breaks the system
                        "I wonder how she is acting so innocent the whole time, but I reckon that she is the evil mastermind around here."
                        "I feel like I shouldn't trust her..."
                    elif persistent.ggwp_monika > 0: # if glitch didnt happened like above
                        "I'm not sure what is happening in this world, but I reckon that she knows everything."
                        if poetappeal == "abs": # a serious discussion (refer to label m_abs_1 and monika_special_1_end)
                            "Maybe I should try discuss this matter with her."
                        else: # not really a serious discussion
                            "I feel like I shouldn't trust her..."
                    else: # this would happen theoretically, not sure how to trigger this, but is there any actually way to do this?
                        "I should start with Monika."
                        "Yesterday she seemed eager to read my poem, and I want her to know I'm putting in effort."
                call mod_poemresponse_monika
        #Increment poem count, then loop back if there's still more to read
        $ poemsread += 1
        if poemsread < 3:
            jump mod_poemresponse_loop

    # Reset variables for next time
    $ n_readpoem = False
    $ y_readpoem = False
    $ m_readpoem = False
    $ poemsread = 0
    return

label mod_poemresponse_natsuki:
    scene bg club_day
    show natsuki 1c at t11 zorder 2
    with wipeleft_scene
    $ preferences.skip_unseen = True
    if mod_npoints >= 2:
        $ poetopinion = "good"
    elif mod_npoints == 1:
        $ poetopinion = "med"
    elif mod_npoints == 0:
        $ poetopinion = "bad"
    $ nextscene = "mod_ch" + str(mod_chapter) + "_n_" + poetopinion
    # $ nextscene = "natsuki_special_" + str(mod_chapter) # temporary
    call expression nextscene
    $ nextscene = "mod_ch" + str(mod_chapter) + "_n_end"
    call expression nextscene
    if config.skipping:
        $ mc_boring = True
    $ preferences.skip_unseen = False
    return

label mod_poemresponse_yuri:
    scene bg club_day
    show yuri 1a at t11 zorder 2
    with wipeleft_scene
    $ preferences.skip_unseen = True
    if mod_ypoints >= 2:
        $ poetopinion = "good"
    elif mod_ypoints == 1:
        $ poetopinion = "med"
    elif mod_ypoints == 0:
        $ poetopinion = "bad"
    $ nextscene = "mod_ch" + str(mod_chapter) + "_y_" + poetopinion
    call expression nextscene
    $ nextscene = "mod_ch" + str(mod_chapter) + "_y_end"
    call expression nextscene
    if config.skipping:
        $ mc_boring = True
    $ preferences.skip_unseen = False
    return

label mod_poemresponse_monika:
    if persistent.monika_secret[0]: # you should refer to label monika_special_1_end
        window show(None)
        stop music
        play sound sgl
        pause 1.0
        stop sound
        scene black
        pause 0.1
        return # returns to mod_poemresponse_loop or going to the next scene, skips the rest of the code below
    scene bg club_day
    show monika 1a at t11 zorder 2
    with wipeleft_scene
    if mod_mpoints >= 2:
        $ poetopinion = "good"
    elif mod_mpoints == 1:
        $ poetopinion = "med"
    elif mod_mpoints == 0:
        $ poetopinion = "bad"
    $ nextscene = "mod_ch" + str(mod_chapter) + "_m_start"
    call expression nextscene
    if poetappeal == "abs":
        $ nextscene = "monika_special_" + str(mod_chapter) + "_end"
    else:
        $ nextscene = "mod_ch" + str(mod_chapter) + "_m_end"
    call expression nextscene
    return

## temporary code, will not use it forever
#label natsuki_special_1: # special case for natsuki
    #return

label mod_ch1_n_good:
    jump ch1_n_good # uses original script, as a placeholder

label mod_ch1_n_med:
    jump ch1_n_med # uses original script, as a placeholder

label mod_ch1_n_bad: # taken from original script, probably a placeholder, except minor changes
    n "..."
    mc "...?"
    $ eyeses = False
    if renpy.random.randint(0, 2) == 0: # 33.33% chance
        # natsuki's eyes popped out in act 2
        $ currentpos = get_pos()
        stop music
        pause 2.0
        play sound "sfx/stab.ogg"
        show n_blackeyes at i11 zorder 3
        show n_eye zorder 3:
            subpixel True
            pos (660,250) xanchor 0.5 yanchor 0.5 zoom 0.8
            parallel:
                linear 2.0 rotate 720
            parallel:
                linear 2.0 xpos 1680
            parallel:
                easein 0.25 ypos 180
                easeout 1.0 ypos 1280
        show n_eye as n_eye2 zorder 3:
            subpixel True
            pos (580,260) xanchor 0.5 yanchor 0.5 zoom 0.8 rotate 180
            parallel:
                linear 2.0 rotate -560
            parallel:
                linear 2.0 xpos -440
            parallel:
                easein 0.10 ypos 240
                easeout 1.0 ypos 1280
        show blood zorder 3:
            pos (645,255)
        show blood as blood2 zorder 3:
            pos (575,260)
        pause 0.4
        hide n_blackeyes
        hide n_eye
        hide n_eye2
        hide blood
        hide blood2
        stop sound
    ############################# minor changes ##################################
        play sound ggg
        window hide(None)
        show screen tear(8, offtimeMult=1, ontimeMult=10)
        pause 0.35
        stop sound
        hide screen tear
        window show(None)
        window auto
        play music "<from " + str(currentpos) + " loop 4.444>bgm/5.ogg"
        $ eyeses = True
    n 2b "[player], if you're not going to take this club seriously then go home."
    if eyeses:
        "What the heck just happened?"
        mc "Wait, what?"
    else:
        mc "W-What??"
    ##############################################################################
    mc "Harsh..."
    n 42c "What, you expect me to believe that you actually put effort into this?"
    n "Do you think I'm stupid?"
    mc "I'm not a writer!"
    mc "Maybe it's not very good, but yeah, I did put in effort."
    mc "We all start somewhere, right?"
    mc "If you're still proud of the first poem {i}you{/i} ever wrote, then I'd like to read it."
    n 1o "!!"
    mc "Painful to think about?"
    n 1r "..."
    n 5q "Fine."
    n "Well, sorry."
    n 5c "You'll get better, anyway."
    n "I'd tell you what to improve, but you're better off just trying again."
    mc "Fair enough..."
    mc "Well, to each their own, I guess."
    n 5q "Anyway, I guess I gotta share mine now..."
    n "Knowing you, you'll probably think it's stupid."
    return

label mod_ch1_y_good:
    $ poemopinion = "good"
    jump ch1_y_good # uses original script, as a placeholder

label mod_ch1_y_med:
    $ poemopinion = "med"
    jump ch1_y_med # uses original script, as a placeholder

label mod_ch1_y_bad:
    $ poemopinion = "bad"
    jump ch1_y_bad # uses original script, as a placeholder

label mod_ch1_n_end:
    jump ch1_n_end # uses original script, as a placeholder

label mod_ch1_y_end:
    jump ch1_y_end # uses original script, as a placeholder

label mod_ch1_m_start:
    m 1b "Hi, [player]!"
    m "Having a good time so far?"
    if poemsread > 0:
        if y_ranaway:
            "Why everything was normal when I shared my poem to Natsuki?"
        elif natsuki_out:
            "Why everything was normal when I shared my poem to Yuri?"
        else:
            "Why everything was normal when I shared my poem to Natsuki and Yuri?"
        "I never seen anything weird happening so far."
    elif persistent.natsuki_glitch == 6:
        "I don't think so, after what I had witnessed something unexpected recently..."
    elif persistent.ggwp_monika > 0:
        "How about no?"
    #mc "Ah...yeah."
    mc "Probably..."
    m 1k "Good! Glad to hear it!"
    m 4a "By the way, since you're new and everything..."
    m "If you ever have any suggestions for the club, like new activities, or things we can do better..."
    m 4b "I'm always listening!"
    m "Don't be afraid to bring things up, okay?"
    show monika 4a
    #mc "Alright...I'll keep that in mind."
    mc "I'll keep that in mind..."
    #"Of course I'll be afraid to bring things up."
    #"I'm much better off just going with the flow until I'm more settled in."
    "I'll definitely going to bring things up when the time comes."
    if persistent.ggwp_monika == 2 or persistent.natsuki_glitch == 6:
        "I am so tired from all of this bulls[sword]..."
    elif persistent.ggwp_monika == 4 or persistent.natsuki_glitch == 5:
        "I'll probably going to break things again..."
    m 1a "Anyway..."
    m "Want to share your poem with me?"
    mc "Eh, I guess I have to..."
    m 5a "Ahahaha!"
    m "Don't worry, [player]!"
    m "We're all a little embarrassed today, you know?"
    m "But it's that sort of barrier that we'll all learn to get past soon."
    mc "Yeah, I guess that's true."
    "Anyway, I hand Monika my poem."
    if poetappeal == "bs" or poetappeal == "abs":
        window show(None)
        pause 2.0
        window show(None)
        window auto
    m 2a "...Mhm!"
    $ nextscene = "m_" + poetappeal + "_1"
    call expression nextscene
    return

label m_cute_1:
    m 2b "I like it, [player]!"
    #mc "Really...?"
    mc "Really? How so?"
    m 2e "It's a lot cuter than I expected."
    m 2k "Ahahaha!"
    #mc "Oh jeez..."
    mc "..."
    m 1b "No, no!"
    m "It kind of makes me think of something Natsuki would write."
    m "And she's a good writer, too."
    m 5a "So take that as a compliment!"
    #mc "Ahaha..."
    mc "Yeah, if you say so..."
    m "Yep!"
    m 3b "If you're interested in Natsuki, then always keep a snack on you."
    m "She'll cling to you like a puppy."
    m 3k "Ahaha!"
    "What?"
    $ _history_list.pop()
    m 1a "Natsuki's dad doesn't give her lunch money or leave her any food in the house, so she's in a fussy mood pretty often..."
    m "But sometimes she just loses all of her strength and shuts down."
    if persistent.natsuki_glitch == 4:
        "What is she talking about?!"
        $ _history_list.pop()
    else:
        m "Like earlier."
        "That's... no good."
        $ _history_list.pop()
    m 2d "This is just a guess, but I think she's so small because her malnutrition is interfering with her adolescent growth..."
    m 2b "...But hey, some guys are into petite girls too, you know?"
    m 5a "Sorry...just trying to look at the bright side!"
    if natsuki_out:
        label natsuki_come_back: # this could be improved a little bit, not sure how
            pause 1.0
            "Suddenly, the door opens."
            m 2b "Natsuki!"
            show monika 2a
            show natsuki 5a at f31 zorder 3
            n "I'm back!"
            n 4e "Wait, what are you two doing right now?"
            show monika at f32 zorder 3
            show natsuki at t31 zorder 2
            m "Well, we all started sharing our poems with each other."
            show natsuki 5g at f31 zorder 3
            show monika at t32 zorder 2
            n "Already?"
            n 5w "Can't you just wait for me? I told you it's only for a while."
            show monika 2a at f32 zorder 3
            show natsuki at t31 zorder 2
            m "We still have plenty of time, so I'm more glad that you took all the time you needed."
            show natsuki 5c at f31 zorder 3
            show monika at t32 zorder 2
            n "Yeah, whatever."
            n 5s "I guess I should go get my poem now."
            show natsuki at thide zorder 1
            hide natsuki
            $ natsuki_out = False
            return
    else:
        "That... doesn't help anything with this current situation that I'm in-{nw}"
        $ _history_list.pop()
    return

label m_mp_1:
    m 1a "Great job, [player]!"
    m "I was going 'Ooh' in my head while reading it."
    m 1j "It's really metaphorical!"
    m 1a "I'm not sure why, but I didn't expect you to go for something so deep."
    m 3b "I guess I underestimated you!"
    mc "It's easiest for me to keep everyone's expectations low." # rephrase needed
    mc "That way, it always counts when I put in some effort." # rephrase needed
    m 5a "Ahaha! That's not very fair!"
    m "Well, I guess it worked, anyway."
    m 2a "You know that Yuri likes this kind of writing, right?"
    m "Writing that's full of imagery and symbolism."
    m 2d "Sometimes I feel like Yuri's mind is just totally detached from reality."
    m "I don't mean that like it's a bad thing, though."
    m 2a "But sometimes I get the impression that she's just totally given up on people."
    m "She spends so much time in her own head that it's probably a much more interesting place for her..."
    "Is that why Yuri were acting strange sometimes?"
    $ _history_list.pop()
    "Now I'm really worried about her..."
    $ _history_list.pop()
    m 2b "But that's why she gets so happy when you treat her with a lot of kindness."
    m "I don't think she's used to being indulged like that."
    m 2j "She must be really starved for social interaction, so don't blame her for coming on a little strongly."
    if y_ranaway:
        m 2d "Like earlier..."
    m 2d "I think if she gets too stimulated, she ends up withdrawing and looking for alone time."
    if y_ranaway:
        label yuri_come_back:
            "Suddenly, the door opens."
            m 2b "Yuri!"
            show monika 2a
            show yuri 1s at f31 zorder 3
            y "I'm back..."
            y "Did I miss anything?"
            show yuri at t31 zorder 2
            show monika at f32 zorder 3
            m 2a "Not really..."
            m "Well, we all started sharing our poems with each other."
            show monika at t32 zorder 2
            show yuri at f31 zorder 3
            y 2t "Eh?"
            y "Already?"
            y 2v "I-I'm sorry for being late..."
            show yuri at t31 zorder 2
            show monika at f32 zorder 3
            m 2j "No need to apologize!"
            m 2a "We still have plenty of time, so I'm more glad that you took all the time you needed."
            show monika at t32 zorder 2
            show yuri at f31 zorder 3
            y 1s "Alright..."
            y "Thanks, Monika."
            y "I suppose I should go get my poem now."
            show yuri at thide zorder 1
            hide yuri
            $ y_ranaway = False
            return
    else:
        mc "What will she do then?"
        m 1a "Hmm...?"
        m "What do you mean, [player]?"
        mc "What happens next?"
        m 2f "What are you talking about?"
        mc "What...?"
        "I'm pretty sure she's crazy right now."
        "Or not."
        mc "You know that I've literally heard everything what you said."
        mc "Who are you talking to anyway?"
        $ currentpos = get_pos()
        stop music
        pause 0.5
        play music "<from " + str(currentpos) + " loop 4.444>bgm/5.ogg"
        $ del _history_list[-10:]
    return

label m_abs_1:
    m 1a "Great job, [player]!"
    m "I was going to-"
    m 1h "Wait a minute..."
    "Monika re-reads my poem for a second time."
    m 1f "Umm..."
    mc "...?"
    "Monika glances at me."
    m 1g "It's..."
    window show(None)
    $ currentpos = get_pos()
    stop music
    pause 1.0
    play music "<from " + str(currentpos) + " loop 4.444>bgm/5.ogg"
    window show(None)
    m 2b "It's very good!"
    window auto
    m 4k "I like this one very much!"
    m 5a "It's almost like you're writing this poem for me~"
    "Did I? I couldn't remember that much when I wrote my own poem yesterday."
    mc "R-Really...?"
    m 3j "Ahaha- I'm just teasing you..."
    mc "Jeez, I don't really know much about your taste in the first place..."
    mc "I wrote it by my own volition."
    m 2a "I see..."
    m 4b "It has a bit of abstract elements, kind of what I usually writes."
    m "I expect you to write something like what Yuri or Natsuki usually writes..."
    mc "Again... I don't know much about their taste. So I just write what I want to write anyway."
    m 5a "But still, you impressed me a lot~"
    mc "Uh... Thanks, I guess..."
    mc "At least I know your taste a little bit."
    m 1j "Aww... did you really want to impress me that much?~"
    if y_ranaway:
        mc "I-Uh..."
        jump yuri_come_back
    else:
        mc "Uh, no...?"
        "F[fword]. I'm being my old-self again."
        m "Ahaha."
    return

label m_bs_1:
    m 1a "Great job, [player]!"
    m "I was going to-"
    m 1c "...."
    m 1d "[player]?"
    mc "...?"
    m 2d "Are you sure this is your first time writing your poem?"
    mc "Ah, so it's that bad."
    m 2m "I didn't say it's bad though. It just that it's different from what Yuri or Natsuki usually writes..."
    if n_readpoem:
        # if mc did read natsuki's poem
        mc "Huh? That's weird."
        mc "Even Natsuki likes my writing style."
        "Or not."
        "I still couldn't figure her out if she really liked my poem."
        mc "Wait, didn't she prefer \"cute\" stuff other than anything else?"
        m 1n "Ahaha. I guess it's just a bug then." # unless the script placeholder isnt actually a placeholder to begin with
        mc "A bug?"
    else:
        # if mc didn't read natsuki's poem yet
        mc "Did you expect my writing to be just like them?"
    m 1l "Ah-No! What I mean is..."
    m 3e "Whenever I read your poem, there's a bit of happiness, and also sadness feel to it."
    show monika 2e at t11 zorder 2
    $ m_temp = "Monika"
    m_temp "\"You could say it's... {nw}"
    m 2m "You could say it's... {fast}{i}bittersweet{/i}."
    show monika 2e at t11 zorder 2
    "That word seems familiar to me..."
    mc "So... is it good or bad?"
    m 1k "It's very good."
    m 3b "Kind of what Sayo-{nw}"
    $ del _history_list[-2:]
    window hide(None)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    stop sound
    hide screen tear
    window show(None)
    m 1k "It's very good.{fast}"
    window auto
    mc "What did you say just now?"
    m 1a "What do you mean?"
    mc "Umm..."
    mc "I thought I heard that name-{nw}"
    m 2l "It's nothing but a compliment. Ahaha..."
    mc "A compliment...?"
    "Is that even a compliment?"
    "I don't even know what's going on with her..."
    mc "Uh... thanks, I guess?"
    if natsuki_out:
        jump natsuki_come_back
    return

label monika_special_1_end:
    if y_ranaway:
        "I don't know why I keep worrying about Yuri..."
        "I feel like something's wrong with her."
    m 1a "Anyway, do you want to read my poem now?"
    mc "Ah, definitely."
    m 1e "Don't worry, I'm not very good..."
    mc "Really? You sound pretty confident for someone who claims to not be very good."
    m 1j "Well...that's 'cause I have to sound confident."
    m 1e "Especially since that I read your poem just now... Ehehe~"
    mc "That's--"
    mc "I didn't know about that..."
    m 1b "Ahaha. That doesn't mean I always feel that way, you know?"
    mc "{cps=100}eyeee ccccccccccc uuu{nw}{/cps}"
    $ _history_list.pop()
    window hide(None)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    stop sound
    hide screen tear
    window show(None)
    mc "I see...{fast}"
    window auto
    mc "Anyway, let's read it, then."

    call showpoem(poem_m1)

    "This poem, for some reason reminds me of one of my dreams that happened yesterday."
    "Is this a coincidence?"
    m 1a "So...what do you think?"
    mc "Hmm..."
    mc "It's kind of abstract. Just like my poem..."
    mc "I mean, it's {i}very{/i} abstract."
    mc "There are some parts that I don't understand that much."
    m 2e "Well, you don't have to worry about the meaning of it and everything."
    mc "How so?"
    m 2q "Hmm..."
    m 2g "It's kind of complicated to answer, but I'll try my best to answer it for you anyway..."
    mc "Okay. I'm all ears."
    m 2d "I'm not sure if I know how to put it..."
    m 2a "I guess you could say that I had some kind of epiphany recently."
    m "It's been influencing my poems a bit."
    mc "An epiphany?"
    "I think I do have that same feeling before."
    m 1a "Yeah...something like that."
    m "I'm kind of nervous to talk about deep stuff like that, because it's kind of coming on strongly..."
    m 1d "Anyway, do you have that kind of experience before?"
    m 1q "That's okay if you don't know anything about it..."
    mc "Maybe..."
    m 2h "Maybe?"
    mc "I mean I already know where you coming from."
    mc "It's hard to explain something that is out of ordinary."
    mc "It's even weird if you don't know much about yourself or what you are capable of."
    mc "No matter how hard you try to understand what is going on, sometimes you just don't get it."
    mc "Then, you realized that there's no point to understand it anyway."
    mc "Thinking that just going with the flow and hope to find some little answers, but probably no avail."
    #mc "There's a bit of feelings where you start to give up on it." # sorry, my writing is bad tbh
    mc "Sorry, I-I think I'm overthinking this..."
    stop music fadeout 10.0
    show noise at noisefade(10) zorder 3
    m 1f "..."
    m 1e "That's okay, I know what're you talking about..."
    m 2e "I didn't know you were interested in something so deep and complicated things."
    m "That's very endearing of you."
    if not persistent.monika_secret[0]: # if monika is the last one that mc shared with
        mc "I-I guess so..."
        m "[player]..."
        m 1e "The truth is, there are just some things I've been hoping to talk about with you..."
        m "Things I know only you could understand."
        show black onlayer front:
            alpha 0.0
            0.25
            linear 3.0 alpha 1.00
        m "If you could hear me out--\"{space=5000}{w=0.75}{nw}"
        m 1g "Wait, not yet!\"{space=5000}{w=0.5}{nw}"
        m "No!\"{space=5000}{w=0.5}{nw}"
        m "Stop it!\"{space=5000}{w=1.0}{nw}"
        $ del _history_list[-4:]
        $ persistent.monika_secret[1] = True
        window hide(None)
        window auto
        scene black
        hide black onlayer front
        pause 0.1
    elif poemsread < 2: # if mc didnt share his poem to others yet
        mc "..."
        mc "A-Anyway, I need to share my poem to others now..."
        mc "Maybe we could talk about this at another time."
        mc "Is that okay?"
        m 1m "A-ah. Sure..."
        m 1e "See you later then..."
        stop music
        hide noise
    else: # if player reloads again, still sharing mc's poem to monika
        if poemsread < 2:
            mc "...{nw}"
        else:
            mc "I-I guess{nw}"
        stop music
        window hide(None)
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.25
        stop sound
        hide screen tear
        window auto
        hide noise
        scene black
        pause 0.1
    #$ persistent.ggwp_monika = 5
    $ persistent.monika_secret[0] = True # honestly, i should use this instead, it's more efficient than ggwp_monika, sometimes i kind of lost track looking at these codes (sry i have such a bad memory)
    return

label mod_ch1_m_end:
    window hide(None)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    stop sound
    hide screen tear
    window show(None)
    window auto
    m 1a "Anyway, do you want to read my poem now?"
    m 1e "Don't worry, I'm not very good..."
    mc "You sound pretty confident for someone who claims to not be very good."
    m 1j "Well...that's 'cause I have to sound confident."
    m 1b "That doesn't mean I always feel that way, you know?"
    mc "I see..."
    mc "Well, let's read it, then."

    call showpoem(poem_m1)

    m 1a "So...what do you think?"
    mc "Hmm..."
    "This poem, for some reason reminds me of one of my dreams that happened yesterday."
    $ _history_list.pop()
    "Is this a coincidence?"
    $ _history_list.pop()
    mc "Hmm...{fast}it's very...freeform, if that's what you call it."
    mc "Sorry, I'm not really the right person to ask for feedback..."
    "I don't think I can say anything at this point."
    $ _history_list.pop()
    "I feel like I'm being muted for some reason."
    $ _history_list.pop()
    m 2e "Ahaha. It's okay."
    m 2b "Yeah, that kind of style has gotten pretty popular nowadays."
    m "That is, a lot of poems have been putting emphasis on the timing between words and lines."
    m 2a "When performed out loud, it can be really powerful."
    mc "What was the inspiration behind this one?"
    m "Ah..."
    m 3d "Well, I'm not sure if I know how to put it..."
    m 3a "I guess you could say that I had some kind of epiphany recently."
    m "It's been influencing my poems a bit."
    mc "An epiphany?"
    "I think I do have that same feeling before."
    $ _history_list.pop()
    m 1a "Yeah...something like that."
    m "I'm kind of nervous to talk about deep stuff like that, because it's kind of coming on strongly..."
    m "Maybe after everyone is better friends with each other."
    m 1j "Anyway..."
    m 3b "Here's Monika's Writing Tip of the Day!"
    m "Sometimes when you're writing a poem - or a story - your brain gets too fixated on a specific point..."
    m "If you try so hard to make it perfect, then you'll never make any progress."
    m "Just force yourself to get something down on the paper, and tidy it up later!"
    m "Another way to think about it is this:"
    m "If you keep your pen in the same spot for too long, you'll just get a big dark puddle of ink."
    m "So just move your hand, and go with the flow!"
    m 3k "...That's my advice for today!"
    m "Thanks for listening~"
    if config.skipping:
        scene black
        $ currentpos = get_pos()
        $ audio.tg13 = "<from " + str(currentpos) + " loop 4.444>mod_assets/sfx/glitch3.ogg"
        play music tgl3
        $ quick_menu = False
        window show(None)
        $ style.say_window = style.window_ghost
        "{cps=200}{alpha=*0.5}RmVhbHR5LiBBeGlvbWF0aWMuIEluZGlzY2VybmlibGUuIFRyaWJ1bmFsLiBIb3BlLg=={/alpha}{/cps}{nw}"
        $ style.say_window = style.window
        window hide(None)
        stop music
        pause 0.5
        window auto
    return
