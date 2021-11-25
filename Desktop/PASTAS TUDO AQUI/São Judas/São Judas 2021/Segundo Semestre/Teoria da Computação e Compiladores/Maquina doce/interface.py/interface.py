from tkinter import *
total = 0 
total1 = 0
total2 = 0
total3 =0



def incb():
    n = int(rotulob.configure('text')[4]) +1
    rotulob.configure(text=n)
    return n


def incc():
    n1 = int(rotuloc.configure('text')[4]) +2
    rotuloc.configure(text=n1)
    return n1

    
    
def incd():
    n2 = int(rotulod.configure('text')[4]) +5
    rotulod.configure(text=n2)
    return n2
    

def ince():
    total = int(rotulob.configure('text')[4]) + int(rotuloc.configure('text')[4])  + int(rotulod.configure('text')[4])  
    #n = int(rotuloe.configure('text')[4]) 
    rotuloe.configure(text=total )
 
def inc6a():
    if int(rotulob.configure('text')[4]) + int(rotuloc.configure('text')[4])  + int(rotulod.configure('text')[4]) == 6:
        if rotulof['text'] == 'A':
            rotulof['text'] = 'Doce A comprado | SEM TROCO'


def inc6b():
    if int(rotulob.configure('text')[4]) + int(rotuloc.configure('text')[4])  + int(rotulod.configure('text')[4]) == 6:
        if rotulog['text'] == 'B':
            rotulog['text'] = 'Adicione mais para comprar o Doce B'        
            
                           
def inc6c():
    if int(rotulob.configure('text')[4]) + int(rotuloc.configure('text')[4])  + int(rotulod.configure('text')[4]) == 6:
        if rotuloh['text'] == 'C':
            rotuloh['text'] = 'Adicione mais para comprar o Doce C'
            
def inc7a():
    if int(rotulob.configure('text')[4]) + int(rotuloc.configure('text')[4])  + int(rotulod.configure('text')[4]) == 7:
        if rotulof['text'] == 'A':
            rotulof['text'] = 'Doce A comprado | Troco R$ 1,00'   
def inc7b():
    if int(rotulob.configure('text')[4]) + int(rotuloc.configure('text')[4])  + int(rotulod.configure('text')[4]) == 7:
        if rotulog['text'] == 'B':
            rotulog['text'] = 'Doce B comprado | SEM TROCO'          
def inc7c():
    if int(rotulob.configure('text')[4]) + int(rotuloc.configure('text')[4])  + int(rotulod.configure('text')[4]) == 7:
        if rotuloh['text'] == 'C':
            rotuloh['text'] = 'Adicione mais para comprar o Doce C' 
def inc8a():
    if int(rotulob.configure('text')[4]) + int(rotuloc.configure('text')[4])  + int(rotulod.configure('text')[4]) == 8:
        if rotulof['text'] == 'A':
            rotulof['text'] = 'Doce A comprado | Troco R$ 2,00'
def inc8b():
    if int(rotulob.configure('text')[4]) + int(rotuloc.configure('text')[4])  + int(rotulod.configure('text')[4]) == 8:
        if rotulog['text'] == 'B':
            rotulog['text'] = 'Doce B comprado | Troco R$ 1,00'
def inc8c():
    if int(rotulob.configure('text')[4]) + int(rotuloc.configure('text')[4])  + int(rotulod.configure('text')[4]) == 8:
        if rotuloh['text'] == 'C':
            rotuloh['text'] = 'Doce C comprado | SEM TROCO'
def inc9a():
    if int(rotulob.configure('text')[4]) + int(rotuloc.configure('text')[4])  + int(rotulod.configure('text')[4]) == 9:
        if rotulof['text'] == 'A':
            rotulof['text'] = 'Doce A comprado | Troco R$ 3,00'
def inc9b():
    if int(rotulob.configure('text')[4]) + int(rotuloc.configure('text')[4])  + int(rotulod.configure('text')[4]) == 9:
        if rotulog['text'] == 'B':
            rotulog['text'] = 'Doce B comprado | Troco R$ 2,00'
def inc9c():
    if int(rotulob.configure('text')[4]) + int(rotuloc.configure('text')[4])  + int(rotulod.configure('text')[4]) == 9:
        if rotuloh['text'] == 'C':
            rotuloh['text'] = 'Doce C comprado | Troco R$ 1,00'
def inc10a():
    if int(rotulob.configure('text')[4]) + int(rotuloc.configure('text')[4])  + int(rotulod.configure('text')[4]) == 10:
        if rotulof['text'] == 'A':
            rotulof['text'] = 'Doce A comprado | Troco R$ 4,00'
def inc10b():
    if int(rotulob.configure('text')[4]) + int(rotuloc.configure('text')[4])  + int(rotulod.configure('text')[4]) == 10:
        if rotulog['text'] == 'B':
            rotulog['text'] = 'Doce B comprado | Troco R$ 3,00'
def inc10c():
    if int(rotulob.configure('text')[4]) + int(rotuloc.configure('text')[4])  + int(rotulod.configure('text')[4]) == 10:
        if rotuloh['text'] == 'C':
            rotuloh['text'] = 'Doce C comprado | Troco R$ 2,00'
def inc11a():
    if int(rotulob.configure('text')[4]) + int(rotuloc.configure('text')[4])  + int(rotulod.configure('text')[4]) == 11:
        if rotulof['text'] == 'A':
            rotulof['text'] = 'Doce A comprado | Troco R$ 5,00'
def inc11b():
    if int(rotulob.configure('text')[4]) + int(rotuloc.configure('text')[4])  + int(rotulod.configure('text')[4]) == 11:
        if rotulog['text'] == 'B':
            rotulog['text'] = 'Doce B comprado | Troco R$ 4,00'
def inc11c():
    if int(rotulob.configure('text')[4]) + int(rotuloc.configure('text')[4])  + int(rotulod.configure('text')[4]) == 11:
        if rotuloh['text'] == 'C':
            rotuloh['text'] = 'Doce C comprado | Troco R$ 3,00'
def inc12a():
    if int(rotulob.configure('text')[4]) + int(rotuloc.configure('text')[4])  + int(rotulod.configure('text')[4]) == 12:
        if rotulof['text'] == 'A':
            rotulof['text'] = 'Doce A comprado | Troco R$ 6,00'
def inc12b():
    if int(rotulob.configure('text')[4]) + int(rotuloc.configure('text')[4])  + int(rotulod.configure('text')[4]) == 12:
        if rotulog['text'] == 'B':
            rotulog['text'] = 'Doce B comprado | Troco R$ 5,00'
def inc12c():
    if int(rotulob.configure('text')[4]) + int(rotuloc.configure('text')[4])  + int(rotulod.configure('text')[4]) == 12:
        if rotuloh['text'] == 'C':
            rotuloh['text'] = 'Doce C comprado | Troco R$ 4,00'
def inc13a():
    if int(rotulob.configure('text')[4]) + int(rotuloc.configure('text')[4])  + int(rotulod.configure('text')[4]) == 13:
        if rotulof['text'] == 'A':
            rotulof['text'] = 'Doce A comprado | Troco R$ 7,00'
def inc13b():
    if int(rotulob.configure('text')[4]) + int(rotuloc.configure('text')[4])  + int(rotulod.configure('text')[4]) == 13:
        if rotulog['text'] == 'B':
            rotulog['text'] = 'Doce B comprado | Troco R$ 6,00'
def inc13c():
    if int(rotulob.configure('text')[4]) + int(rotuloc.configure('text')[4])  + int(rotulod.configure('text')[4]) == 13:
        if rotuloh['text'] == 'C':
            rotuloh['text'] = 'Doce C comprado | Troco R$ 5,00'
def inc14a():
    if int(rotulob.configure('text')[4]) + int(rotuloc.configure('text')[4])  + int(rotulod.configure('text')[4]) == 14:
        if rotulof['text'] == 'A':
            rotulof['text'] = 'Doce A comprado | Troco R$ 8,00'
def inc14b():
    if int(rotulob.configure('text')[4]) + int(rotuloc.configure('text')[4])  + int(rotulod.configure('text')[4]) == 14:
        if rotulog['text'] == 'B':
            rotulog['text'] = 'Doce B comprado | Troco R$ 7,00'
def inc14c():
    if int(rotulob.configure('text')[4]) + int(rotuloc.configure('text')[4])  + int(rotulod.configure('text')[4]) == 14:
        if rotuloh['text'] == 'C':
            rotuloh['text'] = 'Doce C comprado | Troco R$ 6,00'
def inc15a():
    if int(rotulob.configure('text')[4]) + int(rotuloc.configure('text')[4])  + int(rotulod.configure('text')[4]) == 15:
        if rotulof['text'] == 'A':
            rotulof['text'] = 'Doce A comprado | Troco R$ 9,00'
def inc15b():
    if int(rotulob.configure('text')[4]) + int(rotuloc.configure('text')[4])  + int(rotulod.configure('text')[4]) == 15:
        if rotulog['text'] == 'B':
            rotulog['text'] = 'Doce B comprado | Troco R$ 8,00'
def inc15c():
    if int(rotulob.configure('text')[4]) + int(rotuloc.configure('text')[4])  + int(rotulod.configure('text')[4]) == 15:
        if rotuloh['text'] == 'C':
            rotuloh['text'] = 'Doce C comprado | Troco R$ 7,00'



        
        
b = Button(text='Clique para adicionar R$ 1,00', command=incb)
b.pack()
rotulob = Label(text=0)  
rotulob.pack()
            
c = Button(text='Clique para adicionar R$ 2,00', command=incc)
c.pack()
rotuloc = Label(text=0)  
rotuloc.pack()

d = Button(text='Clique para adicionar R$ 5,00', command=incd)
d.pack()
rotulod = Label(text=0)
rotulod.pack()

e = Button(text='TOTAL', command=ince)
e.pack()
rotuloe = Label(text=0)  
rotuloe.pack()



f = Button(text='Doce A', command=inc6a)
f = Button(text='Doce A', command=inc7a)
f = Button(text='Doce A', command=inc8a)
f = Button(text='Doce A', command=inc9a)
f = Button(text='Doce A', command=inc10a)
f = Button(text='Doce A', command=inc11a)
f = Button(text='Doce A', command=inc12a)
f = Button(text='Doce A', command=inc13a)
f = Button(text='Doce A', command=inc14a)
f = Button(text='Doce A', command=inc15a)








f.pack(side= LEFT)
rotulof = Label(text='A')  
rotulof.pack(side= LEFT)

g = Button(text='Doce B', command=inc6b)
g = Button(text='Doce B', command=inc7b)
g = Button(text='Doce B', command=inc8b)
g = Button(text='Doce B', command=inc9b)
g = Button(text='Doce B', command=inc10b)
g = Button(text='Doce B', command=inc11b)
g = Button(text='Doce B', command=inc12b)
g = Button(text='Doce B', command=inc13b)
g = Button(text='Doce B', command=inc14b)
g = Button(text='Doce B', command=inc15b)









g.pack(side= LEFT)
rotulog = Label(text='B')  
rotulog.pack(side= LEFT)

h = Button(text='Doce C', command=inc6c)
h = Button(text='Doce C', command=inc7c)
h = Button(text='Doce C', command=inc8c)
h = Button(text='Doce C', command=inc9c)
h = Button(text='Doce C', command=inc10c)
h = Button(text='Doce C', command=inc11c)
h = Button(text='Doce C', command=inc12c)
h = Button(text='Doce C', command=inc13c)
h = Button(text='Doce C', command=inc14c)
h = Button(text='Doce C', command=inc15c)









h.pack(side= LEFT)
rotuloh = Label(text='C')  
rotuloh.pack(side= LEFT)

    
    
root = Tk()
root.mainloop()

        