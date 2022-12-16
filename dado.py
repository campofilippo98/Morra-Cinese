import random

class dado:
    
    def __init__(self):
        n=0
    def roll(n) -> int:
        n = random.randint(1,6)
        return n

def main():
    d = dado()
    print(d.roll())

if __name__ == "__main__":
    main()
