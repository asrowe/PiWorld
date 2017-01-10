from sense_hat import SenseHat


class PiWorld:
    def __init__(self):
        self.sense = SenseHat()
        self.world = []
        self.x = 8
        self.y = 8
        self.w = self.x * self.y

    def __str__(self):
        return str(self.world)

    def hattest(self):
        self.sense.show_message("Hi!")

    def create(self):
        for i in range(0,self.w):
            self.world.append(True)

    def iterate(self, iterations):
        for i in range(0, iterations):
            self.update()
            print("World " + str(i) + " " + str(self.world))

    def update(self):
        for i in range(0,self.w):
            self.updateCell(i)

    def updateCell(self, cell):
        neighbours = self.getNeighbours(cell)
        self.world[cell] = self.updateState(neighbours)
                
    def getNeighbours(self, cell):
        #n1 = self.world[cell-9]
        #n2 = self.world[cell-8]
        #n3 = self.world[cell-7]
        #n4 = self.world[cell-1]
        #n5 = self.world[cell+1]
        #n6 = self.world[cell+7]
        #n7 = self.world[cell+8]
        #n8 = self.world[cell+9]
        #return ([n1,n2,n3,n4,n5,n6,n7,n8])
        return []

    def updateState(self, neighbours):
        return False
    



pworld = PiWorld()
#pworld.hattest()
pworld.create()
pworld.iterate(1)
        
