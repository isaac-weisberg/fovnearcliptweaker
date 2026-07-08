from vec2 import vec2
import math

class QuadraticRangeMapping:
    def __init__(self, outputRange, anchorInputPercentage, anchorOutputPercentage):
        self.outputRange = outputRange
        self.power = math.log(anchorOutputPercentage) / math.log(anchorInputPercentage)
        self.inversePower = 1 / self.power
    
    def inToOut(self, input):
        return self.outputRange * math.pow(input, self.power)

    def outToIn(self, output):
        return math.pow(output / self.outputRange, self.inversePower)