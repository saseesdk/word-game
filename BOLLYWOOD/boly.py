import tkinter
import random
from tkinter import *
from turtle import color
from PIL\
    import *
from PIL import ImageTk, Image
from tkinter.font import BOLD, Font
import pygame   
from pygame import mixer
import playsound
from playsound import playsound
from tkinter import messagebox

mixer.init()
num = 0
size = 23
count = 0
count2 = 0
win = 5
ram = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
entry = []
synt = []


def check1():
    global boly, count2, win, blank, entry, synt
    click = mixer.Sound("Button Click 2.mp3")
    click.play()
    #global ent, w1
    stg = ent.get()
    stg = str(stg)

    boly = [b, o, l, l2, y, w, o1, o2, d]

    if ran <= 10:
        blank = [a1, b1, c1, d1]
    else:
        blank = [a1, b1, c1, d1, e1]
    if stg in w1:
        count1 = 0
        for i in range(0, len(w1)):
            count1 = i
            if stg in w1[i]:
                if stg in entry and count1 in synt:
                    pass
                else:
                    entry.append(str(stg))
                    print("yes")
                    print(count1)
                    synt.append(count1)
                    blank[count1]["text"] = stg.upper()
                    win = win - 1
                if win == 1:
                    check["text"] = "NEXT"
                    messagebox.showinfo("WINNER", "YOU WON :), Click next")
                    synt = []
                    entry = []
                if win <= 0:
                    count2 = 0
                    #e1.destroy()
                    win = 5
                    page2()

    else:
        if count2 <= 7:
            messagebox.showinfo("Incorrect", "this alphabet isn't in the word")
            boly[count2].config(bg='grey51')
            count2 = count2 + 1
        elif count2 > 7:
            messagebox.showinfo("game over", "GAME OVER:(")
            window.destroy()


def page2():
    global ent, w1, b, o1, l2, l, y, w, o, o2, d, a1,b1, c1, d1, check, ram, win, e1, blank,ran
    Exit1.grid(row=1, column=1, columnspan=2, sticky=NW)
    Mute.grid(row=1, column=17, padx=115)

    '#---------------bollywood label'
    b = Label(window, text="B", font=buttonFont1, height=2, width=4, bg='grey1', fg='white')
    b.grid(row=3, column=5, padx=10, pady=50)

    o = Label(window, text="O", font=buttonFont1, height=2, width=4, bg='grey1', fg='white')
    o.grid(row=3, column=6, padx=5)

    l = Label(window, text="L", font=buttonFont1, height=2, width=4, bg='grey1', fg='white')
    l.grid(row=3, column=7, padx=5)

    l2 = Label(window, text="L", font=buttonFont1, height=2, width=4, bg='grey1', fg='white')
    l2.grid(row=3, column=8, padx=5)

    y = Label(window, text="Y", font=buttonFont1, height=2, width=4, bg='grey1', fg='white')
    y.grid(row=3, column=9, padx=5)

    w = Label(window, text="W", font=buttonFont1, height=2, width=4, bg='grey1', fg='white')
    w.grid(row=3, column=10, padx=5)

    o1 = Label(window, text="O", font=buttonFont1, height=2, width=4, bg='grey1', fg='white')
    o1.grid(row=3, column=11, padx=5)

    o2 = Label(window, text="O", font=buttonFont1, height=2, width=4, bg='grey1', fg='white')
    o2.grid(row=3, column=12, padx=5)

    d = Label(window, text="D", font=buttonFont1, height=2, width=4, bg='grey1', fg='white')
    d.grid(row=3, column=13,padx=5)

    '#-----------------clue'

    ran = random.choice(ram)

    if ran == 1:
        clue1 = Label(window, text="Word : Discredits Darkness, Antonym of darkness", font=buttonFont, height=1, width=45, bg='grey1', fg='misty rose')
        clue1.grid(row=5, column=1, columnspan=12, pady=30)
        w1 = ['b', 'u', 'l', 'b']
        ram.remove(1)
        #blank = [a1, b1, c1, d1]

    if ran == 2:
        clue2 = Label(window, text="Word : Loves fire, Blocks Current", font=buttonFont, height=1, width=45, bg='grey1', fg='misty rose')
        clue2.grid(row=5, column=1, columnspan=12, pady=30)
        w1 = ['w', 'o', 'o', 'd']
        ram.remove(2)
        #blank = [a1, b1, c1, d1]

    if ran == 3:
        clue3 = Label(window, text="Word :  High in calories............", font=buttonFont, height=1, width=45, bg='grey1', fg='misty rose')
        clue3.grid(row=5, column=1, columnspan=12, pady=30)
        w1 = ['c', 'a', 'k', 'e']
        ram.remove(3)
        #blank = [a1, b1, c1, d1]

    if ran == 4:
        clue4 = Label(window, text="Word : Highly rated, Useless", font=buttonFont, height=1, width=45, bg='grey1', fg='misty rose')
        clue4.grid(row=5, column=1, columnspan=12, pady=30)
        w1 = ['g', 'o', 'l', 'd']
        ram.remove(4)
        #blank = [a1, b1, c1, d1]

    if ran == 5:
        clue5 = Label(window, text="Word :  Time pass, No death", font=buttonFont, height=1, width=45,bg='grey1', fg='misty rose')
        clue5.grid(row=5, column=1, columnspan=12, pady=30)
        w1 = ['g', 'a', 'm', 'e']
        ram.remove(5)
        #blank = [a1, b1, c1, d1]

    if ran == 6:
        clue6 = Label(window, text="Word :  Small and large, Big family ", font=buttonFont, height=1, width=45,bg='grey1', fg='misty rose')
        clue6.grid(row=5, column=1, columnspan=12, pady=30)
        w1 = ['s', 't', 'a', 'r']
        ram.remove(6)
        #blank = [a1, b1, c1, d1]

    if ran == 7:
        clue7 = Label(window, text="Word :  Silica, Weight less........", font=buttonFont, height=1, width=45,bg='grey1', fg='misty rose')
        clue7.grid(row=5, column=1, columnspan=12, pady=30)
        w1 = ['s', 'a', 'n', 'd']
        ram.remove(7)
        #blank = [a1, b1, c1, d1]

    if ran == 8:
        clue8 = Label(window, text="Word :  One's imagination come True", font=buttonFont, height=1, width=45,bg='grey1', fg='misty rose')
        clue8.grid(row=5, column=1, columnspan=12, pady=30)
        w1 = ['f', 'i', 'l', 'm']
        ram.remove(8)
        #blank = [a1, b1, c1, d1]

    if ran == 9:
        clue9 = Label(window, text="Word : Has our Notes,............. ", font=buttonFont, height=1, width=45,bg='grey1', fg='misty rose')
        clue9.grid(row=5, column=1, columnspan=12, pady=30)
        w1 = ['b', 'a', 'n', 'k']
        ram.remove(9)
        #blank = [a1, b1, c1, d1]

    if ran == 10:
        clue10 = Label(window, text="Word : Same for all, Connect Quartz", font=buttonFont, height=1, width=45,bg='grey1', fg='misty rose')
        clue10.grid(row=5, column=1, columnspan=12, pady=30)
        w1 = ['t', 'i', 'm', 'e']
        ram.remove(10)
        #blank = [a1, b1, c1, d1]

    if ran == 11:
        e1 = Label(window, text="_", font=buttonFont2, height=1, width=2, fg='lemon chiffon', bg='grey1')
        e1.grid(row=7, column=9)
        clue11 = Label(window, text="Word : Angle of 66½°, swings and spins", font=buttonFont, height=1, width=45,bg='grey1', fg='misty rose')
        clue11.grid(row=5, column=1, columnspan=12, pady=30)
        w1 = ['e', 'a', 'r', 't', 'h']
        win = 6
        #blank = [a1, b1, c1, d1, e1]

    if ran == 12:
        e1 = Label(window, text="_", font=buttonFont2, height=1, width=2, fg='lemon chiffon', bg='grey1')
        e1.grid(row=7, column=9)
        clue11 = Label(window, text="Word : Silica filled, Bluish view", font=buttonFont, height=1, width=45,bg='grey1', fg='misty rose')
        clue11.grid(row=5, column=1, columnspan=12, pady=30)
        w1 = ['b', 'e', 'a', 'c', 'h']
        win = 6
        #blank = [a1, b1, c1, d1, e1]

    if ran == 13:
        e1 = Label(window, text="_", font=buttonFont2, height=1, width=2, fg='lemon chiffon', bg='grey1')
        e1.grid(row=7, column=9)
        clue11 = Label(window, text="Word : Moves things,convert power", font=buttonFont, height=1, width=45,bg='grey1', fg='misty rose')
        clue11.grid(row=5, column=1, columnspan=12, pady=30)
        w1 = ['m', 'o', 't', 'o', 'r']
        #blank = [a1, b1, c1, d1, e1]
        win = 6

    if ran == 14:
        e1 = Label(window, text="_", font=buttonFont2, height=1, width=2, fg='lemon chiffon', bg='grey1')
        e1.grid(row=7, column=9)
        clue11 = Label(window, text="Word : Fluid, Made of salt, water, protein", font=buttonFont, height=1, width=45, bg='grey1', fg='misty rose')
        clue11.grid(row=5, column=1, columnspan=12, pady=30)
        w1 = ['b', 'l', 'o', 'o', 'd']
        win = 6

    if ran == 15:
        e1 = Label(window, text="_", font=buttonFont2, height=1, width=2, fg='lemon chiffon', bg='grey1')
        e1.grid(row=7, column=9)
        clue11 = Label(window, text="Word : Divides things...........", font=buttonFont, height=1, width=45,bg='grey1', fg='misty rose')
        clue11.grid(row=5, column=1, columnspan=12, pady=30)
        w1 = ['k', 'n', 'i', 'f', 'e']
        win = 6

    if ran == 16:
        e1 = Label(window, text="_", font=buttonFont2, height=1, width=2, fg='lemon chiffon', bg='grey1')
        e1.grid(row=7, column=9)
        clue11 = Label(window, text="Word : Divides things...........", font=buttonFont, height=1, width=45, bg='grey1', fg='misty rose')
        clue11.grid(row=5, column=1, columnspan=12, pady=30)
        w1 = ['k', 'n', 'i', 'f', 'e']
        win = 6


    '#--------------word'
    a1 = Label(window, text="_", font=buttonFont2, height=1, width=2, fg='lemon chiffon', bg='grey1')
    a1.grid(row=7, column=5, pady=80)

    b1 = Label(window, text="_", font=buttonFont2, height=1, width=2, fg='lemon chiffon', bg='grey1')
    b1.grid(row=7, column=6)

    c1 = Label(window, text="_", font=buttonFont2, height=1, width=2, fg='lemon chiffon', bg='grey1')
    c1.grid(row=7, column=7)

    d1 = Label(window, text="_", font=buttonFont2, height=1, width=2, fg='lemon chiffon', bg='grey1')
    d1.grid(row=7, column=8)


    '#------------entry'
    def character_limit(entrytext):
        if len(entrytext.get()) > 0:
            entrytext.set(entrytext.get()[-1])

    entrytext = StringVar()
    entrytext.trace("w", lambda *args: character_limit(entrytext))

    ent = Entry(window, font=buttonFont2, width=3, fg='white',  textvariable=entrytext, bg='grey1', insertbackground='white', justify='center')
    ent.grid(row=10, column=11)



    '# --------------note'
    inf = Label(window, text="Enter an alphabet, To find the word : ", font=buttonFont, height=1, width=30, bg='grey1', fg='misty rose')
    inf.grid(row=10, column=5, columnspan=6)

    '#--------------------check box'

    check = Button(window, text='CHECK', font=buttonFont, height=1, width=7, bg='grey1', fg='white', command=check1)
    check.grid(row=10, column=12, columnspan=2, pady=1)

    '#-----------------label'

    note = Label(window, text='YOU GUESS, YOU WIN', font=buttonFont, height=1, width=20, bg='grey1', fg='white')
    note.grid(row=12, column=8, columnspan=4, pady=70)


def play2():
    global num, size
    if num < 10:
        size += 1
        play1.config(font=("bernard", size, 'bold'))
        num += 1
        window.after(10, play2)
    elif num == 10:
        play1.destroy()
        #Exit1.destroy()
        #Mute.destroy()
        page2()


def mute():
    click = mixer.Sound("Button Click 2.mp3")
    click.play()
    global count
    if count % 2 == 0:
        mixer.music.pause()
        count = count+1
        Mute["text"] = "UNMUTE"
    else:
        mixer.music.unpause()
        count = count + 1
        Mute["text"] = "MUTE"


def exit1():
    click = mixer.Sound("Button Click 2.mp3")
    click.play()
    answer = messagebox.askokcancel("Exit", "Are You sure?")
    if answer:
        window.destroy()
    else:
        pass


def play():
    click = mixer.Sound("Button Click 2.mp3")
    click.play()
    play2()


window = tkinter.Tk()
window.attributes('-fullscreen', True)
'#window.geometry("1300x800")'
window.title("sdk")
'#window.resizable(False, False)'

'# background music'
mixer.music.load("piano dark.mpeg")
mixer.music.play(-1)
mixer.music.set_volume(0.08)

'# background image----------'

image = Image.open('bg.jpg')
resiz = image.resize((1340, 790))
bg = ImageTk.PhotoImage(resiz)
"#canvas.create_image(0,0,anchor=NW,image=bg)"
img = Label(window, image=bg)
img.place(x=-2, y=-2)

'# font--------'

buttonFont = Font(family="URW Gothic L", size=23)
buttonFont2 = Font(family="URW Gothic L", size=27)
ExitFont = Font(family='bernard', size=15)
buttonFont1 = Font(family="URW Gothic L", size=30)
MuteFont = Font(family='bernard', size=15)
'# Buttons--------'

play1 = Button(window, text="PLAY", font=buttonFont, height=1, width=10, bg='grey1', fg='white', command=play)
play1.grid(row=2, column=3, padx=450, pady=310)

Exit1 = Button(window, text="EXIT", font=MuteFont, height=1, width=7, bg='grey51', fg='white', command=exit1)
Exit1.grid(row=3, column=1)

Mute = Button(window, text="MUTE", font=ExitFont, height=1, width=7, bg='grey51', fg='white', command=mute)
Mute.grid(row=3, column=5, padx=20)


window.mainloop()
