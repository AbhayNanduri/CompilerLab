def find_left_recursion(grammar):
    left_recursive_non_terminals = []

    for non_terminal, productions in grammar.items():
        for production in productions:
            first_symbol = production.split()[0]
            if first_symbol == non_terminal:
                left_recursive_non_terminals.append(non_terminal)
                break

    return left_recursive_non_terminals

# Example usage:
grammar = {
    'E': ['E + T', 'T'],
    'T': ['T * F', 'F'],
    'F': ['( E )', 'id']
}

left_recursions = find_left_recursion(grammar)
if left_recursions:
    print("Left recursive non-terminals:", left_recursions)
else:
    print("No left recursion found in the grammar.")