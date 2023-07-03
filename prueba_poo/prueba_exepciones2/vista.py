import os
import tkinter as tk

class Vista:
    
    def run(self):
        self.root = tk.Tk()
        self.root.geometry("400x400")
        
        self.sensor1Var = tk.StringVar(value="Apagado")
        self.sensor2Var = tk.StringVar(value="Apagado")
        self.sensor3Var = tk.StringVar(value="Apagado")

        self.sensor1 = tk.Label(self.root,text="Sensor 1").grid(row=0,column=0)
        self.sensor2 = tk.Label(self.root,text="Sensor 2").grid(row=1,column=0)
        self.sensor3 = tk.Label(self.root,text="Sensor 3").grid(row=2,column=0)

        self.sensor1Estado = tk.Label(self.root,textvariable=self.sensor1Var).grid(row=0,column=1)
        self.sensor2Estado = tk.Label(self.root,textvariable=self.sensor2Var).grid(row=1,column=1)
        self.sensor3Estado = tk.Label(self.root,textvariable=self.sensor3Var).grid(row=2,column=1)
        
        self.botonEncender = tk.Button(self.root,text="Encender Sensores",command=self.vistaEncender).grid(row=3,column=1)

        self.root.mainloop()

    def vistaEncender(self):
        os.system("cls")
        print("-- Sistema de control de sensores --")



