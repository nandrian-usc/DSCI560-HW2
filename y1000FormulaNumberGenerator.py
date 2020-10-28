import sys
import matplotlib.pyplot as plt

def main():
    input_file = "1000_x-axis_random_number_ranging_0_to_100.csv"
    output_file = "1000_y-axis_number_by_3x_plus_6.csv"
    
    with open(input_file, "r") as f:
        l = [int(s.replace("\n","")) * 3 + 6 for s in f]
    
    
    dictNumber = {}
    for n in sorted(l):
        if n not in dictNumber: dictNumber[n] = 0
        dictNumber[n] = dictNumber[n] + 1   
    
    
    with open(output_file, "w") as resultFile:
        data = "\n".join([str(n) for n in l])
        resultFile.write(data)
    
    n, bins, patches = plt.hist(l, 100)#, density=True, facecolor='g', alpha=0.75)
    plt.xlabel('y')
    plt.ylabel('Count')
    plt.title('Distribution of y = 3x + 6')
    plt.grid(True)
    plt.show()
    
    print("Generate 1000 y-axis numbers using y = 3x + 6 formula")
    print("y-axis number distribution = (x -> y : # count of number)")
    for (idx, cnt) in dictNumber.items():
        print( str(int(((idx - 6) / 3))) + " -> " + str(idx) + " : " + str(cnt))

if __name__ == '__main__':
    main()
