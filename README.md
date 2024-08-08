# Pygame-Snake
# Snake Game

This project is a simple Snake game created using Python and Pygame. The objective of the game is to control the snake to eat food and grow in length. Avoid letting the snake collide with itself or the game will end.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/snake-game.git
    cd snake-game
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install pygame
    ```

## How to Play

1. Run the game:
    ```bash
    python snake_game.py
    ```

2. Use the arrow keys to control the snake:
    - **Up Arrow**: Move up
    - **Down Arrow**: Move down
    - **Left Arrow**: Move left
    - **Right Arrow**: Move right

3. The goal is to eat the food that appears on the screen. Each time the snake eats food, it grows in length and your score increases.

4. The game ends if the snake collides with itself.

## Features

- Simple and intuitive controls
- Growing snake as it eats food
- Score tracking
- Snake's head with eyes that follow the direction

## Code Overview

- `snake_game.py`: Main game file containing the game loop and logic.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have any suggestions or improvements.
