from tkinter import * 

class Application:
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label(self.widget1, text=1)
        
        self.msg["font"] = ("Calibri", "9", "italic")
        self.msg.pack ()
        #self.sair = Button(self.widget1)
        #self.sair["text"] = "R$ 1,00"
        self.sair["font"] = ("Calibri", "9")
        self.sair["width"] = 10
    
        self.sair['command'] = self.inc
        
        
        
        
        #self.sair.bind("<Button-1>", self.mudarTexto)
        # self.sair.bind("<Button-1>", self.mudarTexto1)
        
        self.sair.pack ()

    def mudarTexto(self):
        while self.msg["text"] == 'Clique para adicionar R$ 1,00':
            if self.msg["text"] == 'Clique para adicionar R$ 1,00':
                self.msg["text"] = "Total | R$ 1,00"
                if self.msg["text"] == 'Clique para adicionar R$ 1,00':
                    self.msg["text"] = "Total | R$ 2,00"
    
    
    b = Button(text='Clique para adicionar R$ 1,00', command=inc)
    b.pack()
    rotulo = Label(text=0)  
    rotulo.pack()
                
    def inc():
        n = int(rotulo.configure('text')[1]) +1
        rotulo.configure(text=str(n))
    
            
            
        
            


root = Tk()
Application(root)
root.mainloop()
