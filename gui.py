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

        # Agora crie as abas
        self.tab1 = ttk.Frame(self.tab_control)
        self.tab2 = ttk.Frame(self.tab_control)

        # Adicione as abas ao controlador de abas
        self.tab_control.add(self.tab1, text='BOT-BBB')
        self.tab_control.add(self.tab2, text='Posicao')

        # Adicione o controlador de abas à janela raiz
        self.tab_control.pack(expand=1, fill="both")

        # Widget Label para exibir a imagem de fundo na aba 1
        self.label_fundo_tab1 = Label(self.tab1, image=self.img_menuprincipal)
        self.label_fundo_tab1.place(x=0, y=0, relwidth=1, relheight=1)

        # Widget Label para exibir a imagem de fundo na aba 2
        self.label_fundo_tab2 = Label(self.tab2, image=self.img_menuprincipal2)
        self.label_fundo_tab2.place(x=0, y=0, relwidth=1, relheight=1)

        # widgets
        #self.lbl1 = Label(self.tab1, text='bot bbb')
        #self.lbl1.grid(column=0, row=0)
        
        #primeira

        label_p = tk.Label(self.tab1, text="posicao botao 1")
        label_p.place(x=50, y=105)
        label_x = tk.Label(self.tab1, text="X:")
        label_x.place(x=50, y=130)
        entry_x = tk.Entry(self.tab1, width=4)
        entry_x.place(x=70, y=130)

        label_y = tk.Label(self.tab1, text="Y:")
        label_y.place(x=100, y=130)
        entry_y = tk.Entry(self.tab1, width=4)
        entry_y.place(x=120, y=130)

        #segunda

        label_s = tk.Label(self.tab1, text="posicao botao 2")
        label_s.place(x=50, y=163)
        label_x1 = tk.Label(self.tab1, text="X:")
        label_x1.place(x=50, y=188)
        entry_x1 = tk.Entry(self.tab1, width=4)
        entry_x1.place(x=70, y=188)

        label_y1 = tk.Label(self.tab1, text="Y:")
        label_y1.place(x=100, y=188)
        entry_y1 = tk.Entry(self.tab1, width=4)
        entry_y1.place(x=120, y=188)

        #terceira

        label_t = tk.Label(self.tab1, text="posicao botao 3")
        label_t.place(x=50, y=222)
        label_x2 = tk.Label(self.tab1, text="X:")
        label_x2.place(x=50, y=247)
        entry_x2 = tk.Entry(self.tab1, width=4)
        entry_x2.place(x=70, y=247)

        label_y2 = tk.Label(self.tab1, text="Y:")
        label_y2.place(x=100, y=247)
        entry_y2 = tk.Entry(self.tab1, width=4)
        entry_y2.place(x=120, y=247)

        #botao do envio do forms

        submit_button = tk.Button(self.tab1, text="Enviar", command= self.script)
        submit_button.place(x=60, y=300,width=70,height=20)

        #self.lbl2 = Label(self.tab2, text='posicao do mouse')
        #self.lbl2.grid(column=0, row=0)

        self.lbl2 = tk.Button(self.tab2,bd=0,image=self.img_botao ,command=self.local)
        self.lbl2.place(x=48,y=142,width=150,height=40)

        self.texto = tk.Label(self.tab2, text="Valor: ")
        self.texto.place(x=48, y=247)

    #-------------------------------local---------------------------------
    def local(self):
        time.sleep(5)
        a = str(pyautogui.position())
        self.texto.config(text="Valor: " + a)

    #-------------------------------local---------------------------------
    def script(self):
        print("ola")
         
#-----------------------------------MAIN-------------------------------

if __name__ == "__main__":

    root = tk.Tk()
    app = meuapp(root)
    root.mainloop()