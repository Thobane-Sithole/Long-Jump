# Long Jump Information System

Welcome to the Long Jump Information System for the Olympics 2024! This program helps to record and evaluate the long jump attempts of competitors. Follow the instructions below to use the system.

## Features

- **Input Competitors**: Enter the names of competitors participating in the long jump event.
- **Record Jumps**: Record up to three jump attempts for each competitor.
- **Evaluate Results**: Determine the best jump for each competitor and identify the winner.

## Usage

1. **Clone the Repository**

    ```bash
    git clone https://github.com/yourusername/long-jump-info-system.git
    cd long-jump-info-system
    ```

2. **Run the Program**

    ```bash
    python long_jump_info_system.py
    ```

## Functions

### `get_competitors()`

Prompts the user to enter the names of competitors. Press enter without typing a name to finish entering competitors.

### `get_jumps(name)`

Records up to three jump attempts for the given competitor. The input can be a positive number representing the jump distance or "foul" for invalid jumps.

### `best_jump(jumps)`

Determines the best valid jump from the list of jumps. Returns the longest distance or "No jump" if all attempts are fouls.

### `print_results(results)`

Displays the longest distance jumped by each competitor.

### `find_winner(results)`

Finds the competitor with the longest valid jump. Returns the winner's name and distance, or `None` if no valid jumps were recorded.

### `main()`

The main function to run the program. It coordinates the input of competitors, recording of jumps, and the evaluation of results to declare the winner.

## Example

```python
if __name__ == "__main__":
    main()
```

When you run the program, follow the on-screen prompts to enter competitors and their jump attempts. The system will display the results and declare the winner.

Enjoy the Olympics 2024 and may the best jumper win!

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

Feel free to contribute to this project by submitting issues or pull requests.

For more information, contact: [your-email@example.com](mailto:your-email@example.com)

---

Happy Jumping! 🏅
