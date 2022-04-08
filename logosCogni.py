from tkinter import *
from PIL import ImageTk, Image
import random
import numpy as np

root=Tk()

########SCORES####################
global scored7
scored7=None

global task1_score
global task2_score
global task3_score
global task4_score
global task5_score
global task6_score
global task_7_score
global task_8_score
global task_9_score
global task10_score
task1_score=0
task2_score=0
task3_score=0
task4_score=0
task5_score=0
task6_score=0
task7_score=3
task8_score=11
task9_score=0
task10_score=0


#status='incomplete'
words=['man', 'cat', 'dog', 'mango', 'sunday', 'sit', 'dress', 'break', 'door', 'drag', 'dance', 'zoo', 'shirt', 'queen', 'country', 'yam', 'trust', 'grease', 'click', 'rest', 'mate', 'ship', 'car', 'salt', 'lock', 'train' ]
select_words=random.sample(words,k=5)


#constants for task 5
drag_data={'item':None, 'x':0, 'y':0}
s1,s2,s3,s4,s5=None,None,None,None,None

#for task 7
background=['green', 'blue', 'red','yellow','red', 'green', 'blue', 'red','yellow','black']
back_list_num=1
task_7_score=7

#for task 8
img_index=1

#for task 10
emotions=['happy', 'angry','sad','friendly', 'sick','shy','proud','surprised']
task10_img_index=0

def change_colour(b):
    if b['text'] in select_words:
        b['bg']='green'
        global task3_score
        task3_score+=1

    else:
        b['bg']='white'

def MousePress(event):
    drag_data['item']=canvas.find_closest(event.x,event.y)[0]
    drag_data['x']=event.x
    drag_data['y']=event.y

def MouseRelease(event):
    drag_data['item']=None
    drag_data['x']=0
    drag_data['y']=0

def drag(event):
    if drag_data['item'] in [s1,s2,s3,s4,s5]:
        canvas.move(drag_data['item'], event.x-drag_data['x'],event.y-drag_data['y'])
        drag_data['x']=event.x
        drag_data['y']=event.y
        
        

def show_time(time,t):
    canvas.create_text(50*time,100, text=f'{time} sec..', font='Tahoma 12 ')
    if time==10:
        if t=='t1':
            button=Button(canvas,text='click to continue to next task', font='Tahoma 15 bold',  bg='red' )
            button.place(x=300,y=100)
            button['command']=lambda b=button:task_2(b)
        if t=='t2':
            button=Button(canvas,text='click to continue to next task', font='Tahoma 15 bold',  bg='red' )
            button.place(x=300,y=100)
            button['command']=lambda b=button:task_3(b)
            
        if t=='t3':
            label=Label(canvas, text='Can you remember the five words shown to you earlier?\nIf you can find them here, click them.', font='Tahoma 20 bold', bg='green')
            label.place(x=20, y=100)

            b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23,b24,b25=None, None, None, None,None, None, None, None,None, None, None, None,None, None, None, None,None, None, None, None,None,None, None, None, None
            button=[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23,b24,b25]
            for i in range (25):
                button[i]=Button(canvas,text=words[i], font='Tahoma 15 bold',  bg='blue', width=6, compound='c')    
                button[i].place(x=100*(i%8)+10,y=np.floor(i/8)*50+400)            
                button[i]['command']=lambda b=button[i]:change_colour(b)
            
            next_button=Button(canvas,text='click to continue to next task', font='Tahoma 15 bold',  bg='red' )
            next_button.place(x=300,y=50)
            next_button['command']=lambda b=button, b_=next_button, l=label:task_4(b,b_,l)


def task_2(button):
    button.destroy()
    instruction=canvas.create_text(380,150, text='Learning and memory: Task 2\n\nTake note of these alphabets, you will be asked to recall them (later).', font='Tahoma 15 bold')

    #numbers to be shown
    letters=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    number=random.sample(letters, k=5)
    
    global letter_task
    letter_task=list(number)

    #show number
    number1=Label(canvas, text=number[0],font='Tahoma 20 bold', bg='yellow' )
    number1.place(x=330, y=270)

    number2=Label(canvas, text=number[1],font='Tahoma 20 bold', bg='yellow' )
    number2.place(x=360, y=270)

    number3=Label(canvas, text=number[2],font='Tahoma 20 bold', bg='yellow' )
    number3.place(x=390, y=270)

    number4=Label(canvas, text=number[3],font='Tahoma 20 bold', bg='yellow' )
    number4.place(x=420, y=270)

    number5=Label(canvas, text=number[4],font='Tahoma 20 bold', bg='yellow' )
    number5.place(x=450, y=270)

    #show time
    root.after(1000, lambda:show_time(1,'t2'))
    root.after(2000, lambda:show_time(2,'t2'))
    root.after(3000, lambda:show_time(3,'t2'))
    root.after(4000, lambda:show_time(4,'t2'))
    root.after(5000, lambda:show_time(5,'t2'))
    root.after(6000, lambda:show_time(6,'t2'))
    root.after(7000, lambda:show_time(7,'t2'))
    root.after(8000, lambda:show_time(8,'t2'))
    root.after(9000, lambda:show_time(9,'t2'))
    root.after(10000, lambda:show_time(10,'t2'))


###remove everything after 10 seconds
    number1.after(10000, lambda:number1.destroy())
    number2.after(10000, lambda:number2.destroy())
    number3.after(10000, lambda:number3.destroy())
    number4.after(10000, lambda:number4.destroy())
    number5.after(10000, lambda:number5.destroy())

    root.after(10000, lambda: canvas.delete('all'))
    
def task_3(button):
    button.destroy()
    instruction=canvas.create_text(350,150, text='Learning and memory: Task 3\n\nTake note of these words, you will be asked to recall them (later).', font='Tahoma 15 bold')

    #numbers to be shown
    number=select_words

    #show number
    number1=Label(canvas, text=number[0],font='Tahoma 20 bold', bg='yellow' )
    number1.place(x=300, y=270)

    number2=Label(canvas, text=number[1],font='Tahoma 20 bold', bg='yellow' )
    number2.place(x=400, y=270)

    number3=Label(canvas, text=number[2],font='Tahoma 20 bold', bg='yellow' )
    number3.place(x=500, y=270)

    number4=Label(canvas, text=number[3],font='Tahoma 20 bold', bg='yellow' )
    number4.place(x=350, y=350)

    number5=Label(canvas, text=number[4],font='Tahoma 20 bold', bg='yellow' )
    number5.place(x=450, y=350)

    #show time
    root.after(1000, lambda:show_time(1,'t3'))
    root.after(2000, lambda:show_time(2,'t3'))
    root.after(3000, lambda:show_time(3,'t3'))
    root.after(4000, lambda:show_time(4,'t3'))
    root.after(5000, lambda:show_time(5,'t3'))
    root.after(6000, lambda:show_time(6,'t3'))
    root.after(7000, lambda:show_time(7,'t3'))
    root.after(8000, lambda:show_time(8,'t3'))
    root.after(9000, lambda:show_time(9,'t3'))
    root.after(10000, lambda:show_time(10,'t3'))


###remove everything after 10 seconds
    number1.after(10000, lambda:number1.destroy())
    number2.after(10000, lambda:number2.destroy())
    number3.after(10000, lambda:number3.destroy())
    number4.after(10000, lambda:number4.destroy())
    number5.after(10000, lambda:number5.destroy())

    root.after(10000, lambda: canvas.delete('all'))
   
def task_4(b,b_,l):
    l.destroy()
    b_.destroy()
    for i in b:
        i.destroy()
    instruction=canvas.create_text(400,150, text='Learning: Task 1 (Naming)\n\nIn this task you are to match the pictures below with a word describing  them.\nYou would need to pick your words from list below', font='Tahoma 15 bold')
    #photos={'guiter','umbrella', 'pot', 'frying-pan', 'pencil','carrot', 'horse', 'mosque' }
    
    root.carrot=carrot=ImageTk.PhotoImage(Image.open('./Images/carrot.jpg'))
    root.frying_pan=frying_pan=ImageTk.PhotoImage(Image.open('./Images/frying-pan.jpg'))
    root.guiter=guiter=ImageTk.PhotoImage(Image.open('./Images/guitar.jpg'))
    root.pot=pot=ImageTk.PhotoImage(Image.open('./Images/pot.jpg'))
    root.pencil=pencil=ImageTk.PhotoImage(Image.open('./Images/pencil.jpg'))

    root.horse=horse=ImageTk.PhotoImage(Image.open('./Images/horse.jpg'))
    root.mosque=mosque=ImageTk.PhotoImage(Image.open('./Images/mosque.jpg'))
    root.plane=plane=ImageTk.PhotoImage(Image.open('./Images/plane.jpg'))
    #root.church=church=ImageTk.PhotoImage(Image.open('./Images/church.png'))
    
        
    canvas.create_image(150,(230+(50)), image=horse)
    canvas.create_image(150,(230+(110)), image=mosque)
    canvas.create_image(150,(230+(170)), image=plane)
    canvas.create_image(150,(230+(230)), image=pencil)
    l_horse, l_mosque, l_plane, l_pencil=Entry(canvas, font='Tahoma 15 bold', width=10),Entry(canvas, font='Tahoma 15 bold', width=10),Entry(canvas, font='Tahoma 15 bold', width=10),Entry(canvas, font='Tahoma 15 bold', width=10)
    l_horse.place(x=200,y=230+(30))
    l_mosque.place(x=200,y=230+(90))
    l_plane.place(x=200,y=230+(160))
    l_pencil.place(x=200,y=230+(220))

    l_carrot, l_frying_pan, l_guitar, l_pot=Entry(canvas, font='Tahoma 15 bold', width=10),Entry(canvas, font='Tahoma 15 bold', width=10),Entry(canvas, font='Tahoma 15 bold', width=10),Entry(canvas, font='Tahoma 15 bold', width=10)
    l_carrot.place(x=450,y=230+(30))
    l_frying_pan.place(x=450,y=230+(90))
    l_guitar.place(x=450,y=230+(160))
    l_pot.place(x=450,y=230+(220))

    canvas.create_image(400,(230+(50)), image=carrot)
    canvas.create_image(400,(230+(110)), image=frying_pan)
    canvas.create_image(400,(230+(170)), image=guiter)
    canvas.create_image(400,(230+(230)), image=pot)
  
    l1=Label(canvas, text='GUITAR    UMBRELLA    RATS  POT FRYING-PAN  PENCIL  CARROT',font='Tahoma 15 bold', bg='yellow')
    l1.place(x=40,y=550)

    l2=Label(canvas, text='HORSE    MONKEY    PLANE  BIRD SCHOOL  HOUSE  CHURCH   MOSQUE      ',font='Tahoma 15 bold', bg='yellow')
    l2.place(x=40,y=580)

    finito=Button(canvas,text='COMPLETE', font='Tahoma 15 bold',  bg='green' )
    finito.place(x=300,y=500)
    finito['command']=lambda f=finito:task_5(f,l1,l2,l_horse, l_mosque, l_plane, l_pencil, l_carrot, l_frying_pan, l_guitar, l_pot)

def task_5(f,l1,l2,l_horse, l_mosque, l_plane, l_pencil, l_carrot, l_frying_pan, l_guitar, l_pot):
    global task4_score
    if l_horse.get().upper()=='HORSE':
        task4_score+=1
    if l_mosque.get().upper()=='MOSQUE':
        task4_score+=1
    if l_plane.get().upper()=='PLANE':
        task4_score+=1
    if l_pencil.get().upper()=='PENCIL':
        task4_score+=1
    if l_carrot.get().upper()=='CARROT':
        task4_score+=1
    if l_frying_pan.get().upper()=='FRYING-PAN':
        task4_score+=1
    if l_guitar.get().upper()=='GUITAR':
        task4_score+=1
    if l_pot.get().upper()=='POT':
        task4_score+=1
    print(task4_score)
    f.destroy()
    l1.destroy()
    l2.destroy()

    l_horse.destroy()
    l_mosque.destroy()
    l_plane.destroy()
    l_pencil.destroy()

    l_carrot.destroy()
    l_frying_pan.destroy()
    l_guitar.destroy()
    l_pot.destroy()

    canvas.delete('all')
    instruction=canvas.create_text(450,50, text='Learning: Task 2 (Comprehension)\n\nIn this task you are to match the group of pictures with a suitable descriptive word.\nYou would need to pick your words from list below', font='Tahoma 15 bold')

    root.cat=cat=ImageTk.PhotoImage(Image.open('./Images/cat.jpg'))
    root.dog=dog=ImageTk.PhotoImage(Image.open('./Images/dog.jpg'))
    root.bird=bird=ImageTk.PhotoImage(Image.open('./Images/bird.jpg'))
    root.tortoise=tortoise=ImageTk.PhotoImage(Image.open('./Images/tortoise.jpg'))
    root.lion=lion=ImageTk.PhotoImage(Image.open('./Images/lion.jpg'))

    root.car=car=ImageTk.PhotoImage(Image.open('./Images/car.jpg'))
    root.ship=ship=ImageTk.PhotoImage(Image.open('./Images/ship.jpg'))
    root.plane=plane=ImageTk.PhotoImage(Image.open('./Images/plane.jpg'))
    root.train=train=ImageTk.PhotoImage(Image.open('./Images/train.jpg'))
    root.truck=truck=ImageTk.PhotoImage(Image.open('./Images/truck.jpg'))

    root.mango=mango=ImageTk.PhotoImage(Image.open('./Images/mango.jpg'))
    root.apple=apple=ImageTk.PhotoImage(Image.open('./Images/apple.jpg'))
    root.bananna=bananna=ImageTk.PhotoImage(Image.open('./Images/bananna.jpg'))
    root.cucumber=cucumber=ImageTk.PhotoImage(Image.open('./Images/cucumber.jpg'))

    root.van=van=ImageTk.PhotoImage(Image.open('./Images/van.jpg'))
    root.house=house=ImageTk.PhotoImage(Image.open('./Images/house.jpg'))
    root.freezer=freezer=ImageTk.PhotoImage(Image.open('./Images/freezer.jpg'))
    root.drawer=drawer=ImageTk.PhotoImage(Image.open('./Images/drawer.jpg'))

    root.phone=phone=ImageTk.PhotoImage(Image.open('./Images/phone.jpg'))
    root.letters=letters=ImageTk.PhotoImage(Image.open('./Images/letters.jpg'))
    root.microphone=microphone=ImageTk.PhotoImage(Image.open('./Images/microphone.jpg'))
    root.email=email=ImageTk.PhotoImage(Image.open('./Images/email.jpg'))
        
    canvas.create_image(100,(100+(50)), image=cat)
    canvas.create_image(170,(100+(50)), image=dog)    
    canvas.create_image(240,(100+(50)), image=bird)
    canvas.create_image(310,(100+(50)), image=tortoise)
    canvas.create_image(380,(100+(50)), image=lion)
    
    canvas.create_image(100,(180+(50)), image=car)
    canvas.create_image(170,(180+(50)), image=ship)    
    canvas.create_image(240,(180+(50)), image=plane)
    canvas.create_image(310,(180+(50)), image=train)
    canvas.create_image(380,(180+(50)), image=truck)
    
    canvas.create_image(100,(260+(50)), image=mango)
    canvas.create_image(170,(260+(50)), image=apple)    
    canvas.create_image(240,(260+(50)), image=bananna)
    canvas.create_image(310,(260+(50)), image=cucumber)
    
    canvas.create_image(100,(340+(50)), image=van)
    canvas.create_image(170,(340+(50)), image=house)    
    canvas.create_image(240,(340+(50)), image=freezer)
    canvas.create_image(310,(340+(50)), image=drawer)

    canvas.create_image(100,(420+(50)), image=phone)
    canvas.create_image(170,(420+(50)), image=letters)    
    canvas.create_image(240,(420+(50)), image=microphone)
    canvas.create_image(310,(420+(50)), image=email)

    group1, group2, group3, group4, group5=Entry(canvas, font='Tahoma 15 bold', width=10),Entry(canvas, font='Tahoma 15 bold', width=10),Entry(canvas, font='Tahoma 15 bold', width=10),Entry(canvas, font='Tahoma 15 bold', width=10),Entry(canvas, font='Tahoma 15 bold', width=10)
    group1.place(x=460,y=90+(50))
    group2.place(x=460,y=170+(50))
    group3.place(x=460,y=250+(50))
    group4.place(x=460,y=330+(50))    
    group5.place(x=460,y=410+(50))

    l1=Label(canvas, text='ANIMAL    PETS    FOOD  VEGETABLES FRUITS TRANSPORT  ',font='Tahoma 15 bold', bg='yellow')
    l1.place(x=40,y=550)

    l2=Label(canvas, text=' INFORMATION    STORAGE  COMMUNICATION SOCIALIZATION  ',font='Tahoma 15 bold', bg='yellow')
    l2.place(x=40,y=580)

    finito=Button(canvas,text='COMPLETE', font='Tahoma 15 bold',  bg='green' )
    finito.place(x=300,y=500)
    finito['command']=lambda f=finito:task_query(f,l1,l2,group1, group2, group3, group4, group5)

def task_query(f,l1,l2,group1, group2, group3, group4, group5):
    global task5_score
    if group1.get().upper()=='ANIMAL':
        task5_score+=1
    if group2.get().upper()=='TRANSPORT':
        task5_score+=1
    if group3.get().upper()=='FRUITS':
        task5_score+=1
    if group4.get().upper()=='STORAGE':
        task5_score+=1
    if group5.get().upper()=='COMMUNICATION':
        task5_score+=1

    f.destroy()
    l1.destroy()
    l2.destroy()

    group1.destroy()
    group2.destroy()
    group3.destroy()
    group4.destroy()
    group5.destroy()

    canvas.delete('all')
    instruction=canvas.create_text(450,50, text='Learning & Memory: \n\nCan you remember the numbers that were shown to you earlier? What were they?', font='Tahoma 15 bold')
    label_num=Label(root, text='Numbers:',font='Tahoma 25 bold',width=10)
    label_num.place(x=200, y=200)

    answer_num1=Entry(root, font='Tahoma 25 bold',width=1)
    answer_num1.place(x=400, y=200)
    answer_num2=Entry(root, font='Tahoma 25 bold',width=1)
    answer_num2.place(x=430, y=200)
    answer_num3=Entry(root, font='Tahoma 25 bold',width=1)
    answer_num3.place(x=460, y=200)
    answer_num4=Entry(root, font='Tahoma 25 bold',width=1)
    answer_num4.place(x=490, y=200)
    answer_num5=Entry(root, font='Tahoma 25 bold',width=1)
    answer_num5.place(x=520, y=200)
 
    label_lett=Label(root, text='Letters:',font='Tahoma 25 bold',width=10)
    label_lett.place(x=200, y=270)
    answer_let1=Entry(root, font='Tahoma 25 bold',width=1)
    answer_let1.place(x=400, y=270)
    answer_let2=Entry(root, font='Tahoma 25 bold',width=1)
    answer_let2.place(x=430, y=270)
    answer_let3=Entry(root, font='Tahoma 25 bold',width=1)
    answer_let3.place(x=460, y=270)
    answer_let4=Entry(root, font='Tahoma 25 bold',width=1)
    answer_let4.place(x=490, y=270)
    answer_let5=Entry(root, font='Tahoma 25 bold',width=1)
    answer_let5.place(x=520, y=270)
    



    finito=Button(canvas,text='COMPLETE', font='Tahoma 15 bold',  bg='green' )
    finito.place(x=300,y=500)
    finito['command']=lambda f=finito:task_6(f,label_lett,answer_let1,answer_let2,answer_let3,answer_let4,answer_let5, label_num,answer_num1,answer_num2,answer_num3,answer_num4,answer_num5)

def task_6(f,label_lett,answer_let1,answer_let2,answer_let3,answer_let4,answer_let5, label_num,answer_num1,answer_num2,answer_num3,answer_num4,answer_num5):
    ######conduct scoring for the two tasks 
    global task1_score
    global task2_score
    task1_score=0
    task2_score=0

    if answer_num1.get() in  number_task:
        task1_score+=1
    if answer_num1.get() ==  number_task[0]:
        task1_score+=1  
    if answer_num2.get() in  number_task:
        task1_score+=1
    if answer_num2.get() ==  number_task[1]:
        task1_score+=1
    if answer_num3.get() in  number_task:
        task1_score+=1
    if answer_num3.get() ==  number_task[2]:
        task1_score+=1  
    if answer_num4.get() in  number_task:
        task1_score+=1
    if answer_num4.get() ==  number_task[3]:
        task1_score+=1
    if answer_num5.get() in  number_task:
        task1_score+=1
    if answer_num5.get() ==  number_task[4]:
        task1_score+=1

    if answer_let1.get().upper() in  letter_task:
        task2_score+=1
    if answer_let1.get().upper() ==  letter_task[0]:
        task2_score+=1  
    if answer_let2.get().upper() in  letter_task:
        task2_score+=1
    if answer_let2.get().upper() ==  letter_task[1]:
        task2_score+=1
    if answer_let3.get().upper() in  letter_task:
        task2_score+=1
    if answer_let3.get().upper() ==  letter_task[2]:
        task2_score+=1  
    if answer_let4.get().upper() in  letter_task:
        task2_score+=1
    if answer_let4.get().upper() ==  letter_task[3]:
        task2_score+=1
    if answer_let5.get().upper() in  letter_task:
        task2_score+=1
    if answer_let5.get().upper() ==  letter_task[4]:
        task2_score+=1


    print(task1_score)
    f.destroy()
    label_lett.destroy()
    answer_let1.destroy()
    answer_let2.destroy()
    answer_let3.destroy()
    answer_let4.destroy()
    answer_let5.destroy()
    label_num.destroy()
    answer_num1.destroy()
    answer_num2.destroy()
    answer_num3.destroy()
    answer_num4.destroy()
    answer_num5.destroy()

    canvas.delete('all')
    ######task 7 code starts here##########
    instruction=canvas.create_text(450,50, text='Executive:\n\nPlease arrange these cards from the smallest to the largest number', font='Tahoma 15 bold')

    card_set=[f'{i}.jpg' for i in range(1,31)]
    temp=random.sample(card_set,k=5)
    global select_cards
    select_cards=temp
    
    root.pic_a=pic_a=ImageTk.PhotoImage(Image.open(f'./Images/{select_cards[0]}'))
    root.pic_b=pic_b=ImageTk.PhotoImage(Image.open(f'./Images/{select_cards[1]}'))
    root.pic_c=pic_c=ImageTk.PhotoImage(Image.open(f'./Images/{select_cards[2]}'))
    root.pic_d=pic_d=ImageTk.PhotoImage(Image.open(f'./Images/{select_cards[3]}'))
    root.pic_e=pic_e=ImageTk.PhotoImage(Image.open(f'./Images/{select_cards[4]}'))

    global s1,s2,s3,s4,s5      
    s1=canvas.create_image(100,(300+(50)), image=pic_a)
    s2=canvas.create_image(250,(300+(50)), image=pic_b) 
    s3=canvas.create_image(400,(300+(50)), image=pic_c)
    s4=canvas.create_image(550,(300+(50)), image=pic_d) 
    s5=canvas.create_image(700,(300+(50)), image=pic_e)
        
    for i in range (5):
        canvas.create_rectangle(50+(i*150),100, 150+(i*150),200)

    canvas.bind('<ButtonPress>',MousePress)
    canvas.bind('<ButtonRelease>', MouseRelease)
    canvas.bind('<Motion>', drag)
    
    finito=Button(canvas,text='COMPLETE', font='Tahoma 15 bold',  bg='green' )
    finito.place(x=300,y=500)
    finito['command']=lambda f=finito:task_7(f)

def task_7(f):
    result=({select_cards[0].split('.')[0]:canvas.coords(s1)[0], select_cards[1].split('.')[0]:canvas.coords(s2)[0], select_cards[2].split('.')[0]:canvas.coords(s3)[0], select_cards[3].split('.')[0]:canvas.coords(s4)[0], select_cards[4].split('.')[0]:canvas.coords(s5)[0]})
    result=dict(sorted(result.items(),key=lambda item:item[1])).keys()
  
    result=[int(item) for item in result]
    answer=sorted(result)
    
    for i in range (5):
        if answer[i]==result[i]:
            global task6_score
            task6_score+=2
            
    f.destroy()
    canvas.delete('all')
    #####Task 7 starts here#######################

    instruction=canvas.create_text(400,50, text='Psychomotor/attention/concentration: Task 1\n\nIn this task, images of different colours appear for 5 seconds\nTap on colour ‘RED’ anytime it pops up', font='Tahoma 15 bold')
    
    finito=Button(canvas,text='                 \n                                  \n                 ', font='Tahoma 15 bold',  bg=background[0])   
    finito.place(x=300,y=250)
    canvas.after(5000,lambda:task_7b(finito))


     
def task_7b(f):
    global back_list_num
    f.destroy()
    finito=Button(canvas,text='                 \n                                  \n                 ', font='Tahoma 15 bold',  bg=background[back_list_num])   
    finito.place(x=300,y=250)
    finito['command']=lambda:task_7_scorer(finito)
    back_list_num+=1
    if back_list_num>9:
        global scored7
        scored7=False
        finito.destroy()
        canvas.delete('all')
        next=Button(canvas,text='Click to move to the next task', font='Tahoma 15 bold',  bg='red')   
        next.place(x=300,y=100)
        next['command']=lambda f=next:task_8(f)
    else:
        canvas.after(5000,lambda:task_7b(finito))
def task_7_scorer(f):
    global task_7_score
    global scored7
    if scored7==False:
        if f['background']=='red':
            task_7_score+=1
            scored7=True
        else:
            task_7_score-=1
            scored7=True
      


def task_8(f,):
    print('Score 7', task_7_score)
    f.destroy()
    canvas.delete('all')
    instruction=canvas.create_text(450,50, text='Psychomotor/attention/concentration: Task 2\n\nIn this task, images of different objects and numbers appear for 5 seconds\nTap on the images or numbers displayed begins with a letter \'F\' when they appear', font='Tahoma 15 bold')

    global s1 
    global s2
    global s3 
    global s4
    global s5
    global s6 
    global s7
    global s8 
    global s9
    global s10 
    global s11 
    global s12
    global s13 
    global s14
    global s15
    global s16 
    global s17
    global s18 
    global s19
    global s20  

    image_task8=['five.jpg', 'two.jpg', 'eight.jpg', 'flute.jpg','phone.jpg','facial.jpg', 'chair.jpg','58.jpg','fork.jpg', '85.jpg', 'book.jpg', 'house.jpg','face-cap.jpg', 'fingerprint.jpg', 'television.jpg', 'fan.jpg', 'pencil.jpg','frame.jpg', 'car.jpg', 'dog.jpg']

    root.s1=s1=ImageTk.PhotoImage(Image.open(f'./Images/{image_task8[0]}'))
    root.s2=s2=ImageTk.PhotoImage(Image.open(f'./Images/{image_task8[1]}'))
    root.s3=s3=ImageTk.PhotoImage(Image.open(f'./Images/{image_task8[2]}'))
    root.s4=s4=ImageTk.PhotoImage(Image.open(f'./Images/{image_task8[3]}'))
    root.s5=s5=ImageTk.PhotoImage(Image.open(f'./Images/{image_task8[4]}'))
    root.s6=s6=ImageTk.PhotoImage(Image.open(f'./Images/{image_task8[5]}'))
    root.s7=s7=ImageTk.PhotoImage(Image.open(f'./Images/{image_task8[6]}'))
    root.s8=s8=ImageTk.PhotoImage(Image.open(f'./Images/{image_task8[7]}'))
    root.s9=s9=ImageTk.PhotoImage(Image.open(f'./Images/{image_task8[8]}'))
    root.s10=s10=ImageTk.PhotoImage(Image.open(f'./Images/{image_task8[10]}'))
    root.s11=s11=ImageTk.PhotoImage(Image.open(f'./Images/{image_task8[11]}'))
    root.s12=s12=ImageTk.PhotoImage(Image.open(f'./Images/{image_task8[12]}'))
    root.s13=s13=ImageTk.PhotoImage(Image.open(f'./Images/{image_task8[13]}'))
    root.s14=s14=ImageTk.PhotoImage(Image.open(f'./Images/{image_task8[14]}'))
    root.s15=s15=ImageTk.PhotoImage(Image.open(f'./Images/{image_task8[15]}'))
    root.s16=s16=ImageTk.PhotoImage(Image.open(f'./Images/{image_task8[16]}'))
    root.s17=s17=ImageTk.PhotoImage(Image.open(f'./Images/{image_task8[17]}'))
    root.s18=s18=ImageTk.PhotoImage(Image.open(f'./Images/{image_task8[18]}'))
    root.s19=s19=ImageTk.PhotoImage(Image.open(f'./Images/{image_task8[19]}'))
    root.s20=s20=ImageTk.PhotoImage(Image.open(f'./Images/{image_task8[9]}'))
    
    global s
    s=[s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20]
    finito=Button(canvas,image=s1)   
    finito.place(x=300,y=250)
    finito['command']=lambda:task_8_scorer(img_index)
    canvas.after(5000,lambda:task_8b(finito))


     
def task_8b(f):
    global img_index
    f.destroy()
    finito=Button(canvas,image=s[img_index])   
    finito.place(x=300,y=250)
    finito['command']=lambda:task_8_scorer(img_index)
    img_index+=1
    
    if img_index>19:
        finito.destroy()
        canvas.delete('all')
        next=Button(canvas,text='Click to move to the next task', font='Tahoma 15 bold',  bg='red')   
        next.place(x=300,y=100)
        next['command']=lambda f=next:task_9(f)
    else:
        canvas.after(5000,lambda:task_8b(finito))

def task_8_scorer(sj):
    global task8_score
    if sj in [1,4,6,8,9,13,14,16,18]:
        task8_score+=1
    else:
        task8_score-=1

      
def task_9(f,):
    f.destroy()
    canvas.delete('all')
    instruction=canvas.create_text(420,100, text='Attention /concentration:\n\nPlease provide the answers to these questions.', font='Tahoma 18 bold', )
    q1a=Label(canvas, text='    T   U\n         3\n+\n         5', font='times 17 bold')
    q1a.place(x=50, y=200)
    q1_answer=Entry(canvas, font='times 17 bold', width=6)
    q1_answer.place(x=60,y=310)

    q2a=Label(canvas, text='    T   U\n         2\n+\n          7', font='times 17 bold')
    q2a.place(x=150, y=200)
    q2_answer=Entry(canvas, font='times 17 bold', width=6)
    q2_answer.place(x=160,y=310)

    q3a=Label(canvas, text='    T   U\n         6\n-\n         4', font='times 17 bold')
    q3a.place(x=250, y=200)
    q3_answer=Entry(canvas, font='times 17 bold', width=6)
    q3_answer.place(x=260,y=310)

    q4a=Label(canvas, text='    T   U\n         8\n+\n         7', font='times 17 bold')
    q4a.place(x=350, y=200)
    q4_answer=Entry(canvas, font='times 17 bold', width=6)
    q4_answer.place(x=360,y=310)

    q5a=Label(canvas, text='    T   U\n         5\n+\n         9', font='times 17 bold')
    q5a.place(x=450, y=200)
    q5_answer=Entry(canvas, font='times 17 bold', width=6)
    q5_answer.place(x=460,y=310)


    q6a=Label(canvas, text='    T   U\n    1   6\n-\n         7', font='times 17 bold')
    q6a.place(x=550, y=200)
    q6_answer=Entry(canvas, font='times 17 bold', width=6)
    q6_answer.place(x=560,y=310)

    q7a=Label(canvas, text='    T   U\n    4   1\n-\n    2   4', font='times 17 bold')
    q7a.place(x=650, y=200)
    q7_answer=Entry(canvas, font='times 17 bold', width=6)
    q7_answer.place(x=660,y=310)

    q8a=Label(canvas, text='    T   U\n    3   3\n+\n    2   7', font='times 17 bold')
    q8a.place(x=750, y=200)
    q8_answer=Entry(canvas, font='times 17 bold', width=6)
    q8_answer.place(x=760,y=310)


    q9a=Label(canvas, text='    T   U\n    6   4\n-\n    3   5', font='times 17 bold')
    q9a.place(x=850, y=200)
    q9_answer=Entry(canvas, font='times 17 bold', width=6)
    q9_answer.place(x=860,y=310)

    q10a=Label(canvas, text='    T   U\n    8   7\n-\n    6   5', font='times 17 bold')
    q10a.place(x=50, y=380)
    q10_answer=Entry(canvas, font='times 17 bold', width=6)
    q10_answer.place(x=60,y=490)

    finito=Button(canvas,text='COMPLETE', font='Tahoma 15 bold',  bg='green' )
    finito.place(x=400,y=550)

    finito['command']=lambda f=finito:task_10(f,[q1a,q2a,q3a,q4a,q5a,q6a,q7a,q8a,q9a,q10a],[q1_answer,q2_answer,q3_answer,q4_answer,q5_answer,q6_answer,q7_answer,q8_answer,q9_answer,q10_answer])


def task_10(f,ls,ls2):
    global task9_score
    if len(ls2[0].get()) > 0:
        task9_score+=1
    if ls2[0].get()==8:
        task9_score+=1
    if len(ls2[1].get()) > 0:
        task9_score+=1
    if ls2[1].get()==9:
        task9_score+=1
    if len(ls2[2].get()) > 0:
        task9_score+=1
    if ls2[2].get()==10:
        task9_score+=1
    if len(ls2[3].get()) > 0:
        task9_score+=1
    if ls2[3].get()==15:
        task9_score+=1

    if len(ls2[4].get()) > 0:
        task9_score+=1
    if ls2[4].get()==14:
        task9_score+=1
    if len(ls2[5].get()) > 0:
        task9_score+=1
    if ls2[5].get()==23:
        task9_score+=1
    if len(ls2[6].get()) > 0:
        task9_score+=1
    if ls2[6].get()==65:
        task9_score+=1
    if len(ls2[7].get()) > 0:
        task9_score+=1
    if ls2[7].get()==60:
        task9_score+=1
    if len(ls2[8].get()) > 0:
        task9_score+=1
    if ls2[8].get()==99:
        task9_score+=1
    if len(ls2[9].get()) > 0:
        task9_score+=1
    if ls2[9].get()==152:
        task9_score+=1

   #Task 10 starts here 
    for item in ls:
        item.destroy()
    for item in ls2:
        item.destroy()
    f.destroy()
    canvas.delete('all')
    instruction=canvas.create_text(450,100, text='Social Cognition:\n\nPlease click on the word that matches the emotion/state \ndescribed in the picture.', font='Tahoma 18 bold', )
    global s1 
    global s2
    global s3 
    global s4
    global s5
    global s6 
    global s7
    global s8 


    root.s1=s1=ImageTk.PhotoImage(Image.open('./Images/happy.jpg'))
    root.s2=s2=ImageTk.PhotoImage(Image.open('./Images/angry.jpg'))
    root.s3=s3=ImageTk.PhotoImage(Image.open(f'./Images/sad.jpg'))
    root.s4=s4=ImageTk.PhotoImage(Image.open(f'./Images/friendly.jpg'))
    root.s5=s5=ImageTk.PhotoImage(Image.open(f'./Images/sick.jpg'))
    root.s6=s6=ImageTk.PhotoImage(Image.open(f'./Images/shy.jpg'))
    root.s7=s7=ImageTk.PhotoImage(Image.open(f'./Images/proud.jpg'))
    root.s8=s8=ImageTk.PhotoImage(Image.open(f'./Images/surprised.jpg'))


    global s
    s=[s1,s2,s3,s4,s5,s6,s7,s8]
    finito=Label(canvas,image=s1)   
    finito.place(x=300,y=250)

    b_happy=Button(canvas,text='happy', font='Tahoma 15 bold',  bg='yellow', width=7)
    b_happy.place(x=850,y=250)
    b_angry=Button(canvas,text='angry', font='Tahoma 15 bold',  bg='yellow', width=7)
    b_angry.place(x=700,y=250)
    b_sad=Button(canvas,text='sad', font='Tahoma 15 bold',  bg='yellow', width=7)
    b_sad.place(x=700,y=350)
    b_friendly=Button(canvas,text='friendly', font='Tahoma 15 bold',  bg='yellow', width=7)
    b_friendly.place(x=850,y=400)
    b_sick=Button(canvas,text='sick', font='Tahoma 15 bold',  bg='yellow', width=7)
    b_sick.place(x=850,y=300)
    b_shy=Button(canvas,text='shy', font='Tahoma 15 bold',  bg='yellow', width=7)
    b_shy.place(x=700,y=300)
    b_proud=Button(canvas,text='proud', font='Tahoma 15 bold',  bg='yellow', width=7)
    b_proud.place(x=850,y=350)
    b_surprised=Button(canvas,text='surprised', font='Tahoma 15 bold',  bg='yellow', width=7)
    b_surprised.place(x=700,y=400)

    b_happy['command']=lambda:task_10b(finito,b_happy,[b_happy,b_angry,b_sad,b_friendly,b_sick,b_shy,b_proud,b_surprised])
    b_angry['command']=lambda:task_10b(finito,b_angry,[b_happy,b_angry,b_sad,b_friendly,b_sick,b_shy,b_proud,b_surprised])
    b_sad['command']=lambda:task_10b(finito,b_sad,[b_happy,b_angry,b_sad,b_friendly,b_sick,b_shy,b_proud,b_surprised])
    b_friendly['command']=lambda:task_10b(finito,b_friendly,[b_happy,b_angry,b_sad,b_friendly,b_sick,b_shy,b_proud,b_surprised])
    b_sick['command']=lambda:task_10b(finito,b_sick,[b_happy,b_angry,b_sad,b_friendly,b_sick,b_shy,b_proud,b_surprised])
    b_shy['command']=lambda:task_10b(finito,b_shy,[b_happy,b_angry,b_sad,b_friendly,b_sick,b_shy,b_proud,b_surprised])
    b_proud['command']=lambda:task_10b(finito,b_proud,[b_happy,b_angry,b_sad,b_friendly,b_sick,b_shy,b_proud,b_surprised])
    b_surprised['command']=lambda:task_10b(finito,b_surprised,[b_happy,b_angry,b_sad,b_friendly,b_sick,b_shy,b_proud,b_surprised])

def task_10b(f,pressed,b):
    global task10_img_index
    global emotions
    global task10_score

    if pressed['text']==emotions[task10_img_index]:
        task10_score+=1
    task10_img_index+=1
    print(task10_score)
    f.destroy()


    for butt in b:
        butt.destroy()

    ###Task 10 starts here
    finito=Label(canvas,image=s[task10_img_index])   
    finito.place(x=300,y=250)

    b_happy=Button(canvas,text='happy', font='Tahoma 15 bold',  bg='yellow', width=7)
    b_happy.place(x=850,y=250)
    b_angry=Button(canvas,text='angry', font='Tahoma 15 bold',  bg='yellow', width=7)
    b_angry.place(x=700,y=250)
    b_sad=Button(canvas,text='sad', font='Tahoma 15 bold',  bg='yellow', width=7)
    b_sad.place(x=700,y=350)
    b_friendly=Button(canvas,text='friendly', font='Tahoma 15 bold',  bg='yellow', width=7)
    b_friendly.place(x=850,y=400)
    b_sick=Button(canvas,text='sick', font='Tahoma 15 bold',  bg='yellow', width=7)
    b_sick.place(x=850,y=300)
    b_shy=Button(canvas,text='shy', font='Tahoma 15 bold',  bg='yellow', width=7)
    b_shy.place(x=700,y=300)
    b_proud=Button(canvas,text='proud', font='Tahoma 15 bold',  bg='yellow', width=7)
    b_proud.place(x=850,y=350)
    b_surprised=Button(canvas,text='surprised', font='Tahoma 15 bold',  bg='yellow', width=7)
    b_surprised.place(x=700,y=400)

    if task10_img_index<5:
        
        b_happy['command']=lambda:task_10b(finito,b_happy,[b_happy,b_angry,b_sad,b_friendly,b_sick,b_shy,b_proud,b_surprised])
        b_sad['command']=lambda:task_10b(finito,b_sad,[b_happy,b_angry,b_sad,b_friendly,b_sick,b_shy,b_proud,b_surprised])
        b_angry['command']=lambda:task_10b(finito,b_angry,[b_happy,b_angry,b_sad,b_friendly,b_sick,b_shy,b_proud,b_surprised])
        b_sick['command']=lambda:task_10b(finito,b_sick,[b_happy,b_angry,b_sad,b_friendly,b_sick,b_shy,b_proud,b_surprised])
        b_friendly['command']=lambda:task_10b(finito,b_friendly,[b_happy,b_angry,b_sad,b_friendly,b_sick,b_shy,b_proud,b_surprised])
        b_shy['command']=lambda:task_10b(finito,b_shy,[b_happy,b_angry,b_sad,b_friendly,b_sick,b_shy,b_proud,b_surprised])
        b_proud['command']=lambda:task_10b(finito,b_proud,[b_happy,b_angry,b_sad,b_friendly,b_sick,b_shy,b_proud,b_surprised])
        b_surprised['command']=lambda:task_10b(finito,b_surprised,[b_happy,b_angry,b_sad,b_friendly,b_sick,b_shy,b_proud,b_surprised])
    else:
        finito.destroy()
        for butt in [b_happy,b_angry,b_sad,b_friendly,b_sick,b_shy,b_proud,b_surprised]:
            butt.destroy()
        canvas.delete('all')
        next=Button(canvas,text='Click to complete test', font='Tahoma 15 bold',  bg='blue')   
        next.place(x=300,y=100)
        next['command']=lambda f=next:felicitation(f)
    
def felicitation(f):
    f.destroy()
    canvas.create_text(450,150, text=f'Thanks for completing the assessment', font='Tahoma 18 bold', )
    canvas.create_text(450,300, text=f'\n\nYour score is:\nLearning and memory: {task1_score+task2_score+task3_score}/25\nLanguage:  {task4_score+task5_score}/18\nExecutive: {task6_score}/10\nPsychomotor: {task7_score+task8_score}/30\nAttention/concentration: {task9_score}/10\nSocial Cognition {task10_score}/10\n\nYour total score: {task1_score+task2_score+task3_score} ', font='Tahoma 18 bold', )




######################################################################################################################################################
#create canvas
canvas=Canvas(root, height=600, width=1000)

instruction=canvas.create_text(470,150, text='LagosCogniTool\n\nThe purpose of this tool is to assess your memory function to determine if your memory is normal for your age. \nThere are about  6 sections with an estimate of 2 minutes to complete each section, making a total of 12 minutes to complete. \nYou need to look for a quiet place without distraction to complete the test. \nTo correctly determine your memory function, it is important you answer these questions on your own without seeking help \nfrom another person or any other source like online materials or use of calculators. \n\nThe test will be based on correct answers and the time taken to perform the tasks. \nThanks\n\n\nYou have 2 minutes to complete each activity ', font='Times  13 bold')
finito=Button(canvas,text='Start Test', font='Tahoma 15 bold',  bg='green' )
finito.place(x=400,y=550)
finito['command']=lambda f=finito:start_task(f)

def start_task(f):
    f.destroy()
    canvas.delete('all')
    instruction=canvas.create_text(350,150, text='Learning and memory: Task 1\nTake note of these numbers, you will be asked to recall them (later).', font='Tahoma 15 bold')

    #numbers to be shown
    number=random.randint(10000,99999)
    number=str(number)

    global number_task
    number_task=list(number)

    #show number
    number1=Label(canvas, text=number[0],font='Tahoma 20 bold', bg='yellow' )
    number1.place(x=330, y=270)

    number2=Label(canvas, text=number[1],font='Tahoma 20 bold', bg='yellow' )
    number2.place(x=360, y=270)

    number3=Label(canvas, text=number[2],font='Tahoma 20 bold', bg='yellow' )
    number3.place(x=390, y=270)

    number4=Label(canvas, text=number[3],font='Tahoma 20 bold', bg='yellow' )
    number4.place(x=420, y=270)

    number5=Label(canvas, text=number[4],font='Tahoma 20 bold', bg='yellow' )
    number5.place(x=450, y=270)

    #show time
    root.after(1000, lambda:show_time(1,'t1'))
    root.after(2000, lambda:show_time(2,'t1'))
    root.after(3000, lambda:show_time(3,'t1'))
    root.after(4000, lambda:show_time(4,'t1'))
    root.after(5000, lambda:show_time(5,'t1'))
    root.after(6000, lambda:show_time(6,'t1'))
    root.after(7000, lambda:show_time(7,'t1'))
    root.after(8000, lambda:show_time(8,'t1'))
    root.after(9000, lambda:show_time(9,'t1'))
    root.after(10000, lambda:show_time(10,'t1'))


###remove everything after 10 seconds
    number1.after(10000, lambda:number1.destroy())
    number2.after(10000, lambda:number2.destroy())
    number3.after(10000, lambda:number3.destroy())
    number4.after(10000, lambda:number4.destroy())
    number5.after(10000, lambda:number5.destroy())

    root.after(10000, lambda: canvas.delete('all'))

#pack canvas
canvas.pack()

root.mainloop()


