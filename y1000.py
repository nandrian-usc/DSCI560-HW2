import sys

def main():
    if (len(sys.argv) != 3):
        print("Usage: y1000.py <input_file> <output_file>")
        sys.exit(-1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    with open(input_file, "r") as f:
        l = [str(int(s.replace("\n","")) * 3 + 6) for s in f]
        
    with open(output_file, "w") as resultFile:
        data = "\n".join(l)
        resultFile.write(data)
    print("Generate 1000 y numbers")

if __name__ == '__main__':
    main()