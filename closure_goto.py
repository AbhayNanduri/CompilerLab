from collections import defaultdict

# Example augmented grammar
# Replace this with your augmented grammar
grammar = {
    'S\'': [('S',)],
    'S': [('E',)],
    'E': [('E', '+', 'T'), ('T',)],
    'T': [('T', '*', 'F'), ('F',)],
    'F': [('(', 'E', ')'), ('id',)]
}

# Define closure function
def closure(items, grammar):
    closure_set = set(items)
    while True:
        new_items = set()
        for item in closure_set:
            dot_index = item[1].index('.')
            if dot_index < len(item[1]) - 1:
                symbol_after_dot = item[1][dot_index + 1]
                if symbol_after_dot in grammar:
                    for prod in grammar[symbol_after_dot]:
                        new_items.add((symbol_after_dot, ('.',) + prod))
        if not new_items.difference(closure_set):
            break
        closure_set = closure_set.union(new_items)
    return closure_set

# Define goto function
def goto(items, symbol, grammar):
    goto_set = set()
    for item in items:
        production = item[0]
        dots = item[1]
        dot_index = dots.index('.')
        if dot_index < len(dots) - 1 and dots[dot_index + 1] == symbol:
            new_dots = list(dots)
            new_dots[dot_index] = new_dots[dot_index + 1]
            new_dots[dot_index + 1] = '.'
            goto_set.add((production, tuple(new_dots)))
    return closure(goto_set, grammar)

# Main function to generate GOTO items set
def generate_goto_items(grammar):
    initial_item = ('S\'', ('.',) + grammar['S\''][0])
    initial_closure = closure({initial_item}, grammar)
    items_sets = [initial_closure]
    symbols = set(grammar.keys()).union(set(term for prods in grammar.values() for prod in prods for term in prod))
    
    for items in items_sets:
        for symbol in symbols:
            goto_items = goto(items, symbol, grammar)
            if goto_items and goto_items not in items_sets:
                items_sets.append(goto_items)
    
    return items_sets

# Example usage
goto_items_sets = generate_goto_items(grammar)
for i, items in enumerate(goto_items_sets):
    print(f"I{i}:", items)
