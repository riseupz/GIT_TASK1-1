from Transportation import *

class Taxi(Transportation):
    
    def __init__( self, start, end, distance ):
        Transportation.__init__( self, start, end, distance)

    def find_cost( self ):
        return 40 * self.distance
