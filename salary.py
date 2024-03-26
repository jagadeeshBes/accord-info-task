from abstract import *
class sal(Employee):
    def salary(self):
        self.s=self.day*1200

        print("salary =",self.s)

sy=sal()
sy.attendance()
sy.salary()
