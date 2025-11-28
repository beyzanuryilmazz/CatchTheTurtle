import turtle
import random

# --- CONFIGURATION ---
drawing_board = turtle.Screen()
DRAWING_BG = "cornsilk"
DRAWING_TITLE = "Catch the Turtle"
DRAWING_SIZE = 600

# --- SETUP ---
drawing_board.bgcolor(DRAWING_BG)
drawing_board.title(DRAWING_TITLE)
drawing_board.setup(DRAWING_SIZE, DRAWING_SIZE)
drawing_board.tracer(0)


class Player(turtle.Turtle):
    def __init__(self):
        super().__init__()
        # The movement must be clear at the beginning
        self.is_moving = True
        self.shape("turtle")
        self.color("green")
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.penup()
        self.onclick(self.handle_click)

    def player_move(self):
        # If the action flag is off, stop the function (CPU Saving)
        if not self.is_moving:
            return

        x = random.randint(-250, 250)
        y = random.randint(-250, 250)

        if hasattr(self, 'teleport'):
            self.teleport(x, y)
        else:
            self.goto(x, y)

        drawing_board.update()

        # Retry after 500ms
        drawing_board.ontimer(self.player_move, 500)

    def handle_click(self, x, y):
        # Collect points only if the game is still running
        if self.is_moving:
            scoreboard.increase_score()

    def stop_movement(self):
        self.is_moving = False  # The key to breaking the loop
        self.hideturtle()


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.timer = 20
        self.score = 0
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        self.score_write()

    def score_write(self):
        self.clear()
        self.write(f"Score: {self.score} | Timer: {self.timer}", align="center", font=("Courier", 24, "bold"))

    def increase_score(self):
        self.score += 1
        self.score_write()

    def decrease_time(self):
        if self.timer > 0:
            self.timer -= 1
            self.score_write()
            drawing_board.ontimer(self.decrease_time, 1000)
        else:
            self.game_over()

    def game_over(self):
        # Call the method instead of controlling the player directly
        player.stop_movement()

        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER\nFinal Score: {self.score}", align="center", font=("Courier", 30, "bold"))

        drawing_board.update()
        # Close after 3 seconds
        drawing_board.ontimer(drawing_board.bye, 3000)


# --- GAME EXECUTION ---
scoreboard = Scoreboard()
player = Player()

# Start game loops
scoreboard.decrease_time()
player.player_move()

drawing_board.mainloop()