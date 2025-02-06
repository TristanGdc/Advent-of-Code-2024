def is_safe(report):
    safe = True
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
    return safe

with open("Advent-of-Code-2024/day02/input02") as f:
    lines = f.readlines()

    result = 0

    for line in lines:
        report = list(map(lambda x: int(x.strip()), line.split(' ')))
        safe = is_safe(report)
        i=0
        while (not safe) and (i<len(report)):
            safe = (is_safe(report[:i]+report[i+1:]))
            i+=1

        if safe :
            result += 1

    print(result)
