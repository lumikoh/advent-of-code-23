import functools

cardvalues = {"2":  2, "3":  3, "4":  4, 
              "5":  5, "6":  6, "7":  7, 
              "8":  8, "9":  9, "T": 10, 
              "J": 11, "Q": 12, "K": 13, "A": 14 }

def handsort(a, b):
    a_1, a_2, a_h, a_v = a
    b_1, b_2, b_h, b_v = b
    
    if a_1 != b_1:
        return 1 if a_1 > b_1 else -1
    
    if a_2 != b_2:
        return 1 if a_2 > b_2 else -1
    
    for i in range(5):
        if cardvalues[a_h[i]] != cardvalues[b_h[i]]:
            return 1 if cardvalues[a_h[i]] > cardvalues[b_h[i]] else -1
    return 1
    

def main():
    result = 0

    allhands = []

    with open('input.txt') as reader:
    
        for line in reader:
            [hand, value] = line.strip("\n").split(" ")
            symbols = set(hand)
            most = 0
            second = 0

            for sym in symbols:
                amount = hand.count(sym)
                if amount > most:
                    second = most
                    most = amount
                elif amount > second:
                    second = amount
            
            allhands.append((most, second, hand, value))

    sorted_all = sorted(allhands, key=functools.cmp_to_key(handsort))   

    for i in range(len(sorted_all)):
        s1, s2, sh, sv = sorted_all[i]
        result = result + int(sv)*(i+1)

    print("The answer is:", result)


if __name__ == "__main__":
    main()