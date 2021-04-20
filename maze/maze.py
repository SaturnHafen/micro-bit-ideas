maze = [ # Caution! mirrored + 90° clockwise rotated
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 9, 9, 9, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 9, 9, 9, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 9, 9, 9, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
player = (10, 10) # x, y
finished = False


def generate_maze():
    pass # currently only one maze...


def normalize_heading():
    heading = input.compass_heading()

    # east
    if 60 < heading < 120: 
        return (1, 0)

    # south
    if 150 < heading < 210: 
        return (0, 1)
    
    # west
    if 240 < heading < 300: 
        return (-1, 0)

    # north
    if 330 < heading or heading < 30: 
        return (0, -1)

    # default
    return (0, 0)


def render_maze():
    for x in range(-2, 3):
        for y in range(-2, 3):
            render_pos = [player[0] + x, player[1] + y]

            if 0 <= render_pos[0] < len(maze[0]) and 0 <= render_pos[1] < len(maze): # check if pixel in bounds
                pixel = maze[render_pos[0]][render_pos[1]]

                if pixel == 1:
                    led.plot(x + 2, y + 2)

                elif pixel == 9:
                    led.plot_brightness(x + 2, y + 2, 125)

                else:
                    led.unplot(x + 2, y + 2)

            else:
                led.unplot(x + 2, y + 2)

    led.plot_brightness(2, 2, 100);


def init():
    finished = False
    generate_maze()
    player = (10, 10)
    render()


def move():
    global player
    heading = normalize_heading()
    new_pos = player[0] + heading[0], player[1] + heading[1]
    if maze[new_pos[0]][new_pos[1]] != 1:
        player = new_pos

    if maze[new_pos[0]][new_pos[1]] == 9:
        global finished
        finished = True


def render():
    if not finished:
        render_maze()
    else:
        basic.show_string("Finsihed!", 100)


def step():
    move()
    render()


input.on_button_pressed(Button.A, step)
input.on_button_pressed(Button.B, init)

init() # init on startup

normalize_heading() # required to force simulator to show compass heading
