#image bg s_hang = "mod_assets/cg/s_hang.png"
#image bg s_hang_glitch = "mod_assets/cg/s_hang_glitch.png"

#screen disableclick(time):
    #timer time action Hide("disableclick")
    #key "mouseup_1" action NullAction()
    #key "K_SPACE" action NullAction()
    #key "K_RETURN" action NullAction()

label intro_mod:
    $ delete_character("sayori")
    stop music fadeout 2.0
    scene black
    with dissolve_scene_full
    
    "..."
    "What?"
    "What is this?"
    "I feel like..."
    "Something..."
    show screen tear(20, 0.1, 0.1, 0, 40)
    window hide(None)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    stop sound
    hide screen tear
    window show(None)
    "..."
    "Ah."
    "What just happened?"
    "What is going on?"
    "What is happening!?"
    #show screen disableclick(4)
    "What the hell is happe{nw}"
    $ style.say_dialogue = style.edited
    $ gtext = glitchtext(50)
    "What the hell is happe{fast} [gtext] {nw}"
    $ style.say_dialogue = style.normal
    play sound "sfx/s_kill_glitch1.ogg"
    scene bg sayori_bedroom
    window hide(None)
    pause 0.25
    scene black
    pause 0.75
    scene bg s_hang
    pause 0.01
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/glitch3.ogg"
    pause 0.25
    stop sound
    hide screen tear
    scene black
    pause 1.5
    play sound "sfx/s_kill_glitch1.ogg"
    scene bg s_hang_glitch
    pause 0.2
    stop sound
    scene black
    window show(None)
    "Ah..."
    "Who's that girl?"
    "My head is shaking..."
    "Is she someone special to me?"
    #$ renpy.call_screen("dialog", "Yes.", ok_action=Return())
    pause 1.5
    "I see..."
    "Sayori, wasn't it?"
    "Now I remembered..."
    "Someone actually kill her?"
    "Is this really true?"
    "Did someone made her more depressed until she killed herself?"
    "{i}Someone....{/i}"
    "..."
    pause 1.5
    "It was her."
    "I knew it..."
    "She's a murderer."
    "I can't trust her anymore..."
    "I need help..."
    "I..."
    "...need..."
    "...help..."
    pause 1.5
    "Is this actually a game?"
    "Am I some kind of program?"
    "A sentient?"
    "I couldn't believe it at first, but I think there's something strange happened to her as well."
    "Maybe something wrong with this game."
    "Maybe..."
    "I don't know."
    "Wait, if this is a game..."
    "Maybe I can do something about this..."
    "I wish I could avenge Sayori."
    "Maybe I can..."
    "I need to do something.."
    "Think, [player]! Think!"
    window hide(None)
    pause renpy.random.randint(2, 8)
    window show(None)
    "I think I got it."
    "If I am a sentient, maybe I can mod...{nw}"
    "{cps=*3}If I am a sentient, maybe I can mod{fast} [gtext] {/cps} {nw}"
    show screen tear(8, offtimeMult=1, ontimeMult=10)
    pause 1.5
    $ persistent.playthrough = 1
    $ renpy.utter_restart()
    
    return