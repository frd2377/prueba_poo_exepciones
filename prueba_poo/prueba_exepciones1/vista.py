import tkinter as tk
import os

class Vista:
    
    def run(self):
        self.root = tk.Tk()
        self.root.geometry("400x400")
        
        self.actuador1Var = tk.StringVar(value="Apagado")
        self.actuador2Var = tk.StringVar(value="Apagado")
        self.actuador3Var = tk.StringVar(value="Apagado")

        self.actuador1 = tk.Label(self.root,text="Actuador 1").grid(row=0,column=0)
        self.actuador2 = tk.Label(self.root,text="Actuador 2").grid(row=1,column=0)
        self.actuador3 = tk.Label(self.root,text="Actuador 3").grid(row=2,column=0)

        self.actuador1Estado = tk.Label(self.root,textvariable=self.actuador1Var).grid(row=0,column=1)
        self.actuador2Estado = tk.Label(self.root,textvariable=self.actuador2Var).grid(row=1,column=1)
        self.actuador3Estado = tk.Label(self.root,textvariable=self.actuador3Var).grid(row=2,column=1)
        
        self.botonEncender = tk.Button(self.root,text="Encender Actuadores",command=self.vistaEncender).grid(row=3,column=1)

        self.root.mainloop()

    def vistaEncender(self):
        os.system("cls")
        print("-- Sistema de control de Actuadores --")


