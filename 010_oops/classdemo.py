class Pen:

    #data memeber / variables
    price = 10
    color = "RED"
    company = "Cello"

    #function member / method
    def to_write(self):
        print(self.price,self.color,self.company)


p1 = Pen()
p1.price = 100
p1.color = "black"
p1.to_write()

p2 = Pen()
p2.company = "SS"
p2.to_write()