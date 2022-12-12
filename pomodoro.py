from tkinter import *
import math


#initialize global variables
FONT_NAME = 'Courier'
LONG_BREAK_MIN = 20
REPS = 0
SHORT_BREAK_MIN = 5
TIMER = None
WORK_MIN = 1
#colors
GREEN = '#9bdeac'
PINK = '#e2979c'
RED = '#e7305b'
YELLOW = '#f7f5dd'
#window relevant
WINDOW = Tk()
CANVAS = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
TOMATO = PhotoImage(file='tomato.png')
#labels
CHECKMARKS = Label(font=(FONT_NAME, 22, 'bold'), bg=YELLOW, fg=GREEN)
TITLE = Label(text='Timer', font=(FONT_NAME, 36, 'bold'), bg=YELLOW, fg=GREEN)


def reset_timer():
    '''Acts as the reset timer functionality.'''
    WINDOW.after_cancel(TIMER)
    CANVAS.itemconfig(TIMER_TEXT, text='00:00')
    TITLE.config(text='Timer')
    CHECKMARKS.config(text='')
    global REPS
    REPS = 0


def start_timer():
    '''Starts the timer and acts as main functionality.'''
    global REPS
    REPS += 1

    sec = WORK_MIN * 60
    short = SHORT_BREAK_MIN * 60
    long = LONG_BREAK_MIN * 60

    if REPS % 8 == 0:
        count_down(long)
        TITLE.config(text='Break', fg=RED)
    if REPS % 2 == 0:
        count_down(short)
        TITLE.config(text='Break', fg=PINK)
    else:
        count_down(sec)
        TITLE.config(text='Work', fg=GREEN)


def count_down(count):
    '''Acts as the count down functionality.'''
    min = math.floor(count / 60)
    sec = count % 60
    if sec < 10:
        sec = f'0{sec}'
    if min < 10:
        min = f'0{min}'

    CANVAS.itemconfig(TIMER_TEXT, text=f'{min}:{sec}')
    if count > 0:
        global TIMER
        TIMER = WINDOW.after(1000, count_down, count - 1)
    else:
        start_timer()
        # temp portrays the checkmarks adding every 2 rounds
        temp = ''
        work_sessions = math.floor(REPS/2)
        for n in range(work_sessions):
            temp += '✅'
        CHECKMARKS.config(text=temp)


#global variable located here because python does not support hoisting
#buttons
START = Button(text='Start', command=start_timer)
RESET = Button(text='Reset', command=reset_timer)


#window configurations
WINDOW.title('Pomodoro')
WINDOW.config(padx=100, pady=50, bg=YELLOW)
CANVAS.create_image(100, 112, image=TOMATO)
TIMER_TEXT = CANVAS.create_text(100, 135, text='00:00', fill='white', font=(FONT_NAME, 30, 'bold'))
CANVAS.grid(column=1, row=1)
START.grid(column=0, row=2)
RESET.grid(column=2, row=2)
TITLE.grid(column=1, row=0)
CHECKMARKS.grid(column=1, row=3)


#necessary for tkinter windows
WINDOW.mainloop()
