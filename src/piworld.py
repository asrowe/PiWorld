from sense_hat import SenseHat
import time


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
            self.world.append(i % 2 == 3)
        self.draw()

    def iterate(self, iterations):
        time.sleep(0.5)
        for i in range(0, iterations):
            
            newworld = [self.updateCell(j) for j in range(0,self.w)]
            self.draw()
            #print("World " + str(i) + " " + str(self.world))

    def updateCell(self, cell):
        neighbours = self.getNeighbours(cell)
        self.world[cell] = self.updateState(cell, neighbours)
                
    def getNeighbours(self, cell):
        neighbours_offset = [-9,-8,-7,-1,1,7,8,9]
        neighbours_offset = [cell+i for i in neighbours_offset]
        neighbours = []
        for i in neighbours_offset:
            if i < 0 or i > self.w:
                neighbours.append(True)
            else:
                neighbours.append(self.world[i])
        #print(str(cell), str(neighbours_offset), str(neighbours) )   
        return neighbours

    def updateState(self, cell, neighbours):
        return not(self.world[cell])
    
    def draw(self):
        pixels = [[255,255,255]if i else [0,0,0] for i in self.world]
        self.sense.set_pixels(pixels)


pworld = PiWorld()
#pworld.hattest()
pworld.create()
pworld.iterate(1)
        
