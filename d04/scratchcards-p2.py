def main():
    result = 0

    lines = []
    counts = []

    with open('input.txt') as reader:
        
        for line in reader:
            lines.append(line)
            counts.append(1)

    for i in range(len(lines)):

        [numbers, winning] = lines[i].split(":")[1].split("|")
        numlist = numbers.strip().split(" ")
        winlist = winning.strip().split(" ")
        
        points = 0

        for num in numlist:
            if num != "" and num in winlist:
                points = points + 1
        
        for j in range(points):
            if(i+j+1 >= len(counts)):
                break
            counts[i+j+1] = counts[i+j+1] + counts[i]

        result = result + counts[i]

    print("The answer is:", result)


if __name__ == "__main__":
    main()