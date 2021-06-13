# Colors
background_color = (50, 50, 50)
square_color = (70, 70, 70)
snake_color = (255, 0, 0)

# Sizes
square_size = 45
square_gap = 5
horizontal_square_amount = 11
vertical_square_amount = 11
window_size = ((square_size + square_gap) * horizontal_square_amount + square_gap,
               (square_size + square_gap) * vertical_square_amount + square_gap)

# Other
initial_snake_pos = (5, 5)
initial_snake_direction = "r"  # Out of u d l r
snake_movement = {"u": (0, -1), "d": (0, 1), "l": (-1, 0), "r": (1, 0)}
snake_movement_time = 0.1
