import sys
import matplotlib.pyplot as plt

def main():
    if (len(sys.argv) != 3):
        print("Usage: visual.py <input_fileX> <input_fileY>")
        sys.exit(-1)
        
    input_fileX = sys.argv[1]
    input_fileY = sys.argv[2]
    
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