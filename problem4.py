class StringManipulator:
    def __init__(self):
        self.string = ""

    def getString(self):
        self.string = input("ENter the name: ")

    def printString(self):
        print("String in upper case:", self.string.upper())

def testStringManipulator():
    manipulator = StringManipulator()
    manipulator.getString()
    manipulator.printString()
testStringManipulator()