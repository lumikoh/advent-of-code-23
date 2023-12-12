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
            winners = 0
            for j in range(1,a[i]+1):
                if j*(a[i]-j) > b[i]:
                    winners = winners + 1
            result = result*winners

    print("The answer is:", result)


if __name__ == "__main__":
    main()