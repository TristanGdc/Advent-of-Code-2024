def respects_rule(update, rule) -> bool:
    if not (rule[0] in update and rule[1] in update):
        return True
    else:
        return update.index(rule[0]) < update.index(rule[1])

with open("Advent-of-Code-2024/inputs/input05") as f:
    input = f.readlines()

    # Clean input
    rules = list(map(lambda e : list(map(lambda i : int(i), e.strip().split('|'))), input[:input.index('\n')]))
    updates = list(map(lambda e : list(map(lambda i : int(i), e.strip().split(','))), input[input.index('\n')+1:]))

    sum = 0 

    for update in updates:
        if all(respects_rule(update, rule) for rule in rules):
            sum += update[int((len(update)-1)/2)]

    print(sum)
