class Car:
    def __init__(self, manf, model):
        self.manf = manf
        self.model = model
        self.v = 0
        self.state = False
        self.fuel = 100
    
    def start(self):
        if self.state == True:
            print('已经启动')
            return
        if self.fuel >= 1:
            self.state = True
            self.fuel -= 1
            print("启动中...完成")
        else:
            print('油量不足无法启动！')
    
    def stop(self):
        if self.v > 0:
            print('有速度时无法停止！')
            return
        if self.state == False:
            print('已经停止')
            return
        self.state = False
        print('停止中...已停止')
    
    def speedUp(self, toV):
        if self.state == False or toV < self.v:
            print("无法加速到 {}".format(toV))
            return
        self.fuel -= (toV - self.v) * 0.1
        if self.fuel == 0:
            self.v = 0
            self.stop()
        else:
            self.v = toV
            print("正在加速...已加速到 {}".format(toV))
    
    def speedDown(self, toV):
        if self.state == False or toV > self.v or toV < 0:
            print("无法减速到 {}".format(toV))
            return
        self.v = toV
        print("正在减速...已减速到 {}".format(toV))
    
    def addOil(self, fuel):
        if self.state:
            print("车辆开启时不能加油！")
            return
        self.fuel += fuel
        print("已加 {} 油".format(fuel))

    def getManf(self):
        print("厂商为 {}".format(self.manf))
        return self.manf

    def getModel(self):
        print("型号为 {}".format(self.model))
        return self.model
    
    def getVel(self):
        print("速度为 {}".format(self.v))
        return self.v
    
    def getFuel(self):
        print("油量为 {}".format(self.fuel))
        return self.fuel

    def getState(self):
        return self.state

if __name__ == '__main__':
    car = Car('Benz', '300')
    car.start()
    car.speedUp(120)
    car.getFuel()
    car.addOil(50)
    car.speedDown(0)
    car.stop()