def main():
    prev = {}
    next = {}

    with open('input.txt') as reader:

        numbers = list(map(int, reader.readline().split(":")[1].strip().split(" ")))
        for i in range(len(numbers)//2):
            next[(numbers[2*i],(numbers[2*i+1]))] = (numbers[2*i],(numbers[2*i+1]))

        for line in reader:
            if line.strip() == "":
                continue

            elif ":" in line:
                prev = next
                next = {}
                for key in prev:
                    next[prev[key]] = prev[key]
            
            else:
                parts = list(map(int,line.split(" ")))
                n_start = parts[1]
                n_end = parts[1]+parts[2]

                copyprev = dict(prev)

                for p_key, p_val in prev:

                    p_start,p_range = prev[(p_key,p_val)]
                    p_end = p_start + p_range

                    if p_start >= n_end or p_end <= n_start:
                        continue

                    next.pop((p_start,p_range))
                    copyprev.pop((p_key,p_val))

                    end = p_end
                    start = p_start

                    if p_end >= n_end:
                        next[(n_end,p_end-n_end)] = (n_end,p_end-n_end)
                        copyprev[(p_key-p_end+n_end,p_end-n_end)] = (n_end,p_end-n_end)
                        end = n_end

                    if p_start < n_start:
                        next[(p_start, n_start-p_start)] = (p_start,n_start-p_start)
                        copyprev[(p_key,n_start-p_start)] = (p_start,n_start-p_start)
                        start = n_start

                    next[(start, end-start)] = (parts[0]+start-n_start, end-start)
                
                prev = dict(copyprev)

    a,b = min(next.values())

    print("The answer is:", a)


if __name__ == "__main__":
    main()