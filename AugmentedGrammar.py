def augment_grammar(grammar):
    augmented_grammar = {}
    start_symbol = 'S\''
    original_start_symbol = list(grammar.keys())[0]
    augmented_grammar[start_symbol] = [original_start_symbol]
    for non_terminal, productions in grammar.items():
        augmented_productions = [production for production in productions]
        augmented_grammar[non_terminal] = augmented_productions
    return augmented_grammar

def main():
    original_grammar = {
        'E': ['E+T', 'T'],
        'T': ['T*F', 'F'],
        'F': ['(E)', 'id']
    }
    augmented_grammar = augment_grammar(original_grammar)
    for non_terminal, productions in original_grammar.items():
        print(f"{non_terminal} -> {' | '.join(productions)}")
    print()
    for non_terminal, productions in augmented_grammar.items():
        print(f"{non_terminal} -> {' | '.join(productions)}")

if __name__ == "__main__":
    main()