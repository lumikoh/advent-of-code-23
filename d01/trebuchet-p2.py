def main():
    
    numbers = {
        "one":   1,
        "two":   2,
        "three": 3,
        "four":  4,
        "five":  5,
        "six":   6,
        "seven": 7,
        "eight": 8,
        "nine":  9
    }

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

                    substr = line[0:i+1]
                    for key in numbers:
                        if key in substr:
                            first = numbers[key]
                            break

                if second == -1:
                    try:
                        second = int(line[-i-1])
                    except:
                        pass   

                    substr = line[-i-1:len(line)]
                    for key in numbers:
                        if key in substr:
                            second = numbers[key]
                            break

                if second != -1 and first != -1:
                    break

            if first == -1 or second == -1:
                continue
            
            sum = sum + first*10 + second

        print("The answer is:", sum)


if __name__ == "__main__":
    main()