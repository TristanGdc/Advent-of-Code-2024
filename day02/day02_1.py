with open("Advent-of-Code-2024/day02/input02") as f:
    lines = f.readlines()

    result = 0

    for line in lines:
        safe = True
        report = list(map(lambda x: int(x.strip()), line.split(' ')))

        if(report[0] > report[1]):
            for i in range(1, len(report)):
                if (not report[i-1] > report[i]) or (report[i-1]-report[i] > 3) :
                    safe = False
                    break
        else :
            for i in range(1, len(report)):
                if (not report[i-1] < report[i]) or (report[i]-report[i-1] > 3) :
                    safe = False
                    break

        if safe :
            result += 1

    print(result)
