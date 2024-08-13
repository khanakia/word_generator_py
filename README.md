# Words Combination Generator

## Description

This Python script generates all possible permutations of a given set of characters and saves them into a SQLite database. It can handle any combination of characters, including letters (a-z), numbers (0-9), or any other custom characters. The script is useful for tasks that require generating all possible combinations of a set of characters, such as password cracking, generating test cases, or combinatorial problems.

## Features

- Generate permutations for any given set of characters.
- Saves permutations into a SQLite database.
- Easy to use and configure.
- Highly customizable to fit different needs.

## Requirements

- Python 3.x
- Taskfile command manager

## Installation

1. Ensure you have Python 3 installed on your system. You can download it from [python](https://www.python.org/downloads/).
2. Ensure you have Taskfile command manager installed. You can find installation instructions [here](https://taskfile.dev/#/installation).
3. Download or clone this repository to your local machine.

## Usage

1. Navigate to the directory where the script is located.
2. Run the `task migrate` command to create the `db.sqlite3` database file:
    ```sh
    task migrate
    ```
3. Open the script file (`main.py`) in a text editor.
4. Customize the `characters` variable with the set of characters you want to generate permutations for. For example:
    ```python
    characters = 'abc'  # Customize this string with your desired characters
    ```
5. Run the script using the following command:
    ```sh
    python main.py
    ```

## Example

Here is an example of how to use the script:

1. Set the characters to 'abc':
    ```python
    characters = 'abc'
    ```
2. Run the `task migrate` command:
    ```sh
    task migrate
    ```
3. Run the script:
    ```sh
    python main.py
    ```
4. The permutations will be saved into the `db.sqlite3` database in the `words` table.

## Customization

- You can change the characters to any combination you want by modifying the `characters` variable.
- You can also change the length of the permutations by modifying the `permutations` function call.

## Database Structure

- The SQLite database file (`db.sqlite3`) will contain a table called `words`.
- The `words` table will have the following structure:
    - `id` (INTEGER PRIMARY KEY AUTOINCREMENT): Unique identifier for each permutation.
    - `name` (TEXT): The generated permutation.

## SQL commands
```sql
SELECT count(*) FROM words;
```

## Permutation Calculator
https://www.calculatorsoup.com/calculators/discretemathematics/permutations.php

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request. We welcome all contributions!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This script uses Python's built-in `itertools` module for generating permutations.
- This script uses SQLite for storing the permutations.

## Contact

If you have any questions or suggestions, please feel free to open an issue or contact the repository owner.

---

Thank you for using the Words Combination Generator! Happy coding!