import sys
from random import randint

def main():
    output_file = "x.csv"
    l = list()
    for _ in range(1000):
        l.append(str(randint(0, 101)))
        
    with open(output_file, "w") as resultFile:
        data = "\n".join(l)
        resultFile.write(data)
    print("Generate 1000 random numbers")

if __name__ == '__main__':
    main()
