def is_number(string):
    try:
        number = int(string)
        return True
    except:
        return False


def recursive_parse_number(row, index):
    if(index+1 > len(row)):
        return ""
    
    if(is_number(row[index])):
        return row[index] + recursive_parse_number(row, index+1)
    
    return ""


def find_adjacent_symbol(coordinates, x, y):
    for i in range(-1,2):
        if(x + i < 0 or x + i +1 >= len(coordinates)):
            continue
        for j in range(-1,2):
            if(y+j < 0 or y+j + 1 >= len(coordinates[x+i])):
                continue
            elif(is_number(coordinates[x+i][y+j])):
                continue
            elif(coordinates[x+i][y+j] == '.'):
                continue
            else:
                return x+i, y+j
    return -1,-1


def main():

    coordinates = []
    result = 0
    gears = {}

    with open('input.txt') as reader:
        
        for line in reader:
            row = []
            for chara in line:
                row.append(chara)
            coordinates.append(row)
    
    for i in range(len(coordinates)):
        passrounds = 0
        for j in range(len(coordinates[i])):
            if passrounds > 0:
                passrounds = passrounds -1
                continue

            number = recursive_parse_number(coordinates[i], j)
            if(number != ""):
                for k in range(len(number)):
                    [x,y] = find_adjacent_symbol(coordinates, i, j+k)
                    if x != -1 and y != -1:
                        if x not in gears:
                            gears[x] = {}
                        if y not in gears[x]:
                            gears[x][y] = []

                        gears[x][y].append(int(number))
                        break
                passrounds = len(number) -1
    
    for xkey in gears:
        for ykey in gears[xkey]:
            if len(gears[xkey][ykey]) != 2:
                continue
            result = result + gears[xkey][ykey][0] * gears[xkey][ykey][1]

    print("The answer is:", result)


if __name__ == "__main__":
    main()