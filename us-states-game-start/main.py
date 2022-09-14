import turtle
import pandas


screen = turtle.Screen()
screen.title("U. S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
# game_on = True
correct_answer = 0
csv_data = pandas.read_csv("50_states.csv")
# print(csv_data)
total_state_count = len(csv_data)
writer = turtle.Turtle()
writer.penup()
writer.hideturtle()
selected_states = []
state_list = csv_data["state"].to_list()

# print(str(csv_data.state).lower())
while len(selected_states) < 50:
    state_name = turtle.textinput(title=f"{correct_answer}/{total_state_count} Correct Answers",
                                  prompt="What's another State name?").title()
    if state_name == "Exit":
        state_to_lear = []
        for item in state_list:
            if item not in selected_states:
                state_to_lear.append(item)
        new_data = pandas.DataFrame(state_to_lear)
        # print(new_data)

        new_data.to_csv("state_to_lear.csv")
        break
    state_data = csv_data[csv_data.state == state_name.title()]
    if state_data.empty:
        pass
    else:
        # print(state_data)
        if state_name not in selected_states:
            writer.goto(int(state_data.x), int(state_data.y))
            writer.write(state_name, align="center")
            correct_answer += 1
            selected_states.append(state_name)


