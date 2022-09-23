import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guess_list = []
right_number = 0

data = pandas.read_csv("50_states.csv")
df = pandas.DataFrame(data)
states_list = df["state"].to_list()
game_is_on = True


while game_is_on:
    if right_number == 50:
        game_is_on = False
    answer_state = screen.textinput(title=f"Correct {right_number}/50",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        no_guess_list = [i for i in states_list if i not in guess_list]
        result = pandas.DataFrame(no_guess_list)
        result.to_csv("states_to_learn.csv")
        break
    if answer_state in states_list and answer_state not in guess_list:
        guess_list.append(answer_state)
        state = data[data.state == answer_state]
        x = int(state.x)
        y = int(state.y)
        new_state = turtle.Turtle()
        new_state.hideturtle()
        new_state.penup()
        new_state.goto(x, y)
        new_state.write(answer_state)
        right_number += 1













screen.exitonclick()