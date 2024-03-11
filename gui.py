import tkinter as tk
from tkinter import *
from tkinter import ttk
import pyautogui
import time

class meuapp:

    def __init__(self,root):

        self.root = root
        self.root.title("bot-bbb")

        #---------------------imagens---------------------------------------

        self.img_menuprincipal   = PhotoImage(file="imagens/bot.png")
        self.img_menuprincipal2   = PhotoImage(file="imagens/bot.png")
        self.img_botao           = PhotoImage(file="imagens/posicao.png")

        #------------------CRIAÇAOO PRIMEIRA JANELA-------------------------
        self.root.geometry("400x400")
        self.root.iconbitmap(default="imagens/robot.ico")
        self.root.resizable(width=1,height=1)

        self.tab_control = ttk.Notebook(self.root)

        #criacoes de abas
        self.tab1 = ttk.Frame(self.tab_control)
        self.tab2 = ttk.Frame(self.tab_control)

        # adiciona as abas ao controlador
        self.tab_control.add(self.tab1, text='BOT-BBB')
        self.tab_control.add(self.tab2, text='Posicao')

        # adicione o controlador de abas a janela raiz
        self.tab_control.pack(expand=1, fill="both")

        # label para exibir a imagem de fundo na aba 1
        self.label_fundo_tab1 = Label(self.tab1, image=self.img_menuprincipal)
        self.label_fundo_tab1.place(x=0, y=0, relwidth=1, relheight=1)

        # label para exibir a imagem de fundo na aba 2
        self.label_fundo_tab2 = Label(self.tab2, image=self.img_menuprincipal2)
        self.label_fundo_tab2.place(x=0, y=0, relwidth=1, relheight=1)

        # widgets

        #aba 1
        
        #primeira

        self.label_p = tk.Label(self.tab1, text="posicao botao 1")
        self.label_p.place(x=50, y=105)
        self.label_x = tk.Label(self.tab1, text="X:")
        self.label_x.place(x=50, y=130)
        self.entry_x = tk.Entry(self.tab1, width=4)
        self.entry_x.place(x=70, y=130)

        self.label_y = tk.Label(self.tab1, text="Y:")
        self.label_y.place(x=100, y=130)
        self.entry_y = tk.Entry(self.tab1, width=4)
        self.entry_y.place(x=120, y=130)

        #segunda

        self.label_s = tk.Label(self.tab1, text="posicao botao 2")
        self.label_s.place(x=50, y=163)
        self.label_x1 = tk.Label(self.tab1, text="X:")
        self.label_x1.place(x=50, y=188)
        self.entry_x1 = tk.Entry(self.tab1, width=4)
        self.entry_x1.place(x=70, y=188)

        self.label_y1 = tk.Label(self.tab1, text="Y:")
        self.label_y1.place(x=100, y=188)
        self.entry_y1 = tk.Entry(self.tab1, width=4)
        self.entry_y1.place(x=120, y=188)

        #terceira

        self.label_t = tk.Label(self.tab1, text="posicao botao 3")
        self.label_t.place(x=50, y=222)
        self.label_x2 = tk.Label(self.tab1, text="X:")
        self.label_x2.place(x=50, y=247)
        self.entry_x2 = tk.Entry(self.tab1, width=4)
        self.entry_x2.place(x=70, y=247)

        self.label_y2 = tk.Label(self.tab1, text="Y:")
        self.label_y2.place(x=100, y=247)
        self.entry_y2 = tk.Entry(self.tab1, width=4)
        self.entry_y2.place(x=120, y=247)

        #botao do envio do forms

        submit_button = tk.Button(self.tab1, text="INICIAR", command= self.script)
        submit_button.place(x=60, y=300,width=70,height=20)

        #aba 2

        self.lbl2 = tk.Button(self.tab2,bd=0,image=self.img_botao ,command=self.local)
        self.lbl2.place(x=48,y=142,width=150,height=40)

        self.texto = tk.Label(self.tab2, text="Valor: ")
        self.texto.place(x=48, y=247)

    #-------------------------------local---------------------------------
    def local(self):
        time.sleep(5)
        a = str(pyautogui.position())
        self.texto.config(text="Valor: " + a)

    #-----------------------------script---------------------------------\
    
    def script(self):
            #pega os valores do formulario
            x =  int(self.entry_x.get())
            y =  int(self.entry_y.get())
            x1 = int(self.entry_x1.get())
            y1 = int(self.entry_y1.get())
            x2 = int(self.entry_x2.get())
            y2 = int(self.entry_y2.get())

            #array com as cordenadas
            posicoes = [(x, y), (x1, y1), (x2, y2)]

            #numero de cliqyues do mouse
            num_cliques_por_posicao = 1

            #repeticoes infinitas 
            while True:
                 #vai percorrer todos os valores do array
                 time.sleep(1)

                 a=1

                 for posicao in posicoes:
                    #mover o mouse nas cordenas
                    if a == 3:
                        pyautogui.moveTo(posicao[0], posicao[1], duration=4)

                    else:
                        a=a+1
                        pyautogui.moveTo(posicao[0], posicao[1], duration=1)

                    pyautogui.click()
                    time.sleep(1)



         
#-----------------------------------MAIN-------------------------------

if __name__ == "__main__":

    root = tk.Tk()
    app = meuapp(root)
    root.mainloop()
