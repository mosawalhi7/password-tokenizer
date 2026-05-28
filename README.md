# Tokenizing Complex Passwords Using Breadth-First Search and Dictionary Matching

This repository contains the official implementation, scripts, and datasets required to reproduce the results presented in the paper "Tokenizing Complex Passwords Using Breadth-First Search and Dictionary Matching" published in IEEE Latin America Transactions.

## Paper Information

* **Title:** Tokenizing Complex Passwords Using Breadth-First Search and Dictionary Matching.
* **Authors:**
   * Salam Al-E'mari (Department of Information Security, Faculty of Information Technology, University of Petra, Amman, Jordan)
   * Mohammad Al Sawalhi (Department of Information Security, Faculty of Information Technology, University of Petra, Amman, Jordan)
   * Yousef Sanjalawe (Department of Information Technology, King Abdullah II School for Information Technology, University of Jordan, Amman, Jordan)
* **Manuscript ID:** 10673

## Repository Structure & File Description

The project files are organized as follows to ensure full reproducibility of the experimental analysis:

| File / Folder Name | Description |
| :--- | :--- |
| `dictionaries/` | Directory containing the three generated leetspeak-enhanced wordlists. |
| ├── `dictionaries/small_dictionary.txt` | Dictionary derived from 10,000 base words (233,813 tokens) using basic leetspeak mappings. |
| ├── `dictionaries/medium_dictionary.txt` | Dictionary derived from 20,000 base words (997,496 tokens) with expanded mappings. |
| └── `dictionaries/large_dictionary.txt` | Full dictionary derived from 44,742 base words (4,414,292 tokens) using extensive mappings. |
| `tokenizer.py` | Main Python script containing the core BFS-based tokenization framework and post-processing leftover segmentation. |
| `passwords_input.txt` | Input file containing the benchmarking real-world dataset of unique password samples used for experimental validation. |
| `passwords_tokenized.txt` | Output file populated automatically by the script to store the final parsed and segmented token sequences. |

## Features

* **BFS-based Tokenization:** Utilizes a Breadth-First Search algorithm to comprehensively identify dictionary words, numeric segments, and symbolic tokens within passwords.
* **Explicit Handling of Symbols and Numbers:** Recognizes and properly tokenizes symbolic characters and numeric substrings, which are often overlooked by conventional tokenizers.
* **Leetspeak Recognition:** Incorporates advanced approaches to identify common character substitutions (e.g., '@' for 'a', '3' for 'e') as valid tokens, addressing morphological transformations and user-generated variations beyond basic dictionary lookups.
* **Customizable Dictionaries:** Supports the use of various dictionary sizes to balance between tokenization accuracy and processing time. Users can also provide their own dictionaries.
* **Efficient Performance:** Designed to maintain practical processing times even with large dictionaries and datasets.

## How it Works

The tokenization process involves two main phases:

1.  **BFS-based Segmentation:** The core of the algorithm, where a Breadth-First Search systematically scans the password string to find valid dictionary words and their variations (including leetspeak).
2.  **Post-processing for Symbols and Numbers:** After the BFS phase, any unmatched segments (typically symbols and numeric sequences) are processed separately to ensure all characters are tokenized. Contiguous digits are grouped, and symbols are treated as individual tokens unless they form known multi-character sequences.

## Dictionaries

The project includes pre-built dictionaries of varying sizes, which impact both performance and accuracy:

* **Small Dictionary:** Derived from the first 10,000 words with basic leetspeak mappings (e.g., a->a, e->3, i->1, c->0, s->S, t->7).
    * **Tokens:** 233,813
    * **Generation Time:** 0.17 seconds
* **Medium Dictionary:** Built from the first 20,000 words with additional mappings (e.g., g->9, s->5).
    * **Tokens:** 997,496
    * **Generation Time:** 0.98 seconds
* **Large Dictionary (Recommended):** Generated from 44,742 words using a comprehensive set of leetspeak mappings (e.g., a ->{a,_,4}, b->{b,8}). This dictionary offers the highest accuracy but may result in slightly longer processing times.
    * **Tokens:** 4,414,292
    * **Generation Time:** 4.45 seconds

The larger dictionaries generally provide higher accuracy due to a more extensive vocabulary and more comprehensive leetspeak variations, allowing the tokenizer to identify more complex patterns.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/mosawalhi7/password-tokenizer.git](https://github.com/mosawalhi7/password-tokenizer.git)
    cd password-tokenizer
    ```
2.  **Prepare your dictionaries:**
    Place your desired dictionary file (e.g., `small_dictionary.txt`, `medium_dictionary.txt`, `large_dictionary.txt`, or your custom dictionary) inside the `dictionaries/` folder.

## Usage

1.  **Modify `tokenizer.py` (if needed):**
    Open `tokenizer.py` and ensure the `dictionary_file` variable points to the dictionary you wish to use, located within the `dictionaries/` folder.

    ```python
    if __name__ == "__main__":
        dictionary_file = 'dictionaries/large_dictionary.txt'  # Change this to your desired dictionary path
        passwords_file = 'passwords_input.txt'                 # Input file of passwords
        output_file = 'passwords_tokenized.txt'               # Where to save tokenized output
    ```

2.  **Add your passwords to the input file:**
    The project expects an input file named `passwords_input.txt` in the root directory. Add the passwords you want to tokenize to this file, with one password per line.

    **Example `passwords_input.txt`:**
    ```
    MyP@ssw0rd123!
    secret_word_456
    anotherTest789
    ```

3.  **Run the tokenizer:**
    ```bash
    python tokenizer.py
    ```

4.  **View the output:**
    The tokenized passwords will be saved to the file specified by `output_file` (default: `passwords_tokenized.txt`).

    **Example `passwords_tokenized.txt` output:**
    ```
    My P@ssw0rd 123 !
    secret _ word _ 456
    another Test 789
    ```

## Evaluation Overview

Based on experimental analysis over 100,000 unique real-world passwords, the underlying framework performance yields deterministic execution characteristics across the respective leetspeak dictionary variants:

* **Small Dictionary:** Execution processing time benchmarked at `6.874 seconds`.
* **Medium Dictionary:** Execution processing time benchmarked at `7.097 seconds`.
* **Large Dictionary:** Execution processing time benchmarked at `8.423 seconds` with an optimized average per-password parsing runtime of `0.084 ms`.
