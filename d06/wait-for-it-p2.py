import math

def main():

    with open('input.txt') as reader:

        a = int(reader.readline().split(":")[1].replace(" ", ""))
        b = int(reader.readline().split(":")[1].replace(" ", ""))
        
        z = a-(2*math.ceil((a-math.sqrt(a**2-4*b))/2))+1

        print("The answer is:", z)


if __name__ == "__main__":
    main()