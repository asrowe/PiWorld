from sense_hat import SenseHat
import time


class PiWorld:
    def __init__(self):
        self.sense = SenseHat()
        self.world = []
        self.X = 8
        self.Y = 8
        self.W = self.X * self.Y

    def __str__(self):
        return str(self.world)

    def hattest(self):
        self.sense.show_message("Hi!")

    def create(self, map = "checks"):
        if map == "checks":
            for y in range(0, self.Y):
                self.world.append([1,0,1,0,1,0,1,0] if y % 2 == 0 else [0,1,0,1,0,1,0,1])
        elif map == "blinker":
            self.world = [[0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0],
                          [0,0,1,1,1,0,0,0],
                          [0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0]]
        elif map == "glider":
            self.world = [[0,0,0,0,0,0,0,0],
                          [0,0,0,1,0,0,0,0],
                          [0,0,0,0,1,0,0,0],
                          [0,0,1,1,1,0,0,0],
                          [0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0]]

        self.draw()

    def iterate(self, iterations):
       
        for i in range(0, iterations):
            time.sleep(0.5)
            new_world = []
            for y in range(0, self.Y):
                new_y = []
                for x in range(0, self.X):
                    new_y.append(self.updateCell((x,y)))
                new_world.append(new_y)
            self.world = new_world
            self.draw()

    def updateCell(self, cell):
        neighbours = self.getNeighbours(cell)
        return self.updateState(cell, neighbours)
                
    def getNeighbours(self, (x,y)):
        neighbours_offset = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]
        neighbours_offset = [(x+o_x, y+o_y) for (o_x, o_y) in neighbours_offset]
        neighbours_offset = [(x % self.X, y % self.Y) for (x, y) in neighbours_offset]

        neighbours = []
        for x,y in neighbours_offset:
            neighbours.append(self.world[y][x])

        return neighbours

    def updateState(self, (x,y), neighbours):
        neighbour_count = sum(neighbours)
        
        if self.world[y][x] == 1:
            if neighbour_count < 2 or neighbour_count > 3:
                new_val = 0
            else:
                new_val = 1
        else:
            if neighbour_count == 3:
                new_val = 1
            else:
                new_val = 0
                    
        #print new_val
        return new_val
    
    def draw(self):
        pixels = []
        for y in self.world:
            for x in y:
                pixels.append([255,255,255]if x == 1 else [0,0,0])
        self.sense.set_pixels(pixels)


pworld = PiWorld()
#pworld.hattest()
pworld.create("blinker")
pworld.iterate(10)
print("finished")
        
