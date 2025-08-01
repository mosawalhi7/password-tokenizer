import re
from collections import deque

def tokenize_passwords(password_list, dictionary):
    tokenized_passwords = []

    for password in password_list:
        # If the password already has spaces, we simply keep it as-is
        if ' ' in password:
            tokenized_passwords.append(password)
            continue

        tokenized_password = shift_and_bfs_match(password, dictionary)

        # Ensure the output is clean by removing extra spaces
        tokenized_password = re.sub(r'\s+', ' ', tokenized_password).strip()

        tokenized_passwords.append(tokenized_password)

    return tokenized_passwords

def shift_and_bfs_match(input_string, dictionary):

    # Base case: if the string is empty, nothing to do
    if not input_string:
        return ""

    n = len(input_string)

    # Try from each possible start position i
    for i in range(n):
        coverage_len, path = bfs_max_coverage(input_string[i:], dictionary)
        # If BFS found at least one dictionary token (coverage_len > 0)
        if coverage_len > 0:
            # Everything before i is leftover_front (unmatched)
            leftover_front = input_string[:i]
            leftover_front = split_symbols_on_leftover(leftover_front)

            matched_part = " ".join(path)

            # Leftover at the end
            leftover_end = input_string[i + coverage_len :]
            # Recursively tokenize leftover_end
            leftover_end_tokenized = shift_and_bfs_match(leftover_end, dictionary)

            # Build final string:
            parts = []
            if leftover_front:
                parts.append(leftover_front)
            if matched_part:
                parts.append(matched_part)
            if leftover_end_tokenized:
                parts.append(leftover_end_tokenized)

            return " ".join(parts)

    return split_symbols_on_leftover(input_string)

def bfs_max_coverage(substring, dictionary):

    length = len(substring)
    queue = deque([(0, [])])  # (current_index, path_of_tokens)
    max_coverage = 0
    best_path = []

    while queue:
        idx, path = queue.popleft()

        if idx > max_coverage:
            max_coverage = idx
            best_path = path

        for j in range(idx + 1, length + 1):
            seg = substring[idx:j]
            if seg.lower() in dictionary:
                queue.append((j, path + [seg]))

    return max_coverage, best_path

def split_symbols_on_leftover(segment):

    tokens = re.findall(r"\d+\.\d+|[A-Za-z]+|\d+|[^A-Za-z0-9\s]", segment)
    return " ".join(tokens)

def load_dictionary(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return set(word.strip().lower() for word in file)

def load_passwords(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file]

def save_tokenized_passwords(file_path, tokenized_passwords):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write("\n".join(tokenized_passwords))

if __name__ == "__main__":
    dictionary_file = 'dictionaries/large_dictionary.txt'          # Dictionary file
    passwords_file = 'passwords_input.txt'            # Input file of passwords
    output_file = 'passwords_tokenized.txt'     # Where to save tokenized output

    # Load data
    dictionary = load_dictionary(dictionary_file)
    password_list = load_passwords(passwords_file)

    # Tokenize
    tokenized = tokenize_passwords(password_list, dictionary)

    # Save results
    save_tokenized_passwords(output_file, tokenized)
    print(f"Tokenized passwords have been saved to {output_file}")