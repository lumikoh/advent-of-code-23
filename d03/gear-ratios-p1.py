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
                return True
    return False


def main():

    coordinates = []
    sum = 0

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
                    if find_adjacent_symbol(coordinates, i, j+k):
                        sum = sum + int(number)
                        break
                passrounds = len(number) -1
    
    print("The answer is:", sum)



if __name__ == "__main__":
    main()