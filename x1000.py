import sys
from random import randint

def main():
    output_file = "1000_x-axis_random_number_ranging_0_to_100.csv"
    l = list()
    for _ in range(1000):
        l.append(randint(0, 100))
        
    #setNumber = {n for n in sorted(l)}
    #print(setNumber)
    dictNumber = {}
    for n in sorted(l):
        if n not in dictNumber: dictNumber[n] = 0
        dictNumber[n] = dictNumber[n] + 1   
        
        
    with open(output_file, "w") as resultFile:
        data = "\n".join([str(n) for n in l])
        resultFile.write(data)
    print("Generate 1000 random numbers for x-axis ranging in 0-100.")
    print("Random number distribution -> (Key number : # count of number)")
    for (idx, cnt) in dictNumber.items():
        print(str(idx) + " : " + str(cnt))

if __name__ == '__main__':
    main()
