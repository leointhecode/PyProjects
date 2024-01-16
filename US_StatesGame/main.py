import pandas
import turtle as t
IMAGE = "blank_states_img.gif"
FONT = ('Arial', 8, 'normal')

data = pandas.read_csv("50_states.csv")
state_name = data.state

screen = t.Screen()
screen.title("US states game")
screen.addshape(IMAGE)
t.shape(IMAGE)

writer = t.Turtle()
writer.ht()
writer.penup()

guessed_states = []
counter = 0
while counter <= 50:
    state_answer = screen.textinput(title=f"{counter}/50 States Correct", prompt="Which state can you identify?")
    if state_answer == "Exit":
        missing_states = [state for state in data.state if (state.lower() not in guessed_states)]
        states_to_learn = pandas.Series(missing_states)
        states_to_learn.to_csv("states to learn")
        break
    
    for names in state_name:
        if state_answer.lower() == names.lower():
            writer.goto(int(data[data.state == names].x), int(data[data.state == names].y))
            writer.write(arg=names, align="center", font=FONT)
            guessed_states.append(state_answer)
            counter += 1

screen.exitonclick()
