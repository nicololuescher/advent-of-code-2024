def generate_rules(input):
    rules = {}
    for rule in input:
        if rule[0] not in rules:
            rules[rule[0]] = {"before": set(), "after": set()}
        if rule[1] not in rules:
            rules[rule[1]] = {"before": set(), "after": set()}
        rules[rule[0]]["after"].add(rule[1])
        rules[rule[1]]["before"].add(rule[0])
    return rules


def evaluate_instructions(instruction, rules):
    for i, element in enumerate(instruction):
        if element not in rules:
            continue
        if not (is_before(instruction, element, i, rules) and is_after(instruction, element, i, rules)):
            return False
    return instruction[len(instruction) // 2]

def visit(node, dependencies, visited, visiting, sorted_instruction, instruction):
    if node in visited:
        return
    if node in visiting:
        raise ValueError("Circular dependency detected")
    visiting.add(node)
    for dep in dependencies[node]:
        if dep in instruction:
            visit(dep, dependencies, visited, visiting, sorted_instruction, instruction)
    visiting.remove(node)
    visited.add(node)
    sorted_instruction.append(node)


def fix_instruction(instruction, rules):
    dependencies = {x: set() for x in instruction}
    for element in instruction:
        if element in rules:
            dependencies[element].update(rules[element]["before"])
    sorted_instruction = []
    visited = set()
    visiting = set()

    for element in instruction:
        visit(element, dependencies, visited, visiting, sorted_instruction, instruction)
    return sorted_instruction[len(sorted_instruction) // 2]



def is_before(instruction, element, index, rules):
    return all(
        required in instruction[:index] or required not in instruction
        for required in rules[element]["before"]
    )

def is_after(instruction, element, index, rules):
    return all(
        required in instruction[index + 1:] or required not in instruction
        for required in rules[element]["after"]
    )

def part1(instructions, rules):
    total = 0
    for instruction in instructions:
        total += int(evaluate_instructions(instruction, rules))
    return total

def part2(instructions, rules):
    total = 0
    for instruction in instructions:
        if not evaluate_instructions(instruction, rules):
            total += int(fix_instruction(instruction, rules))
    return total


def main():
    rules = []
    instructions = []
    with open("day5/data.txt", "r") as data:
        for line in data:
            if "|" in line:
                rules.append(line.strip().split("|"))
            elif "," in line:
                instructions.append(line.strip().split(","))
    rules = generate_rules(rules)
    print(part1(instructions, rules))
    print(part2(instructions, rules))

if __name__ == "__main__":
    main()
