class Rectangle:
    def __init__(self,length : int, breadth:int):
        self.length = length
        self.breadth = breadth
        
    def __iter__(self):
        yield{'length': self.length}
        yield{'breadth': self.breadth}
        
if __name__ == "__main__":
    rect = Rectangle(10, 5)

    for item in rect:
        print(item)
