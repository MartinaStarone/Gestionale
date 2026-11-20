from tkinter import *
from PIL import Image, ImageTk
window = Tk() #instantiate an instance of a window
window.geometry("420x420")
window.title("Bilancio")
icon = PhotoImage(file='icon.png')#transform image in photoimage format
window.iconphoto(True, icon)
#change background color

window.config(background='white')

label = Label(window,
              text="Bilancio",
              font=('Arial',40,'bold'),
              fg ='green',
              bg='white',
              relief=SUNKEN,#border style RAISED
              bd=10,
              padx=20, #border from text#
              image = icon,
              compound = 'bottom'
     )
label.pack()#apply label to the window
#label.place(x=100, y=100)#position with coordinates
cnt =0
def click():
    global cnt
    cnt+=1
    label.config(text=cnt)
    label2.pack()
#buttons
button = Button(window,text="click me!!!")
button.pack()
button.config(command=click) #performs call back function
button.config(font=('Ink Free', 50, 'bold'))
button.config(bg='red')
button.config(fg='white')
button.config(activebackground='green')#changes background clicking on the button
button.config(activeforeground='white')
label = Label(window,text = cnt)
label.config(font=('Arial',20,'bold'))
label.pack()

#button.config(image=)
#button.config(compund ='left''right''top'...)
#button.pack()
#button.config(active=DISABLED)#disables buttons(ACTIVE/DISABLE)

label2 = Label(window,image=icon)
#entry widgets = textbox that accepts a single line of user input
def submit():
    username = entry.get()#gets the text and stores in user
    print("hello"+username)
def delete():
    entry.delete(0, END)#deletes the line of text

def backspace():
    entry.delete(len(entry.get()),END) #delete last char
submit = Button(window,text="submit",command=submit)
submit.pack(side=RIGHT)

delete = Button(window,text="delete",command=delete)
delete.pack(side=RIGHT)
backspace = Button(window,text="backspace",command=backspace)
backspace.pack(side=RIGHT)
entry = Entry()
entry.config(font=('Helvetica', 20, 'bold'))
entry.config(bg='#111111')
entry.config(fg='#00FF00')
#entry.insert(0,'Spongbob') inserts a script in the tab
entry.config(width=10)#size entry box
entry.config(show='*') #hides the things we write
entry.pack()


#Checkboxes
x = IntVar()
y = IntVar()
def display():
    if(x.get()==1)&(y.get()==0):
        print("I like Python")
    elif(x.get()==0)&(y.get()==1):
        print("I like Java")
    elif(x.get()==1)&(y.get()==1):
        print("I like both Python & Java")
    else:
        print("I don't like either")


python = Checkbutton(window, text = 'Python', variable = x, onvalue = 1, offvalue = 0, command = display)#unvalue = inizializza x, offvalue = valore finale

python.config(font=('Arial', 20))
python.config(fg = 'orange')
python.config(fg='#00FF00') #foreground color
python.config(bg='#000000') #background color
python.config(activeforeground='#0000FF') #active foreground color
python.config(activebackground='#000000') #active background color

photo = PhotoImage(file='python.png')
img = Image.open('python.png')
img.thumbnail((50,50))

photo1 = ImageTk.PhotoImage(img)
python.config(image=photo1, compound= 'left')#compounds leaves the text
python.config(padx=25, pady=10, width=250, height=50)
python.config(anchor='w') #anchor to west
python.pack(fill='x',padx=20,pady=10)

java = Checkbutton(window, text = 'Java', variable = y, onvalue = 1, offvalue = 0, command = display)#unvalue = inizializza x, offvalue = valore finale
java.pack()
java.config(font=('Arial', 20))
java.config(fg='#0000FF') #foreground color
java.config(bg='#000000') #background color
java.config(activeforeground='#0000FF') #active foreground color
java.config(activebackground='#000000') #active background color


img = Image.open('java.png')
img.thumbnail((50,50))

photo2 = ImageTk.PhotoImage(img)
java.config(image=photo2, compound= 'left')#compounds leaves the text
java.config(padx=25, pady=10, width=250, height=50)
java.config(anchor='w')
python.pack(fill='y',padx=20,pady=10)


#radiobuttons=similar to checkboxes, but only one from a group
def order():
    if(x.get()==0):
        print("You ordered pizza!")
    elif(x.get()==1):
        print("You ordered hamburger!")
    elif(x.get()==2):
        print("You ordered hotdog!")
    else:
        print("huh?")

x = IntVar()

food = ['pizza', 'hamburger', 'hotdog']

img = Image.open('pizza.png')
img.thumbnail((50,50))
pizzaImage = ImageTk.PhotoImage(img)
img = Image.open('hamburger.png')
img.thumbnail((50,50))
hamburgerImage = ImageTk.PhotoImage(img)
img = Image.open('hotdog.png')
img.thumbnail((50,50))
hotdogImage = ImageTk.PhotoImage(img)

image = [pizzaImage, hamburgerImage, hotdogImage]
for index in range(len(food)): #iterate once in the element of the list and creates one radiobutton for each
    radiobutton = Radiobutton(window,
                              text=food[index],#text to radio buttons
                              variable = x,#groups radiobuttons together
                              value = index,#assign each radiobutton a different value
                              padx = 25,
                              font = ("Courier 10 Pitch", 50),
                              image=image[index],
                              compound = 'left',
                              bg = 'white',
                              indicatoron = 0, #changes buttons
                              width = 375,
                              command = order
                              )
    radiobutton.pack(anchor='w')

#SCALES
def tmp():
    print("temp is:"+str(scale.get())+"degree")

hotLabel = Label(image=hotdogImage)
hotLabel.pack()
scale = Scale(window,from_= 0, to=100,
              length=600,
              orient= VERTICAL,
              font = ("DejaVu", 20),
              tickinterval = 10,#adds numeric indicator for value
              showvalue= 0, #hide current value next to the slider
              resolution = 5,
              troughcolor = '#69EAFF',
              fg = "#FF1C00"
              )#if write from_=100 to =0 scales up
scale.pack(anchor='w')
scale.set(50) #starting position of the slider
#scale.set(scale['from]-scale['to])/2)+scale['to']) makes it in the middle
button3 = Button(window, text='tmp', command = tmp)
button3.pack()
window.mainloop() #display window on computer screen and listen for events




