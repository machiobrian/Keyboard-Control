import curses
import RPi.GPIO as gpio

screen = curses.initscr() # Get the curses window,
curses.noecho() # turn off echoing of the keyboard to screen
                # turn on instantly key response -> no waiting,
curses.cbreak() # use special values for cursor keys
screen.keypad(True)

#set the gpio numbering mode and define the output pins
gpio.setmode(gpio.BOARD)
gpio.setup(7, gpio.out)
gpio.setup(11, gpio.out)
gpio.setup(13, gpio.out)
gpio.setup(15, gpio.out)


try: #lets us check for errors
    while True:
        char = screen.getch()
        if char == ord('q'):
            break
        elif char == curses.KEY_UP:
            gpio.output(7,True) #dependent on hoe we've set up our motors
            gpio.output(7,False)
            gpio.output(7,False)
            gpio.output(7,True)
        elif char == curses.KEY_DOWN:
            gpio.output(7,False)
            gpio.output(7,False)
            gpio.output(7,True)
            gpio.output(7,True)
        elif char == curses.KEY_RIGHT:
            gpio.output(7,True)
            gpio.output(7,True)
            gpio.output(7,False)
            gpio.output(7,False)
        elif char == curses.KEY_LEFT:
            gpio.output(7,False)
            gpio.output(7,True)
            gpio.output(7,True)
            gpio.output(7,False)
        elif char == 10: #the enter key
            gpio.output(7,False)
            gpio.output(7,False)
            gpio.output(7,False)
            gpio.output(7,False)
finally:
    #close down curses properly.
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()