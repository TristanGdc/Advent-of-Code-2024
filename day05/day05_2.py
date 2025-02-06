def respects_rule(update, rule) -> bool:
    if not (rule[0] in update and rule[1] in update):
        return True
    else:
        return update.index(rule[0]) < update.index(rule[1])
    
def sort(update, rules) -> list:
    superiors = {val:[] for val in update}
    for val in update:
        for comparative_val in update:
            if [comparative_val, val] in rules:
                superiors[val].append(comparative_val)
    
    ordered = []
    for i in range(len(update)):
        max = list(superiors.keys())[list(superiors.values()).index([])]
        
        for key in superiors.keys():
            if key != max:
                superiors[key] = list(filter(lambda val : val != max, superiors[key]))
        ordered.append(max)
        del superiors[max]

    return ordered

with open("Advent-of-Code-2024/day05/input05") as f:
    input = f.readlines()

    rules = list(map(lambda e : list(map(lambda i : int(i), e.strip().split('|'))), input[:input.index('\n')]))
    updates = list(map(lambda e : list(map(lambda i : int(i), e.strip().split(','))), input[input.index('\n')+1:]))

    to_sum_unordered = []

    for update in updates:
        if not all(respects_rule(update, rule) for rule in rules):
            to_sum_unordered.append(update)

    sum = 0

    for update in to_sum_unordered:
        sum += sort(update, rules)[int((len(update)-1)/2)]

    print(sum)
