max_cubes = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def validate(line):
    [game, data] = line.split(":")

    for part in data.split(";"):
        for cubes in part.split(","):
            [count, color] = cubes.strip().split(" ")
            if(max_cubes[color] < int(count)):
                return 0
    print(game)
    return int(game.strip("Game "))

def main():

    with open('input.txt') as reader:

        sum = 0

        for line in reader:
            sum = sum + validate(line)

        print("The answer is:", sum)


if __name__ == "__main__":
    main()