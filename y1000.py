import sys

def main():
    input_file = "x.csv"
    output_file = "y.csv"
    
    with open(input_file, "r") as f:
        l = [str(int(s.replace("\n","")) * 3 + 6) for s in f]
        
    with open(output_file, "w") as resultFile:
        data = "\n".join(l)
        resultFile.write(data)
    print("Generate 1000 y numbers")

if __name__ == '__main__':
    main()
