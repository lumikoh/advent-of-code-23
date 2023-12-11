import functools

def find_power(line):
    min_cubes = {
        "red": 1,
        "green": 1,
        "blue": 1
    }

    [game, data] = line.split(":")

    for part in data.split(";"):
        for cubes in part.split(","):
            [count, color] = cubes.strip().split(" ")

            if(min_cubes[color] < int(count)):
                min_cubes[color] = int(count)
            
    return functools.reduce(lambda a, b: a*b, min_cubes.values(), 1)

def main():

    with open('input.txt') as reader:

        sum = 0

        for line in reader:
            sum = sum + find_power(line)

        print("The answer is:", sum)


if __name__ == "__main__":
    main()