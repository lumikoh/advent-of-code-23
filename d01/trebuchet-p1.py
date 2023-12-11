def main():
    with open('input.txt') as reader:

        sum = 0

        for line in reader:
            first = -1
            second = -1

            for i in range(len(line)):

                if first == -1:
                    try:
                        first = int(line[i])
                    except:
                        pass       

                if second == -1:
                    try:
                        second = int(line[-i-1])
                    except:
                        pass   

                if second != -1 and first != -1:
                    break

            if first == -1 or second == -1:
                continue
            
            sum = sum + first*10 + second

        print("The answer is:", sum)


if __name__ == "__main__":
    main()