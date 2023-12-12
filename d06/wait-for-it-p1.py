import math

def main():
    result = 1

    with open('input.txt') as reader:
        
        a = list(filter(str.strip, reader.readline().strip("\n").split(" ")))
        a.pop(0)
        a = list(map(int,a))
        b = list(filter(str.strip, reader.readline().strip("\n").split(" ")))
        b.pop(0)
        b = list(map(int,b))

        for i in range(len(a)):
            result = result*(a[i]-(2*math.ceil((a[i]-math.sqrt(a[i]**2-4*b[i]))/2))+1)

    print("The answer is:", result)


if __name__ == "__main__":
    main()