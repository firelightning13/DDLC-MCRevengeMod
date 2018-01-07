screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.8

        spacing gui.navigation_spacing

        #if not persistent.autoload or not main_menu:

        if main_menu:

            if persistent.playthrough == 1:
                textbutton _("ŔŗñĮ¼»ŧþŀÂŻŕěōì«") action If(persistent.playername, true=Start(), false=Show(screen="name_input", message="Please enter your name", ok_action=Function(FinishEnterName)))
            elif persistent.demu_demu:
                textbutton _("Just Monika") action If(persistent.playername, true=Start(), false=Show(screen="name_input", message="Just Monika", ok_action=Function(FinishEnterName)))
            else:
                textbutton _("New Game") action If(persistent.playername, true=Start(), false=Show(screen="name_input", message="Please enter your name", ok_action=Function(FinishEnterName)))

        else:

            textbutton _("History") action [ShowMenu("history"), SensitiveIf(renpy.get_screen("history") == None)]

            textbutton _("Save Game") action [ShowMenu("save"), SensitiveIf(renpy.get_screen("save") == None)]

        if persistent.demu_demu:
            textbutton _("Just Monika") action [ShowMenu("load"), SensitiveIf(renpy.get_screen("load") == None)]
        else:
            textbutton _("Load Game") action [ShowMenu("load"), SensitiveIf(renpy.get_screen("load") == None)]

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:
            #if persistent.playthrough != 3:
            textbutton _("Main Menu") action MainMenu()
            #else:
                #textbutton _("Main Menu") action NullAction()

        if persistent.demu_demu:
            textbutton _("Just Monika") action [ShowMenu("preferences"), SensitiveIf(renpy.get_screen("preferences") == None)]
        else:
            textbutton _("Settings") action [ShowMenu("preferences"), SensitiveIf(renpy.get_screen("preferences") == None)]

            #textbutton _("About") action ShowMenu("about")

        if renpy.variant("pc"):

                ## Help isn't necessary or relevant to mobile devices.
            if persistent.demu_demu:
                textbutton _("Just Monika") action Help("README.html")
            else:
                textbutton _("Help") action Help("README.html")

                ## The quit button is banned on iOS and unnecessary on Android.
            if persistent.demu_demu:
                textbutton _("Just Monika") action Quit(confirm=not main_menu)
            else:
                textbutton _("Quit") action Quit(confirm=not main_menu)
        #else:
            #timer 1.75 action Start("autoload_yurikill")

screen main_menu():

    # This ensures that any other menu screen is replaced.
    tag menu

    style_prefix "main_menu"


    if not persistent.demu_demu:
        add "menu_bg"
        add "menu_art_y"
        add "menu_art_n"
    else:
        add "hi_monika"
    frame:
        pass

## The use statement includes another screen inside this one. The actual
## contents of the main menu are in the navigation screen.
    use navigation
    
    add "menu_particles"
    add "menu_particles"
    add "menu_particles"
    add "menu_logo"
    if persistent.playthrough == 1:
        add "menu_art_s_glitch"
    elif persistent.playthrough == 2:
        pass
    else:
        add "menu_art_s"
    add "menu_particles"
    add "menu_art_m"
    add "menu_fade"

    if gui.show_name:

        vbox:
            if not persistent.demu_demu:
                text "[config.name!t]":
                    style "main_menu_title"

                text "v. [config.version] demo":
                    style "main_menu_version"
            else:
                text "Just Monika":
                    style "main_menu_title"

                text "Just Monika":
                    style "main_menu_version"


    key "K_ESCAPE" action Quit(confirm=False)

style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text:
    color "#000000"
    size 16
    outlines []

style main_menu_frame:
    xsize 310
    yfill True

    background "menu_nav"

style main_menu_vbox:
    xalign 1.0
    xoffset -20
    xmaximum 800
    yalign 1.0
    yoffset -20

style main_menu_text:
    xalign 1.0

    layout "subtitle"
    text_align 1.0
    color gui.accent_color

style main_menu_title:
    size gui.title_text_size
