from time import sleep
from car import Car
from tkinter import *

class gCar(Car):
    def __init__(self, manf, model):
        super().__init__(manf, model)
        self.root = Tk()

        self.c = Canvas(self.root, width=320, height=200)
        self.c.pack()

        self.c.create_text(150, 30, text=self.manf, anchor=E)
        self.c.create_text(170, 30, text=self.model, anchor=W)
        self.c.create_text(275, 30, text='addOil')
        btnAddOil = self.c.create_rectangle(250, 20, 300, 40)
        self.c.tag_bind(btnAddOil, '<Enter>', func=self.addOilD)

        self.tSpeed = self.c.create_text(70, 120, text='Speed:')
        self.c.create_text(70, 140, text='SpeedUp')
        btnSpeedUp = self.c.create_rectangle(20, 130, 120, 150)
        self.c.tag_bind(btnSpeedUp, '<Enter>', func=self.speedUpD)

        self.tState = self.c.create_text(160, 70, text='Off')
        self.btnStarter = self.c.create_oval(150, 80, 170, 100)
        self.c.tag_bind(self.btnStarter, '<Enter>', func=self.toggle)

        self.tFuel = self.c.create_text(250, 120, text='Fuel:')
        self.c.create_text(250, 140, text='SpeedDn')
        btnSpeedDn = self.c.create_rectangle(200, 130, 300, 150)
        self.c.tag_bind(btnSpeedDn, '<Enter>', func=self.speedDownD)

        self.root.mainloop()

    def update(self):
        self.c.itemconfig(self.tSpeed, text='Speed: {}'.format(self.v))
        self.c.itemconfig(self.tFuel, text='Fuel: {}'.format(self.fuel))
        self.c.itemconfig(self.tState, text=('On' if self.state else 'Off'))
        self.c.itemconfig(self.btnStarter, fill='red' if self.state else 'white')

    def speedUpD(self, event):
        toV = self.v + 10
        self.speedUp(toV)
        self.update()

    def speedDownD(self, event):
        toV = self.v - 10
        self.speedDown(toV)
        self.update()

    def toggle(self, event):
        if self.getState():
            self.stop()
        else:
            self.start()
        self.update()
        sleep(1)

    def addOilD(self, event):
        self.addOil(10)
        self.update()

if __name__=='__main__':
    gCar('Benz', '300')