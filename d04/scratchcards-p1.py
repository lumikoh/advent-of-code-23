def main():
    result = 0

    with open('input.txt') as reader:
        
        for line in reader:
            [numbers, winning] = line.split(":")[1].split("|")
            numlist = numbers.strip().split(" ")
            winlist = winning.strip().split(" ")
            
            points = 0

            for num in numlist:
                if num != "" and num in winlist:
                    points = points + 1
            
            if points != 0:
                result = result + 2**(points-1)


    print("The answer is:", result)


if __name__ == "__main__":
    main()