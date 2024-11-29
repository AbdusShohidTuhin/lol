class A():
    def sound(self):
        print("hello")
        
class B(A):
    def sound(self):
        super().sound
        print("is ok")
        
my = B()
my.sound()