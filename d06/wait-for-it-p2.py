def main():
    result = 0

    with open('input.txt') as reader:

        a = int(reader.readline().split(":")[1].replace(" ", ""))
        b = int(reader.readline().split(":")[1].replace(" ", ""))

        for j in range(1,a+1):
            if j*(a-j) > b:
                result = result + 1

    print("The answer is:", result)


if __name__ == "__main__":
    main()