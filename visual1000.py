import sys
import matplotlib.pyplot as plt

def main():
    input_fileX = "x.csv"
    input_fileY = "y.csv"
    
    with open(input_fileX, "r") as f:
        x = [int(s.replace("\n","")) for s in f]
    with open(input_fileY, "r") as f:
        y = [int(s.replace("\n","")) for s in f]
    
    plt.plot(x, y, marker='o')
    plt.grid(True)    
    plt.savefig('lineplot.png')
    plt.show()
    
    

if __name__ == '__main__':
    main()
