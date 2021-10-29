# Tkinter math Capstone project
# This will be a GUI program that showcases almost almost all the math projects located in the udemy course
# Each project will be separated by a tab

# The programs are as follows:

# Find Pi to the nth digit [complete]
# Find E to the nth digit  [complete]

# Fibonacci sequence [incomplete] - tidy gui, centralise widgets properly, change result to scrollbar, update limit
# Prime Factorization [incomplete] - tidy gui, centralise widgets properly, change result to scrollbar, update limit
# Next prime number [incomplete] - tidy gui, centralise widgets properly, change result to scrollbar, update limit
# Find the cost to cover W x H floor [incomplete] - tidy gui
# Mortgage calculator [incomplete] - tidy gui
# Change return program [incomplete]  - tidy gui, allow results ro remain central, fix code?
# Binary to Decimal and Back Converter [incomplete] - tidy gui

# Scientific Calculator [complete]

# Unit Converter (temp, currency, volume, mass and more) [incomplete] - change this program to use the internet for conversions
# Alarm Clock [incomplete] - add text wrapping to song title, stop song button on message box
# Distance Between Two Cities [incomplete] - change colour to blue for drop down boxes?
# Credit Card Validator [incomplete] - add examples for credit card numbers, drop down box?

# Tax Calculator [complete]

# Factorial Finder [incomplete] - add scroll bar to results
# Happy Numbers [incomplete] - add calculations to a scroll bar , add focus if needed

# Number Names [complete]
# Coin Flip Simulation [complete]
# Exponentiation [complete]

# once all completed, upload to GITHUB

### IMPORTS ###
from tkinter import *
from mpmath import mp
from tkinter import ttk
import tkinter.scrolledtext as scrolledtext
import decimal
import sympy
import winsound
import datetime
import math
import numpy # potentially need to remove this if not used
from tkinter import messagebox
from tkinter import filedialog
import os
import pygame
from ttkwidgets.autocomplete import AutocompleteCombobox
import bs4
import requests
import pyttsx3
import threading
import random
### END OF IMPORTS ###


### TKINTER WINDOW CONFIGURATION ###
window = Tk()
window.title("Udemy Mathematics Capstone Project")
window.resizable(True, True)
window.state("zoomed")
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
### END OF TKINTER WINDOW CONFIGURATION ###


### INITIALISE SOUND ###
# Initialise Pygame mixer
pygame.mixer.init()

# Initial text to speech engine
engine = pyttsx3.init()
### END OF INITIALISE SOUND ###


### TKINTER FRAME CONFIGURATION ###
# Creates all the frames and sets their background to blue
welcome_screen_frame = Frame(window, bg='royalblue4')
pi_to_nth_digit_frame = Frame(window, bg='royalblue4')
e_to_nth_digit_frame = Frame(window, bg='royalblue4')
fibonacci_sequence_frame = Frame(window, bg='royalblue4')
prime_factorization_frame = Frame(window, bg='royalblue4')
next_prime_frame = Frame(window, bg='royalblue4')
w_x_h_floor_frame = Frame(window, bg='royalblue4')
morgage_calculator_frame = Frame(window, bg='royalblue4')
binary_to_decimal_frame = Frame(window, bg='royalblue4')
change_return_frame = Frame(window, bg='royalblue4')
calculator_frame = Frame(window, bg='royalblue4')
unit_converter_frame = Frame(window, bg='royalblue4')
alarm_clock_frame = Frame(window, bg='royalblue4')
distance_two_cities_frame = Frame(window, bg='royalblue4')
credit_card_validator_frame = Frame(window, bg='royalblue4')
tax_calculator_frame = Frame(window, bg='royalblue4')
factorial_finder_frame = Frame(window, bg='royalblue4')
happy_number_frame = Frame(window, bg='royalblue4')
number_name_frame = Frame(window, bg='royalblue4')
coin_flip_frame = Frame(window, bg='royalblue4')
exponentiation_frame = Frame(window, bg='royalblue4')

# Stretches all frame to fit window
for frame in (welcome_screen_frame,
              pi_to_nth_digit_frame,
              e_to_nth_digit_frame,
              fibonacci_sequence_frame,
              next_prime_frame,
              prime_factorization_frame,
              w_x_h_floor_frame,
              morgage_calculator_frame,
              change_return_frame,
              binary_to_decimal_frame,
              calculator_frame,
              unit_converter_frame,
              alarm_clock_frame,
              distance_two_cities_frame,
              credit_card_validator_frame,
              tax_calculator_frame,
              factorial_finder_frame,
              happy_number_frame,
              number_name_frame,
              coin_flip_frame,
              exponentiation_frame):
    frame.grid(row=0, column=0, sticky="nsew")

# Allows different frames to be shown when clicking on the menubar, also adds focus to the entry box if relevant
def show_frame(frame_parameter):

    frame_parameter.tkraise()

    if frame_parameter == pi_to_nth_digit_frame:
        pi_to_nth_digit_entry.focus()
    elif frame_parameter == e_to_nth_digit_frame:
        e_to_nth_digit_entry.focus()
    elif frame_parameter == fibonacci_sequence_frame:
        fibonacci_sequence_entry.focus()
    elif frame_parameter == next_prime_frame:
        next_prime_entry.focus()
    elif frame_parameter == w_x_h_floor_frame:
        w_x_h_floor_cost_label.focus()
    elif frame_parameter == morgage_calculator_frame:
        morgage_calculator_total_entry.focus()
    elif frame_parameter == change_return_frame:
        change_return_item_cost_entry.focus()
    elif frame_parameter == binary_to_decimal_frame:
        binary_to_decimal_entry.focus()
    elif frame_parameter == credit_card_validator_frame:
        card_validator_entry.focus()
    elif frame_parameter == tax_calculator_frame:
        simple_tax_entry.focus()
    elif frame_parameter == factorial_finder_frame:
        factorial_finder_entry.focus()
    elif frame_parameter == happy_number_frame:
        happy_numbers_entry.focus()
    elif frame_parameter == number_name_frame:
        number_name_entry.focus()
    elif frame_parameter == coin_flip_frame:
        coin_flip_entry.focus()
    elif frame_parameter == exponentiation_frame:
        exponentiation_x_entry.focus()


# Creates menubar that has a list of all the frames
menubar = Menu(window)

select_program = Menu(menubar, tearoff=0)

menubar.add_cascade(label='Select Program', menu=select_program)

select_program.add_command(label='Welcome Screen', command=lambda: show_frame(welcome_screen_frame))
select_program.add_separator()
select_program.add_command(label='Find Pi to the nth digit', command=lambda: show_frame(pi_to_nth_digit_frame))
select_program.add_command(label='Find e to the nth digit', command=lambda: show_frame(e_to_nth_digit_frame))
select_program.add_command(label='Fibonachi Sequence', command=lambda: show_frame(fibonacci_sequence_frame))
select_program.add_command(label='Prime Factorization', command=lambda: show_frame(prime_factorization_frame))
select_program.add_command(label='Next prime number', command=lambda: show_frame(next_prime_frame))
select_program.add_command(label='Cost to cover W x H floor', command=lambda: show_frame(w_x_h_floor_frame))
select_program.add_command(label='Mortgage calculator', command=lambda: show_frame(morgage_calculator_frame))
select_program.add_command(label='Change return', command=lambda: show_frame(change_return_frame))
select_program.add_command(label='Binary to Decimal and Back Converter', command=lambda: show_frame(binary_to_decimal_frame))
select_program.add_command(label='Scientific Calculator', command=lambda: show_frame(calculator_frame))
select_program.add_command(label='Unit Converter', command=lambda: show_frame(unit_converter_frame))
select_program.add_command(label='Alarm Clock', command=lambda: show_frame(alarm_clock_frame))
select_program.add_command(label='Distance Between Two Cities', command=lambda: show_frame(distance_two_cities_frame))
select_program.add_command(label='Credit Card Validator', command=lambda: show_frame(credit_card_validator_frame))
select_program.add_command(label='Tax Calculator', command=lambda: show_frame(tax_calculator_frame))
select_program.add_command(label='Factorial Finder', command=lambda: show_frame(factorial_finder_frame))
select_program.add_command(label='Happy Numbers', command=lambda: show_frame(happy_number_frame))
select_program.add_command(label='Number Names', command=lambda: show_frame(number_name_frame))
select_program.add_command(label='Coin Flip Simulation', command=lambda: show_frame(coin_flip_frame))
select_program.add_command(label='Exponentiation', command=lambda: show_frame(exponentiation_frame))
select_program.add_separator()
select_program.add_command(label='Exit', command=exit)
### END OF TKINTER FRAME CONFIGURATION ###


# Global variables for number to text: - potentially need to remove this once I get to it
one_to_nine_dict = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six',
                    '7': 'seven', '8': 'eight', '9': 'nine'}
ten_to_nineteen_dict = {'10': 'ten', '11': 'eleven', '12': 'twelve', '13': 'thirteen', '14': 'fourteen',
                        '15': 'fifteen', '16': 'sixteen', '17': 'seventeen', '18': 'eighteen', '19': 'nineteen'}
twenty_to_ninety_dict = {'2': 'twenty', '3': 'thirty', '4': 'forty', '5': 'fifty', '6': 'sixty', '7': 'seventy',
                         '8': 'eighty', '9': 'ninety'}

groups_of_three_list = []
text_output = ''


### BUTTON FUNCTIONS ###

### Pi to nth Digit ###
def pi_to_nth_digit_submit():
    try:
        pi_to_nth_digit_results.delete('1.0', END)

        if 0 < int(pi_to_nth_digit_entry.get()) <= 10000:
            mp.dps = int(pi_to_nth_digit_entry.get())
            pi_to_nth_digit_results.insert(END, f'Pi to {pi_to_nth_digit_entry.get()} digits is:\n\n{mp.pi}')

        else:
            pi_to_nth_digit_results.insert(END, 'Please enter a valid number between 1-10,000')
            pi_to_nth_digit_entry.delete(0, END)

    except ValueError:
        pi_to_nth_digit_results.insert(END, 'Please enter a valid number between 1-10,000')
        pi_to_nth_digit_entry.delete(0, END)


### e to the nth digit button ###
def e_to_nth_digit_submit():

    try:
        e_to_nth_digit_results.delete('1.0', END)

        if 0 < int(e_to_nth_digit_entry.get()) <= 10000:
            e_to_nth_digit_results.insert(END, f'e to {e_to_nth_digit_entry.get()} digits is:\n\n{sympy.N(sympy.E, int(e_to_nth_digit_entry.get()))}')

        else:
            e_to_nth_digit_results.insert(END, 'Please enter a valid number between 1-10,000')
            e_to_nth_digit_results.delete(0, END)

    except ValueError:
        e_to_nth_digit_results.insert(END, 'Please enter a valid number between 1-10,000')
        e_to_nth_digit_results.delete(0, END)


### fibonachi sequence ###
def fibonacci_sequence_submit():
    num_1 = 0
    num_2 = 1
    fib_seq = []

    try:
        if int(fibonacci_sequence_entry.get()) > 30 or int(fibonacci_sequence_entry.get()) < 1:
            fibonacci_sequence_results.config(text='Please enter a valid number between 1-30')
            fibonacci_sequence_entry.delete(0, END)
        else:
            digits = int(fibonacci_sequence_entry.get())

            for digit in range(int(digits)):
                fib_seq.append(str(num_1))
                next_fib = num_1 + num_2
                num_1 = num_2
                num_2 = next_fib

            fib_text = ', '.join(fib_seq)

            fibonacci_sequence_results.config(
                text=f'The first {fibonacci_sequence_entry.get()} numbers in the fibonacci sequence are:\n\n{fib_text}')
            fibonacci_sequence_entry.delete(0, END)

    except ValueError:
        fibonacci_sequence_results.config(text='Please enter a valid number between 1-30')
        fibonacci_sequence_entry.delete(0, END)


### Next prime number ###
def next_prime_submit():
    prime_counter = 0
    prime_index = 2
    prime_list = []

    try:
        if int(next_prime_entry.get()) > 40 or int(next_prime_entry.get()) < 1:
            next_prime_results.config(text='Please enter a valid number between 1-40')
            next_prime_entry.delete(0, END)

        else:
            total_prime_request = int(next_prime_entry.get())

            while prime_counter < total_prime_request:
                prime_check = 0
                if prime_index > 1:
                    for prime_index_2 in range(2, prime_index):
                        if (prime_index % prime_index_2) == 0:
                            prime_check = 1
                if prime_check == 0:
                    prime_counter += 1

                    prime_list.append(str(prime_index))

                prime_text = ', '.join(prime_list)

                next_prime_results.config(text=f'The first {total_prime_request} prime numbers are:\n\n{prime_text}')

                prime_index += 1
                next_prime_entry.delete(0, END)

    except ValueError:
        next_prime_results.config(text='Please enter a valid number between 1-40')
        next_prime_entry.delete(0, END)


### Cost to cover W x H floor ###
def w_x_h_floor_button():
    try:
        tile_cost = float(w_x_h_floor_cost_entry.get())
        tile_height = int(w_x_h_floor_height_entry.get())
        tile_width = int(w_x_h_floor_width_entry.get())

        tile_text = tile_cost * tile_height * tile_width

        w_x_h_floor_results.config(text=f'\nTotal cost to tile the floor is:\n ${"{0:.2f}".format(tile_text)}')

    except ValueError:
        w_x_h_floor_results.config(text='\n\n\n\nPlease enter a valid number.')


### Morgage Calculator ###
def morgage_calculator_button():
    try:
        total = float(morgage_calculator_total_entry.get())
        interest = float(morgage_calculator_interest_rate_entry.get())
        years = float(morgage_calculator_year_of_loan_entry.get())

        interest = interest / 100
        monthly_interest = interest / 12
        months = years * 12

        if float(morgage_calculator_total_entry.get()) < 0:
            morgage_calculator_results.config(text='Morgage total needs to be larger than 0.')

        elif float(morgage_calculator_interest_rate_entry.get()) < 0:
            morgage_calculator_results.config(text='Interest rate needs to be larger than 0.')

        elif float(morgage_calculator_year_of_loan_entry.get()) < 0:
            morgage_calculator_results.config(text='Total months of loan needs to be larger than 0.')

        else:

            monthly_amount = float("{0:.2f}".format(total * (monthly_interest * ((1 + monthly_interest) ** months)) / (
                    (1 + monthly_interest) ** months - 1)))

            if morgage_calculator_combobox.get() == 'Monthly':
                morgage_calculator_results.config(
                    text=f'Your morgage repayment are:\n ${monthly_amount} per month, for {int(months)} months')

            elif morgage_calculator_combobox.get() == 'Fortnightly':
                morgage_calculator_results.config(
                    text=f'Your morgage repayment are:\n ${monthly_amount / 2} per Fortnight, for {int(months * 2)} Fortnights')

            else:
                morgage_calculator_results.config(
                    text=f'Your morgage repayment are:\n ${monthly_amount / 4} per week, for {int(months * 4)} weeks')

    except ValueError:
        morgage_calculator_results.config(text='Please enter valid numbers into fields.')


### Change return program ###
def change_return_submit():
    fifty_dollars = 0
    twenty_dollars = 0
    ten_dollars = 0
    five_dollars = 0
    two_dollars = 0
    one_dollars = 0
    fifty_cents = 0
    twenty_cents = 0
    ten_cents = 0
    five_cents = 0

    try:

        item_cost = decimal.Decimal(change_return_item_cost_entry.get())
        amount_paid = decimal.Decimal(change_return_amount_paid_entry.get())

        difference = amount_paid * 100 - item_cost * 100

        change_return_change_owed_label.config(text=f'Change owed ${difference / 100}')

        while difference - 5000 >= 0:
            fifty_dollars += 1
            difference -= 5000

        while difference - 2000 >= 0:
            twenty_dollars += 1
            difference -= 2000

        while difference - 1000 >= 0:
            ten_dollars += 1
            difference -= 1000

        while difference - 500 >= 0:
            five_dollars += 1
            difference -= 500

        while difference - 200 >= 0:
            two_dollars += 1
            difference -= 200

        while difference - 100 >= 0:
            one_dollars += 1
            difference -= 100

        while difference - 50 >= 0:
            fifty_cents += 1
            difference -= 50

        while difference - 20 >= 0:
            twenty_cents += 1
            difference -= 20

        while difference - 10 >= 0:
            ten_cents += 1
            difference -= 10

        while difference - 5 >= 0:
            five_cents += 1
            difference -= 5

        change_return_results.config(text=f'$50 notes:     {fifty_dollars}\n'
                                          f'$20 notes:     {twenty_dollars}\n'
                                          f'$10 notes:     {ten_dollars}\n'
                                          f'$5 notes:      {five_dollars}\n'
                                          f'$2 coins:      {two_dollars}\n'
                                          f'$1 coins:      {one_dollars}\n'
                                          f'$0.50 coins: {fifty_cents}\n'
                                          f'$0.20 coins: {twenty_cents}\n'
                                          f'$0.10 coins: {ten_cents}\n'
                                          f'$0.05 coins: {five_cents}')

    except ValueError:
        change_return_change_owed_label.config(text='Please enter valid numbers into fields.')

    except decimal.InvalidOperation:
        change_return_change_owed_label.config(text='Please enter valid numbers into fields.')


### binary to decimal converter ###
def binary_to_decimal_submit():
    try:

        if binary_combobox.get() == 'Decimal to Binary':
            bin_dec_value = int(binary_to_decimal_entry.get())
            binary_to_decimal_results.config(text=f'The binary value of {bin_dec_value} is:\n\n{bin(bin_dec_value)}')
            binary_to_decimal_entry.delete(0, END)

        elif binary_combobox.get() == 'Binary to Decimal':
            bin_dec_value = binary_to_decimal_entry.get()
            binary_to_decimal_results.config(
                text=f'The numerical value of {bin_dec_value} is:\n\n{int(bin_dec_value, 2)}')
            binary_to_decimal_entry.delete(0, END)

    except ValueError:
        binary_to_decimal_results.config(text='Please enter a valid value.')
        binary_to_decimal_entry.delete(0, END)


## SCIENTIFIC CALCULATOR BUTTON FUNCTIONS ##
calculator_string = ''


def formatNumber(num):
    if num % 1 == 0:
        return int(num)
    else:
        return num


def calc_all_clear():
    global calculator_string
    calculator_entry.config(state=NORMAL)
    calculator_entry.delete(0, END)
    calculator_string = ''
    calculator_entry.config(state=DISABLED)


def calc_delete_last():
    global calculator_string
    calculator_entry.config(state=NORMAL)
    calculator_entry.delete(calculator_entry.index("end") - 1)
    calculator_string = calculator_string[:-1]
    calculator_entry.config(state=DISABLED)


def calc_equals():
    global calculator_string, ans_string
    calculator_entry.config(state=NORMAL)
    calculator_entry.delete(0, END)
    try:
        calculator_string = str(formatNumber(eval(calculator_string)))
        calculator_entry.insert(0, calculator_string)

        ans_string = f'{calculator_string}'
        calculator_entry.config(state=DISABLED)
    except SyntaxError:
        calculator_entry.insert(0, 'Syntax ERROR')
        calculator_entry.config(state=DISABLED)

    except ValueError:
        calculator_entry.insert(0, 'Syntax ERROR')
        calculator_entry.config(state=DISABLED)


def calc_1():
    global calculator_string
    calculator_entry.config(state=NORMAL)
    calculator_entry.insert(calculator_entry.index("end"), 1)
    calculator_string += '1'
    calculator_entry.config(state=DISABLED)


def calc_2():
    global calculator_string
    calculator_entry.config(state=NORMAL)
    calculator_entry.insert(calculator_entry.index("end"), 2)
    calculator_string += '2'
    calculator_entry.config(state=DISABLED)


def calc_3():
    global calculator_string
    calculator_entry.config(state=NORMAL)
    calculator_entry.insert(calculator_entry.index("end"), 3)
    calculator_string += '3'
    calculator_entry.config(state=DISABLED)


def calc_4():
    global calculator_string
    calculator_entry.config(state=NORMAL)
    calculator_entry.insert(calculator_entry.index("end"), 4)
    calculator_string += '4'
    calculator_entry.config(state=DISABLED)


def calc_5():
    global calculator_string
    calculator_entry.config(state=NORMAL)
    calculator_entry.insert(calculator_entry.index("end"), 5)
    calculator_string += '5'
    calculator_entry.config(state=DISABLED)


def calc_6():
    global calculator_string
    calculator_entry.config(state=NORMAL)
    calculator_entry.insert(calculator_entry.index("end"), 6)
    calculator_string += '6'
    calculator_entry.config(state=DISABLED)


def calc_7():
    global calculator_string
    calculator_entry.config(state=NORMAL)
    calculator_entry.insert(calculator_entry.index("end"), 7)
    calculator_string += '7'
    calculator_entry.config(state=DISABLED)


def calc_8():
    global calculator_string
    calculator_entry.config(state=NORMAL)
    calculator_entry.insert(calculator_entry.index("end"), 8)
    calculator_string += '8'
    calculator_entry.config(state=DISABLED)


def calc_9():
    global calculator_string
    calculator_entry.config(state=NORMAL)
    calculator_entry.insert(calculator_entry.index("end"), 9)
    calculator_string += '9'
    calculator_entry.config(state=DISABLED)


def calc_0():
    global calculator_string
    calculator_entry.config(state=NORMAL)
    calculator_entry.insert(calculator_entry.index("end"), 0)
    calculator_string += '0'
    calculator_entry.config(state=DISABLED)


def calc_plus():
    global calculator_string
    calculator_entry.config(state=NORMAL)
    calculator_entry.insert(calculator_entry.index("end"), '+')
    calculator_string += '+'
    calculator_entry.config(state=DISABLED)


def calc_minus():
    global calculator_string
    calculator_entry.config(state=NORMAL)
    calculator_entry.insert(calculator_entry.index("end"), '-')
    calculator_string += '-'
    calculator_entry.config(state=DISABLED)


def calc_decimal():
    global calculator_string
    calculator_entry.config(state=NORMAL)
    calculator_entry.insert(calculator_entry.index("end"), '.')
    calculator_string += '.'
    calculator_entry.config(state=DISABLED)


def calc_multiply():
    global calculator_string
    calculator_entry.config(state=NORMAL)
    calculator_entry.insert(calculator_entry.index("end"), 'x')
    calculator_string += '*'
    calculator_entry.config(state=DISABLED)


def calc_divide():
    global calculator_string
    calculator_entry.config(state=NORMAL)
    calculator_entry.insert(calculator_entry.index("end"), '÷')
    calculator_string += '/'
    calculator_entry.config(state=DISABLED)


def calc_left_bracket():
    global calculator_string
    calculator_entry.config(state=NORMAL)
    calculator_entry.insert(calculator_entry.index("end"), '(')
    calculator_string += '('
    calculator_entry.config(state=DISABLED)


def calc_right_bracket():
    global calculator_string
    calculator_entry.config(state=NORMAL)
    calculator_entry.insert(calculator_entry.index("end"), ')')
    calculator_string += ')'
    calculator_entry.config(state=DISABLED)


def calc_pi():
    global calculator_string
    calculator_entry.config(state=NORMAL)
    calculator_entry.insert(calculator_entry.index("end"), 'π')
    calculator_string += 'math.pi'
    calculator_entry.config(state=DISABLED)


def calc_square():
    global calculator_string
    calculator_entry.config(state=NORMAL)
    calculator_entry.insert(calculator_entry.index("end"), '^2')
    calculator_string += '**2'
    calculator_entry.config(state=DISABLED)


def calc_cube():
    global calculator_string
    calculator_entry.config(state=NORMAL)
    calculator_entry.insert(calculator_entry.index("end"), '^3')
    calculator_string += '**3'
    calculator_entry.config(state=DISABLED)


def calc_power():
    global calculator_string
    calculator_entry.config(state=NORMAL)
    calculator_entry.insert(calculator_entry.index("end"), '^')
    calculator_string += '**'
    calculator_entry.config(state=DISABLED)


def calc_sin():
    global calculator_string
    calculator_entry.config(state=NORMAL)
    calculator_entry.insert(calculator_entry.index("end"), 'sin(')
    calculator_string += 'math.sin('
    calculator_entry.config(state=DISABLED)


def calc_cos():
    global calculator_string
    calculator_entry.config(state=NORMAL)
    calculator_entry.insert(calculator_entry.index("end"), 'cos(')
    calculator_string += 'math.cos('
    calculator_entry.config(state=DISABLED)


def calc_tan():
    global calculator_string
    calculator_entry.config(state=NORMAL)
    calculator_entry.insert(calculator_entry.index("end"), 'tan(')
    calculator_string += 'math.tan('
    calculator_entry.config(state=DISABLED)


def calc_sqrt():
    global calculator_string
    calculator_entry.config(state=NORMAL)
    calculator_entry.insert(calculator_entry.index("end"), '√(')
    calculator_string += 'math.sqrt('
    calculator_entry.config(state=DISABLED)


def calc_inverse():
    global calculator_string
    calculator_entry.config(state=NORMAL)
    calculator_entry.insert(calculator_entry.index("end"), '^(-1)')
    calculator_string += '**(-1)'
    calculator_entry.config(state=DISABLED)


def calc_percent():
    global calculator_string
    calculator_entry.config(state=NORMAL)
    calculator_entry.insert(calculator_entry.index("end"), '%')
    calculator_string += '/(100)'
    calculator_entry.config(state=DISABLED)


def calc_third_root():
    global calculator_string
    calculator_entry.config(state=NORMAL)
    calculator_entry.insert(calculator_entry.index("end"), '3√(')
    calculator_string += 'numpy.cbrt('
    calculator_entry.config(state=DISABLED)


def calc_abs():
    global calculator_string
    calculator_entry.config(state=NORMAL)
    calculator_entry.insert(calculator_entry.index("end"), 'Abs(')
    calculator_string += 'abs('
    calculator_entry.config(state=DISABLED)


def calc_log():
    global calculator_string
    calculator_entry.config(state=NORMAL)
    calculator_entry.insert(calculator_entry.index("end"), 'log(')
    calculator_string += 'math.log10('
    calculator_entry.config(state=DISABLED)


def calc_ln():
    global calculator_string
    calculator_entry.config(state=NORMAL)
    calculator_entry.insert(calculator_entry.index("end"), 'ln(')
    calculator_string += 'math.log('
    calculator_entry.config(state=DISABLED)


def calc_e():
    global calculator_string
    calculator_entry.config(state=NORMAL)
    calculator_entry.insert(calculator_entry.index("end"), 'e')
    calculator_string += 'math.e'
    calculator_entry.config(state=DISABLED)


def calc_factorial():
    global calculator_string
    calculator_entry.config(state=NORMAL)
    calculator_entry.insert(calculator_entry.index("end"), 'factorial(')
    calculator_string += 'math.factorial('
    calculator_entry.config(state=DISABLED)


def calc_ans():
    global calculator_string, ans_string
    calculator_entry.config(state=NORMAL)
    calculator_entry.insert(calculator_entry.index("end"), 'Ans')
    calculator_string += ans_string
    calculator_entry.config(state=DISABLED)


## UNIT CONVERTER  ##


# TOP COMBOBOX
def unit_converter_top_combobox(*args):
    if top_combobox.get() == "Area":
        left_combobox['values'] = (
            'Square kilometer', 'Square meter', 'Square mile', 'Square yard', 'Square foot', 'Square inch', 'Hectare',
            'Acre')
        right_combobox['values'] = (
            'Square kilometer', 'Square meter', 'Square mile', 'Square yard', 'Square foot', 'Square inch', 'Hectare',
            'Acre')

    elif top_combobox.get() == "Energy":
        left_combobox['values'] = ('Joule', 'Kilojoule', 'Watt hour', 'kilowatt hour')
        right_combobox['values'] = ('Joule', 'Kilojoule', 'Watt hour', 'kilowatt hour')

    elif top_combobox.get() == "Frequency":
        left_combobox['values'] = ('Hertz', 'Kilohertz', 'Megahertz', 'Gigahertz')
        right_combobox['values'] = ('Hertz', 'Kilohertz', 'Megahertz', 'Gigahertz')

    elif top_combobox.get() == "Length":
        left_combobox['values'] = (
            'kilometer', 'Meter', 'Centimeter', 'Millimeter', 'Mile', 'Yard', 'Foot', 'Inch', 'Nautical mile')
        right_combobox['values'] = (
            'kilometer', 'Meter', 'Centimeter', 'Millimeter', 'Mile', 'Yard', 'Foot', 'Inch', 'Nautical mile')

    elif top_combobox.get() == "Mass":
        left_combobox['values'] = ('tonne', 'kilogram', 'gram', 'milligram', 'Microgram')
        right_combobox['values'] = ('tonne', 'kilogram', 'gram', 'milligram', 'Microgram')

    elif top_combobox.get() == "Pressure":
        left_combobox['values'] = ('Bar', 'Pascal', 'pound per square inch', 'Standard atmosphere', 'Torr')
        right_combobox['values'] = ('Bar', 'Pascal', 'pound per square inch', 'Standard atmosphere', 'Torr')

    elif top_combobox.get() == "Temperature":
        left_combobox['values'] = ('Celsius', 'Fehrenheit', 'Kelvin')
        right_combobox['values'] = ('Celsius', 'Fehrenheit', 'Kelvin')

    elif top_combobox.get() == "Time":
        left_combobox['values'] = (
            'Nanosecond', 'Microsecond', 'Millisecond', 'Second', 'Minute', 'Hour', 'Day', 'Week', 'Month', 'Year',
            'Decade', 'Century')
        right_combobox['values'] = (
            'Nanosecond', 'Microsecond', 'Millisecond', 'Second', 'Minute', 'Hour', 'Day', 'Week', 'Month', 'Year',
            'Decade', 'Century')

    elif top_combobox.get() == "Volume":
        left_combobox['values'] = ('Liter', 'Milliliter', 'Cubic Meter', 'Imperial tablespoon', 'Imperial teaspoon')
        right_combobox['values'] = ('Liter', 'Milliliter', 'Cubic Meter', 'Imperial tablespoon', 'Imperial teaspoon')

    left_combobox.current(0)
    right_combobox.current(0)
    unit_converter_right_entry.delete(0, END)
    unit_converter_left_entry.delete(0, END)


### Unit convertor submit button ###
def unit_converter_submit():
    unit_converter_right_entry.config(state=NORMAL)
    unit_converter_right_entry.delete(0, END)

    # Area

    # Square kilometer

    # Square kilometer to square kilometer
    if left_combobox.get() == 'Square kilometer' and right_combobox.get() == 'Square kilometer':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()))

    # square kilometer to square meter
    if left_combobox.get() == 'Square kilometer' and right_combobox.get() == 'Square meter':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 1000000)

    # square kilometer to square mile
    if left_combobox.get() == 'Square kilometer' and right_combobox.get() == 'Square mile':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 2.59)

    # square kilometer to Square yard
    if left_combobox.get() == 'Square kilometer' and right_combobox.get() == 'Square yard':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 1195990.046301)

    # square kilometer to Square foot
    if left_combobox.get() == 'Square kilometer' and right_combobox.get() == 'Square foot':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 10763910.41671)

    # square kilometer to Square inch
    if left_combobox.get() == 'Square kilometer' and right_combobox.get() == 'Square inch':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 1550003100.0062)

    # square kilometer to Hectare
    if left_combobox.get() == 'Square kilometer' and right_combobox.get() == 'Hectare':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 100)

    # square kilometer to Acre
    if left_combobox.get() == 'Square kilometer' and right_combobox.get() == 'Acre':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 247.11)

    # Square meter

    # Square meter to square kilometer
    if left_combobox.get() == 'Square meter' and right_combobox.get() == 'Square kilometer':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 1000000)

    # Square meter to square meter
    if left_combobox.get() == 'Square meter' and right_combobox.get() == 'Square meter':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()))

    # Square meter to square mile
    if left_combobox.get() == 'Square meter' and right_combobox.get() == 'Square mile':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 0.00000038610)

    # Square meter to Square yard
    if left_combobox.get() == 'Square meter' and right_combobox.get() == 'Square yard':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 1.19599)

    # Square meter to Square foot
    if left_combobox.get() == 'Square meter' and right_combobox.get() == 'Square foot':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 10.76391041671)

    # Square meter to Square inch
    if left_combobox.get() == 'Square meter' and right_combobox.get() == 'Square inch':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 1550.0031)

    # Square meter to Hectare
    if left_combobox.get() == 'Square meter' and right_combobox.get() == 'Hectare':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 10000)

    # Square meter to Acre
    if left_combobox.get() == 'Square meter' and right_combobox.get() == 'Acre':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 4047)

    # Square mile

    # Square mile to square kilometer
    if left_combobox.get() == 'Square mile' and right_combobox.get() == 'Square kilometer':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 0.38610)

    # Square mile to square meter
    if left_combobox.get() == 'Square mile' and right_combobox.get() == 'Square meter':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 0.00000038610)

    # Square mile to square mile
    if left_combobox.get() == 'Square mile' and right_combobox.get() == 'Square mile':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()))

    # Square mile to Square yard
    if left_combobox.get() == 'Square mile' and right_combobox.get() == 'Square yard':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 3097600)

    # Square mile to Square foot
    if left_combobox.get() == 'Square mile' and right_combobox.get() == 'Square foot':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 27878400)

    # Square mile to Square inch
    if left_combobox.get() == 'Square mile' and right_combobox.get() == 'Square inch':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 4014489599.4792)

    # Square mile to Hectare
    if left_combobox.get() == 'Square mile' and right_combobox.get() == 'Hectare':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 258.998811)

    # Square mile to Acre
    if left_combobox.get() == 'Square mile' and right_combobox.get() == 'Acre':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 640)

    # Square mile

    # Square mile to square kilometer
    if left_combobox.get() == 'Square mile' and right_combobox.get() == 'Square kilometer':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 0.38610)

    # Square mile to square meter
    if left_combobox.get() == 'Square mile' and right_combobox.get() == 'Square meter':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 0.00000038610)

    # Square mile to square mile
    if left_combobox.get() == 'Square mile' and right_combobox.get() == 'Square mile':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()))

    # Square mile to Square yard
    if left_combobox.get() == 'Square mile' and right_combobox.get() == 'Square yard':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 3097600)

    # Square mile to Square foot
    if left_combobox.get() == 'Square mile' and right_combobox.get() == 'Square foot':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 27878400)

    # Square mile to Square inch
    if left_combobox.get() == 'Square mile' and right_combobox.get() == 'Square inch':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 4014489599.4792)

    # Square mile to Hectare
    if left_combobox.get() == 'Square mile' and right_combobox.get() == 'Hectare':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 258.998811)

    # Square mile to Acre
    if left_combobox.get() == 'Square mile' and right_combobox.get() == 'Acre':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 640)

    # Square yard

    # Square yard to square kilometer
    if left_combobox.get() == 'Square yard' and right_combobox.get() == 'Square kilometer':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 0.00000083613)

    # Square yard to square meter
    if left_combobox.get() == 'Square yard' and right_combobox.get() == 'Square meter':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 1.1960)

    # Square yard to square mile
    if left_combobox.get() == 'Square yard' and right_combobox.get() == 'Square mile':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 3097600)

    # Square yard to Square yard
    if left_combobox.get() == 'Square yard' and right_combobox.get() == 'Square yard':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()))

    # Square yard to Square foot
    if left_combobox.get() == 'Square yard' and right_combobox.get() == 'Square foot':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 9)

    # Square yard to Square inch
    if left_combobox.get() == 'Square yard' and right_combobox.get() == 'Square inch':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 1296)

    # Square yard to Hectare
    if left_combobox.get() == 'Square yard' and right_combobox.get() == 'Hectare':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 0.000083613)

    # Square yard to Acre
    if left_combobox.get() == 'Square yard' and right_combobox.get() == 'Acre':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 4840)

    # Square foot

    # Square foot to square kilometer
    if left_combobox.get() == 'Square foot' and right_combobox.get() == 'Square kilometer':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 0.000000092903)

    # Square foot to square meter
    if left_combobox.get() == 'Square foot' and right_combobox.get() == 'Square meter':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 0.09290304)

    # Square foot to square mile
    if left_combobox.get() == 'Square foot' and right_combobox.get() == 'Square mile':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 27878400)

    # Square foot to Square yard
    if left_combobox.get() == 'Square foot' and right_combobox.get() == 'Square yard':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 9)

    # Square foot to Square foot
    if left_combobox.get() == 'Square foot' and right_combobox.get() == 'Square foot':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()))

    # Square foot to Square inch
    if left_combobox.get() == 'Square foot' and right_combobox.get() == 'Square inch':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 144)

    # Square foot to Hectare
    if left_combobox.get() == 'Square foot' and right_combobox.get() == 'Hectare':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 107639.10417)

    # Square foot to Acre
    if left_combobox.get() == 'Square foot' and right_combobox.get() == 'Acre':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 43560)

    # Square inch

    # Square inch to square kilometer
    if left_combobox.get() == 'Square inch' and right_combobox.get() == 'Square kilometer':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 0.00000000064516)

    # Square inch to square meter
    if left_combobox.get() == 'Square inch' and right_combobox.get() == 'Square meter':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 0.000645)

    # Square inch to square mile
    if left_combobox.get() == 'Square inch' and right_combobox.get() == 'Square mile':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 0.0000000002491)

    # Square inch to Square yard
    if left_combobox.get() == 'Square inch' and right_combobox.get() == 'Square yard':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 1296)

    # Square inch to Square foot
    if left_combobox.get() == 'Square inch' and right_combobox.get() == 'Square foot':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 144)

    # Square inch to Square inch
    if left_combobox.get() == 'Square inch' and right_combobox.get() == 'Square inch':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()))

    # Square inch to Hectare
    if left_combobox.get() == 'Square inch' and right_combobox.get() == 'Hectare':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 0.000000064516)

    # Square inch to Acre
    if left_combobox.get() == 'Square inch' and right_combobox.get() == 'Acre':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 6272640)

    # Hectare

    # Hectare to square kilometer
    if left_combobox.get() == 'Hectare' and right_combobox.get() == 'Square kilometer':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 100)

    # Hectare to square meter
    if left_combobox.get() == 'Hectare' and right_combobox.get() == 'Square meter':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 10000)

    # Hectare to square mile
    if left_combobox.get() == 'Hectare' and right_combobox.get() == 'Square mile':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 0.0038610)

    # Hectare to Square yard
    if left_combobox.get() == 'Hectare' and right_combobox.get() == 'Square yard':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 11959.8993)

    # Hectare to Square foot
    if left_combobox.get() == 'Hectare' and right_combobox.get() == 'Square foot':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 107640)

    # Hectare to Square inch
    if left_combobox.get() == 'Hectare' and right_combobox.get() == 'Square inch':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 15500031)

    # Hectare to Hectare
    if left_combobox.get() == 'Hectare' and right_combobox.get() == 'Hectare':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()))

    # Hectare to Acre
    if left_combobox.get() == 'Hectare' and right_combobox.get() == 'Acre':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 2.4711)

    # Acre

    # Acre to square kilometer
    if left_combobox.get() == 'Acre' and right_combobox.get() == 'Square kilometer':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 247.11)

    # Acre to square meter
    if left_combobox.get() == 'Acre' and right_combobox.get() == 'Square meter':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 0.00024711)

    # Acre to square mile
    if left_combobox.get() == 'Acre' and right_combobox.get() == 'Square mile':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 0.00156)

    # Acre to Square yard
    if left_combobox.get() == 'Acre' and right_combobox.get() == 'Square yard':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 4840)

    # Acre to Square foot
    if left_combobox.get() == 'Acre' and right_combobox.get() == 'Square foot':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 43560)

    # Acre to Square inch
    if left_combobox.get() == 'Acre' and right_combobox.get() == 'Square inch':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 6272640)

    # Acre to Hectare
    if left_combobox.get() == 'Acre' and right_combobox.get() == 'Hectare':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 2.4711)

    # Acre to Acre
    if left_combobox.get() == 'Acre' and right_combobox.get() == 'Acre':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()))

    # ENERGY

    # Joule

    # Joule to Joule
    if left_combobox.get() == 'Joule' and right_combobox.get() == 'Joule':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()))

    # Joule to Kilojoule
    if left_combobox.get() == 'Joule' and right_combobox.get() == 'Kilojoule':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 1000)

    # Joule to Watt hour
    if left_combobox.get() == 'Joule' and right_combobox.get() == 'Watt hour':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 3600)

    # Joule to kilowatt hour
    if left_combobox.get() == 'Joule' and right_combobox.get() == 'kilowatt hour':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 3600000)

    # Kilojoule

    # Kilojoule to Joule
    if left_combobox.get() == 'Kilojoule' and right_combobox.get() == 'Joule':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 1000)

    # Kilojoule to Kilojoule
    if left_combobox.get() == 'Kilojoule' and right_combobox.get() == 'Kilojoule':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()))

    # Kilojoule to Watt hour
    if left_combobox.get() == 'Kilojoule' and right_combobox.get() == 'Watt hour':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 3.6)

    # Kilojoule to kilowatt hour
    if left_combobox.get() == 'Kilojoule' and right_combobox.get() == 'kilowatt hour':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 3600)

    # Watt hour

    # Watt hour to Joule
    if left_combobox.get() == 'Watt hour' and right_combobox.get() == 'Joule':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 3600)

    # Watt hour to Kilojoule
    if left_combobox.get() == 'Watt hour' and right_combobox.get() == 'Kilojoule':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 3.6)

    # Watt hour to Watt hour
    if left_combobox.get() == 'Watt hour' and right_combobox.get() == 'Watt hour':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()))

    # Watt hour to kilowatt hour
    if left_combobox.get() == 'Watt hour' and right_combobox.get() == 'kilowatt hour':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 1000)

    # kilowatt hour

    # kilowatt hour to Joule
    if left_combobox.get() == 'kilowatt hour' and right_combobox.get() == 'Joule':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 3600000)

    # kilowatt hour to Kilojoule
    if left_combobox.get() == 'kilowatt hour' and right_combobox.get() == 'Kilojoule':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 3600)

    # kilowatt hour to Watt hour
    if left_combobox.get() == 'kilowatt hour' and right_combobox.get() == 'Watt hour':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 1000)

    # kilowatt hour to kilowatt hour
    if left_combobox.get() == 'kilowatt hour' and right_combobox.get() == 'kilowatt hour':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()))

    # FREQUENCY

    # Hertz

    # Hertz to Hertz
    if left_combobox.get() == 'Hertz' and right_combobox.get() == 'Hertz':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()))

    # Hertz to Kilohertz
    if left_combobox.get() == 'Hertz' and right_combobox.get() == 'Kilohertz':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 1000)

    # Hertz to Megahertz
    if left_combobox.get() == 'Hertz' and right_combobox.get() == 'Megahertz':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 1000000)

    # Hertz to Gigahertz
    if left_combobox.get() == 'Hertz' and right_combobox.get() == 'Gigahertz':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 1000000000)

    # Kilohertz

    # Kilohertz to Hertz
    if left_combobox.get() == 'Kilohertz' and right_combobox.get() == 'Hertz':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 1000)

    # Kilohertz to Kilohertz
    if left_combobox.get() == 'Kilohertz' and right_combobox.get() == 'Kilohertz':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()))

    # Kilohertz to Megahertz
    if left_combobox.get() == 'Kilohertz' and right_combobox.get() == 'Megahertz':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 1000)

    # Kilohertz to Gigahertz
    if left_combobox.get() == 'Kilohertz' and right_combobox.get() == 'Gigahertz':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 1000000)

    # Megahertz

    # Megahertz to Hertz
    if left_combobox.get() == 'Megahertz' and right_combobox.get() == 'Hertz':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 1000000)

    # Megahertz to Kilohertz
    if left_combobox.get() == 'Megahertz' and right_combobox.get() == 'Kilohertz':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 1000)

    # Megahertz to Megahertz
    if left_combobox.get() == 'Megahertz' and right_combobox.get() == 'Megahertz':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()))

    # Megahertz to Gigahertz
    if left_combobox.get() == 'Megahertz' and right_combobox.get() == 'Gigahertz':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 1000)

    # Gigahertz

    # Gigahertz to Hertz
    if left_combobox.get() == 'Gigahertz' and right_combobox.get() == 'Hertz':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 1000000000)

    # Gigahertz to Kilohertz
    if left_combobox.get() == 'Gigahertz' and right_combobox.get() == 'Kilohertz':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 1000000)

    # Gigahertz to Megahertz
    if left_combobox.get() == 'Gigahertz' and right_combobox.get() == 'Megahertz':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 1000)

    # Gigahertz to Gigahertz
    if left_combobox.get() == 'Gigahertz' and right_combobox.get() == 'Gigahertz':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()))

    # LENGTH

    # kilometer

    # kilometer to kilometer
    if left_combobox.get() == 'kilometer' and right_combobox.get() == 'kilometer':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()))

    # kilometer to Meter
    if left_combobox.get() == 'kilometer' and right_combobox.get() == 'Meter':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 1000)

    # kilometer to Centimeter
    if left_combobox.get() == 'kilometer' and right_combobox.get() == 'Centimeter':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 100000)

    # kilometer to Millimeter
    if left_combobox.get() == 'kilometer' and right_combobox.get() == 'Millimeter':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 1000000)

    # kilometer to Mile
    if left_combobox.get() == 'kilometer' and right_combobox.get() == 'Mile':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 0.6214)

    # kilometer to Yard
    if left_combobox.get() == 'kilometer' and right_combobox.get() == 'Yard':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 1093.6)

    # kilometer to Foot
    if left_combobox.get() == 'kilometer' and right_combobox.get() == 'Foot':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 3280.8)

    # kilometer to Inch
    if left_combobox.get() == 'kilometer' and right_combobox.get() == 'Inch':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 39370.07874)

    # kilometer to Nautical mile
    if left_combobox.get() == 'kilometer' and right_combobox.get() == 'Nautical mile':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 0.53996)

    # Meter

    # Meter to kilometer
    if left_combobox.get() == 'Meter' and right_combobox.get() == 'kilometer':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 1000)

    # Meter to Meter
    if left_combobox.get() == 'Meter' and right_combobox.get() == 'Meter':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()))

    # Meter to Centimeter
    if left_combobox.get() == 'Meter' and right_combobox.get() == 'Centimeter':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 100)

    # Meter to Millimeter
    if left_combobox.get() == 'Meter' and right_combobox.get() == 'Millimeter':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 1000)

    # Meter to Mile
    if left_combobox.get() == 'Meter' and right_combobox.get() == 'Mile':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 0.000621)

    # Meter to Yard
    if left_combobox.get() == 'Meter' and right_combobox.get() == 'Yard':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 1.093613)

    # Meter to Foot
    if left_combobox.get() == 'Meter' and right_combobox.get() == 'Foot':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 3.2808)

    # Meter to Inch
    if left_combobox.get() == 'Meter' and right_combobox.get() == 'Inch':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 39.36)

    # Meter to Nautical mile
    if left_combobox.get() == 'Meter' and right_combobox.get() == 'Nautical mile':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 1852)

    # Centimeter

    # Centimeter to kilometer
    if left_combobox.get() == 'Centimeter' and right_combobox.get() == 'kilometer':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 100000)

    # Centimeter to Meter
    if left_combobox.get() == 'Centimeter' and right_combobox.get() == 'Meter':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 100)

    # Centimeter to Centimeter
    if left_combobox.get() == 'Centimeter' and right_combobox.get() == 'Centimeter':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()))

    # Centimeter to Millimeter
    if left_combobox.get() == 'Centimeter' and right_combobox.get() == 'Millimeter':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 10)

    # Centimeter to Mile
    if left_combobox.get() == 'Centimeter' and right_combobox.get() == 'Mile':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 160934.4)

    # Centimeter to Yard
    if left_combobox.get() == 'Centimeter' and right_combobox.get() == 'Yard':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 0.010936)

    # Centimeter to Foot
    if left_combobox.get() == 'Centimeter' and right_combobox.get() == 'Foot':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 0.0328084)

    # Centimeter to Inch
    if left_combobox.get() == 'Centimeter' and right_combobox.get() == 'Inch':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 0.39370)

    # Centimeter to Nautical mile
    if left_combobox.get() == 'Centimeter' and right_combobox.get() == 'Nautical mile':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 0.0000054)

    # Millimeter

    # Millimeter to kilometer
    if left_combobox.get() == 'Millimeter' and right_combobox.get() == 'kilometer':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 1000000)

    # Millimeter to Meter
    if left_combobox.get() == 'Millimeter' and right_combobox.get() == 'Meter':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 1000)

    # Millimeter to Centimeter
    if left_combobox.get() == 'Millimeter' and right_combobox.get() == 'Centimeter':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 10)

    # Millimeter to Millimeter
    if left_combobox.get() == 'Millimeter' and right_combobox.get() == 'Millimeter':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()))

    # Millimeter to Mile
    if left_combobox.get() == 'Millimeter' and right_combobox.get() == 'Mile':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 1609344)

    # Millimeter to Yard
    if left_combobox.get() == 'Millimeter' and right_combobox.get() == 'Yard':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 0.001094)

    # Millimeter to Foot
    if left_combobox.get() == 'Millimeter' and right_combobox.get() == 'Foot':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 0.00328084)

    # Millimeter to Inch
    if left_combobox.get() == 'Millimeter' and right_combobox.get() == 'Inch':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 0.03937)

    # Millimeter to Nautical mile
    if left_combobox.get() == 'Millimeter' and right_combobox.get() == 'Nautical mile':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 0.00000054)

    # Mile

    # Mile to kilometer
    if left_combobox.get() == 'Mile' and right_combobox.get() == 'kilometer':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 0.6214)

    # Mile to Meter
    if left_combobox.get() == 'Mile' and right_combobox.get() == 'Meter':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 1609.344)

    # Mile to Centimeter
    if left_combobox.get() == 'Mile' and right_combobox.get() == 'Centimeter':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 160934.4)

    # Mile to Millimeter
    if left_combobox.get() == 'Mile' and right_combobox.get() == 'Millimeter':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 1609344)

    # Mile to Mile
    if left_combobox.get() == 'Mile' and right_combobox.get() == 'Mile':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()))

    # Mile to Yard
    if left_combobox.get() == 'Mile' and right_combobox.get() == 'Yard':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 1760)

    # Mile to Foot
    if left_combobox.get() == 'Mile' and right_combobox.get() == 'Foot':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 5280)

    # Mile to Inch
    if left_combobox.get() == 'Mile' and right_combobox.get() == 'Inch':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 63360)

    # Mile to Nautical mile
    if left_combobox.get() == 'Mile' and right_combobox.get() == 'Nautical mile':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 0.86897583)

    # Yard

    # Yard to kilometer
    if left_combobox.get() == 'Yard' and right_combobox.get() == 'kilometer':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 0.000914)

    # Yard to Meter
    if left_combobox.get() == 'Yard' and right_combobox.get() == 'Meter':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 1.0936)

    # Yard to Centimeter
    if left_combobox.get() == 'Yard' and right_combobox.get() == 'Centimeter':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 0.010936)

    # Yard to Millimeter
    if left_combobox.get() == 'Yard' and right_combobox.get() == 'Millimeter':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 914.4)

    # Yard to Mile
    if left_combobox.get() == 'Yard' and right_combobox.get() == 'Mile':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 1760)

    # Yard to Yard
    if left_combobox.get() == 'Yard' and right_combobox.get() == 'Yard':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()))

    # Yard to Foot
    if left_combobox.get() == 'Yard' and right_combobox.get() == 'Foot':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 3)

    # Yard to Inch
    if left_combobox.get() == 'Yard' and right_combobox.get() == 'Inch':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 36)

    # Yard to Nautical mile
    if left_combobox.get() == 'Yard' and right_combobox.get() == 'Nautical mile':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 2025.37183)

    # Foot

    # Foot to kilometer
    if left_combobox.get() == 'Foot' and right_combobox.get() == 'kilometer':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 0.000305)

    # Foot to Meter
    if left_combobox.get() == 'Foot' and right_combobox.get() == 'Meter':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 3.2808)

    # Foot to Centimeter
    if left_combobox.get() == 'Foot' and right_combobox.get() == 'Centimeter':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 0.032808)

    # Foot to Millimeter
    if left_combobox.get() == 'Foot' and right_combobox.get() == 'Millimeter':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 304.8)

    # Foot to Mile
    if left_combobox.get() == 'Foot' and right_combobox.get() == 'Mile':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 5280)

    # Foot to Yard
    if left_combobox.get() == 'Foot' and right_combobox.get() == 'Yard':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 3)

    # Foot to Foot
    if left_combobox.get() == 'Foot' and right_combobox.get() == 'Foot':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()))

    # Foot to Inch
    if left_combobox.get() == 'Foot' and right_combobox.get() == 'Inch':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 12)

    # Foot to Nautical mile
    if left_combobox.get() == 'Foot' and right_combobox.get() == 'Nautical mile':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 6076.11549)

    # Inch

    # Inch to kilometer
    if left_combobox.get() == 'Inch' and right_combobox.get() == 'kilometer':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 39370)

    # Inch to Meter
    if left_combobox.get() == 'Inch' and right_combobox.get() == 'Meter':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 0.0254)

    # Inch to Centimeter
    if left_combobox.get() == 'Inch' and right_combobox.get() == 'Centimeter':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 0.39370)

    # Inch to Millimeter
    if left_combobox.get() == 'Inch' and right_combobox.get() == 'Millimeter':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 25.4)

    # Inch to Mile
    if left_combobox.get() == 'Inch' and right_combobox.get() == 'Mile':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 63360)

    # Inch to Yard
    if left_combobox.get() == 'Inch' and right_combobox.get() == 'Yard':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 36)

    # Inch to Foot
    if left_combobox.get() == 'Inch' and right_combobox.get() == 'Foot':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 12)

    # Inch to Inch
    if left_combobox.get() == 'Inch' and right_combobox.get() == 'Inch':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()))

    # Inch to Nautical mile
    if left_combobox.get() == 'Inch' and right_combobox.get() == 'Nautical mile':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 0.00001371)

    # Nautical mile

    # Nautical mile to kilometer
    if left_combobox.get() == 'Nautical mile' and right_combobox.get() == 'kilometer':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 1.852)

    # Nautical mile to Meter
    if left_combobox.get() == 'Nautical mile' and right_combobox.get() == 'Meter':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 0.00053996)

    # Nautical mile to Centimeter
    if left_combobox.get() == 'Nautical mile' and right_combobox.get() == 'Centimeter':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 0.0000054)

    # Nautical mile to Millimeter
    if left_combobox.get() == 'Nautical mile' and right_combobox.get() == 'Millimeter':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 0.00000054)

    # Nautical mile to Mile
    if left_combobox.get() == 'Nautical mile' and right_combobox.get() == 'Mile':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 0.86897583)

    # Nautical mile to Yard
    if left_combobox.get() == 'Nautical mile' and right_combobox.get() == 'Yard':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 0.00049374)

    # Nautical mile to Foot
    if left_combobox.get() == 'Nautical mile' and right_combobox.get() == 'Foot':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 0.00016458)

    # Nautical mile to Inch
    if left_combobox.get() == 'Nautical mile' and right_combobox.get() == 'Inch':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 72913)

    # Nautical mile to Nautical mile
    if left_combobox.get() == 'Nautical mile' and right_combobox.get() == 'Nautical mile':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()))

    # MASS

    # tonne

    # tonne to tonne
    if left_combobox.get() == 'tonne' and right_combobox.get() == 'tonne':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()))

    # tonne to kilogram
    if left_combobox.get() == 'tonne' and right_combobox.get() == 'kilogram':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 1000)

    # tonne to gram
    if left_combobox.get() == 'tonne' and right_combobox.get() == 'gram':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 1000000)

    # tonne to milligram
    if left_combobox.get() == 'tonne' and right_combobox.get() == 'milligram':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 1000000000)

    # tonne to Microgram
    if left_combobox.get() == 'tonne' and right_combobox.get() == 'Microgram':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 0.0000000000010000)

    # kilogram

    # kilogram to tonne
    if left_combobox.get() == 'kilogram' and right_combobox.get() == 'tonne':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 1000)

    # kilogram to kilogram
    if left_combobox.get() == 'kilogram' and right_combobox.get() == 'kilogram':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()))

    # kilogram to gram
    if left_combobox.get() == 'kilogram' and right_combobox.get() == 'gram':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 1000)

    # kilogram to milligram
    if left_combobox.get() == 'kilogram' and right_combobox.get() == 'milligram':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 1000000)

    # kilogram to Microgram
    if left_combobox.get() == 'kilogram' and right_combobox.get() == 'Microgram':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 0.0000000010000)

    # gram

    # gram to tonne
    if left_combobox.get() == 'gram' and right_combobox.get() == 'tonne':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 1000000)

    # gram to kilogram
    if left_combobox.get() == 'gram' and right_combobox.get() == 'kilogram':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 1000)

    # gram to gram
    if left_combobox.get() == 'gram' and right_combobox.get() == 'gram':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()))

    # gram to milligram
    if left_combobox.get() == 'gram' and right_combobox.get() == 'milligram':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 1000)

    # gram to Microgram
    if left_combobox.get() == 'gram' and right_combobox.get() == 'Microgram':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 1000000)

    # milligram

    # milligram to tonne
    if left_combobox.get() == 'milligram' and right_combobox.get() == 'tonne':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 1000000000)

    # milligram to kilogram
    if left_combobox.get() == 'milligram' and right_combobox.get() == 'kilogram':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 1000000)

    # milligram to gram
    if left_combobox.get() == 'milligram' and right_combobox.get() == 'gram':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 1000)

    # milligram to milligram
    if left_combobox.get() == 'milligram' and right_combobox.get() == 'milligram':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()))

    # milligram to Microgram
    if left_combobox.get() == 'milligram' and right_combobox.get() == 'Microgram':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 1000)

    # Microgram

    # Microgram to tonne
    if left_combobox.get() == 'Microgram' and right_combobox.get() == 'tonne':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 1000000000000)

    # Microgram to kilogram
    if left_combobox.get() == 'Microgram' and right_combobox.get() == 'kilogram':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 1000000000)

    # Microgram to gram
    if left_combobox.get() == 'Microgram' and right_combobox.get() == 'gram':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 1000000)

    # Microgram to milligram
    if left_combobox.get() == 'Microgram' and right_combobox.get() == 'milligram':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 1000)

    # Microgram to Microgram
    if left_combobox.get() == 'Microgram' and right_combobox.get() == 'Microgram':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()))

    # PRESSURE

    # Bar

    # Bar to Bar
    if left_combobox.get() == 'Bar' and right_combobox.get() == 'Bar':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()))

    # Bar to Pascal
    if left_combobox.get() == 'Bar' and right_combobox.get() == 'Pascal':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 100000)

    # Bar to pound per square inch
    if left_combobox.get() == 'Bar' and right_combobox.get() == 'pound per square inch':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 14.503789)

    # Bar to Standard atmosphere
    if left_combobox.get() == 'Bar' and right_combobox.get() == 'Standard atmosphere':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 0.98692326671601)

    # Bar to Torr
    if left_combobox.get() == 'Bar' and right_combobox.get() == 'Torr':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 750.061683)

    # Pascal

    # Pascal to Bar
    if left_combobox.get() == 'Pascal' and right_combobox.get() == 'Bar':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 100000)

    # Pascal to Pascal
    if left_combobox.get() == 'Pascal' and right_combobox.get() == 'Pascal':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()))

    # Pascal to pound per square inch
    if left_combobox.get() == 'Pascal' and right_combobox.get() == 'pound per square inch':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 0.000145)

    # Pascal to Standard atmosphere
    if left_combobox.get() == 'Pascal' and right_combobox.get() == 'Standard atmosphere':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 101325)

    # Pascal to Torr
    if left_combobox.get() == 'Pascal' and right_combobox.get() == 'Torr':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 0.007501)

    # pound per square inch

    # pound per square inch to Bar
    if left_combobox.get() == 'pound per square inch' and right_combobox.get() == 'Bar':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 14.504)

    # pound per square inch to Pascal
    if left_combobox.get() == 'pound per square inch' and right_combobox.get() == 'Pascal':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 6894.75)

    # pound per square inch to pound per square inch
    if left_combobox.get() == 'pound per square inch' and right_combobox.get() == 'pound per square inch':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()))

    # pound per square inch to Standard atmosphere
    if left_combobox.get() == 'pound per square inch' and right_combobox.get() == 'Standard atmosphere':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 0.068046)

    # pound per square inch to Torr
    if left_combobox.get() == 'pound per square inch' and right_combobox.get() == 'Torr':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 51.714878)

    # Standard atmosphere

    # Standard atmosphere to Bar
    if left_combobox.get() == 'Standard atmosphere' and right_combobox.get() == 'Bar':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 1.01325)

    # Standard atmosphere to Pascal
    if left_combobox.get() == 'Standard atmosphere' and right_combobox.get() == 'Pascal':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 101325)

    # Standard atmosphere to pound per square inch
    if left_combobox.get() == 'Standard atmosphere' and right_combobox.get() == 'pound per square inch':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 14.6959)

    # Standard atmosphere to Standard atmosphere
    if left_combobox.get() == 'Standard atmosphere' and right_combobox.get() == 'Standard atmosphere':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()))

    # Standard atmosphere to Torr
    if left_combobox.get() == 'Standard atmosphere' and right_combobox.get() == 'Torr':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 760)

    # Torr

    # Torr to Bar
    if left_combobox.get() == 'Torr' and right_combobox.get() == 'Bar':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 0.001333)

    # Torr to Pascal
    if left_combobox.get() == 'Torr' and right_combobox.get() == 'Pascal':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 133.322368)

    # Torr to pound per square inch
    if left_combobox.get() == 'Torr' and right_combobox.get() == 'pound per square inch':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 51.715)

    # Torr to Standard atmosphere
    if left_combobox.get() == 'Torr' and right_combobox.get() == 'Standard atmosphere':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 760)

    # Torr to Torr
    if left_combobox.get() == 'Torr' and right_combobox.get() == 'Torr':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()))

    # Temperature 'Kelvin')

    # Celsius

    # Celsius to Celsius
    if left_combobox.get() == 'Celsius' and right_combobox.get() == 'Celsius':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()))

    # Celsius to Fehrenheit
    if left_combobox.get() == 'Celsius' and right_combobox.get() == 'Fehrenheit':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 1.8 + 32)

    # Celsius to Kelvin
    if left_combobox.get() == 'Celsius' and right_combobox.get() == 'Kelvin':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) + 273.15)

    # Fehrenheit

    # Fehrenheit to Celsius
    if left_combobox.get() == 'Fehrenheit' and right_combobox.get() == 'Celsius':
        unit_converter_right_entry.insert(0, float((unit_converter_left_entry.get() + 32) * 1.8))

    # Fehrenheit to Fehrenheit
    if left_combobox.get() == 'Fehrenheit' and right_combobox.get() == 'Fehrenheit':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()))

    # Fehrenheit to Kelvin
    if left_combobox.get() == 'Fehrenheit' and right_combobox.get() == 'Kelvin':
        unit_converter_right_entry.insert(0, float(((unit_converter_left_entry.get() + 32) * 1.8)) + 273.15)

    # Kelvin

    # Kelvin to Celsius
    if left_combobox.get() == 'Kelvin' and right_combobox.get() == 'Celsius':
        unit_converter_right_entry.insert(0, float((unit_converter_left_entry.get() - 273.15)))

    # Kelvin to Fehrenheit
    if left_combobox.get() == 'Kelvin' and right_combobox.get() == 'Fehrenheit':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()))

    # Kelvin to Kelvin
    if left_combobox.get() == 'Kelvin' and right_combobox.get() == 'Kelvin':
        unit_converter_right_entry.insert(0, float(((unit_converter_left_entry.get() - 273.15) * 1.8)) + 32)

    # TIME

    # Nanosecond

    # Nanosecond to Nanosecond
    if left_combobox.get() == 'Nanosecond' and right_combobox.get() == 'Nanosecond':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()))

    # Nanosecond to Microsecond
    if left_combobox.get() == 'Nanosecond' and right_combobox.get() == 'Microsecond':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 1000)

    # Nanosecond to Millisecond
    if left_combobox.get() == 'Nanosecond' and right_combobox.get() == 'Millisecond':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 1000000)

    # Nanosecond to Second
    if left_combobox.get() == 'Nanosecond' and right_combobox.get() == 'Second':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 1000000000)

    # Nanosecond to Minute
    if left_combobox.get() == 'Nanosecond' and right_combobox.get() == 'Minute':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 60000000000)

    # Nanosecond to Hour
    if left_combobox.get() == 'Nanosecond' and right_combobox.get() == 'Hour':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 3600000000000)

    # Nanosecond to Day
    if left_combobox.get() == 'Nanosecond' and right_combobox.get() == 'Day':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 86400000000000)

    # Nanosecond to Week
    if left_combobox.get() == 'Nanosecond' and right_combobox.get() == 'Week':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 0.0000000000000016534)

    # Nanosecond to Month
    if left_combobox.get() == 'Nanosecond' and right_combobox.get() == 'Month':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 0.00000000000000038026)

    # Nanosecond to Year
    if left_combobox.get() == 'Nanosecond' and right_combobox.get() == 'Year':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 0.000000000000000031689)

    # Nanosecond to Decade
    if left_combobox.get() == 'Nanosecond' and right_combobox.get() == 'Decade':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 0.0000000000000000031689)

    # Nanosecond to Century
    if left_combobox.get() == 'Nanosecond' and right_combobox.get() == 'Century':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 0.00000000000000000031689)

    # Microsecond

    # Microsecond to Nanosecond
    if left_combobox.get() == 'Microsecond' and right_combobox.get() == 'Nanosecond':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 1000)

    # Microsecond to Microsecond
    if left_combobox.get() == 'Microsecond' and right_combobox.get() == 'Microsecond':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()))

    # Microsecond to Millisecond
    if left_combobox.get() == 'Microsecond' and right_combobox.get() == 'Millisecond':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 1000)

    # Microsecond to Second
    if left_combobox.get() == 'Microsecond' and right_combobox.get() == 'Second':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 1000000)

    # Microsecond to Minute
    if left_combobox.get() == 'Microsecond' and right_combobox.get() == 'Minute':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 60000000)

    # Microsecond to Hour
    if left_combobox.get() == 'Microsecond' and right_combobox.get() == 'Hour':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 3600000000)

    # Microsecond to Day
    if left_combobox.get() == 'Microsecond' and right_combobox.get() == 'Day':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 86400000000)

    # Microsecond to Week
    if left_combobox.get() == 'Microsecond' and right_combobox.get() == 'Week':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 604800000000)

    # Microsecond to Month
    if left_combobox.get() == 'Microsecond' and right_combobox.get() == 'Month':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 2629746000000)

    # Microsecond to Year
    if left_combobox.get() == 'Microsecond' and right_combobox.get() == 'Year':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 31556952000000)

    # Microsecond to Decade
    if left_combobox.get() == 'Microsecond' and right_combobox.get() == 'Decade':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 0.0000000000000031689)

    # Microsecond to Century
    if left_combobox.get() == 'Microsecond' and right_combobox.get() == 'Century':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 0.00000000000000031689)

    # Millisecond

    # Millisecond to Nanosecond
    if left_combobox.get() == 'Millisecond' and right_combobox.get() == 'Nanosecond':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 1000000)

    # Millisecond to Microsecond
    if left_combobox.get() == 'Millisecond' and right_combobox.get() == 'Microsecond':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 1000)

    # Millisecond to Millisecond
    if left_combobox.get() == 'Millisecond' and right_combobox.get() == 'Millisecond':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()))

    # Millisecond to Second
    if left_combobox.get() == 'Millisecond' and right_combobox.get() == 'Second':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 1000)

    # Millisecond to Minute
    if left_combobox.get() == 'Millisecond' and right_combobox.get() == 'Minute':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 60000)

    # Millisecond to Hour
    if left_combobox.get() == 'Millisecond' and right_combobox.get() == 'Hour':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 3600000)

    # Millisecond to Day
    if left_combobox.get() == 'Millisecond' and right_combobox.get() == 'Day':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 86400000)

    # Millisecond to Week
    if left_combobox.get() == 'Millisecond' and right_combobox.get() == 'Week':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 604800000)

    # Millisecond to Month
    if left_combobox.get() == 'Millisecond' and right_combobox.get() == 'Month':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 2629746000)

    # Millisecond to Year
    if left_combobox.get() == 'Millisecond' and right_combobox.get() == 'Year':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 31556952000)

    # Millisecond to Decade
    if left_combobox.get() == 'Millisecond' and right_combobox.get() == 'Decade':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 315569520000)

    # Millisecond to Century
    if left_combobox.get() == 'Millisecond' and right_combobox.get() == 'Century':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 3155695200000)

    # Second

    # Second to Nanosecond
    if left_combobox.get() == 'Second' and right_combobox.get() == 'Nanosecond':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 1000000000)

    # Second to Microsecond
    if left_combobox.get() == 'Second' and right_combobox.get() == 'Microsecond':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 1000000)

    # Second to Millisecond
    if left_combobox.get() == 'Second' and right_combobox.get() == 'Millisecond':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 1000)

    # Second to Second
    if left_combobox.get() == 'Second' and right_combobox.get() == 'Second':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()))

    # Second to Minute
    if left_combobox.get() == 'Second' and right_combobox.get() == 'Minute':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 60)

    # Second to Hour
    if left_combobox.get() == 'Second' and right_combobox.get() == 'Hour':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 3600)

    # Second to Day
    if left_combobox.get() == 'Second' and right_combobox.get() == 'Day':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 86400)

    # Second to Week
    if left_combobox.get() == 'Second' and right_combobox.get() == 'Week':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 604800)

    # Second to Month
    if left_combobox.get() == 'Second' and right_combobox.get() == 'Month':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 2629746)

    # Second to Year
    if left_combobox.get() == 'Second' and right_combobox.get() == 'Year':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 31556952)

    # Second to Decade
    if left_combobox.get() == 'Second' and right_combobox.get() == 'Decade':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 315569520)

    # Second to Century
    if left_combobox.get() == 'Second' and right_combobox.get() == 'Century':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 3155695200)

    # Minute

    # Minute to Nanosecond
    if left_combobox.get() == 'Minute' and right_combobox.get() == 'Nanosecond':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 60000000000)

    # Minute to Microsecond
    if left_combobox.get() == 'Minute' and right_combobox.get() == 'Microsecond':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 60000000)

    # Minute to Millisecond
    if left_combobox.get() == 'Minute' and right_combobox.get() == 'Millisecond':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 60000)

    # Minute to Second
    if left_combobox.get() == 'Minute' and right_combobox.get() == 'Second':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 60)

    # Minute to Minute
    if left_combobox.get() == 'Minute' and right_combobox.get() == 'Minute':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()))

    # Minute to Hour
    if left_combobox.get() == 'Minute' and right_combobox.get() == 'Hour':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 60)

    # Minute to Day
    if left_combobox.get() == 'Minute' and right_combobox.get() == 'Day':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 1440)

    # Minute to Week
    if left_combobox.get() == 'Minute' and right_combobox.get() == 'Week':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 10080)

    # Minute to Month
    if left_combobox.get() == 'Minute' and right_combobox.get() == 'Month':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 43830)

    # Minute to Year
    if left_combobox.get() == 'Minute' and right_combobox.get() == 'Year':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 525600)

    # Minute to Decade
    if left_combobox.get() == 'Minute' and right_combobox.get() == 'Decade':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 5259492)

    # Minute to Century
    if left_combobox.get() == 'Minute' and right_combobox.get() == 'Century':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 52594920)

    # Hour

    # Hour to Nanosecond
    if left_combobox.get() == 'Hour' and right_combobox.get() == 'Nanosecond':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 3600000000000)

    # Hour to Microsecond
    if left_combobox.get() == 'Hour' and right_combobox.get() == 'Microsecond':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 3600000000)

    # Hour to Millisecond
    if left_combobox.get() == 'Hour' and right_combobox.get() == 'Millisecond':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 3600000)

    # Hour to Second
    if left_combobox.get() == 'Hour' and right_combobox.get() == 'Second':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 3600)

    # Hour to Minute
    if left_combobox.get() == 'Hour' and right_combobox.get() == 'Minute':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 60)

    # Hour to Hour
    if left_combobox.get() == 'Hour' and right_combobox.get() == 'Hour':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()))

    # Hour to Day
    if left_combobox.get() == 'Hour' and right_combobox.get() == 'Day':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 24)

    # Hour to Week
    if left_combobox.get() == 'Hour' and right_combobox.get() == 'Week':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 168)

    # Hour to Month
    if left_combobox.get() == 'Hour' and right_combobox.get() == 'Month':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 730.5)

    # Hour to Year
    if left_combobox.get() == 'Hour' and right_combobox.get() == 'Year':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 8760)

    # Hour to Decade
    if left_combobox.get() == 'Hour' and right_combobox.get() == 'Decade':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 87600)

    # Hour to Century
    if left_combobox.get() == 'Hour' and right_combobox.get() == 'Century':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 876582)

    # Day

    # Day to Nanosecond
    if left_combobox.get() == 'Day' and right_combobox.get() == 'Nanosecond':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 86400000000000)

    # Day to Microsecond
    if left_combobox.get() == 'Day' and right_combobox.get() == 'Microsecond':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 86400000000)

    # Day to Millisecond
    if left_combobox.get() == 'Day' and right_combobox.get() == 'Millisecond':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 86400000)

    # Day to Second
    if left_combobox.get() == 'Day' and right_combobox.get() == 'Second':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 86400)

    # Day to Minute
    if left_combobox.get() == 'Day' and right_combobox.get() == 'Minute':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 1440)

    # Day to Hour
    if left_combobox.get() == 'Day' and right_combobox.get() == 'Hour':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 24)

    # Day to Day
    if left_combobox.get() == 'Day' and right_combobox.get() == 'Day':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()))

    # Day to Week
    if left_combobox.get() == 'Day' and right_combobox.get() == 'Week':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 7)

    # Day to Month
    if left_combobox.get() == 'Day' and right_combobox.get() == 'Month':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 30.5)

    # Day to Year
    if left_combobox.get() == 'Day' and right_combobox.get() == 'Year':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 365)

    # Day to Decade
    if left_combobox.get() == 'Day' and right_combobox.get() == 'Decade':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 3650)

    # Day to Century
    if left_combobox.get() == 'Day' and right_combobox.get() == 'Century':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 36500)

    # Week

    # Week to Nanosecond
    if left_combobox.get() == 'Week' and right_combobox.get() == 'Nanosecond':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 604800000000000)

    # Week to Microsecond
    if left_combobox.get() == 'Week' and right_combobox.get() == 'Microsecond':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 604800000000)

    # Week to Millisecond
    if left_combobox.get() == 'Week' and right_combobox.get() == 'Millisecond':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 604800000)

    # Week to Second
    if left_combobox.get() == 'Week' and right_combobox.get() == 'Second':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 604800)

    # Week to Minute
    if left_combobox.get() == 'Week' and right_combobox.get() == 'Minute':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 10080)

    # Week to Hour
    if left_combobox.get() == 'Week' and right_combobox.get() == 'Hour':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 168)

    # Week to Day
    if left_combobox.get() == 'Week' and right_combobox.get() == 'Day':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 7)

    # Week to Week
    if left_combobox.get() == 'Week' and right_combobox.get() == 'Week':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()))

    # Week to Month
    if left_combobox.get() == 'Week' and right_combobox.get() == 'Month':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 4.345)

    # Week to Year
    if left_combobox.get() == 'Week' and right_combobox.get() == 'Year':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 52)

    # Week to Decade
    if left_combobox.get() == 'Week' and right_combobox.get() == 'Decade':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 520)

    # Week to Century
    if left_combobox.get() == 'Week' and right_combobox.get() == 'Century':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 5200)

    # Month

    # Month to Nanosecond
    if left_combobox.get() == 'Month' and right_combobox.get() == 'Nanosecond':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 2592000000000000)

    # Month to Microsecond
    if left_combobox.get() == 'Month' and right_combobox.get() == 'Microsecond':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 2592000000000)

    # Month to Millisecond
    if left_combobox.get() == 'Month' and right_combobox.get() == 'Millisecond':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 2592000000)

    # Month to Second
    if left_combobox.get() == 'Month' and right_combobox.get() == 'Second':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 2592000)

    # Month to Minute
    if left_combobox.get() == 'Month' and right_combobox.get() == 'Minute':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 43800)

    # Month to Hour
    if left_combobox.get() == 'Month' and right_combobox.get() == 'Hour':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 730)

    # Month to Day
    if left_combobox.get() == 'Month' and right_combobox.get() == 'Day':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 30.5)

    # Month to Week
    if left_combobox.get() == 'Month' and right_combobox.get() == 'Week':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 4.345)

    # Month to Month
    if left_combobox.get() == 'Month' and right_combobox.get() == 'Month':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()))

    # Month to Year
    if left_combobox.get() == 'Month' and right_combobox.get() == 'Year':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 12)

    # Month to Decade
    if left_combobox.get() == 'Month' and right_combobox.get() == 'Decade':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 120)

    # Month to Century
    if left_combobox.get() == 'Month' and right_combobox.get() == 'Century':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 1200)

    # Year

    # Year to Nanosecond
    if left_combobox.get() == 'Year' and right_combobox.get() == 'Nanosecond':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 31557000000000000)

    # Year to Microsecond
    if left_combobox.get() == 'Year' and right_combobox.get() == 'Microsecond':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 31557000000000)

    # Year to Millisecond
    if left_combobox.get() == 'Year' and right_combobox.get() == 'Millisecond':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 31557000000)

    # Year to Second
    if left_combobox.get() == 'Year' and right_combobox.get() == 'Second':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 31557000)

    # Year to Minute
    if left_combobox.get() == 'Year' and right_combobox.get() == 'Minute':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 525600)

    # Year to Hour
    if left_combobox.get() == 'Year' and right_combobox.get() == 'Hour':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 8760)

    # Year to Day
    if left_combobox.get() == 'Year' and right_combobox.get() == 'Day':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 365)

    # Year to Week
    if left_combobox.get() == 'Year' and right_combobox.get() == 'Week':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 52)

    # Year to Month
    if left_combobox.get() == 'Year' and right_combobox.get() == 'Month':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 12)

    # Year to Year
    if left_combobox.get() == 'Year' and right_combobox.get() == 'Year':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()))

    # Year to Decade
    if left_combobox.get() == 'Year' and right_combobox.get() == 'Decade':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 10)

    # Year to Century
    if left_combobox.get() == 'Year' and right_combobox.get() == 'Century':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 100)

    # Decade

    # Decade to Nanosecond
    if left_combobox.get() == 'Decade' and right_combobox.get() == 'Nanosecond':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 315570000000000000)

    # Decade to Microsecond
    if left_combobox.get() == 'Decade' and right_combobox.get() == 'Microsecond':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 315570000000000)

    # Decade to Millisecond
    if left_combobox.get() == 'Decade' and right_combobox.get() == 'Millisecond':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 315570000000)

    # Decade to Second
    if left_combobox.get() == 'Decade' and right_combobox.get() == 'Second':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 315570000000)

    # Decade to Minute
    if left_combobox.get() == 'Decade' and right_combobox.get() == 'Minute':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 5259492)

    # Decade to Hour
    if left_combobox.get() == 'Decade' and right_combobox.get() == 'Hour':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 87600)

    # Decade to Day
    if left_combobox.get() == 'Decade' and right_combobox.get() == 'Day':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 3650)

    # Decade to Week
    if left_combobox.get() == 'Decade' and right_combobox.get() == 'Week':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 520)

    # Decade to Month
    if left_combobox.get() == 'Decade' and right_combobox.get() == 'Month':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 120)

    # Decade to Year
    if left_combobox.get() == 'Decade' and right_combobox.get() == 'Year':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 10)

    # Decade to Decade
    if left_combobox.get() == 'Decade' and right_combobox.get() == 'Decade':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()))

    # Decade to Century
    if left_combobox.get() == 'Decade' and right_combobox.get() == 'Century':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 10)

    # Century

    # Century to Nanosecond
    if left_combobox.get() == 'Century' and right_combobox.get() == 'Nanosecond':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 3155700000000000000)

    # Century to Microsecond
    if left_combobox.get() == 'Century' and right_combobox.get() == 'Microsecond':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 31557000000000000)

    # Century to Millisecond
    if left_combobox.get() == 'Century' and right_combobox.get() == 'Millisecond':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 31557000000000)

    # Century to Second
    if left_combobox.get() == 'Century' and right_combobox.get() == 'Second':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 31557000000)

    # Century to Minute
    if left_combobox.get() == 'Century' and right_combobox.get() == 'Minute':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 52594920)

    # Century to Hour
    if left_combobox.get() == 'Century' and right_combobox.get() == 'Hour':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 876000)

    # Century to Day
    if left_combobox.get() == 'Century' and right_combobox.get() == 'Day':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 36500)

    # Century to Week
    if left_combobox.get() == 'Century' and right_combobox.get() == 'Week':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 5200)

    # Century to Month
    if left_combobox.get() == 'Century' and right_combobox.get() == 'Month':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 1200)

    # Century to Year
    if left_combobox.get() == 'Century' and right_combobox.get() == 'Year':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 100)

    # Century to Decade
    if left_combobox.get() == 'Century' and right_combobox.get() == 'Decade':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 10)

    # Century to Century
    if left_combobox.get() == 'Century' and right_combobox.get() == 'Century':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()))

    # Volume 'Imperial tablespoon', 'Imperial teaspoon'

    # Liter

    # Liter to Liter
    if left_combobox.get() == 'Liter' and right_combobox.get() == 'Liter':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()))

    # Liter to Milliliter
    if left_combobox.get() == 'Liter' and right_combobox.get() == 'Milliliter':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 1000000)

    # Liter to Cubic Meter
    if left_combobox.get() == 'Liter' and right_combobox.get() == 'Cubic Meter':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 0.001)

    # Liter to Imperial tablespoon
    if left_combobox.get() == 'Liter' and right_combobox.get() == 'Imperial tablespoon':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 56.3121)

    # Liter to Imperial teaspoon
    if left_combobox.get() == 'Liter' and right_combobox.get() == 'Imperial teaspoon':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 168.936)

    # Milliliter

    # Milliliter to Liter
    if left_combobox.get() == 'Milliliter' and right_combobox.get() == 'Liter':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 1000)

    # Milliliter to Milliliter
    if left_combobox.get() == 'Milliliter' and right_combobox.get() == 'Milliliter':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()))

    # Milliliter to Cubic Meter
    if left_combobox.get() == 'Milliliter' and right_combobox.get() == 'Cubic Meter':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 1000000)

    # Milliliter to Imperial tablespoon
    if left_combobox.get() == 'Milliliter' and right_combobox.get() == 'Imperial tablespoon':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 17.758)

    # Milliliter to Imperial teaspoon
    if left_combobox.get() == 'Milliliter' and right_combobox.get() == 'Imperial teaspoon':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 5.919)

    # Cubic Meter

    # Cubic Meter to Liter
    if left_combobox.get() == 'Cubic Meter' and right_combobox.get() == 'Liter':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 1000)

    # Cubic Meter to Milliliter
    if left_combobox.get() == 'Cubic Meter' and right_combobox.get() == 'Milliliter':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 1000000)

    # Cubic Meter to Cubic Meter
    if left_combobox.get() == 'Cubic Meter' and right_combobox.get() == 'Cubic Meter':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()))

    # Cubic Meter to Imperial tablespoon
    if left_combobox.get() == 'Cubic Meter' and right_combobox.get() == 'Imperial tablespoon':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 56312)

    # Cubic Meter to Imperial teaspoon
    if left_combobox.get() == 'Cubic Meter' and right_combobox.get() == 'Imperial teaspoon':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 168936)

    # Imperial tablespoon

    # Imperial tablespoon to Liter
    if left_combobox.get() == 'Imperial tablespoon' and right_combobox.get() == 'Liter':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 56.312)

    # Imperial tablespoon to Milliliter
    if left_combobox.get() == 'Imperial tablespoon' and right_combobox.get() == 'Milliliter':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 17.758)

    # Imperial tablespoon to Cubic Meter
    if left_combobox.get() == 'Imperial tablespoon' and right_combobox.get() == 'Cubic Meter':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 56312)

    # Imperial tablespoon to Imperial tablespoon
    if left_combobox.get() == 'Imperial tablespoon' and right_combobox.get() == 'Imperial tablespoon':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()))

    # Imperial tablespoon to Imperial teaspoon
    if left_combobox.get() == 'Imperial tablespoon' and right_combobox.get() == 'Imperial teaspoon':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 3)

    # Imperial teaspoon

    # Imperial teaspoon to Liter
    if left_combobox.get() == 'Imperial teaspoon' and right_combobox.get() == 'Liter':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 169)

    # Imperial teaspoon to Milliliter
    if left_combobox.get() == 'Imperial teaspoon' and right_combobox.get() == 'Milliliter':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) * 5.91939)

    # Imperial teaspoon to Cubic Meter
    if left_combobox.get() == 'Imperial teaspoon' and right_combobox.get() == 'Cubic Meter':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 168936)

    # Imperial teaspoon to Imperial tablespoon
    if left_combobox.get() == 'Imperial teaspoon' and right_combobox.get() == 'Imperial tablespoon':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()) / 3)

    # Imperial teaspoon to Imperial teaspoon
    if left_combobox.get() == 'Imperial teaspoon' and right_combobox.get() == 'Imperial teaspoon':
        unit_converter_right_entry.insert(0, float(unit_converter_left_entry.get()))

    unit_converter_right_entry.config(state=DISABLED)


### ALARM CLOCK ###
def clock_time():
    global alarm_toggle_on, filename

    current_time = datetime.datetime.now().strftime("%I:%M:%S  %p")

    alarm_clock_clockface.config(state=NORMAL)
    alarm_clock_clockface.delete(0, END)
    alarm_clock_clockface.insert(0, current_time)
    alarm_clock_clockface.after(1000, clock_time)
    alarm_clock_clockface.config(state=DISABLED)

    if alarm_toggle_on:

        set_alarm_time = f"{hour_combobox.get()}:{min_combobox.get()}:{sec_combobox.get()}  {am_pm_combobox.get()}"

        if current_time == set_alarm_time:
            if alarm_type_combobox.get() == 'default sound only':
                winsound.PlaySound("Music.wav", winsound.SND_ASYNC)

            if alarm_type_combobox.get() == 'custom message only':
                messagebox.askokcancel("Custom Alarm Message", alarm_clock_entry.get())

            if alarm_type_combobox.get() == 'custom .mp3 only':
                try:
                    pygame.mixer.music.play(loops=0)
                except pygame.error:
                    winsound.PlaySound("Music.wav", winsound.SND_ASYNC)

            if alarm_type_combobox.get() == 'default sound and custom message':
                messagebox.showinfo("Custom Alarm Message", alarm_clock_entry.get())

            if alarm_type_combobox.get() == 'custom .mp3 and custom message':
                try:
                    pygame.mixer.music.play(loops=0)
                    messagebox.askokcancel("Custom Alarm Message", alarm_clock_entry.get())
                except pygame.error:
                    winsound.PlaySound("Music.wav", winsound.SND_ASYNC)
                    messagebox.askokcancel("Custom Alarm Message", alarm_clock_entry.get())

            alarm_on_button.config(text='Alarm Off', fg='snow2')
            alarm_toggle_on = False


alarm_toggle_on = False


def alarm_on_off_button():
    global alarm_toggle_on

    if not alarm_toggle_on:
        alarm_on_button.config(text='Alarm On', fg='lawn green')
        alarm_toggle_on = True

    elif alarm_toggle_on:
        alarm_on_button.config(text='Alarm Off', fg='snow2')
        alarm_toggle_on = False


def custom_mp3_button():
    global filename

    filename = filedialog.askopenfilename(initialdir="C:/Users",
                                          title=f"Select .mp3 file",
                                          filetypes=(("mp3 files", "*.mp3*"), ("all files", "*.*")))

    if filename == '':
        mp3_selected_label.config(text='No custom song selected')

    else:
        file_only = os.path.basename(filename)
        mp3_selected_label.config(text=file_only)
        pygame.mixer.music.load(filename)


def stop_music_button():
    pygame.mixer.music.stop()


### DISTANCE TWO CITIES ###
def refresh_connection():
    global requests_cities, soup_cities, list_of_cities, from_entry, to_entry, in_entry, distance_two_cities_internet_status

    try:
        requests_cities = requests.get(cities_url)

        soup_cities = bs4.BeautifulSoup(requests_cities.text, 'lxml')

        list_of_cities = [i.text for i in soup_cities.find_all('a', href=True) if i['href'] != ""]

        list_of_cities = list_of_cities[32:-104]

        list_of_cities = sorted(set(list_of_cities))

        from_entry = AutocompleteCombobox(distance_two_cities_frame, font=('helvetica', 20),
                                          completevalues=list_of_cities)
        from_entry.grid(row=2, column=1, sticky='W')

        to_entry = AutocompleteCombobox(distance_two_cities_frame, font=('helvetica', 20),
                                        completevalues=list_of_cities)
        to_entry.grid(row=2, column=3, sticky='W')

        in_entry = AutocompleteCombobox(distance_two_cities_frame, font=('helvetica', 20),
                                        completevalues=['kilometers', 'miles'])
        in_entry.grid(row=2, column=5, sticky='W')

        distance_two_cities_internet_status.config(text="Connected to the internet", fg='green')

    except requests.exceptions.ConnectionError:
        distance_two_cities_internet_status.config(text='No internet connection, Please try again', fg='red')
        distance_two_cities_results.config(text='')

    except NameError:
        distance_two_cities_internet_status.config(text='No internet connection, Please try again', fg='red')
        distance_two_cities_results.config(text='')


def distance_two_cities_calculator():
    try:
        from_location = from_entry.get()
        to_location = to_entry.get()
        in_units = in_entry.get()

        distance_url = f"https://www.google.com/search?q=distance+between+{from_location}+and+{to_location}+in+{in_units}&sxsrf=AOaemvKZ2xmOJsD242QnsgBof_CJz1eWeg%3A1634341122190&ei=AhFqYcaQC4n0rAHCvb7wCA&ved=0ahUKEwjGmZ6Qy83zAhUJOisKHcKeD44Q4dUDCA4&uact=5&oq=distance+between+london+and+brisbane+in+kilometers&gs_lcp=Cgdnd3Mtd2l6EAMyBwgjELADECcyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsANKBAhBGABQAFgAYLEnaAJwAngAgAEAiAEAkgEAmAEAyAEJwAEB&sclient=gws-wiz"

        requests_distance = requests.get(distance_url)

        soup_distance = bs4.BeautifulSoup(requests_distance.text, "lxml")

        distance_title = soup_distance.find('div', {'class': 'BNeawe tAd8D AP7Wnd'}).text
        actual_distance = soup_distance.find('div', {'class': 'BNeawe deIvCb AP7Wnd'}).text

        if actual_distance == 'Images':
            distance_two_cities_results.config(text='Invalid Entry, please try again')

        else:
            distance_two_cities_results.config(text=distance_title + '\n\n' + actual_distance)

    except AttributeError:
        distance_two_cities_results.config(text='Invalid Entry, please try again')

    except requests.exceptions.ConnectionError:
        distance_two_cities_internet_status.config(text='No internet connection, Please try again', fg='red')
        distance_two_cities_results.config(text='')

    except NameError:
        distance_two_cities_internet_status.config(text='No internet connection, Please try again', fg='red')
        distance_two_cities_results.config(text='')


### Credit Card validator ###

def credit_card_validation():
    try:
        credit_card_number_list = [int(num) for num in card_validator_entry.get() if num != ' ']

        if 13 <= len(credit_card_number_list) <= 16:

            sum_odd_credit_numbers = sum(credit_card_number_list[-1::-2])

            doubled_reverse_even_list = [num * 2 for num in credit_card_number_list[-2::-2]]

            doubled_reverse_even_list_after_adding_digits_over_nine = []

            for num in doubled_reverse_even_list:
                if num > 9:
                    doubled_reverse_even_list_after_adding_digits_over_nine.append(int(str(num)[0]) + int(str(num)[1]))
                else:
                    doubled_reverse_even_list_after_adding_digits_over_nine.append(num)

            sum_even_credit_numbers = sum(doubled_reverse_even_list_after_adding_digits_over_nine)

            sum_of_odd_and_even = sum_even_credit_numbers + sum_odd_credit_numbers

            if sum_of_odd_and_even % 10 == 0 and credit_card_number_list[0] == 4:
                card_validator_results.config(text='Valid Visa card number', fg='green')

            elif sum_of_odd_and_even % 10 == 0 and credit_card_number_list[0] == 5:
                card_validator_results.config(text='Valid Master card number', fg='green')

            elif sum_of_odd_and_even % 10 == 0 and credit_card_number_list[0] == 6:
                card_validator_results.config(text='Valid Discover card number', fg='green')

            elif sum_of_odd_and_even % 10 == 0 and credit_card_number_list[0] == 3 and credit_card_number_list[1] == 7:
                card_validator_results.config(text='Valid American Express card number', fg='green')

            else:
                card_validator_results.config(
                    text='Invalid credit card number. Fails the Luhn check (Modulus 10 check).', fg='red')

        else:
            card_validator_results.config(
                text='Invalid credit card number. A credit card must have between 13 and 16 digits.', fg='red')

    except ValueError:
        card_validator_results.config(text='Invalid credit card number. Must only contain numbers', fg='red')


### INCOME TAX CALCULATOR ###

def income_tax_calc():
    try:

        simple_tax_results.config(text='The estimated tax on your taxable income is $0.00')

        tax_input = int(simple_tax_entry.get())

        if tax_input < 18200:
            simple_tax_results.config(text='The estimated tax on your taxable income is $0.00', fg='green')

        if 18200 < tax_input <= 45000:
            simple_tax_results.config(
                text=f'The estimated tax on your taxable income is ${"{:.2f}".format(float(((tax_input - 18200) * 19) / 100))}',
                fg='green')

        if 45000 < tax_input <= 120000:
            simple_tax_results.config(
                text=f'The estimated tax on your taxable income is ${"{:.2f}".format(5092 + float(((tax_input - 45000) * 32.5) / 100))}',
                fg='green')

        if 120000 < tax_input <= 180000:
            simple_tax_results.config(
                text=f'The estimated tax on your taxable income is ${"{:.2f}".format(29467 + float(((tax_input - 120000) * 37) / 100))}',
                fg='green')

        if tax_input > 180000:
            simple_tax_results.config(
                text=f'The estimated tax on your taxable income is ${"{:.2f}".format(51667 + float(((tax_input - 180000) * 45) / 100))}',
                fg='green')

    except ValueError:
        simple_tax_results.config(text='Incorrect entry, Please enter a number only', fg='red')


### FACTORIAL FINDER ###
def factorial_finder():
    try:
        if int(factorial_finder_entry.get()) == 0:
            factorial_finder_results.config(text=f'The factorial of 0 is 1')

        elif int(factorial_finder_entry.get()) == 1:
            factorial_finder_results.config(text=f'The factorial of 1 is 1')

        elif 1 <= int(factorial_finder_entry.get()) <= 50:
            factorial = 1
            for num in range(int(factorial_finder_entry.get()), 1, -1):
                factorial = factorial * num
                factorial_finder_results.config(
                    text=f'The factorial of {factorial_finder_entry.get()} is: \n{factorial}')

        else:
            factorial_finder_results.config(text='Please enter a valid number between 0 - 50.')

    except ValueError:
        factorial_finder_results.config(text='Please enter a valid number.')


### Prime Factorization ###


def prime_factorizaton_func():
    user_num = int(prime_factorization_entry.get())
    number = user_num

    prime_list = []

    for num in range(2, int(number / 2) + 1):

        while number % int(num) == 0:
            prime_list.append(str(num))
            number = number / int(num)

            if number % int(num) != 0:

                if num > int(math.sqrt(number)):
                    num += 1

    if len(prime_list) == 0:
        prime_factorization_results.config(text=f"{user_num} has no prime factors.")
    else:

        new_prime_list = ", ".join(prime_list)

        prime_factorization_results.config(text=f"The Prime Factorization of {user_num} is:\n {new_prime_list}")


### HAPPY NUMBERS ###

def happy_number_submit():
    try:
        happy_number = happy_numbers_entry.get()
        original_number = happy_number

        while int(happy_number) >= 1:
            my_num = 0
            for digit in str(happy_number):
                my_num += (int(digit) ** 2)
            happy_number = my_num
            if happy_number == 4:
                happy_numbers_results.config(text=f'{original_number}: Not a happy number')
                break
            elif happy_number == 1:
                happy_numbers_results.config(text=f'{original_number}: Happy number!!')
                break

    except ValueError:
        happy_numbers_results.config(text='Please enter a valid number')


### NUMBER NAMES ###

def three_digits_to_text(group_of_three, number_amount):
    global text_output

    try:

        # Three digit numbers if all digits are a 0 (skip text)
        if len(group_of_three) == 3 and group_of_three[0] == '0' and group_of_three[1] == '0' and group_of_three[
            2] == '0':
            group_of_three = group_of_three[3:]

        # Three digit numbers if the first digit is a zero (delete zero, add an 'and')
        if len(group_of_three) == 3 and group_of_three[0] == '0' and group_of_three[1] != '0':
            group_of_three = group_of_three[1:]
            text_output += ' and '

        # Three digit numbers if the first and second digits are zeros (delete zeros, add an 'and')
        if len(group_of_three) == 3 and group_of_three[0] == '0' and group_of_three[1] == '0' and group_of_three[
            2] != '0':
            group_of_three = group_of_three[2:]
            text_output += ' and '

        # Three digit numbers with 0's as the second and third digit
        if len(group_of_three) == 3 and group_of_three[1] == '0' and group_of_three[2] == '0':
            text_output += (one_to_nine_dict[group_of_three[0]] + ' hundred ' + number_amount)

        # Three digit numbers from 100 to 999
        if len(group_of_three) == 3 and (group_of_three[1] != '0' or group_of_three[2] != '0'):
            text_output += (one_to_nine_dict[group_of_three[0]] + ' hundred and ')
            group_of_three = group_of_three[1:]

        # Two digit numbers from 20 to 99
        if len(group_of_three) == 2 and int(group_of_three) >= 20:
            text_output += (twenty_to_ninety_dict[group_of_three[0]] + ' ')
            group_of_three = group_of_three[1:]

        # Two digit numbers from 10 to 19 (this covers all the 'teen' numbers)
        if len(group_of_three) == 2 and 9 < int(group_of_three) < 20:
            text_output += (ten_to_nineteen_dict[group_of_three] + ' ')
            if len(groups_of_three_list) >= 2:
                text_output += number_amount + ' '

        # Two digit numbers if the first digit is a 0 (delete the zero)
        if len(group_of_three) == 2 and group_of_three[0] == '0':
            group_of_three = group_of_three[1:]

        # Single digit numbers
        if len(group_of_three) == 1:
            text_output += (one_to_nine_dict[group_of_three] + ' ')
            if len(groups_of_three_list) > 1:
                text_output += number_amount + ' '

    except KeyError:
        number_name_results.config(text="Please enter a number")


def number_name_submit():
    global text_output

    try:

        text_output = ''

        number_input = str(int(number_name_entry.get()))

        if 0 <= int(number_input) <= 999999999999999:

            if len(number_input) in [1, 2, 3]:
                groups_of_three_list.append(number_input)

            elif len(number_input) in [4, 5, 6]:
                hundred = number_input[-3:]
                thousand = number_input[:-3]
                groups_of_three_list.append(thousand)
                groups_of_three_list.append(hundred)

            elif len(number_input) in [7, 8, 9]:
                hundred = number_input[-3:]
                thousand = number_input[-6:-3]
                million = number_input[-9:-6]
                groups_of_three_list.append(million)
                groups_of_three_list.append(thousand)
                groups_of_three_list.append(hundred)

            elif len(number_input) in [10, 11, 12]:
                hundred = number_input[-3:]
                thousand = number_input[-6:-3]
                million = number_input[-9:-6]
                billion = number_input[-12:-9]
                groups_of_three_list.append(billion)
                groups_of_three_list.append(million)
                groups_of_three_list.append(thousand)
                groups_of_three_list.append(hundred)

            elif len(number_input) in [13, 14, 15]:
                hundred = number_input[-3:]
                thousand = number_input[-6:-3]
                million = number_input[-9:-6]
                billion = number_input[-12:-9]
                trillion = number_input[-15:-12]
                groups_of_three_list.append(trillion)
                groups_of_three_list.append(billion)
                groups_of_three_list.append(million)
                groups_of_three_list.append(thousand)
                groups_of_three_list.append(hundred)

            if len(groups_of_three_list) == 5:
                three_digits_to_text(groups_of_three_list[0], 'trillion ')
                groups_of_three_list.pop(0)

            if len(groups_of_three_list) == 4:
                three_digits_to_text(groups_of_three_list[0], 'billion ')
                groups_of_three_list.pop(0)

            if len(groups_of_three_list) == 3:
                three_digits_to_text(groups_of_three_list[0], 'million ')
                groups_of_three_list.pop(0)

            if len(groups_of_three_list) == 2:
                three_digits_to_text(groups_of_three_list[0], 'thousand ')
                groups_of_three_list.pop(0)

            if len(groups_of_three_list) == 1:
                three_digits_to_text(groups_of_three_list[0], 'hundred ')
                groups_of_three_list.pop(0)

            if number_input == '69':
                number_name_results.config(text=" ".join(text_output.split()) + '\n...nice')

            elif number_input == '80085':
                number_name_results.config(text=" ".join(text_output.split()) + '\n( . )( . )')

            else:
                number_name_results.config(text=" ".join(text_output.split()))

        else:
            number_name_results.config(text="Number must be between 0 and 999,999,999,999,999")

    except KeyError:
        number_name_results.config(text="Please enter a number")

    except ValueError:
        number_name_results.config(text="Please enter a number")


def text_to_speech():
    global text_output

    number_name_submit()

    text = text_output
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)

    if number_name_entry.get() == '69':
        engine.setProperty("rate", 75)
        engine.say('nice')
        engine.runAndWait()

    elif number_name_entry.get() == '80085':
        engine.setProperty("rate", 100)
        engine.say('boobies')
        engine.runAndWait()

    else:
        engine.setProperty("rate", 200)
        engine.say(text)
        # play the speech
        engine.runAndWait()


### COIN FLIP SIMULATOR ###
def coin_flip_submit():
    coin_flip_text_box.delete('1.0', END)

    try:
        if 0 < int(coin_flip_entry.get()) < 1001:

            coin_face = ['HEADS', 'TAIL']
            total_count = 0
            head_count = 0
            tail_count = 0

            for flips in range(int(coin_flip_entry.get())):

                total_count += 1

                flip_result = random.choice(coin_face)

                if flip_result == 'HEADS':
                    head_count += 1
                    if total_count == int(coin_flip_entry.get()):
                        coin_flip_text_box.insert(END, 'H', 'head')
                        coin_flip_text_box.tag_config('head', foreground='red')
                    else:
                        coin_flip_text_box.insert(END, 'H, ', 'head')
                        coin_flip_text_box.tag_config('head', foreground='red')

                elif flip_result == 'TAIL':
                    tail_count += 1
                    if total_count == int(coin_flip_entry.get()):
                        coin_flip_text_box.insert(END, 'T', 'tail')
                        coin_flip_text_box.tag_config('tail', foreground='light green')
                    else:
                        coin_flip_text_box.insert(END, 'T, ', 'tail')
                        coin_flip_text_box.tag_config('tail', foreground='light green')

            coin_flip_head_count.config(text=f'HEAD COUNT: {head_count}')
            coin_flip_tail_count.config(text=f'TAIL COUNT: {tail_count}')

            try:
                coin_flip_head_percent.config(
                    text=f"HEAD PERCENT: {round(head_count / int(coin_flip_entry.get()) * 100, 2)}%")
            except ZeroDivisionError:
                coin_flip_head_percent.config(text=f"HEAD PERCENT: 0%")
            try:
                coin_flip_tail_percent.config(
                    text=f"TAIL PERCENT: {round(tail_count / int(coin_flip_entry.get()) * 100, 2)}%")
            except ZeroDivisionError:
                coin_flip_head_percent.config(text=f"TAIL PERCENT: 0%")

        else:
            coin_flip_text_box.insert(END, 'Please insert a number between 1-1000')

    except ValueError:
        coin_flip_text_box.insert(END, 'Please insert a number between 1-1000')


def exponentiation_submit():
    exponentiation_results.config(text='')

    try:

        if 0 <= int(exponentiation_x_entry.get()) <= 100 and 0 <= int(exponentiation_y_entry.get()) <= 100:

            x_value = int(exponentiation_x_entry.get())
            y_value = int(exponentiation_y_entry.get())

            x_to_power_of_y_result = pow(x_value, y_value)

            exponentiation_results.config(text=x_to_power_of_y_result)

        else:
            exponentiation_results.config(text='Enter a valid number between 0-100')

    except ValueError:
        exponentiation_results.config(text='Enter a valid number')


### FRAME WIDGET CONFIG ###


### WELCOME FRAME TKINTER CONFIG ###
# Frame config
welcome_screen_frame.rowconfigure(0, weight=1)
welcome_screen_frame.columnconfigure(0, weight=1)

# Title label
welcome_label = Label(welcome_screen_frame, text="Mathematics Toolkit", bg='royalblue4', fg='snow1', font=('helvetica', 50))
welcome_label.grid(row=0)

# Creator label
creator_label = Label(welcome_screen_frame, text="Created by Brenton O'Brien", bg='royalblue4', fg='snow1', font=('helvetica', 20))
creator_label.grid(row=1)
### END OF WELCOME FRAME TKINTER CONFIG ###


### PI TO THE NTH DIGIT TKINTER CONFIG ###
# Frame config
pi_to_nth_digit_frame.columnconfigure(0, weight=1)

# Title label
pi_to_nth_digit_label = Label(pi_to_nth_digit_frame, text="Pi to the nth digit", bg='royalblue4', fg='snow1', font=('helvetica', 50))
pi_to_nth_digit_label.grid(row=0)

# Instructions label
pi_to_nth_digit_instructions = Label(pi_to_nth_digit_frame, text="Enter a to generate π (pi) up to that many digits. Limit is 10,000 digits.", bg='royalblue4', fg='snow1', font=('helvetica', 20), pady=50)
pi_to_nth_digit_instructions.grid(row=1)

# Entry box
pi_to_nth_digit_entry = Entry(pi_to_nth_digit_frame, font=('helvetica', 25), width=25, relief=RIDGE, bd=4, bg='Dodger Blue', fg='snow2')
pi_to_nth_digit_entry.grid(row=2)

# Submit button
pi_to_nth_digit_submit_button = Button(pi_to_nth_digit_frame, text='Submit', font=('helvetica', 20), relief=RAISED, bd=4, bg='Dodger Blue', fg='snow2', command=pi_to_nth_digit_submit)
pi_to_nth_digit_submit_button.grid(row=3, pady=2)

# Scrolled results box
pi_to_nth_digit_results = scrolledtext.ScrolledText(pi_to_nth_digit_frame, bg='royalblue4', fg='snow1', font=('helvetica', 20), height=12, wrap=WORD)
pi_to_nth_digit_results.grid(row=4, pady=2)
### END OF PI TO THE NTH DIGIT TKINTER CONFIG ###


### E TO THE NTH DIGIT TKINTER CONFIG ###
# Frame config
e_to_nth_digit_frame.columnconfigure(0, weight=1)

# Title label
e_to_nth_digit_label = Label(e_to_nth_digit_frame, text="e to the nth digit", bg='royalblue4', fg='snow1',font=('helvetica', 50))
e_to_nth_digit_label.grid(row=0, sticky='N')

# Instructions label
e_to_nth_digit_instructions = Label(e_to_nth_digit_frame, text="Enter a number to generate e up to that many digits. Limit is 10,000 digits.", bg='royalblue4', fg='snow1', font=('helvetica', 20), pady=50)
e_to_nth_digit_instructions.grid(row=1)

# Entry box
e_to_nth_digit_entry = Entry(e_to_nth_digit_frame, font=('helvetica', 25), width=25, relief=RIDGE, bd=4, bg='Dodger Blue', fg='snow2')
e_to_nth_digit_entry.grid(row=2)

# Submit button
e_to_nth_digit_submit_button = Button(e_to_nth_digit_frame, text='Submit', font=('helvetica', 20), relief=RAISED, bd=4, bg='Dodger Blue', fg='snow2', command=e_to_nth_digit_submit)
e_to_nth_digit_submit_button.grid(row=3, pady=2)

# Scrolled results box
e_to_nth_digit_results = scrolledtext.ScrolledText(e_to_nth_digit_frame, bg='royalblue4', fg='snow1', font=('helvetica', 20), height=12, wrap=WORD)
e_to_nth_digit_results.grid(row=4, pady=2)
### END OF E TO THE NTH DIGIT TKINTER CONFIG ###


### fibonachi sequence ###
fibonacci_sequence_frame.columnconfigure(0, weight=1)

fibonacci_sequence_label = Label(fibonacci_sequence_frame, text="Fibonacci Sequence", bg='royalblue4', fg='snow1',
                                 font=('helvetica', 50))
fibonacci_sequence_label.grid(row=0, sticky='N')

fibonacci_sequence_instructions = Label(fibonacci_sequence_frame,
                                        text="Enter a number and the program will generate the fibonacci sequence up to that many numbers. Limit is 30 numbers.",
                                        bg='royalblue4', fg='snow1', font=('helvetica', 20), pady=50)
fibonacci_sequence_instructions.grid(row=1)

fibonacci_sequence_entry = Entry(fibonacci_sequence_frame, font=('helvetica', 25), width=25, relief=RIDGE, bd=4,
                                 bg='Dodger Blue', fg='snow2')
fibonacci_sequence_entry.grid(row=2)

fibonacci_sequence_submit_button = Button(fibonacci_sequence_frame, text='Submit', font=('helvetica', 20),
                                          command=fibonacci_sequence_submit)
fibonacci_sequence_submit_button.grid(row=3, pady=2)

fibonacci_sequence_results = Label(fibonacci_sequence_frame, text="", bg='royalblue4', fg='snow1',
                                   font=('helvetica', 16))
fibonacci_sequence_results.grid(row=4, pady=50)

### Next prime number ###
next_prime_frame.columnconfigure(0, weight=1)

next_prime_label = Label(next_prime_frame, text="Prime Number generator", bg='royalblue4', fg='snow1',
                         font=('helvetica', 50))
next_prime_label.grid(row=0, sticky='N')

next_prime_instructions = Label(next_prime_frame,
                                text="Enter a number and the program will generate that many prime numbers. Limit is 40 numbers.",
                                bg='royalblue4', fg='snow1', font=('helvetica', 20), pady=50)
next_prime_instructions.grid(row=1)

next_prime_entry = Entry(next_prime_frame, font=('helvetica', 25), width=25, relief=RIDGE, bd=4, bg='Dodger Blue',
                         fg='snow2')
next_prime_entry.grid(row=2)

next_prime_submit_button = Button(next_prime_frame, text='Submit', font=('helvetica', 20), command=next_prime_submit)
next_prime_submit_button.grid(row=3, pady=2)

next_prime_results = Label(next_prime_frame, text="", bg='royalblue4', fg='snow1', font=('helvetica', 15))
next_prime_results.grid(row=4, pady=50)

### Cost to cover W x H floor ###
w_x_h_floor_frame.columnconfigure(0, weight=1)

w_x_h_floor_title = Label(w_x_h_floor_frame, text="Tile cost calculator", bg='royalblue4', fg='snow1',
                          font=('helvetica', 50))
w_x_h_floor_title.grid(sticky='N', row=0)

w_x_h_floor_instructions = Label(w_x_h_floor_frame,
                                 text='Enter cost per tile, width and height to calculate the total cost.',
                                 bg='royalblue4', fg='snow1', font=('helvetica', 20), pady=50)
w_x_h_floor_instructions.grid(row=1)

w_x_h_floor_cost_label = Label(w_x_h_floor_frame, text='Enter cost per tile $:                  ', bg='royalblue4',
                               fg='snow1',
                               font=('helvetica', 20))
w_x_h_floor_cost_label.grid(row=2)

w_x_h_floor_cost_entry = Entry(w_x_h_floor_frame, font=('helvetica', 25), relief=RIDGE, bd=4, bg='Dodger Blue',
                               fg='snow2', width=25)
w_x_h_floor_cost_entry.grid(row=3)

w_x_h_floor_width_label = Label(w_x_h_floor_frame, text='\nEnter number of tiles for width:  ', bg='royalblue4',
                                fg='snow1',
                                font=('helvetica', 20))
w_x_h_floor_width_label.grid(row=4)

w_x_h_floor_width_entry = Entry(w_x_h_floor_frame, font=('helvetica', 25), relief=RIDGE, bd=4, bg='Dodger Blue',
                                fg='snow2', width=25)
w_x_h_floor_width_entry.grid(row=5)

w_x_h_floor_height_label = Label(w_x_h_floor_frame, text='\nEnter number of tiles for height: ', bg='royalblue4',
                                 fg='snow1', font=('helvetica', 20))
w_x_h_floor_height_label.grid(row=6)

w_x_h_floor_height_entry = Entry(w_x_h_floor_frame, font=('helvetica', 25), relief=RIDGE, bd=4, bg='Dodger Blue',
                                 fg='snow2', width=25)
w_x_h_floor_height_entry.grid(row=7)

w_x_h_floor_submit = Button(w_x_h_floor_frame, text='Submit', font=('helvetica', 20), command=w_x_h_floor_button)
w_x_h_floor_submit.grid(row=8, pady=2)

w_x_h_floor_results = Label(w_x_h_floor_frame, text='', bg='royalblue4', fg='snow1', font=('helvetica', 40))
w_x_h_floor_results.grid(row=9)

### Morgage Calculator ###
morgage_calculator_frame.columnconfigure(0, weight=1)

morgage_calculator_title = Label(morgage_calculator_frame, text="Morgage Calculator", bg='royalblue4', fg='snow1',
                                 font=('helvetica', 50))
morgage_calculator_title.grid(row=0, sticky='N')

morgage_calculator_instructions = Label(morgage_calculator_frame,
                                        text='Enter the total Loan Amount, monthly interest rate, length of loan in months,\n'
                                             'and payment frequency then click submit', bg='royalblue4', fg='snow1',
                                        font=('helvetica', 20), pady=25)
morgage_calculator_instructions.grid(row=1)

morgage_calculator_total_label = Label(morgage_calculator_frame, text='Morgage amount $:        ', bg='royalblue4',
                                       fg='snow1',
                                       font=('helvetica', 20))
morgage_calculator_total_label.grid(row=2)

morgage_calculator_total_entry = Entry(morgage_calculator_frame, font=('helvetica', 20))
morgage_calculator_total_entry.grid(row=3, pady=(0, 20))

morgage_calculator_interest_rate_label = Label(morgage_calculator_frame, text='Interest Rate %:             ',
                                               bg='royalblue4',
                                               fg='snow1', font=('helvetica', 20))
morgage_calculator_interest_rate_label.grid(row=4)

morgage_calculator_interest_rate_entry = Entry(morgage_calculator_frame, font=('helvetica', 20))
morgage_calculator_interest_rate_entry.grid(row=5, pady=(0, 20))

morgage_calculator_year_of_loan_label = Label(morgage_calculator_frame, text='Total years of the loan:   ',
                                              bg='royalblue4',
                                              fg='snow1', font=('helvetica', 20))
morgage_calculator_year_of_loan_label.grid(row=6)

morgage_calculator_year_of_loan_entry = Entry(morgage_calculator_frame, font=('helvetica', 20))
morgage_calculator_year_of_loan_entry.grid(row=7, pady=(0, 20))

morgage_calculator_payment_frequency_label = Label(morgage_calculator_frame, text='Payment Frequency:       ',
                                                   bg='royalblue4',
                                                   fg='snow1', font=('helvetica', 20))
morgage_calculator_payment_frequency_label.grid(row=8)

selected_frequency = StringVar()
morgage_calculator_combobox = ttk.Combobox(morgage_calculator_frame, textvariable=selected_frequency, width=19,
                                           font=('helvetica', 20))
morgage_calculator_combobox['values'] = ('Monthly', 'Fortnightly', 'Weekly')
morgage_calculator_combobox['state'] = 'readonly'
morgage_calculator_combobox.current(0)
morgage_calculator_combobox.grid(row=9, pady=5)

morgage_calculator_submit = Button(morgage_calculator_frame, text='Submit', font=('helvetica', 20),
                                   command=morgage_calculator_button)
morgage_calculator_submit.grid(row=10)

morgage_calculator_results = Label(morgage_calculator_frame, text='', bg='royalblue4', fg='snow1',
                                   font=('helvetica', 30))
morgage_calculator_results.grid(row=11, pady=25)

### Change return program ###
change_return_frame.columnconfigure(0, weight=1)

change_return_submit_title = Label(change_return_frame, text="Change Return Calculator", bg='royalblue4', fg='snow1',
                                   font=('helvetica', 50))
change_return_submit_title.grid(row=0, sticky='N')

change_return_instructions = Label(change_return_frame,
                                   text='Enter unit price and amount paid, then click submit', bg='royalblue4',
                                   fg='snow1', font=('helvetica', 20))
change_return_instructions.grid(row=1, pady=(0, 25))

change_return_item_cost_label = Label(change_return_frame, text='Item cost $:                    ', bg='royalblue4',
                                      fg='snow1',
                                      font=('helvetica', 20))
change_return_item_cost_label.grid(row=2)

change_return_item_cost_entry = Entry(change_return_frame, font=('helvetica', 20))
change_return_item_cost_entry.grid(row=3, pady=(0, 20))

change_return_amount_paid_label = Label(change_return_frame, text='Amount paid $:               ', bg='royalblue4',
                                        fg='snow1',
                                        font=('helvetica', 20))
change_return_amount_paid_label.grid(row=4)

change_return_amount_paid_entry = Entry(change_return_frame, font=('helvetica', 20))
change_return_amount_paid_entry.grid(row=5)

change_return_submit_button = Button(change_return_frame, text='Submit', font=('helvetica', 20),
                                     command=change_return_submit)
change_return_submit_button.grid(row=6, pady=2)

change_return_change_owed_label = Label(change_return_frame, text='Change owed: $', bg='royalblue4', fg='snow1',
                                        font=('helvetica', 20))
change_return_change_owed_label.grid(row=7, pady=10)

change_return_results = Label(change_return_frame, text='$50 notes:    0\n'
                                                        '$20 notes:    0\n'
                                                        '$10 notes:    0\n'
                                                        '$5 notes:     0\n'
                                                        '$2 coins:     0\n'
                                                        '$1 coins:     0\n'
                                                        '$0.50 coins: 0\n'
                                                        '$0.20 coins: 0\n'
                                                        '$0.10 coins: 0\n'
                                                        '$0.05 coins: 0', bg='royalblue4', fg='snow1',
                              font=('helvetica', 20))
change_return_results.grid(row=8)

### binary to decimal converter ###
binary_to_decimal_frame.columnconfigure(0, weight=1)

binary_to_decimal_title = Label(binary_to_decimal_frame, text="Binary and Decimal Convertor", bg='royalblue4',
                                fg='snow1', font=('helvetica', 50))
binary_to_decimal_title.grid(row=0, sticky='N')

binary_to_decimal_instructions = Label(binary_to_decimal_frame,
                                       text='Use the drop down menu to select conversion type, enter a figure then click submit',
                                       bg='royalblue4', fg='snow1', font=('helvetica', 20))
binary_to_decimal_instructions.grid(row=1, pady=50)

binary_to_decimal_combobox_label = Label(binary_to_decimal_frame, text='Select a conversion type:  ',
                                         bg='royalblue4', fg='snow1', font=('helvetica', 20))
binary_to_decimal_combobox_label.grid(row=2)

selected_binary = StringVar()
binary_combobox = ttk.Combobox(binary_to_decimal_frame, textvariable=selected_binary, width=20, font=('helvetica', 20))
binary_combobox['values'] = ('Decimal to Binary', 'Binary to Decimal')
binary_combobox['state'] = 'readonly'
binary_combobox.current(0)
binary_combobox.grid(row=3, pady=5)

binary_to_decimal_num_label = Label(binary_to_decimal_frame, text='Enter binary or number:    ',
                                    bg='royalblue4', fg='snow1', font=('helvetica', 20))
binary_to_decimal_num_label.grid(row=4, pady=(20, 0))

binary_to_decimal_entry = Entry(binary_to_decimal_frame, font=('helvetica', 20), width=21)
binary_to_decimal_entry.grid(row=5)

binary_to_decimal_button = Button(binary_to_decimal_frame, text='Submit', font=('helvetica', 20),
                                  command=binary_to_decimal_submit)
binary_to_decimal_button.grid(row=6, pady=2)

binary_to_decimal_results = Label(binary_to_decimal_frame, text='', bg='royalblue4', fg='snow1', font=('helvetica', 40))
binary_to_decimal_results.grid(row=7, pady=50)

### Scientific Calculator ###

calculator_title = Label(calculator_frame, text="Scientific Calculator", bg='royalblue4', fg='snow1',
                         font=('helvetica', 50))
calculator_title.grid(row=0, columnspan=6, padx=200, sticky="nsew")

calculator_entry = Entry(calculator_frame, font=('helvetica', 50), width=41, relief=RIDGE, justify=RIGHT, bd=10,
                         bg='Dodger Blue', fg='snow2', disabledbackground='Dodger Blue', disabledforeground='snow2',
                         state=DISABLED)
calculator_entry.grid(row=1, columnspan=6, pady=20, sticky="nsew")

# Row 2
# ABS button
calculator_abs_button = Button(calculator_frame, font=('helvetica', 25), text='Abs', relief=RAISED, bd=4,
                               bg='Dodger Blue', fg='snow2', width=4, height=1, command=calc_abs)
calculator_abs_button.grid(row=2, column=0, sticky="nsew")

# log button
calculator_log_button = Button(calculator_frame, font=('helvetica', 25), text='log', relief=RAISED, bd=4,
                               bg='Dodger Blue', fg='snow2', width=4, height=1, command=calc_log)
calculator_log_button.grid(row=2, column=1, sticky="nsew")

# ln button
calculator_ln_button = Button(calculator_frame, font=('helvetica', 25), text='ln', relief=RAISED, bd=4,
                              bg='Dodger Blue', fg='snow2', width=4, height=1, command=calc_ln)
calculator_ln_button.grid(row=2, column=2, sticky="nsew")

# e button
calculator_e_button = Button(calculator_frame, font=('helvetica', 25), text='e', relief=RAISED, bd=4, bg='Dodger Blue',
                             fg='snow2', width=4, height=1, command=calc_e)
calculator_e_button.grid(row=2, column=3, sticky="nsew")

# x! button
calculator_factorial_button = Button(calculator_frame, font=('helvetica', 25), text='x!', relief=RAISED, bd=4,
                                     bg='Dodger Blue', fg='snow2', width=4, height=1, command=calc_factorial)
calculator_factorial_button.grid(row=2, column=4, sticky="nsew")

# ANS button
calculator_ans_button = Button(calculator_frame, font=('helvetica', 25), text='Ans', relief=RAISED, bd=4,
                               bg='Dodger Blue', fg='snow2', width=4, height=1, command=calc_ans)
calculator_ans_button.grid(row=2, column=5, sticky="nsew")

# Row 3
# Squared button
calculator_squared_button = Button(calculator_frame, font=('helvetica', 25), text='x^2', relief=RAISED, bd=4,
                                   bg='Dodger Blue', fg='snow2', width=4, height=1, command=calc_square)
calculator_squared_button.grid(row=3, column=0, sticky="nsew")

# Cubed button
calculator_cubed_button = Button(calculator_frame, font=('helvetica', 25), text='x^3', relief=RAISED, bd=4,
                                 bg='Dodger Blue', fg='snow2', width=4, height=1, command=calc_cube)
calculator_cubed_button.grid(row=3, column=1, sticky="nsew")

# x to the power of y button
calculator_power_button = Button(calculator_frame, font=('helvetica', 25), text='x^y', relief=RAISED, bd=4,
                                 bg='Dodger Blue', fg='snow2', width=4, height=1, command=calc_power)
calculator_power_button.grid(row=3, column=2, sticky="nsew")

# square root button
calculator_sqrt_button = Button(calculator_frame, font=('helvetica', 25), text='√x', relief=RAISED, bd=4,
                                bg='Dodger Blue', fg='snow2', width=4, height=1, command=calc_sqrt)
calculator_sqrt_button.grid(row=3, column=3, sticky="nsew")

# 3rd root button
calculator_third_root_button = Button(calculator_frame, font=('helvetica', 25), text='3√x', relief=RAISED, bd=4,
                                      bg='Dodger Blue', fg='snow2', width=4, height=1, command=calc_third_root)
calculator_third_root_button.grid(row=3, column=4, sticky="nsew")

# inverse button
calculator_inverse_button = Button(calculator_frame, font=('helvetica', 25), text='x^-1', relief=RAISED, bd=4,
                                   bg='Dodger Blue', fg='snow2', width=4, height=1, command=calc_inverse)
calculator_inverse_button.grid(row=3, column=5, sticky="nsew")

# Row 4
# sin button
calculator_sin_button = Button(calculator_frame, font=('helvetica', 25), text='sin', relief=RAISED, bd=4,
                               bg='Dodger Blue', fg='snow2', width=4, height=1, command=calc_sin)
calculator_sin_button.grid(row=4, column=0, sticky="nsew")

# cos button
calculator_cos_button = Button(calculator_frame, font=('helvetica', 25), text='cos', relief=RAISED, bd=4,
                               bg='Dodger Blue', fg='snow2', width=4, height=1, command=calc_cos)
calculator_cos_button.grid(row=4, column=1, sticky="nsew")

# tan button
calculator_tan_button = Button(calculator_frame, font=('helvetica', 25), text='tan', relief=RAISED, bd=4,
                               bg='Dodger Blue', fg='snow2', width=4, height=1, command=calc_tan)
calculator_tan_button.grid(row=4, column=2, sticky="nsew")

# pi button
calculator_pi_button = Button(calculator_frame, font=('helvetica', 25), text='π', relief=RAISED, bd=4, bg='Dodger Blue',
                              fg='snow2', width=4, height=1, command=calc_pi)
calculator_pi_button.grid(row=4, column=3, sticky="nsew")

# left bracket button
calculator_left_bracket_button = Button(calculator_frame, font=('helvetica', 25), text='(', relief=RAISED, bd=4,
                                        bg='Dodger Blue', fg='snow2', width=4, height=1, command=calc_left_bracket)
calculator_left_bracket_button.grid(row=4, column=4, sticky="nsew")

# right bracket button
calculator_right_bracket_button = Button(calculator_frame, font=('helvetica', 25), text=')', relief=RAISED, bd=4,
                                         bg='Dodger Blue', fg='snow2', width=4, height=1, command=calc_right_bracket)
calculator_right_bracket_button.grid(row=4, column=5, sticky="nsew")

# Row 5
# 7 button
calculator_7_button = Button(calculator_frame, font=('helvetica', 25), text='7', relief=RAISED, bd=4, bg='Dodger Blue',
                             fg='snow2', width=4, height=1, command=calc_7)
calculator_7_button.grid(row=5, column=0, sticky="nsew")

# 8 button
calculator_8_button = Button(calculator_frame, font=('helvetica', 25), text='8', relief=RAISED, bd=4, bg='Dodger Blue',
                             fg='snow2', width=4, height=1, command=calc_8)
calculator_8_button.grid(row=5, column=1, sticky="nsew")

# 9 button
calculator_9_button = Button(calculator_frame, font=('helvetica', 25), text='9', relief=RAISED, bd=4, bg='Dodger Blue',
                             fg='snow2', width=4, height=1, command=calc_9)
calculator_9_button.grid(row=5, column=2, sticky="nsew")

# % button
calculator_percent_button = Button(calculator_frame, font=('helvetica', 25), text='%', relief=RAISED, bd=4,
                                   bg='Dodger Blue', fg='snow2', width=4, height=1, command=calc_percent)
calculator_percent_button.grid(row=5, column=3, sticky="nsew")

# AC button
calculator_ac_button = Button(calculator_frame, font=('helvetica', 25), text='AC', relief=RAISED, bd=4, bg='orange',
                              fg='snow2', width=4, height=1, command=calc_all_clear)
calculator_ac_button.grid(row=5, column=4, columnspan=2, sticky="nsew")

# Row 6
# 4 button
calculator_4_button = Button(calculator_frame, font=('helvetica', 25), text='4', relief=RAISED, bd=4, bg='Dodger Blue',
                             fg='snow2', width=4, height=1, command=calc_4)
calculator_4_button.grid(row=6, column=0, sticky="nsew")

# 5 button
calculator_5_button = Button(calculator_frame, font=('helvetica', 25), text='5', relief=RAISED, bd=4, bg='Dodger Blue',
                             fg='snow2', width=4, height=1, command=calc_5)
calculator_5_button.grid(row=6, column=1, sticky="nsew")

# 6 button
calculator_6_button = Button(calculator_frame, font=('helvetica', 25), text='6', relief=RAISED, bd=4, bg='Dodger Blue',
                             fg='snow2', width=4, height=1, command=calc_6)
calculator_6_button.grid(row=6, column=2, sticky="nsew")

# x button
calculator_x_button = Button(calculator_frame, font=('helvetica', 25), text='x', relief=RAISED, bd=4, bg='Dodger Blue',
                             fg='snow2', width=4, height=1, command=calc_multiply)
calculator_x_button.grid(row=6, column=3, sticky="nsew")

# DEL button
calculator_del_button = Button(calculator_frame, font=('helvetica', 25), text='DEL', relief=RAISED, bd=4, bg='orange',
                               fg='snow2', width=4, height=1, command=calc_delete_last)
calculator_del_button.grid(row=6, column=4, columnspan=2, sticky="nsew")

# Row 7
# 1 button
calculator_1_button = Button(calculator_frame, font=('helvetica', 25), text='1', relief=RAISED, bd=4, bg='Dodger Blue',
                             fg='snow2', width=4, height=1, command=calc_1)
calculator_1_button.grid(row=7, column=0, sticky="nsew")

# 2 button
calculator_2_button = Button(calculator_frame, font=('helvetica', 25), text='2', relief=RAISED, bd=4, bg='Dodger Blue',
                             fg='snow2', width=4, height=1, command=calc_2)
calculator_2_button.grid(row=7, column=1, sticky="nsew")

# 3 button
calculator_3_button = Button(calculator_frame, font=('helvetica', 25), text='3', relief=RAISED, bd=4, bg='Dodger Blue',
                             fg='snow2', width=4, height=1, command=calc_3)
calculator_3_button.grid(row=7, column=2, sticky="nsew")

# ÷ button
calculator_divide_button = Button(calculator_frame, font=('helvetica', 25), text='÷', relief=RAISED, bd=4,
                                  bg='Dodger Blue', fg='snow2', width=4, height=1, command=calc_divide)
calculator_divide_button.grid(row=7, column=3, sticky="nsew")

# = button
calculator_equal_button = Button(calculator_frame, font=('helvetica', 25), text='=', relief=RAISED, bd=4,
                                 bg='Dodger Blue', fg='snow2', width=4, height=1, command=calc_equals)
calculator_equal_button.grid(row=7, column=4, columnspan=2, rowspan=2, sticky="nsew")

# Row 8
# 0 button
calculator_0_button = Button(calculator_frame, font=('helvetica', 25), text='0', relief=RAISED, bd=4, bg='Dodger Blue',
                             fg='snow2', width=4, height=1, command=calc_0)
calculator_0_button.grid(row=8, column=0, sticky="nsew")

# . button
calculator_period_button = Button(calculator_frame, font=('helvetica', 25), text='.', relief=RAISED, bd=4,
                                  bg='Dodger Blue', fg='snow2', width=4, height=1, command=calc_decimal)
calculator_period_button.grid(row=8, column=1, sticky="nsew")

# + button
calculator_plus_button = Button(calculator_frame, font=('helvetica', 25), text='+', relief=RAISED, bd=4,
                                bg='Dodger Blue', fg='snow2', width=4, height=1, command=calc_plus)
calculator_plus_button.grid(row=8, column=2, sticky="nsew")

# - button
calculator_minus_button = Button(calculator_frame, font=('helvetica', 25), text='-', relief=RAISED, bd=4,
                                 bg='Dodger Blue', fg='snow2', width=4, height=1, command=calc_minus)
calculator_minus_button.grid(row=8, column=3, sticky="nsew")

### Unit Converter ###

# Title
unit_converter_title = Label(unit_converter_frame, text="Unit Converter", bg='royalblue4', fg='snow1',
                             font=('helvetica', 50))
unit_converter_title.grid(row=0, sticky='N', column=0, padx=100, columnspan=3)

# Instructions
unit_converter_instructions = Label(unit_converter_frame,
                                    text="Use the drop down menu's to select conversion type, enter a figure then click submit.",
                                    bg='royalblue4', fg='snow1', font=('helvetica', 20))
unit_converter_instructions.grid(row=1, pady=50, column=0, padx=200, columnspan=3)

# Top combo box
selected_unit = StringVar()
top_combobox = ttk.Combobox(unit_converter_frame, textvariable=selected_unit, width=20, font=('helvetica', 20))
top_combobox['values'] = ('Area', 'Energy', 'Frequency', 'Length', 'Mass', 'Pressure', 'Temperature', 'Time', 'Volume')
top_combobox['state'] = 'readonly'
top_combobox.current(0)
top_combobox.grid(row=2, pady=5, column=0, padx=100, columnspan=3)
top_combobox.bind('<<ComboboxSelected>>', unit_converter_top_combobox)

# Equals label
unit_converter_equals_label = Label(unit_converter_frame, text="=", bg='royalblue4', fg='snow1',
                                    font=('helvetica', 100))
unit_converter_equals_label.grid(row=3, rowspan=2, column=1)

# Left entry
unit_converter_left_entry = Entry(unit_converter_frame, font=('helvetica', 20), width=21, justify=RIGHT, relief=RIDGE,
                                  bd=5, bg='Dodger Blue', fg='snow2', disabledbackground='Dodger Blue',
                                  disabledforeground='snow2', state=NORMAL)
unit_converter_left_entry.grid(row=3, column=0, sticky='E', rowspan=2)

# Left combo box
selected_left_unit = StringVar()
left_combobox = ttk.Combobox(unit_converter_frame, textvariable=selected_left_unit, width=20, font=('helvetica', 20))
left_combobox['values'] = (
    'Square kilometer', 'Square meter', 'Square mile', 'Square yard', 'Square foot', 'Square inch', 'Hectare', 'Acre')
left_combobox['state'] = 'readonly'
left_combobox.current(0)
left_combobox.grid(row=4, column=0, sticky='E', pady=(50, 0))

# Right entry
unit_converter_right_entry = Entry(unit_converter_frame, font=('helvetica', 20), width=21, relief=RIDGE, bd=5,
                                   bg='Dodger Blue', fg='snow2', disabledbackground='Dodger Blue',
                                   disabledforeground='snow2', state=DISABLED)
unit_converter_right_entry.grid(row=3, column=2, rowspan=2, sticky='W')

# Right combo box
selected_right_unit = StringVar()
right_combobox = ttk.Combobox(unit_converter_frame, textvariable=selected_right_unit, width=20, font=('helvetica', 20))
right_combobox['values'] = (
'Square kilometer', 'Square meter', 'Square mile', 'Square yard', 'Square foot', 'Square inch', 'Hectare', 'Acre')
right_combobox['state'] = 'readonly'
right_combobox.current(0)
right_combobox.grid(row=4, column=2, sticky='W', pady=(50, 0))

# Submit button
unit_converter_button = Button(unit_converter_frame, text='Submit', font=('helvetica', 20), relief=RAISED, bd=4,
                               bg='Dodger Blue', fg='snow2', command=unit_converter_submit)
unit_converter_button.grid(row=5, pady=2, column=1)

### Alarm Clock ###

# Title
alarm_clock_title = Label(alarm_clock_frame, text="Alarm Clock", bg='royalblue4', fg='snow1', font=('helvetica', 50))
alarm_clock_title.grid(row=0, columnspan=6, padx=200, sticky="nsew")

# Clock face
alarm_clock_clockface = Entry(alarm_clock_frame, font=('helvetica', 97), width=21, relief=RIDGE, justify=CENTER, bd=10,
                              bg='Dodger Blue', fg='snow2', disabledbackground='Dodger Blue',
                              disabledforeground='snow2', state=NORMAL)
alarm_clock_clockface.grid(row=1, columnspan=6, pady=20, sticky="nsew")

# Alarm labels
set_alarm_time_label = Label(alarm_clock_frame, text="Set alarm time:", bg='royalblue4', fg='snow1',
                             font=('helvetica', 25))
set_alarm_time_label.grid(row=2, column=0, columnspan=2, sticky='W', pady=(25, 0))

set_alarm_label_hour = Label(alarm_clock_frame, text="Hour", bg='royalblue4', fg='snow1', font=('helvetica', 25))
set_alarm_label_hour.grid(row=3, column=0)

set_alarm_label_min = Label(alarm_clock_frame, text="Min", bg='royalblue4', fg='snow1', font=('helvetica', 25))
set_alarm_label_min.grid(row=3, column=1)

set_alarm_label_sec = Label(alarm_clock_frame, text="Sec", bg='royalblue4', fg='snow1', font=('helvetica', 25))
set_alarm_label_sec.grid(row=3, column=2)

set_alarm_label_am_pm = Label(alarm_clock_frame, text="AM / PM", bg='royalblue4', fg='snow1', font=('helvetica', 25))
set_alarm_label_am_pm.grid(row=3, column=3)

alarm_on_button = Button(alarm_clock_frame, text='Alarm Off', font=('helvetica', 20), relief=RAISED, bd=4,
                         bg='Dodger Blue', fg='snow2', command=None)
alarm_on_button.grid(row=3, column=4)

set_alarm_type_label = Label(alarm_clock_frame, text="Set alarm type:", bg='royalblue4', fg='snow1',
                             font=('helvetica', 25))
set_alarm_type_label.grid(row=5, column=0, columnspan=2, sticky='W', pady=(25, 0))

set_alarm_type_label = Label(alarm_clock_frame, text="Set custom message (optional):", bg='royalblue4', fg='snow1',
                             font=('helvetica', 25))
set_alarm_type_label.grid(row=7, column=0, columnspan=2, sticky='W', pady=(25, 0))

mp3_selected_label = Label(alarm_clock_frame, text="No custom song selected", bg='royalblue4', fg='gray',
                           font=('helvetica', 25))
mp3_selected_label.grid(row=5, column=3, columnspan=4, pady=25)

# Combo boxes for alarms
selected_hour = StringVar()
hour_combobox = ttk.Combobox(alarm_clock_frame, textvariable=selected_hour, font=('helvetica', 50), width=3)
hour_combobox['values'] = ([str(num).zfill(2) for num in range(0, 13)])
hour_combobox['state'] = 'readonly'
hour_combobox.current(0)
hour_combobox.grid(row=4, column=0)

selected_min = StringVar()
min_combobox = ttk.Combobox(alarm_clock_frame, textvariable=selected_min, font=('helvetica', 50), width=3)
min_combobox['values'] = ([str(num).zfill(2) for num in range(0, 60)])
min_combobox['state'] = 'readonly'
min_combobox.current(0)
min_combobox.grid(row=4, column=1)

selected_sec = StringVar()
sec_combobox = ttk.Combobox(alarm_clock_frame, textvariable=selected_sec, font=('helvetica', 50), width=3)
sec_combobox['values'] = ([str(num).zfill(2) for num in range(0, 60)])
sec_combobox['state'] = 'readonly'
sec_combobox.current(0)
sec_combobox.grid(row=4, column=2)

selected_am_pm = StringVar()
am_pm_combobox = ttk.Combobox(alarm_clock_frame, textvariable=selected_am_pm, font=('helvetica', 50), width=3)
am_pm_combobox['values'] = ('AM', 'PM')
am_pm_combobox['state'] = 'readonly'
am_pm_combobox.current(0)
am_pm_combobox.grid(row=4, column=3)

selected_alarm_type = StringVar()
alarm_type_combobox = ttk.Combobox(alarm_clock_frame, textvariable=selected_alarm_type, font=('helvetica', 20),
                                   width=30)
alarm_type_combobox['values'] = (
    'default sound only', 'custom message only', 'custom .mp3 only', 'default sound and custom message',
    'custom .mp3 and custom message')
alarm_type_combobox['state'] = 'readonly'
alarm_type_combobox.current(0)
alarm_type_combobox.grid(row=6, column=0, columnspan=2, pady=10)

# Custom entry
alarm_clock_entry = Entry(alarm_clock_frame, font=('helvetica', 25), width=25, relief=RIDGE, bd=4, bg='Dodger Blue',
                          fg='snow2')
alarm_clock_entry.grid(row=8, column=0, columnspan=2)

# Buttons
alarm_on_button = Button(alarm_clock_frame, text='Alarm Off', width=15, font=('helvetica', 20), relief=RAISED, bd=4,
                         bg='Dodger Blue', fg='snow2', command=alarm_on_off_button)
alarm_on_button.grid(row=3, column=4)

select_mp3_button = Button(alarm_clock_frame, text='Select custom mp3', font=('helvetica', 20), relief=RAISED, bd=4,
                           bg='Dodger Blue', fg='snow2', command=custom_mp3_button)
select_mp3_button.grid(row=4, column=4)

alarm_stop_music_button = Button(alarm_clock_frame, text='Stop music', width=15, font=('helvetica', 20), relief=RAISED,
                                 bd=4, bg='Dodger Blue', fg='snow2', command=stop_music_button)
alarm_stop_music_button.grid(row=6, column=4)

### Distance Between Two Cities ###
distance_two_cities_title = Label(distance_two_cities_frame, text="Distance Between Two Cities", bg='royalblue4',
                                  fg='snow1', font=('helvetica', 50))
distance_two_cities_title.grid(row=0, column=0, sticky="nsew", padx=300, columnspan=6)

distance_two_cities_instructions = Label(distance_two_cities_frame,
                                         text="Ensure you are connected to the internet, then click submit once you have made your selection",
                                         bg='royalblue4', fg='snow1', font=('helvetica', 25))
distance_two_cities_instructions.grid(row=1, column=0, columnspan=6, pady=50)

distance_two_cities_from_label = Label(distance_two_cities_frame, text="From:", bg='royalblue4', fg='snow1',
                                       font=('helvetica', 25))
distance_two_cities_from_label.grid(row=2, column=0)

distance_two_cities_to_label = Label(distance_two_cities_frame, text="To:", bg='royalblue4', fg='snow1',
                                     font=('helvetica', 25))
distance_two_cities_to_label.grid(row=2, column=2)

distance_two_cities_in_label = Label(distance_two_cities_frame, text="In:", bg='royalblue4', fg='snow1',
                                     font=('helvetica', 25))
distance_two_cities_in_label.grid(row=2, column=4)

distance_two_cities_button = Button(distance_two_cities_frame, text='Submit', width=7, font=('helvetica', 20),
                                    relief=RAISED, bd=4, bg='Dodger Blue', fg='snow2',
                                    command=distance_two_cities_calculator)
distance_two_cities_button.grid(row=4, column=0, columnspan=7)

distance_two_cities_results = Label(distance_two_cities_frame, text="", bg='royalblue4', fg='snow1',
                                    font=('helvetica', 25))
distance_two_cities_results.grid(row=6, column=0, columnspan=7, pady=25)

distance_two_cities_internet_status = Label(distance_two_cities_frame, text="Connected to the internet",
                                            bg='royalblue4', fg='green', font=('helvetica', 25))
distance_two_cities_internet_status.grid(row=3, column=0, columnspan=7, pady=25)

distance_two_cities_refresh_button = Button(distance_two_cities_frame, text='Refresh', width=7, font=('helvetica', 20),
                                            relief=RAISED, bd=4, bg='Dodger Blue', fg='snow2',
                                            command=refresh_connection)
distance_two_cities_refresh_button.grid(row=5, pady=2, column=0, columnspan=7)

# Create a list of major cities and country from the following website: 'https://worldpopulationreview.com/world-cities'

cities_url = 'https://worldpopulationreview.com/world-cities'

try:
    requests_cities = requests.get(cities_url)

    soup_cities = bs4.BeautifulSoup(requests_cities.text, 'lxml')

    list_of_cities = [i.text for i in soup_cities.find_all('a', href=True) if i['href'] != ""]

    list_of_cities = list_of_cities[32:-104]

    list_of_cities = sorted(set(list_of_cities))

except requests.exceptions.ConnectionError:
    distance_two_cities_internet_status.config(text='No internet connection, Please try again', fg='red')

# Distance between two countries entry boxes
try:
    from_entry = AutocompleteCombobox(distance_two_cities_frame, font=('helvetica', 20), completevalues=list_of_cities)
    from_entry.grid(row=2, column=1, sticky='W')

    to_entry = AutocompleteCombobox(distance_two_cities_frame, font=('helvetica', 20), completevalues=list_of_cities)
    to_entry.grid(row=2, column=3, sticky='W')

    in_entry = AutocompleteCombobox(distance_two_cities_frame, font=('helvetica', 20),
                                    completevalues=['kilometers', 'miles'])
    in_entry.grid(row=2, column=5, sticky='W')

except NameError:
    distance_two_cities_internet_status.config(text='No internet connection, Please try again', fg='red')

### Credit Card validator ###
card_validator_title = Label(credit_card_validator_frame, text="Credit Card Validator", bg='royalblue4', fg='snow1',
                             font=('helvetica', 50))
card_validator_title.grid(row=0, column=0, sticky="nsew", padx=300, columnspan=6)

card_validator_instructions = Label(credit_card_validator_frame,
                                    text="Enter a credit card number between 13 and 16 digits and click submit",
                                    bg='royalblue4', fg='snow1', font=('helvetica', 25))
card_validator_instructions.grid(row=1, column=0, columnspan=6, pady=50)

card_validator_entry = Entry(credit_card_validator_frame, font=('helvetica', 25), width=25, relief=RIDGE, bd=4,
                             bg='Dodger Blue', fg='snow2')
card_validator_entry.grid(row=2, column=0, columnspan=6)

card_validator_button = Button(credit_card_validator_frame, text='Submit', width=7, font=('helvetica', 20),
                               relief=RAISED, bd=4, bg='Dodger Blue', fg='snow2', command=credit_card_validation)
card_validator_button.grid(row=3, column=0, columnspan=6, pady=2)

card_validator_results = Label(credit_card_validator_frame, text="", bg='royalblue4', fg='snow1',
                               font=('helvetica', 25))
card_validator_results.grid(row=4, column=0, columnspan=6, pady=20)

card_validator_further_instructions = Label(credit_card_validator_frame,
                                            text="This validator works using Luhn Algorithm (Mod10 Check)\n"
                                                 "Luhn algorithm consists of the following five steps:          \n"
                                                 "1) Double every second digit from right to left. If this “doubling” results in a two-digit number, add the two-digit number to get a single digit.\n"
                                                 "2) Now add all single digit numbers from step 1.                                                                                                                                          \n"
                                                 "3) Add all digits in the odd places from right to left in the credit card number.                                                                                               \n"
                                                 "4) Sum the results from steps 2 & 3.                                                                                                                                                             \n"
                                                 "5) If the result from step 4 is divisible by 10, the card number is valid; otherwise, it is invalid.                                                                         \n\n"
                                                 "Note:                                                                                           \n "
                                                 "-Numbers beginning with a 4 are a visa card                   \n"
                                                 "-Numbers beginning with a 5 are a Master card              \n"
                                                 "-Numbers beginning with a 7 are Discover cards             \n"
                                                 "-Numbers beginning with 37 are American Express cards",
                                            bg='royalblue4', fg='snow1', font=('helvetica', 18))
card_validator_further_instructions.grid(row=5, column=0, columnspan=6, sticky='W')

### INCOME TAX CALCULATOR ###
simple_tax_title = Label(tax_calculator_frame, text="Simple Tax Calculator", bg='royalblue4', fg='snow1',
                         font=('helvetica', 50))
simple_tax_title.grid(row=0, column=0, sticky="nsew", padx=450, columnspan=6)

simple_tax_instructions = Label(tax_calculator_frame,
                                text="Enter your total taxible income in dollars for the year and click submit",
                                bg='royalblue4',
                                fg='snow1', font=('helvetica', 25))
simple_tax_instructions.grid(row=1, column=0, columnspan=6, pady=50)

simple_tax_entry = Entry(tax_calculator_frame, font=('helvetica', 25), width=25, relief=RIDGE, bd=4, bg='Dodger Blue',
                         fg='snow2')
simple_tax_entry.grid(row=2, column=0, columnspan=6)

simple_tax_button = Button(tax_calculator_frame, text='Submit', width=7, font=('helvetica', 20), relief=RAISED, bd=4,
                           bg='Dodger Blue', fg='snow2', command=income_tax_calc)
simple_tax_button.grid(row=3, column=0, columnspan=6, pady=2)

simple_tax_results = Label(tax_calculator_frame, text="", bg='royalblue4', fg='snow1',
                           font=('helvetica', 25))
simple_tax_results.grid(row=4, column=0, columnspan=6, pady=20)

simple_tax_further_instructions = Label(tax_calculator_frame, text="Australian Resident tax rates 2021–22\n\n"
                                                                   "Taxable income                 Tax on this income\n"
                                                                   "------------------------------------------------------------------------------------------------\n"
                                                                   "0 – $18,200                       Nil\n"
                                                                   "$18,201 – $45,000            19 cents for each $1 over $18,200\n"
                                                                   "$45,001 – $120,000          $5,092 plus 32.5 cents for each $1 over $45,000\n"
                                                                   "$120,001 – $180,000        $29,467 plus 37 cents for each $1 over $120,000\n"
                                                                   "$180,001 and over            $51,667 plus 45 cents for each $1 over $180,000",
                                        bg='royalblue4', fg='snow1', font=('helvetica', 25),
                                        justify=LEFT, anchor="w")
simple_tax_further_instructions.grid(row=5, column=1, columnspan=6, sticky='W')

### Factorial Finder ###
factorial_finder_title = Label(factorial_finder_frame, text="Factorial Finder", bg='royalblue4', fg='snow1',
                               font=('helvetica', 50))
factorial_finder_title.grid(row=0, column=0, sticky="nsew", padx=525, columnspan=6)

factorial_finder_instructions = Label(factorial_finder_frame,
                                      text="Enter a number and click submit to find its factorial. limit is 50",
                                      bg='royalblue4', fg='snow1', font=('helvetica', 25))
factorial_finder_instructions.grid(row=1, column=0, columnspan=6, pady=50)

factorial_finder_entry = Entry(factorial_finder_frame, font=('helvetica', 25), width=25, relief=RIDGE, bd=4,
                               bg='Dodger Blue', fg='snow2')
factorial_finder_entry.grid(row=2, column=0, columnspan=6)

factorial_finder_button = Button(factorial_finder_frame, text='Submit', width=7, font=('helvetica', 20), relief=RAISED,
                                 bd=4, bg='Dodger Blue', fg='snow2', command=factorial_finder)
factorial_finder_button.grid(row=3, column=0, columnspan=6, pady=2)

factorial_finder_results = Label(factorial_finder_frame, text="", bg='royalblue4', fg='snow1', font=('helvetica', 25))
factorial_finder_results.grid(row=4, column=0, columnspan=6, pady=20)

### Prime Factorization ###
prime_factorization_title = Label(prime_factorization_frame, text="Prime Factorization", bg='royalblue4', fg='snow1',
                                  font=('helvetica', 50))
prime_factorization_title.grid(row=0, column=0, sticky="nsew", padx=525, columnspan=6)

prime_factorization_instructions = Label(prime_factorization_frame,
                                         text="Enter a number and click submit to find all its prime factors.",
                                         bg='royalblue4', fg='snow1', font=('helvetica', 25))
prime_factorization_instructions.grid(row=1, column=0, columnspan=6, pady=50)

prime_factorization_entry = Entry(prime_factorization_frame, font=('helvetica', 25), width=25, relief=RIDGE, bd=4,
                                  bg='Dodger Blue', fg='snow2')
prime_factorization_entry.grid(row=2, column=0, columnspan=6)

prime_factorization_button = Button(prime_factorization_frame, text='Submit', width=7, font=('helvetica', 20),
                                    relief=RAISED, bd=4, bg='Dodger Blue', fg='snow2', command=prime_factorizaton_func)
prime_factorization_button.grid(row=3, column=0, columnspan=6, pady=2)

prime_factorization_results = Label(prime_factorization_frame, text="", bg='royalblue4', fg='snow1',
                                    font=('helvetica', 25))
prime_factorization_results.grid(row=4, column=0, columnspan=6, pady=20)

# HAPPY NUMBERS #
happy_numbers_title = Label(happy_number_frame, text="Happy numbers", bg='royalblue4', fg='snow1',
                            font=('helvetica', 50))
happy_numbers_title.grid(row=0, column=0, sticky="nsew", padx=525, columnspan=6)

happy_numbers_instructions = Label(happy_number_frame,
                                   text="A happy number is a number which eventually reaches 1 when replaced by\n"
                                        " the sum of the square of each digit.                                                               \n"
                                        "Enter a number and click submit to see if it is a happy or a sad number.      ",
                                   bg='royalblue4', fg='snow1', font=('helvetica', 25))
happy_numbers_instructions.grid(row=1, column=0, columnspan=6, pady=50)

happy_numbers_entry = Entry(happy_number_frame, font=('helvetica', 25), width=25, relief=RIDGE, bd=4, bg='Dodger Blue',
                            fg='snow2')
happy_numbers_entry.grid(row=2, column=0, columnspan=6)

happy_numbers_button = Button(happy_number_frame, text='Submit', width=7, font=('helvetica', 20), relief=RAISED, bd=4,
                              bg='Dodger Blue', fg='snow2', command=happy_number_submit)
happy_numbers_button.grid(row=3, column=0, columnspan=6, pady=2)

happy_numbers_results = Label(happy_number_frame, text="", bg='royalblue4', fg='snow1', font=('helvetica', 25))
happy_numbers_results.grid(row=4, column=0, columnspan=6, pady=20)

### NUMBER NAMES ###
number_name_title = Label(number_name_frame, text="Number names", bg='royalblue4', fg='snow1', font=('helvetica', 50))
number_name_title.grid(row=0, column=0, sticky="nsew", padx=525, columnspan=6)

number_name_instructions = Label(number_name_frame,
                                 text="Enter a positive number in digit form and the program will return the number in written english.",
                                 bg='royalblue4', fg='snow1', font=('helvetica', 25))
number_name_instructions.grid(row=1, column=0, columnspan=6, pady=50)

number_name_entry = Entry(number_name_frame, font=('helvetica', 25), width=25, relief=RIDGE, bd=4, bg='Dodger Blue',
                          fg='snow2')
number_name_entry.grid(row=2, column=0, columnspan=6)

number_name_button = Button(number_name_frame, text='Submit', width=7, font=('helvetica', 20), relief=RAISED, bd=4,
                            bg='Dodger Blue', fg='snow2', command=number_name_submit)
number_name_button.grid(row=3, column=0, columnspan=5, pady=2)

number_name_speech_button = Button(number_name_frame, text='Read', width=7, font=('helvetica', 20), relief=RAISED, bd=4,
                                   bg='Dodger Blue', fg='snow2',
                                   command=lambda: threading.Thread(target=text_to_speech, daemon=True).start())
number_name_speech_button.grid(row=3, column=1, columnspan=6, pady=2)

number_name_results = Label(number_name_frame, text="", bg='royalblue4', fg='snow1', font=('helvetica', 25),
                            wraplength=1500, justify=CENTER)
number_name_results.grid(row=4, column=0, columnspan=6, pady=20)

### COIN FLIP SIMULATION ###
coin_flip_title = Label(coin_flip_frame, text="Coin Flip Simulator", bg='royalblue4', fg='snow1',
                        font=('helvetica', 50))
coin_flip_title.grid(row=0, column=0, sticky="nsew", padx=500, columnspan=6)

coin_flip_instructions = Label(coin_flip_frame,
                               text="Enter a postive number from 1-1000 to represent the number of coin flips you would like to simulate",
                               bg='royalblue4', fg='snow1', font=('helvetica', 25))
coin_flip_instructions.grid(row=1, column=0, columnspan=6, pady=50)

coin_flip_entry = Entry(coin_flip_frame, font=('helvetica', 25), width=25, relief=RIDGE, bd=4, bg='Dodger Blue',
                        fg='snow2')
coin_flip_entry.grid(row=2, column=0, columnspan=6)

coin_flip_button = Button(coin_flip_frame, text='Submit', width=7, font=('helvetica', 20), relief=RAISED, bd=4,
                          bg='Dodger Blue', fg='snow2', command=coin_flip_submit)
coin_flip_button.grid(row=3, column=0, columnspan=6, pady=2)

coin_flip_head_count = Label(coin_flip_frame, text="HEAD COUNT: 0", justify=LEFT, bg='royalblue4', fg='snow1',
                             font=('helvetica', 25))
coin_flip_head_count.grid(row=4, column=1, columnspan=6, pady=25, sticky='W')

coin_flip_head_percent = Label(coin_flip_frame, text="HEAD PERCENT: 0%", justify=LEFT, bg='royalblue4', fg='snow1',
                               font=('helvetica', 25))
coin_flip_head_percent.grid(row=5, column=1, columnspan=6, pady=25, sticky='W')

coin_flip_tail_count = Label(coin_flip_frame, text="TAIL COUNT: 0", justify=LEFT, bg='royalblue4', fg='snow1',
                             font=('helvetica', 25))
coin_flip_tail_count.grid(row=6, column=1, columnspan=6, pady=25, sticky='W')

coin_flip_tail_percent = Label(coin_flip_frame, text="TAIL PERCENT: 0%", justify=LEFT, bg='royalblue4', fg='snow1',
                               font=('helvetica', 25))
coin_flip_tail_percent.grid(row=7, column=1, columnspan=6, pady=25, sticky='W')

coin_flip_text_box = scrolledtext.ScrolledText(coin_flip_frame, bg='royalblue4', fg='snow1', font=('helvetica', 15),
                                               height=15, wrap=WORD)
coin_flip_text_box.grid(row=4, column=5, columnspan=1, rowspan=10, pady=25, sticky='W')

### Exponentiation ###
exponentiation_title = Label(exponentiation_frame, text="Exponentiation", bg='royalblue4', fg='snow1',
                             font=('helvetica', 50))
exponentiation_title.grid(row=0, column=0, sticky="nsew", padx=500, columnspan=6)

exponentiation_instructions = Label(exponentiation_frame,
                                    text="Enter x to the power of y in the entry boxes and click submit to get the result.",
                                    bg='royalblue4', fg='snow1', font=('helvetica', 25))
exponentiation_instructions.grid(row=1, column=0, columnspan=6, pady=50)

exponentiation_x_entry = Entry(exponentiation_frame, font=('helvetica', 25), width=15, relief=RIDGE, bd=4,
                               bg='Dodger Blue', fg='snow2')
exponentiation_x_entry.grid(row=2, column=1, columnspan=6, sticky='W')

exponentiation_to_the_power_of_label = Label(exponentiation_frame, text="to the power of", bg='royalblue4',
                                             fg='snow1', font=('helvetica', 25))
exponentiation_to_the_power_of_label.grid(row=2, column=0, columnspan=6, pady=25)

exponentiation_y_entry = Entry(exponentiation_frame, font=('helvetica', 25), width=15, relief=RIDGE, bd=4,
                               bg='Dodger Blue', fg='snow2')
exponentiation_y_entry.grid(row=2, column=4, columnspan=6, sticky='W')

exponentiation_button = Button(exponentiation_frame, text='Submit', width=7, font=('helvetica', 20), relief=RAISED,
                               bd=4, bg='Dodger Blue', fg='snow2', command=exponentiation_submit)
exponentiation_button.grid(row=3, column=0, columnspan=6, pady=2)

exponentiation_results = Label(exponentiation_frame, text="", bg='royalblue4', fg='snow1', font=('helvetica', 25),
                               wraplength=1000, justify="center")
exponentiation_results.grid(row=4, column=0, columnspan=6, pady=50)

window.config(menu=menubar)

show_frame(welcome_screen_frame)

clock_time()

window.mainloop()
