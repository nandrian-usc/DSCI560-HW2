import sys
import matplotlib.pyplot as plt

def main():
    input_fileX = "1000_x-axis_random_number_ranging_0_to_100.csv"
    input_fileY = "1000_y-axis_number_by_3x_plus_6.csv"
    
    with open(input_fileX, "r") as f:
        x = [int(s.replace("\n","")) for s in f]
    with open(input_fileY, "r") as f:
        y = [int(s.replace("\n","")) for s in f]
    
    plt.plot(x, y, marker='o')
    plt.grid(True)    
    plt.savefig('lineplot_random_x_and_3xPlus6_y.png')
    plt.show()
    
    

if __name__ == '__main__':
    main()
