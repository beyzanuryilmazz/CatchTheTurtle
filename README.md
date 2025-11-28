# Catch the Turtle

A dynamic, arcade-style reflex game developed using Python and the Turtle graphics library. This project demonstrates Object-Oriented Programming (OOP) principles, event-driven architecture, and asynchronous timer management in a single-threaded environment.

## Game Overview

The goal is simple: **Catch the turtle before time runs out!**
The turtle teleports to random coordinates on the screen every 0.5 seconds. You must click on it to increase your score within a 20-second timeframe.

### Key Features
- **Object-Oriented Design:** Distinct separation of concerns between the `Player` (turtle) and the `Scoreboard`.
- **Event-Driven Mechanics:** Utilizes `onclick` events for user interaction.
- **Custom Timer Logic:** Implements a recursive `ontimer` loop to manage the countdown and movement without blocking the main thread.
- **Optimization:** CPU-efficient state management (`is_moving` flag) prevents ghost processes after the game ends.
- **Graceful Shutdown:** Features a polished "Game Over" sequence with a non-blocking exit delay.

## Technical Stack

- **Language:** Python 3.x
- **Library:** `turtle` (Python Standard Library), `random`, `time` mechanism.
- **Architecture:** OOP, Event Loop.

## How to Run

Since the project uses Python's standard libraries, no external installation (`pip install`) is required.

1. **Clone the repository:**
   ```bash
   git clone git clone https://github.com/beyzanuryilmazz/catch-the-turtle.git
   cd catch-the-turtle
   
2. **Run the game:**
    ```bash
   python main.py
   
## Project Structure
   ```bash
    catch-the-turtle/
    │
    ├── main.py        # The entry point containing Game Loop and Classes
    ├── .gitignore     # Configuration for clean repository
    └── README.md      # Project documentation
