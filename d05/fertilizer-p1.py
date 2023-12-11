def main():
    prev = {}
    next = {}

    with open('input.txt') as reader:

        mode = 0

        for line in reader:
            if line.strip() == "":
                mode = 1
                continue

            if mode == 0:
                numbers = list(map(int, line.split(":")[1].strip().split(" ")))
                for num in numbers:
                    next[num] = num

            
            elif ":" in line:
                prev = next
                next = {}
                for key in prev:
                    next[prev[key]] = prev[key]
            
            else:
                parts = list(map(int,line.split(" ")))
                for number in prev:
                    if prev[number] >= parts[1] and prev[number] < parts[1]+parts[2]:
                        next[prev[number]] = (parts[0]+prev[number]-parts[1])

    print("The answer is:", min(next.values()))


if __name__ == "__main__":
    main()