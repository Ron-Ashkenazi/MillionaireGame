from Question import Question
import random
from questionsList import *
from tkinter import *
import pygame
from tkinter import messagebox

pygame.init()
root = Tk()
root.title("Who Wants To Be A Millionaire")
root.geometry("1352x652+0+0")
root.configure(background="black")

# Randomize The Questions

random.shuffle(questions)
d = 0
while d < 15:
    rando = [questions[d].A1, questions[d].A2, questions[d].A3, questions[d].A4]
    random.shuffle(rando)

    questions[d].A1 = rando[0]
    questions[d].A2 = rando[1]
    questions[d].A3 = rando[2]
    questions[d].A4 = rando[3]
    d += 1

questions.append(ques16)
global value
value = "a"
global i
i = 0
q1 = PhotoImage(file="Picture1.png")
q2 = PhotoImage(file="Picture2.png")
q3 = PhotoImage(file="Picture3.png")
q4 = PhotoImage(file="Picture4.png")
q5 = PhotoImage(file="Picture5.png")
q6 = PhotoImage(file="Picture6.png")
q7 = PhotoImage(file="Picture7.png")
q8 = PhotoImage(file="Picture8.png")
q9 = PhotoImage(file="Picture9.png")
q10 = PhotoImage(file="Picture10.png")
q11 = PhotoImage(file="Picture11.png")
q12 = PhotoImage(file="Picture12.png")
q13 = PhotoImage(file="Picture13.png")
q14 = PhotoImage(file="Picture14.png")
q15 = PhotoImage(file="Picture15.png")
q16 = PhotoImage(file="Picture15.png")

MP = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16]

P_Answers = ["It might be ", "I think it's ", "Maybe ", "Definitely ", "Try ", "I would go for " ]

QQ = StringVar()
AA1 = StringVar()
AA2 = StringVar()
AA3 = StringVar()
AA4 = StringVar()
AAB1 = BooleanVar()
AAB2 = BooleanVar()
AAB3 = BooleanVar()
AAB4 = BooleanVar()


# Frames

ABC = Frame(root, bg="white")
ABC.grid()

ABC1 = Frame(root, bg="black", bd=20, width=900, height=600)
ABC1.grid(row=0, column=0)

ABC2 = Frame(root, bg="black", bd=20, width=452, height=600)
ABC2.grid(row=0, column=1)

ABC1a = Frame(ABC1, bg="black", bd=20, padx=100, width=900, height=200)
ABC1a.grid(row=0, column=0)

ABC1b = Frame(ABC1, bg="black", bd=20, width=900, height=200)
ABC1b.grid(row=1, column=0)

ABC1c = Frame(ABC1, bg="black", bd=20, width=900, height=200)
ABC1c.grid(row=2, column=0)


# Change Images
def starting():
    global AAB1
    global AAB2
    global AAB3
    global AAB4
    QQ.set(questions[i].Q)
    AA1.set(questions[i].A1[0])
    AA2.set(questions[i].A2[0])
    AA3.set(questions[i].A3[0])
    AA4.set(questions[i].A4[0])
    AAB1 = (questions[i].A1[1])
    AAB2 = (questions[i].A2[1])
    AAB3 = (questions[i].A3[1])
    AAB4 = (questions[i].A4[1])

def change50_50(A1, A2, A3, A4):
    global i
    canvas = Canvas(ABC1a, bg="black", width=180, height=70)
    canvas.grid(row=0, column=0)
    canvas.delete("all")
    image1 = PhotoImage(file="50X.png")
    canvas.create_image(90, 35, image=image1)
    canvas.image = image1
    if A1 == True:
        numbers = [2,3,4]
        value = random.choice(numbers)
        if value == 2:
            AA3.set("")
            AA4.set("")
        if value == 3:
            AA2.set("")
            AA4.set("")
        if value == 4:
            AA2.set("")
            AA3.set("")
    if A2 == True:
        numbers = [1, 3, 4]
        value = random.choice(numbers)
        if value == 1:
            AA3.set("")
            AA4.set("")
        if value == 3:
            AA1.set("")
            AA4.set("")
        if value == 4:
            AA1.set("")
            AA3.set("")
    if A3 == True:
        numbers = [1, 2, 4]
        value = random.choice(numbers)
        if value == 1:
            AA2.set("")
            AA4.set("")
        if value == 2:
            AA1.set("")
            AA4.set("")
        if value == 4:
            AA1.set("")
            AA2.set("")
    if A4 == True:
        numbers = [1, 2, 3]
        value = random.choice(numbers)
        if value == 1:
            AA2.set("")
            AA3.set("")
        if value == 2:
            AA1.set("")
            AA3.set("")
        if value == 3:
            AA1.set("")
            AA2.set("")


def change_people():
    canvas = Canvas(ABC1a, bg="black", width=180, height=70)
    canvas.grid(row=0, column=1)
    canvas.delete("all")
    image1 = PhotoImage(file="PeopleX.png")
    canvas.create_image(90, 35, image=image1)
    canvas.image = image1


def change_phone():
    canvas = Canvas(ABC1a, bg="black", width=180, height=70)
    canvas.grid(row=0, column=2)
    canvas.delete("all")
    image1 = PhotoImage(file="PhoneX.png")
    canvas.create_image(90, 35, image=image1)
    canvas.image = image1
    answers = [questions[i].A1[0], questions[i].A2[0], questions[i].A3[0], questions[i].A4[0]]
    global value
    value = random.choice(P_Answers) + random.choice(answers)
    global lblPhone
    lblPhone = Label(ABC1b, font=("ariel", 17, "bold"), text=value, bg="black", fg="white"
                         , bd=0, justify=CENTER)
    lblPhone.grid(row=1, column=0, pady=0, sticky=W)


def pick_answer(b):
    global AAB1
    global AAB2
    global AAB3
    global AAB4
    global i
    if value != "":
        lblPhone.destroy()

    if b == True:
        i += 1
        if i == 15:
            messagebox.showinfo("Won", "Congrats You Won")
        canvas = Canvas(ABC2, bg="black", width=370, height=600)
        canvas.grid(row=0, column=0)
        canvas.delete("all")
        image1 = MP[i]
        canvas.create_image(185, 300, image=image1)
        canvas.image = image1
        QQ.set(questions[i].Q)
        AA1.set(questions[i].A1[0])
        AA2.set(questions[i].A2[0])
        AA3.set(questions[i].A3[0])
        AA4.set(questions[i].A4[0])
        AAB1 = (questions[i].A1[1])
        AAB2 = (questions[i].A2[1])
        AAB3 = (questions[i].A3[1])
        AAB4 = (questions[i].A4[1])
    else:
        messagebox.showinfo("Lost", "You Lost")
        quit()

# Images

CenterImage = PhotoImage(file='center.png')
LogoCenter = Button(ABC1b, image=CenterImage, bg="black", width=300, height=200, command=starting)
LogoCenter.grid(row=0, column=0)

Image50_50 = PhotoImage(file='50.png.')
Logo50_50 = Button(ABC1a, image=Image50_50, bg="black", width=180, height=70,
                   command=lambda:change50_50(AAB1,AAB2,AAB3,AAB4))
Logo50_50.grid(row=0, column=0)

ImagePepole = PhotoImage(file='People.png')
LogoPepole = Button(ABC1a, image=ImagePepole, bg="black", width=180, height=70, command=change_people)
LogoPepole.grid(row=0, column=1)

ImagePhone = PhotoImage(file='Phone.png')
LogoPhone = Button(ABC1a, image=ImagePhone, bg="black", width=180, height=70, command=change_phone)
LogoPhone.grid(row=0, column=2)
lblPhone = Label(ABC1b, font=("ariel", 17, "bold"), text=value, bg="black", fg="white"
                         , bd=0, justify=CENTER)


ImageLevels = MP[i]
LogoLevels = Button(ABC2, image=ImageLevels, bg="black", width=370, height=600)
LogoLevels.grid(row=0, column=0)

# Text, Labels, Buttons

txtQuestion = Entry(ABC1c, font=("ariel", 14, "bold"), bg="white", fg="black",
                    bd=5, width=40, justify=CENTER, textvariable=QQ)
txtQuestion.grid(row=0, column=0, columnspan=4, pady=4)

lblQuestion1 = Label(ABC1c, font=("ariel", 14, "bold"), text="(1) ", bg="black", fg="white"
                     , bd=5, justify=CENTER)
lblQuestion1.grid(row=1, column=0, pady=4, sticky=W)

txtQuestion1 = Button(ABC1c, font=("ariel", 14, "bold"), bg="white", fg="black", command=lambda: pick_answer(AAB1),
                      bd=1, width=15, height=2, justify=CENTER, textvariable=AA1)
txtQuestion1.grid(row=1, column=1, pady=4)

lblQuestion2 = Label(ABC1c, font=("ariel", 14, "bold"), text="(2) ", bg="black",
                     fg="white", bd=5, justify=CENTER)
lblQuestion2.grid(row=1, column=2, pady=4, sticky=W)

txtQuestion2 = Button(ABC1c, font=("ariel", 14, "bold"), bg="white", fg="black", command=lambda: pick_answer(AAB2),
                      bd=1, width=15, height=2, justify=CENTER, textvariable=AA2)
txtQuestion2.grid(row=1, column=3, pady=4)

lblQuestion3 = Label(ABC1c, font=("ariel", 14, "bold"), text="(3) ", bg="black",
                     fg="white", bd=5, justify=CENTER)
lblQuestion3.grid(row=2, column=0, pady=4, sticky=W)

txtQuestion3 = Button(ABC1c, font=("ariel", 14, "bold"), bg="white", fg="black", command=lambda: pick_answer(AAB3),
                      bd=1, width=15, height=2, justify=CENTER, textvariable=AA3)
txtQuestion3.grid(row=2, column=1, pady=4)

lblQuestion4 = Label(ABC1c, font=("ariel", 14, "bold"), text="(4) ", bg="black",
                     fg="white", bd=5, justify=CENTER)
lblQuestion4.grid(row=2, column=2, pady=4, sticky=W)

txtQuestion4 = Button(ABC1c, font=("ariel", 14, "bold"), bg="white", fg="black", command=lambda: pick_answer(AAB4),
                      bd=1, width=15, height=2, justify=CENTER, textvariable=AA4)
txtQuestion4.grid(row=2, column=3, pady=4)

mainloop()