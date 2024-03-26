def left_factoring(grammar):
    new_grammar = {}
    for non_terminal, productions in grammar.items():
        while productions:
            prefix = productions[0][0]
            common_prefix = [production for production in productions if production.startswith(prefix)]
            if len(common_prefix) == 1:
                new_grammar.setdefault(non_terminal, []).append(common_prefix[0])
                productions.remove(common_prefix[0])
            else:
                new_non_terminal = non_terminal + "'"
                new_grammar.setdefault(non_terminal, []).append(prefix + new_non_terminal)
                new_grammar.setdefault(new_non_terminal, []).extend(production[1:] for production in common_prefix)
                productions = [production for production in productions if not production.startswith(prefix)]
    return new_grammar

def main():
    grammar = {
        'S': ['if E then S else S', 'if E then S', 'id := E', 'print E'],
        'E': ['E + T', 'T'],
        'T': ['T * F', 'F'],
        'F': ['(E)', 'id']
    }

    new_grammar = left_factoring(grammar)

    print("Original Grammar:")
    for non_terminal, productions in grammar.items():
        print(f"{non_terminal} -> {' | '.join(productions)}")

    print("\nGrammar after left factoring:")
    for non_terminal, productions in new_grammar.items():
        print(f"{non_terminal} -> {' | '.join(productions)}")

if __name__ == "__main__":
    main()