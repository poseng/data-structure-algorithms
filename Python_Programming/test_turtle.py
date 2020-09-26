# imports at the top
import turtle

# other function def
def main():
    # this line reads a line of input from the user
    filename = input("Please enter drawing filename: ")

    # create a turtle graphi window to draw in
    t = turtle.Turtle()

    # the screen is used at the end of the program
    screen = t.getscreen()

    # open the drawing command file

    file = open(filename, "r")

    # for loop to read the command line by line
    for line in file:
        # strip off the newline character at the end of the line and any blank
        text = line.strip()
        commandList = text.split(",")

        # get the drawing command
        command = commandList[0]
        if command == "goto":
            x = float(commandList[1])
            y = float(commandList[2])
            width = float(commandList[3])
            color = commandList[4].strip()
            t.width(width)
            t.pencolor(color)
            t.goto(x,y)
        elif command == "circle":
            radius = float(commandList[1])
            width = float(commandList[2])
            color = commandList[3].strip()
            t.width(width)
            t.pencolor(color)
            t.circle(radius)
        elif command == "beginfill":
            color = commandList[1].strip()
            t.fillcolor(color)
            t.begin_fill()
        elif command == "endfill":
            t.end_fill();
        elif command == "penup":
            t.penup()
        elif command == "pendown":
            t.pendown()
        else:
            print("Unknown command found in file : ", command)

    # close file
    file.close()
    # hide the turtle that we use to draw the picture
    t.ht()


    # This caused the program to hold the turtle graphic window open until click on it
    screen.exitonclick()
    print("Program Execution complete")

# this code call the main function to get everything started. The condition in
# this if statement evaluate to True when teh module is executed by teh ine.
if __name__ == "__main__":
    main()