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
                for i in range(len(numbers)//2):
                    next[(numbers[2*i],(numbers[2*i+1]))] = (numbers[2*i],(numbers[2*i+1]))

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

                    if p_start >= n_start and p_start < n_end:
                        next.pop((p_start,p_range))
                        copyprev.pop((p_key,p_val))

                        if p_end < n_end:
                            next[(p_start, p_range)] = (parts[0]+p_start-n_start,p_range)

                        else:
                            next[(p_start, n_end-p_start)] = (parts[0]+p_start-n_start,n_end-p_start)
                            next[(n_end,p_end-n_end)] = (n_end,p_end-n_end)
                            copyprev[(p_key-p_end+n_end,p_end-n_end)] = (n_end,p_end-n_end)

                    elif p_end > n_start and p_end <= n_end:
                        next.pop((p_start,p_range))
                        copyprev.pop((p_key,p_val))

                        next[(n_start, p_end-n_start)] = (parts[0],p_end-n_start)
                        next[(p_start, n_start-p_start)] = (p_start,n_start-p_start)
                        copyprev[(p_key,n_start-p_start)] = (p_start,n_start-p_start)

                    elif p_end > n_end and p_start < n_start:
                        next.pop((p_start,p_range))
                        copyprev.pop((p_key,p_val))

                        next[(n_start, n_end-n_start)] = (parts[0],n_end-n_start)
                        next[(n_end, p_end-n_end)] = (n_end, p_end-n_end)
                        next[(p_start, n_start-p_start)] = (p_start, n_start-p_start)
                        copyprev[(p_key+n_end-p_end,p_end-n_end)] = (n_end, p_end-n_end)
                        copyprev[(p_key, n_start-p_start)] = (p_start, n_start-p_start)
                
                prev = dict(copyprev)

    a,b = min(next.values())

    print("The answer is:", a)


if __name__ == "__main__":
    main()