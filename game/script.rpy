# The script of the game goes in this file.
image teacher = "teacehr.png"
image schoolEntrance = "school_entrance.png"
image classroom = "classroom.jpeg"
image right = "true.png"
image wrong = "false.png"
image 1p1 = "1+1.jpg" #1 additions
image 1p2 = "1+2.jpg"
image 1p3 = "1+3.jpg"
image 1p4 = "1+4.jpg"
image 1p5 = "1+5.jpg"
image 1p6 = "1+6.jpg"
image 1p7 = "1+7.jpg"
image 1p8 = "1+8.jpg"
image 1p9 = "1+9.jpg"
image 2p1 = "2+1.jpg" #2 additions
image 2p2 = "2+2.jpg"
image 2p4 = "2+4.jpg"
image 2p5 = "2+5.jpg"
image 2p9 = "2+9.jpg"
image 3p1 = "3+1.jpg" #3 additions
image 3p2 = "3+2.jpg"
image 3p5 = "3+5.jpg"
image 3p7 = "3+7.jpg"
image 3p9 = "3+9.jpg"
image 4p2 = "4+2.jpg" #4 additions
image 4p4 = "4+4.jpg"
image 4p8 = "4+8.jpg"
image 5p1 = "5+1.jpg" #5 additions
image 5p4 = "5+4.jpg"
image 5p9 = "5+9.jpg"
image 6p1 = "6+1.jpg" #6 additions
image 6p3 = "6+3.jpg"
image 6p5 = "6+5.jpg"
image 6p8 = "6+8.jpg"
image 7p2 = "7+2.jpg" #7 additions
image 7p5 = "7+5.jpg"
image 7p8 = "7+8.jpg"
image 8p1 = "8+1.jpg" #8 additions
image 8p3 = "8+3.jpg"
image 8p9 = "8+9.jpg"
image 9p3 = "9+3.jpg" #9 additions
image 9p6 = "9+6.jpg"
image 9p9 = "9+9.jpg"
image 9s1 = "9-1.jpg" #9 subtraction
image 9s5 = "9-5.jpg"
image 9s7 = "9-7.jpg"
image 8s1 = "8-1.jpg" #8 subtraction
image 8s4 = "8-4.jpg"
image 8s6 = "8-6.jpg"
image 7s1 = "7-1.jpg" #7 subtraction
image 7s4 = "7-4.jpg"
image 7s7 = "7-7.jpg"
image 12s7 = "12-7.jpg"
image 16s9 = "16-9.jpg"
image 20s12 = "20-12.jpg"
image 2x0 = "2x0.jpg" # Multiplication
image 2x2 = "2x2.jpg"
image 2x4 = "2x4.jpg"
image 2x9 = "2x9.jpg"
image 3x7 = "3x7.jpg"
image 3x9 = "3x9.jpg"
image 5x4 = "5x4.jpg"
image 5x8 = "5x8.jpg"
image 6x7 = "6x7.jpg"
image 7x1 = "7x1.jpg"
image 7x9 = "7x9.jpg"
image 8x8 = "8x8.jpg"
image 9x6 = "9x6.jpg"
image 2d2 = "2d2.jpg" # Division
image 3d1 = "3d1.jpg"
image 4d1 = "4d1.jpg"
image 6d2 = "6d2.jpg"
image 12d3 = "12d3.jpg"
image 18d6 = "18d6.jpg"
image 20d4 = "20d4.jpg"
image 56d8 = "56d8.jpg"
image 81d9 = "81d9.jpg"

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define g = Character("Girl")
define b = Character("Boy")
define t = Character("Teacher")


# The game starts here.

label start:
    $ score = 0

    scene schoolEntrance
    show teacher
    t "Welcome to our Math App"

    menu:
        "Select Addition":
            jump Addition

        "Select Subtraction":
            jump Subtraction

        "Select Multiplication":
            jump Multiplication

        "Select Division":
            jump Division

    label Addition:

         t "Select a difficulty"

    menu:
        "Easy":
            jump EasyA
        "Medium":
            jump MediumA
        "Hard":
            jump HardA

    label Subtraction:

         t "Select a difficulty"

    menu:
        "Easy":
            jump EasyS
        "Medium":
            jump MediumS
        "Hard":
            jump HardS

    label Multiplication:

         t "Select a difficulty"

    menu:
        "Easy":
            jump EasyM
        "Medium":
            jump MediumM
        "Hard":
            jump HardM

    label Division:

         t "Select a difficulty"

    menu:
        "Easy":
            jump EasyD
        "Medium":
            jump MediumD
        "Hard":
            jump HardD

    label EasyA: #Addition section
        scene classroom
        t "Please answer the following questions"
        $ question = renpy.random.randint(0, 3)
        if question == 0:
            scene 1p3
            $ answer = renpy.input("Enter answer here")
            if answer == "4":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 2p4
            $ answer = renpy.input("Enter answer here")
            if answer == "6":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 3p2
            $ answer = renpy.input("Enter answer here")
            if answer == "5":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"

        elif question == 1:
            scene 2p4
            $ answer = renpy.input("Enter answer here")
            if answer == "6":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 3p2
            $ answer = renpy.input("Enter answer here")
            if answer == "5":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 1p3
            $ answer = renpy.input("Enter answer here")
            if answer == "4":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"

        else:
            scene 3p2
            $ answer = renpy.input("Enter answer here")
            if answer == "5":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 1p3
            $ answer = renpy.input("Enter answer here")
            if answer == "4":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 2p4
            $ answer = renpy.input("Enter answer here")
            if answer == "6":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"

        show teacher at left
        t "You finished easy addition practice"
        if score == 0:
            t "I suggest more practice"
        elif score < 3:
            t "This seems to be your level"
        else:
            t "I suggest a harder difficulty"
        menu:
            "Try again":
                jump EasyA
            "Next difficulty":
                jump MediumA
            "Finish":
                return



    label MediumA:
        scene classroom
        t "Please answer the following questions"
        $ question = renpy.random.randint(0, 3)
        if question == 0:
            scene 4p4
            $ answer = renpy.input("Enter answer here")
            if answer == "8":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 6p5
            $ answer = renpy.input("Enter answer here")
            if answer == "11":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 3p9
            $ answer = renpy.input("Enter answer here")
            if answer == "12":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 2p9
            $ answer = renpy.input("Enter answer here")
            if answer == "11":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"

        elif question == 1:
            scene 3p9
            $ answer = renpy.input("Enter answer here")
            if answer == "12":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 4p4
            $ answer = renpy.input("Enter answer here")
            if answer == "8":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 6p5
            $ answer = renpy.input("Enter answer here")
            if answer == "11":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 2p9
            $ answer = renpy.input("Enter answer here")
            if answer == "11":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"

        else:
            scene 6p5
            $ answer = renpy.input("Enter answer here")
            if answer == "11":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 4p4
            $ answer = renpy.input("Enter answer here")
            if answer == "8":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 3p9
            $ answer = renpy.input("Enter answer here")
            if answer == "12":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 2p9
            $ answer = renpy.input("Enter answer here")
            if answer == "11":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"

        show teacher at left
        t "You finished medium addition practice"
        if score == 0:
            t "I suggest an easier difficulty"
        elif score < 3:
            t "This seems to be your level"
        else:
            t "I suggest a harder difficulty"
        menu:
            "Try again":
                jump MediumA
            "Previous difficulty":
                jump EasyA
            "Next difficulty":
                jump HardA
            "Finish":
                return

    label HardA:
        scene classroom
        t "Please answer the following questions"
        $ question = renpy.random.randint(0, 3)
        if question == 0:
            scene 6p8
            $ answer = renpy.input("Enter answer here")
            if answer == "14":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 8p9
            $ answer = renpy.input("Enter answer here")
            if answer == "17":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 9p6
            $ answer = renpy.input("Enter answer here")
            if answer == "15":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 7p8
            $ answer = renpy.input("Enter answer here")
            if answer == "15":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"

        if question == 1:
            scene 9p6
            $ answer = renpy.input("Enter answer here")
            if answer == "15":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 6p8
            $ answer = renpy.input("Enter answer here")
            if answer == "14":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 8p9
            $ answer = renpy.input("Enter answer here")
            if answer == "17":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 7p8
            $ answer = renpy.input("Enter answer here")
            if answer == "15":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"

        else:
            scene 7p8
            $ answer = renpy.input("Enter answer here")
            if answer == "15":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 6p8
            $ answer = renpy.input("Enter answer here")
            if answer == "14":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 8p9
            $ answer = renpy.input("Enter answer here")
            if answer == "17":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 9p6
            $ answer = renpy.input("Enter answer here")
            if answer == "15":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"

        show teacher at left
        t "You finished hard addition practice"
        if score == 0:
            t "I suggest an easier difficulty"
        elif score < 3:
            t "This seems to be your level"
        else:
            t "Very good"
        menu:
            "Try again":
                jump HardA
            "Previous difficulty":
                jump MediumA
            "Finish":
                return

    label EasyS: #Subtraction section
        scene classroom
        t "Please answer the following questions"
        $ question = renpy.random.randint(0, 3)
        if question == 0:
            scene 7s7
            $ answer = renpy.input("Enter answer here")
            if answer == "0":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 9s1
            $ answer = renpy.input("Enter answer here")
            if answer == "8":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 7s1
            $ answer = renpy.input("Enter answer here")
            if answer == "6":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"

        if question == 1:
            scene 9s1
            $ answer = renpy.input("Enter answer here")
            if answer == "8":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 7s7
            $ answer = renpy.input("Enter answer here")
            if answer == "0":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 7s1
            $ answer = renpy.input("Enter answer here")
            if answer == "6":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"

        else:
            scene 7s1
            $ answer = renpy.input("Enter answer here")
            if answer == "6":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 7s7
            $ answer = renpy.input("Enter answer here")
            if answer == "0":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 9s1
            $ answer = renpy.input("Enter answer here")
            if answer == "8":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"

        show teacher at left
        t "You finished easy subtraction practice"
        if score == 0:
            t "I suggest more practice"
        elif score < 3:
            t "This seems to be your level"
        else:
            t "I suggest a harder difficulty"
        menu:
            "Try again":
                jump EasyA
            "Next difficulty":
                jump MediumA
            "Finish":
                return

    label MediumS:
        scene classroom
        t "Please answer the following questions"
        $ question = renpy.random.randint(0, 3)
        if question == 0:
            scene 7s4
            $ answer = renpy.input("Enter answer here")
            if answer == "3":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 8s4
            $ answer = renpy.input("Enter answer here")
            if answer == "4":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 9s5
            $ answer = renpy.input("Enter answer here")
            if answer == "4":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"

        if question == 1:
            scene 9s5
            $ answer = renpy.input("Enter answer here")
            if answer == "4":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 7s4
            $ answer = renpy.input("Enter answer here")
            if answer == "3":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 8s4
            $ answer = renpy.input("Enter answer here")
            if answer == "4":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"

        else:
            scene 8s4
            $ answer = renpy.input("Enter answer here")
            if answer == "4":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 7s4
            $ answer = renpy.input("Enter answer here")
            if answer == "3":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 9s5
            $ answer = renpy.input("Enter answer here")
            if answer == "4":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"

        show teacher at left
        t "You finished medium subtraction practice"
        if score == 0:
            t "I suggest an easier difficulty"
        elif score < 3:
            t "This seems to be your level"
        else:
            t "I suggest a harder difficulty"
        menu:
            "Try again":
                jump MediumA
            "Previous difficulty":
                jump EasyS
            "Next difficulty":
                jump HardS
            "Finish":
                return

    label HardS:
        scene classroom
        t "Please answer the following questions"
        $ question = renpy.random.randint(0, 3)
        if question == 0:
            scene 12s7
            $ answer = renpy.input("Enter answer here")
            if answer == "5":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 20s12
            $ answer = renpy.input("Enter answer here")
            if answer == "8":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 16s9
            $ answer = renpy.input("Enter answer here")
            if answer == "7":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"

        if question == 1:
            scene 16s9
            $ answer = renpy.input("Enter answer here")
            if answer == "7":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 12s7
            $ answer = renpy.input("Enter answer here")
            if answer == "5":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 20s12
            $ answer = renpy.input("Enter answer here")
            if answer == "8":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"

        else:
            scene 20s12
            $ answer = renpy.input("Enter answer here")
            if answer == "8":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 12s7
            $ answer = renpy.input("Enter answer here")
            if answer == "5":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 16s9
            $ answer = renpy.input("Enter answer here")
            if answer == "7":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"

        show teacher at left
        t "You finished hard subtraction practice"
        if score == 0:
            t "I suggest an easier difficulty"
        elif score < 3:
            t "This seems to be your level"
        else:
            t "Very good"
        menu:
            "Try again":
                jump HardS
            "Previous difficulty":
                jump MediumA
            "Finish":
                return

    label EasyM: #Multiplication section
        scene classroom
        t "Please answer the following questions"
        $ question = renpy.random.randint(0, 3)
        if question == 0:
            scene 2x0
            $ answer = renpy.input("Enter answer here")
            if answer == "0":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 7x1
            $ answer = renpy.input("Enter answer here")
            if answer == "7":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 2x4
            $ answer = renpy.input("Enter answer here")
            if answer == "8":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 2x2
            $ answer = renpy.input("Enter answer here")
            if answer == "4":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"

        if question == 1:
            scene 2x4
            $ answer = renpy.input("Enter answer here")
            if answer == "8":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 2x2
            $ answer = renpy.input("Enter answer here")
            if answer == "4":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 2x0
            $ answer = renpy.input("Enter answer here")
            if answer == "0":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 7x1
            $ answer = renpy.input("Enter answer here")
            if answer == "7":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"

        else:
            scene 7x1
            $ answer = renpy.input("Enter answer here")
            if answer == "7":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 2x4
            $ answer = renpy.input("Enter answer here")
            if answer == "8":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 2x0
            $ answer = renpy.input("Enter answer here")
            if answer == "0":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 2x2
            $ answer = renpy.input("Enter answer here")
            if answer == "4":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"

        show teacher at left
        t "You finished easy addition practice"
        if score == 0:
            t "I suggest more practice"
        elif score < 3:
            t "This seems to be your level"
        else:
            t "I suggest a harder difficulty"
        menu:
            "Try again":
                jump EasyM
            "Next difficulty":
                jump MediumM
            "Finish":
                return



    label MediumM:
        scene classroom
        t "Please answer the following questions"
        $ question = renpy.random.randint(0, 3)
        if question == 0:
            scene 3x7
            $ answer = renpy.input("Enter answer here")
            if answer == "21":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 5x4
            $ answer = renpy.input("Enter answer here")
            if answer == "20":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 2x9
            $ answer = renpy.input("Enter answer here")
            if answer == "18":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"

        if question == 1:
            scene 5x4
            $ answer = renpy.input("Enter answer here")
            if answer == "20":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 2x9
            $ answer = renpy.input("Enter answer here")
            if answer == "18":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 3x7
            $ answer = renpy.input("Enter answer here")
            if answer == "21":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"

        else:
            scene 2x9
            $ answer = renpy.input("Enter answer here")
            if answer == "18":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 3x7
            $ answer = renpy.input("Enter answer here")
            if answer == "21":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 5x4
            $ answer = renpy.input("Enter answer here")
            if answer == "20":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"

        show teacher at left
        t "You finished medium addition practice"
        if score == 0:
            t "I suggest an easier difficulty"
        elif score < 3:
            t "This seems to be your level"
        else:
            t "I suggest a harder difficulty"
        menu:
            "Try again":
                jump MediumM
            "Previous difficulty":
                jump EasyM
            "Next difficulty":
                jump HardM
            "Finish":
                return

    label HardM:
        scene classroom
        t "Please answer the following questions"
        $ question = renpy.random.randint(0, 3)
        if question == 0:
            scene 6x7
            $ answer = renpy.input("Enter answer here")
            if answer == "42":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 8x8
            $ answer = renpy.input("Enter answer here")
            if answer == "64":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 9x6
            $ answer = renpy.input("Enter answer here")
            if answer == "54":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"

        if question == 1:
            scene 9x6
            $ answer = renpy.input("Enter answer here")
            if answer == "54":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 6x7
            $ answer = renpy.input("Enter answer here")
            if answer == "42":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 8x8
            $ answer = renpy.input("Enter answer here")
            if answer == "64":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"

        else:
            scene 8x8
            $ answer = renpy.input("Enter answer here")
            if answer == "64":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 6x7
            $ answer = renpy.input("Enter answer here")
            if answer == "42":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 9x6
            $ answer = renpy.input("Enter answer here")
            if answer == "54":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"

        show teacher at left
        t "You finished hard addition practice"
        if score == 0:
            t "I suggest an easier difficulty"
        elif score < 3:
            t "This seems to be your level"
        else:
            t "Very good"
        menu:
            "Try again":
                jump HardM
            "Previous difficulty":
                jump MediumM
            "Finish":
                return

    label EasyD: #division section
        scene classroom
        t "Please answer the following questions"
        $ question = renpy.random.randint(0, 3)
        if question == 0:
            scene 2d2
            $ answer = renpy.input("Enter answer here")
            if answer == "1":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 3d1
            $ answer = renpy.input("Enter answer here")
            if answer == "3":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 4d1
            $ answer = renpy.input("Enter answer here")
            if answer == "4":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 6d2
            $ answer = renpy.input("Enter answer here")
            if answer == "3":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"

        if question == 1:
            scene 6d2
            $ answer = renpy.input("Enter answer here")
            if answer == "3":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 2d2
            $ answer = renpy.input("Enter answer here")
            if answer == "1":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 3d1
            $ answer = renpy.input("Enter answer here")
            if answer == "3":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 4d1
            $ answer = renpy.input("Enter answer here")
            if answer == "4":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"

        else:
            scene 4d1
            $ answer = renpy.input("Enter answer here")
            if answer == "4":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 2d2
            $ answer = renpy.input("Enter answer here")
            if answer == "1":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 3d1
            $ answer = renpy.input("Enter answer here")
            if answer == "3":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 6d2
            $ answer = renpy.input("Enter answer here")
            if answer == "3":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"

        show teacher at left
        t "You finished easy addition practice"
        if score == 0:
            t "I suggest more practice"
        elif score < 3:
            t "This seems to be your level"
        else:
            t "I suggest a harder difficulty"
        menu:
            "Try again":
                jump EasyD
            "Next difficulty":
                jump MediumD
            "Finish":
                return



    label MediumD:
        scene classroom
        t "Please answer the following questions"
        $ question = renpy.random.randint(0, 3)
        if question == 0:
            scene 6d2
            $ answer = renpy.input("Enter answer here")
            if answer == "3":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 12d3
            $ answer = renpy.input("Enter answer here")
            if answer == "4":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 20d4
            $ answer = renpy.input("Enter answer here")
            if answer == "5":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"

        if question == 1:
            scene 20d4
            $ answer = renpy.input("Enter answer here")
            if answer == "5":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 6d2
            $ answer = renpy.input("Enter answer here")
            if answer == "3":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 12d3
            $ answer = renpy.input("Enter answer here")
            if answer == "4":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"

        else:
            scene 12d3
            $ answer = renpy.input("Enter answer here")
            if answer == "4":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 6d2
            $ answer = renpy.input("Enter answer here")
            if answer == "3":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 20d4
            $ answer = renpy.input("Enter answer here")
            if answer == "5":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"

        show teacher at left
        t "You finished medium addition practice"
        if score == 0:
            t "I suggest an easier difficulty"
        elif score < 3:
            t "This seems to be your level"
        else:
            t "I suggest a harder difficulty"
        menu:
            "Try again":
                jump MediumD
            "Previous difficulty":
                jump EasyD
            "Next difficulty":
                jump HardD
            "Finish":
                return

    label HardD:
        scene classroom
        t "Please answer the following questions"
        $ question = renpy.random.randint(0, 3)
        if question == 0:
            scene 18d6
            $ answer = renpy.input("Enter answer here")
            if answer == "3":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 56d8
            $ answer = renpy.input("Enter answer here")
            if answer == "7":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 81d9
            $ answer = renpy.input("Enter answer here")
            if answer == "9":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"

        if question == 1:
            scene 56d8
            $ answer = renpy.input("Enter answer here")
            if answer == "7":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 81d9
            $ answer = renpy.input("Enter answer here")
            if answer == "9":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 18d6
            $ answer = renpy.input("Enter answer here")
            if answer == "3":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"

        else:
            scene 81d9
            $ answer = renpy.input("Enter answer here")
            if answer == "9":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 18d6
            $ answer = renpy.input("Enter answer here")
            if answer == "3":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"
            scene 56d8
            $ answer = renpy.input("Enter answer here")
            if answer == "7":
                $ score += 1
                show right at right
                t "Correct"
            else:
                show wrong at right
                t "Wrong"

        show teacher at left
        t "You finished hard addition practice"
        if score == 0:
            t "I suggest an easier difficulty"
        elif score < 3:
            t "This seems to be your level"
        else:
            t "Very good"
        menu:
            "Try again":
                jump HardD
            "Previous difficulty":
                jump MediumD
            "Finish":
                return
