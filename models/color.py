class color:
    def __init__(self, red: int, green: int, blue: int):
        self.red = red
        self.green = green
        self.blue = blue

    def getTuple(self) -> tuple:
        return (self.red, self.green, self.blue)
