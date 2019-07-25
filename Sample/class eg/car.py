
class Car:

    def __init__(self,regno,no_gears):
        self.regno = regno
        self.no_gears = no_gears
        self.is_started = False
        self.c_gear = 0

    def start(self):
        if self.is_started:
            print(f"the car with reg.no {self.regno} already started...")
        else:
            print(f"the car with reg.no {self.regno} started...")
            self.is_started = True
    
    def stop(self):
        if self.is_started:
            print(f"the car with reg.no {self.regno} stopped...")
            self.is_started = False
        else:
            print(f"the car with reg.no {self.regno} already stopped...")
    
    def change_gear(self):
        if self.is_started:
            if self.c_gear < self.no_gears:
                self.c_gear += 1    
                print(f"the car with reg.no {self.regno} changed gear to {self.c_gear}...")
            else:
                print(f"the car with reg.no {self.regno} already at max gear {self.c_gear}...")
        else:
            print(f"the car with reg.no {self.regno} cant change gears...because its stopped")
    
    def show_info(self):
        print(f"The Car reg.no {self.regno} Start :{self.is_started} Gears : {self.no_gears} Current Gear :{self.c_gear}")