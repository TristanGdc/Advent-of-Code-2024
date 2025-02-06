def evaluate(input):
    input = input.strip("\n")
    n1, n2 = None, None

    if len(input)>0:

        i = 0
        while input[i].isdigit():
            i+=1
        if i>0:
            n1 = int(input[0:i])

        if len(input[i:])>3 and input[i] == ',':
            j = i+1
            while input[j].isdigit():
                j+=1

            if j> i+1 and len(input)>j and input[j] == ')':
                n2 = int(input[i+1:j])
    
    if(n1 and n2):
        return n1*n2
    else:
        return 0

with open("Advent-of-Code-2024/day03/input03") as f:
    lines = f.readlines()

    answer = 0

    for line in lines :
        inputs = line.split("mul(")
        for input in inputs:
            answer += (evaluate(input))
    
    print(answer)
            