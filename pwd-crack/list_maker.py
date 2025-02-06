import argparse
from itertools import product

def generate_case_combinations(word):
    # Create a list to store the variations for each character in the word.
    variations = []

    # Loop through each character in the word.
    for ch in word:
        # Start with the base variations: lowercase and uppercase.
        base_variations = [ch.lower(), ch.upper()]

        # Add mutations for specific characters.
        if ch.lower() == 'a':
            base_variations.append('@')
        if ch.lower() == 'a':
            base_variations.extend('4')
        if ch.lower() == 'i':
            base_variations.extend(['!', '1'])
        if ch.lower() == 'e':
            base_variations.extend('3')
        if ch.lower() == 's':
            base_variations.extend('$')

        # Add the variations for the current character to the list.
        variations.append(base_variations)

    # Generate all combinations from the list of variations.
    return [''.join(comb) for comb in product(*variations)]

def main(file1, file2, output_file):
    try:
        # Read the list of words.
        with open(file1, 'r') as f1:
            words = [line.strip() for line in f1]

        # Read the list of numbers.
        with open(file2, 'r') as f2:
            numbers = [line.strip() for line in f2]

        # Open the output file to write the results.
        with open(output_file, 'w') as out:
            for word in words:
                # Generate all case and mutation combinations for the word.
                word_combinations = generate_case_combinations(word)

                for comb in word_combinations:
                    # Write each combination.
                    out.write(comb + '\n')

                    # Add number combinations.
                    for number in numbers:
                        out.write(f"{comb}\n")  # Number before word.
                        out.write(f"{comb}!\n")  # Number before word.
                        out.write(f"!{comb}\n")  # Number before word.
                        out.write(f"{number}{comb}\n")  # Number before word.
                        out.write(f"{comb}{number}\n")  # Number after word.
                        out.write(f"{number}{comb}!\n")  # Number before word.
                        out.write(f"!{comb}{number}\n")  # Number after word.

        print(f"Output written to {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Set up the argument parser for command-line options.
    parser = argparse.ArgumentParser(
        description="Generate word variations with upper/lower case and specific character mutations."
    )
    parser.add_argument(
        'file1',
        type=str,
        help='Path to the first file containing a list of words (one per line).'
    )
    parser.add_argument(
        'file2',
        type=str,
        help='Path to the second file containing a list of numbers (one per line).'
    )
    parser.add_argument(
        'output_file',
        type=str,
        help='Path to the output file where the generated list of combinations will be saved.'
    )

    # Parse the arguments.
    args = parser.parse_args()

    # Call the main function with the parsed arguments.
    main(args.file1, args.file2, args.output_file)