import random

class dado:
    
    def __init__(self):
        n=0
    def roll() -> int:
        n = random.randint(1,7)
        return n

def main():
    d = dado()
    valore = d.roll()
    print(valore)
