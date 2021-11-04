# Tkinter math Capstone project
# This will be a GUI program that showcases almost almost all the math projects located in the udemy course
# Each project will be separated by a tab

# The programs are as follows:

# Find Pi to the nth digit [complete]
# Find E to the nth digit  [complete]
# Fibonacci sequence [complete]
# Prime Factorization [complete]
# Prime number generator [complete]
# Find the cost to cover W x H floor [complete]
# Mortgage calculator [complete]
# Change return program [complete]
# Binary to Decimal and Back Converter [complete]
# Scientific Calculator [complete]
# Unit Converter [complete]
# Alarm Clock [complete]
# Distance Between Two Cities [complete]
# Credit Card Validator [complete]

# Tax Calculator [incomplete] - Center instructions properly, perhaps split instructions up line by line

# Factorial Finder [incomplete] - add scroll bar to results
# Happy Numbers [incomplete] - add calculations to a scroll bar , add focus if needed

# Number Names [complete]
# Coin Flip Simulation [complete]

# Exponentiation [incomplete] - add scrollable text box and increase limit

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
import numpy # this import is used exclusively for the cube root function of the scientific calculator
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
prime_number_generator_frame = Frame(window, bg='royalblue4')
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
              prime_number_generator_frame,
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
    elif frame_parameter == prime_factorization_frame:
        prime_factorization_entry.focus()
    elif frame_parameter == prime_number_generator_frame:
        prime_number_generator_entry.focus()
    elif frame_parameter == w_x_h_floor_frame:
        w_x_h_floor_cost_label.focus()
    elif frame_parameter == morgage_calculator_frame:
        morgage_calculator_total_entry.focus()
    elif frame_parameter == change_return_frame:
        change_return_item_cost_entry.focus()
    elif frame_parameter == binary_to_decimal_frame:
        binary_to_decimal_entry.focus()
    elif frame_parameter == unit_converter_frame:
        unit_converter_left_entry.focus()
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
select_program.add_command(label='Prime Number Generator', command=lambda: show_frame(prime_number_generator_frame))
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


### GLOBAL COMBOBOX THEME CONFIGURATION ###
# Combobox theme creation
style = ttk.Style()
style.theme_use('alt')

# the following alters the Listbox
window.option_add('*TCombobox*Listbox*Background', 'Dodger Blue')
window.option_add('*TCombobox*Listbox*Foreground', 'snow1')
window.option_add('*TCombobox*Listbox*selectBackground', 'snow1')
window.option_add('*TCombobox*Listbox*selectForeground', 'royalblue4')
window.option_add("*TCombobox*Listbox*Font", ('helvetica', 25))

# the following alters the Combobox entry field
style.map('TCombobox', fieldbackground=[('readonly', 'Dodger Blue')])
style.map('TCombobox', selectbackground=[('readonly', 'Dodger Blue')])
style.map('TCombobox', selectforeground=[('readonly', 'snow1')])
style.map('TCombobox', background=[('readonly', 'Dodger Blue')])
style.map('TCombobox', foreground=[('readonly', 'snow1')])
style.map('TCombobox', relief=[('readonly', RIDGE)])
style.configure('TCombobox', arrowsize=30)
style.configure('Vertical.TScrollbar', arrowsize=28)
### END OF GLOBAL COMBOBOX THEME CONFIGURATION ###


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

### PI TO THE NTH DIGIT FUNCTION ###
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
### END OF PI TO THE NTH DIGIT FUNCTION ###


### E TO THE NTH DIGIT FUNCTION ###
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
### END OF E TO THE NTH DIGIT FUNCTION ###


### FIBONACCI SEQUENCE FUNCTION ###
def fibonacci_sequence_submit():
    num_1 = 0
    num_2 = 1
    fib_seq = []

    try:
        fibonacci_sequence_results.delete('1.0', END)

        if 0 < int(fibonacci_sequence_entry.get()) <= 10000:

            digits = int(fibonacci_sequence_entry.get())

            for digit in range(int(digits)):
                fib_seq.append(str(num_1))
                next_fib = num_1 + num_2
                num_1 = num_2
                num_2 = next_fib

            fib_text = ',\n'.join(fib_seq)

            fibonacci_sequence_results.insert(END, f'The first {fibonacci_sequence_entry.get()} numbers in the fibonacci sequence are:\n\n{fib_text}')

        else:
            fibonacci_sequence_results.insert('Please enter a valid number between 1-10,000')
            fibonacci_sequence_entry.delete(0, END)

    except ValueError:
        fibonacci_sequence_results.insert('Please enter a valid number between 1-10,000')
        fibonacci_sequence_entry.delete(0, END)
### END OF FIBONACCI SEQUENCE FUNCTION ###


### PRIME FACTORIZATION FUNCTION ###
def prime_factorizaton_func():

    try:
        prime_factorization_results.delete('1.0', END)

        if 0 < int(prime_factorization_entry.get()) <= 1000000:

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
                prime_factorization_results.insert(END, f"{user_num} is a prime number. ")

            elif len(prime_list) != 0:
                new_prime_list = ",\n".join(prime_list)
                prime_factorization_results.insert(END, f"The Prime Factorization of {user_num} is:\n\n{new_prime_list}")

            else:
                prime_factorization_results.insert(END, 'Please enter a valid number between 1-1,000,000')
                prime_factorization_entry.delete(0, END)
        else:
            prime_factorization_results.insert(END, 'Please enter a valid number between 1-1,000,000')
            prime_factorization_entry.delete(0, END)

    except ValueError:
        prime_factorization_results.insert(END, 'Please enter a valid number between 1-1,000,000')
        prime_factorization_entry.delete(0, END)
### END OF PRIME FACTORIZATION FUNCTION ###


### PRIME NUMBER GENERATOR FUNCTION ###
def prime_generator_submit():
    try:
        prime_number_generator_results.delete('1.0', END)

        if 0 < int(prime_number_generator_entry.get()) <= 1000:

            number_of_primes_found = 0
            current_number_to_check = 1
            prime_list = []

            while number_of_primes_found < int(prime_number_generator_entry.get()):
                current_number_to_check += 1
                more_than_two_factors = False

                for num in range(2, current_number_to_check):
                    if (current_number_to_check % num) == 0:
                        more_than_two_factors = True

                if not more_than_two_factors:
                    number_of_primes_found += 1
                    prime_list.append(str(current_number_to_check))

            prime_text = ',\n'.join(prime_list)
            prime_number_generator_results.insert(END, f'The first {int(prime_number_generator_entry.get())} prime numbers are:\n\n{prime_text}')

        else:
            prime_number_generator_results.insert(END, 'Please enter a valid number between 1-1000')
            prime_number_generator_entry.delete(0, END)

    except ValueError:
        prime_number_generator_results.insert(END, 'Please enter a valid number between 1-1000')
        prime_number_generator_entry.delete(0, END)
### END OF PRIME NUMBER GENERATOR FUNCTION ###


### COST TO COVER W X H FLOOR FUNCTION ###
def w_x_h_floor_button():
    try:
        w_x_h_floor_results.delete('1.0', END)

        tile_cost = float(w_x_h_floor_cost_entry.get())
        tile_height = int(w_x_h_floor_height_entry.get())
        tile_width = int(w_x_h_floor_width_entry.get())

        total_cost = tile_cost * tile_height * tile_width

        w_x_h_floor_results.insert(END, f'Total cost to tile the floor is:\n${"{0:.2f}".format(total_cost)}')

    except ValueError:
        w_x_h_floor_results.insert(END, f'Please enter valid values')
### END OF COST TO COVER W X H FLOOR FUNCTION ###


### MORGAGE CALCULATOR FUNCTION ###
def morgage_calculator_button():
    try:
        morgage_calculator_results.delete('1.0', END)

        total = float(morgage_calculator_total_entry.get())
        interest = float(morgage_calculator_interest_rate_entry.get())
        years = float(morgage_calculator_year_of_loan_entry.get())

        interest = interest / 100
        monthly_interest = interest / 12
        months = years * 12

        if float(morgage_calculator_total_entry.get()) < 0:
            morgage_calculator_results.insert(END, 'Morgage total needs to be larger than 0.')

        elif float(morgage_calculator_interest_rate_entry.get()) < 0:
            morgage_calculator_results.insert(END, 'Interest rate needs to be larger than 0.')

        elif float(morgage_calculator_year_of_loan_entry.get()) < 0:
            morgage_calculator_results.insert(END, 'Total months of loan needs to be larger than 0.')

        else:
            monthly_amount = float("{0:.2f}".format(total * (monthly_interest * ((1 + monthly_interest) ** months)) / ((1 + monthly_interest) ** months - 1)))

            if morgage_calculator_combobox.get() == 'Monthly':
                morgage_calculator_results.insert(END, f'Your morgage repayment are:\n ${monthly_amount} per month, for {int(months)} months')

            elif morgage_calculator_combobox.get() == 'Fortnightly':
                morgage_calculator_results.insert(END, f'Your morgage repayment are:\n ${monthly_amount / 2} per fortnight, for {int(months * 2)} fortnights')

            else:
                morgage_calculator_results.insert(END, f'Your morgage repayment are:\n ${monthly_amount / 4} per week, for {int(months * 4)} weeks')

    except ValueError:
        morgage_calculator_results.insert(END, 'Please enter valid numbers into fields.')
### END OF MORGAGE CALCULATOR FUNCTION ###


### CHANGE RETURN FUNCTION ###
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

        fifty_dollar_result.config(text=f'{fifty_dollars}')
        twenty_dollar_result.config(text=f'{twenty_dollars}')
        ten_dollar_result.config(text=f'{ten_dollars}')
        five_cent_result.config(text=f'{five_dollars}')
        two_dollar_result.config(text=f'{two_dollars}')
        one_dollar_result.config(text=f'{one_dollars}')
        fifty_cent_result.config(text=f'{fifty_cents}')
        twenty_cent_result.config(text=f'{twenty_cents}')
        ten_cent_result.config(text=f'{ten_cents}')
        five_cent_result.config(text=f'{five_cents}')

    except ValueError:
        change_return_change_owed_label.config(text='Please enter valid numbers into fields.')

    except decimal.InvalidOperation:
        change_return_change_owed_label.config(text='Please enter valid numbers into fields.')
### END OF CHANGE RETURN FUNCTION ###


### BINARY TO DECIMAL CONVERTER FUNCTION ###
def binary_to_decimal_submit():
    try:
        binary_to_decimal_results.delete('1.0', END)

        if binary_combobox.get() == 'Decimal to Binary':
            bin_dec_value = int(binary_to_decimal_entry.get())
            binary_to_decimal_results.insert(END, f'The binary value of {bin_dec_value} is:\n\n{bin(bin_dec_value)}')

        elif binary_combobox.get() == 'Binary to Decimal':
            bin_dec_value = binary_to_decimal_entry.get()
            binary_to_decimal_results.insert(END, f'The numerical value of {bin_dec_value} is:\n\n{int(bin_dec_value, 2)}')

    except ValueError:
        binary_to_decimal_results.insert(END, 'Please enter a valid value.')
### END OF BINARY TO DECIMAL CONVERTER FUNCTION ###


### SCIENTIFIC CALCULATOR BUTTON FUNCTIONS ###
calculator_string = ''

# Returns an int if the answer ends in .0
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
    global calculator_string, ans_string, numpy
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
### END OF SCIENTIFIC CALCULATOR BUTTON FUNCTIONS ###


### UNIT CONVERTER FUNCTION ###
# Top Combobox Function
def unit_converter_top_combobox(*args):
    if top_combobox.get() == "Area":
        left_combobox['values'] = ('Square kilometer', 'Square meter', 'Square mile', 'Square yard', 'Square foot', 'Square inch', 'Hectare', 'Acre')
        right_combobox['values'] = ('Square kilometer', 'Square meter', 'Square mile', 'Square yard', 'Square foot', 'Square inch', 'Hectare', 'Acre')

    elif top_combobox.get() == "Energy":
        left_combobox['values'] = ('Joule', 'Kilojoule', 'Watt hour', 'kilowatt hour')
        right_combobox['values'] = ('Joule', 'Kilojoule', 'Watt hour', 'kilowatt hour')

    elif top_combobox.get() == "Frequency":
        left_combobox['values'] = ('Hertz', 'Kilohertz', 'Megahertz', 'Gigahertz')
        right_combobox['values'] = ('Hertz', 'Kilohertz', 'Megahertz', 'Gigahertz')

    elif top_combobox.get() == "Length":
        left_combobox['values'] = ('kilometer', 'Meter', 'Centimeter', 'Millimeter', 'Mile', 'Yard', 'Foot', 'Inch', 'Nautical mile')
        right_combobox['values'] = ('kilometer', 'Meter', 'Centimeter', 'Millimeter', 'Mile', 'Yard', 'Foot', 'Inch', 'Nautical mile')

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
            'Nanosecond', 'Microsecond', 'Millisecond', 'Second', 'Minute', 'Hour', 'Day', 'Week', 'Month', 'Year', 'Decade', 'Century')
        right_combobox['values'] = ('Nanosecond', 'Microsecond', 'Millisecond', 'Second', 'Minute', 'Hour', 'Day', 'Week', 'Month', 'Year', 'Decade', 'Century')

    elif top_combobox.get() == "Volume":
        left_combobox['values'] = ('Liter', 'Milliliter', 'Cubic Meter', 'Imperial tablespoon', 'Imperial teaspoon')
        right_combobox['values'] = ('Liter', 'Milliliter', 'Cubic Meter', 'Imperial tablespoon', 'Imperial teaspoon')

    left_combobox.current(0)
    right_combobox.current(0)
    unit_converter_right_entry.delete(0, END)
    unit_converter_left_entry.delete(0, END)
    unit_converter_left_entry.focus()


# Unit converter Refresh button
def unit_converter_refresh():
    try:
        from_units = left_combobox.get()
        to_units = right_combobox.get()
        from_unit_amount = unit_converter_left_entry.get()

        unit_url = f'https://www.google.com/search?q=from+{from_unit_amount}+{from_units}+to+{to_units}&sxsrf=AOaemvIa19K04JwWp9NZYCFCo4KXaZqjFA%3A1635719557396&ei=hRl_YaPXF9ma4-EPsv2IwAE&oq=from+meters+to+kilometers&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEIAEMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeOgcILhBDEJMCOgUIABCRAjoECAAQQzoOCC4QgAQQsQMQxwEQowI6BQguEIAEOggIABCABBCxAzoLCC4QgAQQxwEQ0QM6CAguEIAEELEDOgkIABBDEEYQggI6CAguEIAEEJMCSgQIQRgAUJDa1QJYgZTWAmDamNYCaABwAXgBgAHKAogBsSSSAQgwLjIyLjIuMZgBAKABAcABAQ&sclient=gws-wiz&ved=0ahUKEwjjra6Z2vXzAhVZzTgGHbI-AhgQ4dUDCA4&uact=5'

        requests_conversion = requests.get(unit_url)

        soup_distance = bs4.BeautifulSoup(requests_conversion.text, "lxml")

        unit_conversion = soup_distance.find('div', {'class': "BNeawe iBp4i AP7Wnd"}).text

        print(unit_conversion)

        unit_converter_internet_label.config(text="Connected to the internet", fg='green')

    except requests.exceptions.ConnectionError:
        unit_converter_internet_label.config(text='No internet connection, Please try again', fg='red')


# Unit convertor submit button
def unit_converter_submit():
    try:
        unit_converter_right_entry.delete(0, END)

        from_units = left_combobox.get()
        to_units = right_combobox.get()
        from_unit_amount = unit_converter_left_entry.get()

        if from_units == to_units:
            unit_converter_right_entry.insert(0, unit_converter_left_entry.get())

        else:
            unit_url = f'https://www.google.com/search?q=from+{from_unit_amount}+{from_units}+to+{to_units}&sxsrf=AOaemvIa19K04JwWp9NZYCFCo4KXaZqjFA%3A1635719557396&ei=hRl_YaPXF9ma4-EPsv2IwAE&oq=from+meters+to+kilometers&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEIAEMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeOgcILhBDEJMCOgUIABCRAjoECAAQQzoOCC4QgAQQsQMQxwEQowI6BQguEIAEOggIABCABBCxAzoLCC4QgAQQxwEQ0QM6CAguEIAEELEDOgkIABBDEEYQggI6CAguEIAEEJMCSgQIQRgAUJDa1QJYgZTWAmDamNYCaABwAXgBgAHKAogBsSSSAQgwLjIyLjIuMZgBAKABAcABAQ&sclient=gws-wiz&ved=0ahUKEwjjra6Z2vXzAhVZzTgGHbI-AhgQ4dUDCA4&uact=5'

            requests_conversion = requests.get(unit_url)

            soup_distance = bs4.BeautifulSoup(requests_conversion.text, "lxml")

            unit_conversion = soup_distance.find('div', {'class': "BNeawe iBp4i AP7Wnd"}).text

            unit_converter_right_entry.insert(0, unit_conversion)

    except requests.exceptions.ConnectionError:
        unit_converter_internet_label.config(text='No internet connection, Please try again', fg='red')
### END OF UNIT CONVERTER FUNCTION ###


### ALARM CLOCK FUNCTION ###
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
                msg_box = messagebox.askokcancel("Custom Alarm Message", alarm_clock_entry.get())
                if msg_box in ['OK', 'Cancel']:
                    stop_music_button()

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
                    msg_box = messagebox.askokcancel("Custom Alarm Message", alarm_clock_entry.get())

                except pygame.error:
                    winsound.PlaySound("Music.wav", winsound.SND_ASYNC)
                    msg_box = messagebox.askokcancel("Custom Alarm Message", alarm_clock_entry.get())

                if msg_box:
                    stop_music_button()
                elif not msg_box:
                    stop_music_button()

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

    mp3_selected_entry.delete(0, END)

    filename = filedialog.askopenfilename(initialdir="C:/Users", title=f"Select .mp3 file", filetypes=(("mp3 files", "*.mp3*"), ("all files", "*.*")))

    if filename == '':
        mp3_selected_entry.insert(END, 'No custom song selected')

    else:
        file_only = os.path.basename(filename)
        mp3_selected_entry.delete(0, END)
        mp3_selected_entry.insert(END, file_only)
        pygame.mixer.music.load(filename)


def stop_music_button():
    pygame.mixer.music.stop()
### END OF ALARM CLOCK FUNCTION ###


### DISTANCE TWO CITIES ###
def refresh_connection():
    global requests_cities, soup_cities, list_of_cities, from_entry, to_entry, in_entry, distance_two_cities_internet_status

    try:
        requests_cities = requests.get(cities_url)

        soup_cities = bs4.BeautifulSoup(requests_cities.text, 'lxml')

        list_of_cities = [i.text for i in soup_cities.find_all('a', href=True) if i['href'] != ""]

        list_of_cities = list_of_cities[32:-104]

        list_of_cities = sorted(set(list_of_cities))

        # From Entry
        from_entry = AutocompleteCombobox(distance_two_cities_frame, font=('helvetica', 20), completevalues=list_of_cities)
        from_entry.grid(row=2, sticky='W', padx=(150, 0))

        # To Entry
        to_entry = AutocompleteCombobox(distance_two_cities_frame, font=('helvetica', 20), completevalues=list_of_cities)
        to_entry.grid(row=2)

        # In Entry
        in_entry = AutocompleteCombobox(distance_two_cities_frame, font=('helvetica', 20), completevalues=['kilometers', 'miles'])
        in_entry.grid(row=2, sticky='E', padx=(0, 150))

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
### END OF DISTANCE TWO CITIES ###


### CREDIT CARD VALIDATOR ###
def credit_card_validation():

    if card_validator_combobox.get() == 'Visa card example':
        card_validator_entry.delete(0, END)
        card_validator_entry.insert(END, '4111111111111111')
        card_validator_results.config(text='Valid Visa card number', fg='green')

    elif card_validator_combobox.get() == 'Master card example':
        card_validator_entry.delete(0, END)
        card_validator_entry.insert(END, '5555555555554444')
        card_validator_results.config(text='Valid Master card number', fg='green')

    elif card_validator_combobox.get() == 'Discover card example':
        card_validator_entry.delete(0, END)
        card_validator_entry.insert(END, '6011111111111117')
        card_validator_results.config(text='Valid Discover card number', fg='green')

    elif card_validator_combobox.get() == 'American Express card example':
        card_validator_entry.delete(0, END)
        card_validator_entry.insert(END, '371449635398431')
        card_validator_results.config(text='Valid American Express card number', fg='green')

    elif card_validator_combobox.get() == 'Custom':
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
### END OF CREDIT CARD VALIDATOR ###


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
        if len(group_of_three) == 3 and group_of_three[0] == '0' and group_of_three[1] == '0' and group_of_three[2] == '0':
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


### WIDGET CONFIGURATION FOR EACH FRAME ###


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
e_to_nth_digit_label.grid(row=0)

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


### FIBONACHI SEQUENCE TKINTER CONFIG ###
# Frame config
fibonacci_sequence_frame.columnconfigure(0, weight=1)

# Title label
fibonacci_sequence_label = Label(fibonacci_sequence_frame, text="Fibonacci Sequence", bg='royalblue4', fg='snow1',font=('helvetica', 50))
fibonacci_sequence_label.grid(row=0)

# Instructions label
fibonacci_sequence_instructions = Label(fibonacci_sequence_frame, text="Enter the number of fibonacci numbers to generate. Limit is 10,000 numbers.", bg='royalblue4', fg='snow1', font=('helvetica', 20), pady=50)
fibonacci_sequence_instructions.grid(row=1)

# Entry box
fibonacci_sequence_entry = Entry(fibonacci_sequence_frame, font=('helvetica', 25), width=25, relief=RIDGE, bd=4, bg='Dodger Blue', fg='snow2')
fibonacci_sequence_entry.grid(row=2)

# Submit button
fibonacci_sequence_submit_button = Button(fibonacci_sequence_frame, text='Submit', font=('helvetica', 20), relief=RAISED, bd=4, bg='Dodger Blue', fg='snow2', command=fibonacci_sequence_submit)
fibonacci_sequence_submit_button.grid(row=3, pady=2)

# Scrolled results box
fibonacci_sequence_results = scrolledtext.ScrolledText(fibonacci_sequence_frame, bg='royalblue4', fg='snow1', font=('helvetica', 20), height=12, wrap=WORD)
fibonacci_sequence_results.grid(row=4, pady=2)
### END OF FIBONACHI SEQUENCE TKINTER CONFIG ###


### PRIME FACTORIZATION TKINTER CONFIG ###
# Frame config
prime_factorization_frame.columnconfigure(0, weight=1)

# Title label
prime_factorization_title = Label(prime_factorization_frame, text="Prime Factorization", bg='royalblue4', fg='snow1', font=('helvetica', 50))
prime_factorization_title.grid(row=0)

# Instructions Label
prime_factorization_instructions = Label(prime_factorization_frame, text="Enter a number to find all its prime factors. Limit is 1,000,000.", bg='royalblue4', fg='snow1', font=('helvetica', 20), pady=50)
prime_factorization_instructions.grid(row=1)

# Entry box
prime_factorization_entry = Entry(prime_factorization_frame, font=('helvetica', 25), width=25, relief=RIDGE, bd=4, bg='Dodger Blue', fg='snow2')
prime_factorization_entry.grid(row=2)

# Submit button
prime_factorization_button = Button(prime_factorization_frame, text='Submit', font=('helvetica', 20), relief=RAISED, bd=4, bg='Dodger Blue', fg='snow2', command=prime_factorizaton_func)
prime_factorization_button.grid(row=3, pady=2)

# Scrolled results box
prime_factorization_results = scrolledtext.ScrolledText(prime_factorization_frame, bg='royalblue4', fg='snow1', font=('helvetica', 20), height=12, wrap=WORD)
prime_factorization_results.grid(row=4, pady=2)
### END OF PRIME FACTORIZATION TKINTER CONFIG ###


### PRIME NUMBER GENERATOR TKINTER CONFIG ###
# Frame config
prime_number_generator_frame.columnconfigure(0, weight=1)

# Title label
prime_number_generator_label = Label(prime_number_generator_frame, text="Prime Number generator", bg='royalblue4', fg='snow1', font=('helvetica', 50))
prime_number_generator_label.grid(row=0)

# Instructions Label
prime_number_generator_instructions = Label(prime_number_generator_frame, text="Enter a number to generate that many prime numbers. Limit is 1000 numbers.", bg='royalblue4', fg='snow1', font=('helvetica', 20), pady=50)
prime_number_generator_instructions.grid(row=1)

# Entry box
prime_number_generator_entry = Entry(prime_number_generator_frame, font=('helvetica', 25), width=25, relief=RIDGE, bd=4, bg='Dodger Blue', fg='snow2')
prime_number_generator_entry.grid(row=2)

# Submit button
prime_number_generator_submit = Button(prime_number_generator_frame, text='Submit', font=('helvetica', 20), relief=RAISED, bd=4, bg='Dodger Blue', fg='snow2', command=prime_generator_submit)
prime_number_generator_submit.grid(row=3, pady=2)

# Scrolled results box
prime_number_generator_results = scrolledtext.ScrolledText(prime_number_generator_frame, bg='royalblue4', fg='snow1', font=('helvetica', 20), height=12, wrap=WORD)
prime_number_generator_results.grid(row=4, pady=2)
### END OF PRIME NUMBER GENERATOR TKINTER CONFIG ###


### COST TO COVER W X H FLOOR TKINTER CONFIG###
# Frame config
w_x_h_floor_frame.columnconfigure(0, weight=1)

# Title label
w_x_h_floor_title = Label(w_x_h_floor_frame, text="Tile cost calculator", bg='royalblue4', fg='snow1', font=('helvetica', 50))
w_x_h_floor_title.grid(row=0)

# Instructions Label
w_x_h_floor_instructions = Label(w_x_h_floor_frame, text='Enter cost per tile, width and height to calculate the total cost.', bg='royalblue4', fg='snow1', font=('helvetica', 20), pady=50)
w_x_h_floor_instructions.grid(row=1)

# Cost Label
w_x_h_floor_cost_label = Label(w_x_h_floor_frame, text='Enter cost per tile $:', bg='royalblue4', fg='snow1', font=('helvetica', 20))
w_x_h_floor_cost_label.grid(row=2, sticky='w', padx=533)

# Cost Entry
w_x_h_floor_cost_entry = Entry(w_x_h_floor_frame, font=('helvetica', 25), relief=RIDGE, bd=4, bg='Dodger Blue', fg='snow2', width=25)
w_x_h_floor_cost_entry.grid(row=3)

# Width Label
w_x_h_floor_width_label = Label(w_x_h_floor_frame, text='Enter number of tiles for width:  ', bg='royalblue4', fg='snow1', font=('helvetica', 20))
w_x_h_floor_width_label.grid(row=4, sticky='w', padx=533)

# Width Entry
w_x_h_floor_width_entry = Entry(w_x_h_floor_frame, font=('helvetica', 25), relief=RIDGE, bd=4, bg='Dodger Blue', fg='snow2', width=25)
w_x_h_floor_width_entry.grid(row=5)

# Height Label
w_x_h_floor_height_label = Label(w_x_h_floor_frame, text='Enter number of tiles for height: ', bg='royalblue4', fg='snow1', font=('helvetica', 20))
w_x_h_floor_height_label.grid(row=6, sticky='w', padx=533)

# Height Entry
w_x_h_floor_height_entry = Entry(w_x_h_floor_frame, font=('helvetica', 25), relief=RIDGE, bd=4, bg='Dodger Blue', fg='snow2', width=25)
w_x_h_floor_height_entry.grid(row=7)

# Submit Button
w_x_h_floor_submit = Button(w_x_h_floor_frame, text='Submit', font=('helvetica', 20), relief=RAISED, bd=4, bg='Dodger Blue', fg='snow2', command=w_x_h_floor_button)
w_x_h_floor_submit.grid(row=8, pady=2)

# Scrolled results box
w_x_h_floor_results = scrolledtext.ScrolledText(w_x_h_floor_frame, bg='royalblue4', fg='snow1', font=('helvetica', 20), height=5, wrap=WORD)
w_x_h_floor_results.grid(row=9, pady=2)
### END OF COST TO COVER W X H FLOOR TKINTER CONFIG###


### MORGAGE CALCULATOR TKINTER CONFIG ###
# Frame config
morgage_calculator_frame.columnconfigure(0, weight=1)

# Title label
morgage_calculator_title = Label(morgage_calculator_frame, text="Morgage Calculator", bg='royalblue4', fg='snow1', font=('helvetica', 50))
morgage_calculator_title.grid(row=0)

# Instructions Label
morgage_calculator_instructions = Label(morgage_calculator_frame, text='Enter the Morgage Amount, Interest rate, Total years of the loan,\nchoose a payment frequency then click submit', bg='royalblue4', fg='snow1', font=('helvetica', 20), pady=25)
morgage_calculator_instructions.grid(row=1)

# Morgage amount label
morgage_calculator_total_label = Label(morgage_calculator_frame, text='Morgage amount $:', bg='royalblue4', fg='snow1', font=('helvetica', 20))
morgage_calculator_total_label.grid(row=2, sticky='w', padx=533)

# Morgage amount entry
morgage_calculator_total_entry = Entry(morgage_calculator_frame, font=('helvetica', 25), relief=RIDGE, bd=4, bg='Dodger Blue', fg='snow2', width=25)
morgage_calculator_total_entry.grid(row=3, pady=(0, 20))

# Interest Rate Label
morgage_calculator_interest_rate_label = Label(morgage_calculator_frame, text='Interest Rate %:', bg='royalblue4', fg='snow1', font=('helvetica', 20))
morgage_calculator_interest_rate_label.grid(row=4, sticky='w', padx=533)

# Interest Rate Entry
morgage_calculator_interest_rate_entry = Entry(morgage_calculator_frame, font=('helvetica', 25), relief=RIDGE, bd=4, bg='Dodger Blue', fg='snow2', width=25)
morgage_calculator_interest_rate_entry.grid(row=5, pady=(0, 20))

# Total years label
morgage_calculator_year_of_loan_label = Label(morgage_calculator_frame, text='Total years of the loan:', bg='royalblue4', fg='snow1', font=('helvetica', 20))
morgage_calculator_year_of_loan_label.grid(row=6, sticky='w', padx=533)

# Total years entry
morgage_calculator_year_of_loan_entry = Entry(morgage_calculator_frame, font=('helvetica', 25), relief=RIDGE, bd=4, bg='Dodger Blue', fg='snow2', width=25)
morgage_calculator_year_of_loan_entry.grid(row=7, pady=(0, 20))

# Payment frequency Label
morgage_calculator_payment_frequency_label = Label(morgage_calculator_frame, text='Payment Frequency:', bg='royalblue4', fg='snow1', font=('helvetica', 20))
morgage_calculator_payment_frequency_label.grid(row=8, sticky='w', padx=533)

# Payment frequency Combobox
morgage_calculator_combobox = ttk.Combobox(morgage_calculator_frame, width=24, font=('helvetica', 25))
morgage_calculator_combobox['values'] = ('Monthly', 'Fortnightly', 'Weekly')
morgage_calculator_combobox['state'] = 'readonly'
morgage_calculator_combobox.current(0)
morgage_calculator_combobox.grid(row=9, pady=5)

# Submit button
morgage_calculator_submit = Button(morgage_calculator_frame, text='Submit', font=('helvetica', 20), relief=RAISED, bd=4, bg='Dodger Blue', fg='snow2', command=morgage_calculator_button)
morgage_calculator_submit.grid(row=10)

# Scrolled results box
morgage_calculator_results = scrolledtext.ScrolledText(morgage_calculator_frame, bg='royalblue4', fg='snow1', font=('helvetica', 20), height=3, wrap=WORD)
morgage_calculator_results.grid(row=11, pady=2)
### END OF MORGAGE CALCULATOR TKINTER CONFIG ###


### CHANGE RETURN PROGRAM TKINTER CONFIG###
# Frame config
change_return_frame.columnconfigure(0, weight=1)

# Title Label
change_return_submit_title = Label(change_return_frame, text="Change Return Calculator", bg='royalblue4', fg='snow1', font=('helvetica', 50))
change_return_submit_title.grid(row=0)

# Instructions Label
change_return_instructions = Label(change_return_frame, text='Enter unit price and amount paid, then click submit', bg='royalblue4', fg='snow1', font=('helvetica', 20))
change_return_instructions.grid(row=1, pady=5)

# Item Cost Label
change_return_item_cost_label = Label(change_return_frame, text='Item cost $:', bg='royalblue4', fg='snow1', font=('helvetica', 20))
change_return_item_cost_label.grid(row=2, sticky='w', padx=533)

# Item Cost Entry
change_return_item_cost_entry = Entry(change_return_frame, font=('helvetica', 25), relief=RIDGE, bd=4, bg='Dodger Blue', fg='snow2', width=25)
change_return_item_cost_entry.grid(row=3)

# Amount Paid Label
change_return_amount_paid_label = Label(change_return_frame, text='Amount paid $:', bg='royalblue4', fg='snow1', font=('helvetica', 20))
change_return_amount_paid_label.grid(row=4, sticky='w', padx=533)

# Amount Paid Entry
change_return_amount_paid_entry = Entry(change_return_frame, font=('helvetica', 25), relief=RIDGE, bd=4, bg='Dodger Blue', fg='snow2', width=25)
change_return_amount_paid_entry.grid(row=5)

# Submit Button
change_return_submit_button = Button(change_return_frame, text='Submit', font=('helvetica', 20), relief=RAISED, bd=4, bg='Dodger Blue', fg='snow2', command=change_return_submit)
change_return_submit_button.grid(row=6)

# Change Owed Label
change_return_change_owed_label = Label(change_return_frame, text='Change owed:', bg='royalblue4', fg='snow1', font=('helvetica', 20))
change_return_change_owed_label.grid(row=7, sticky='W', padx=533)

# Change Return Labels
fifty_dollar_label = Label(change_return_frame, text='$50.00 notes:', bg='royalblue4', fg='snow1', font=('helvetica', 20))
fifty_dollar_label.grid(row=8, sticky='W', padx=533)

twenty_dollar_label = Label(change_return_frame, text='$20.00 notes:', bg='royalblue4', fg='snow1', font=('helvetica', 20))
twenty_dollar_label.grid(row=9, sticky='W', padx=533)

ten_dollar_label = Label(change_return_frame, text='$10.00 notes:', bg='royalblue4', fg='snow1', font=('helvetica', 20))
ten_dollar_label.grid(row=10, sticky='W', padx=533)

five_dollar_label = Label(change_return_frame, text='$5.00 notes:', bg='royalblue4', fg='snow1', font=('helvetica', 20))
five_dollar_label.grid(row=11, sticky='W', padx=533)

two_dollar_label = Label(change_return_frame, text='$2.00 coins:', bg='royalblue4', fg='snow1', font=('helvetica', 20))
two_dollar_label.grid(row=12, sticky='W', padx=533)

one_dollar_label = Label(change_return_frame, text='$1.00 coins:', bg='royalblue4', fg='snow1', font=('helvetica', 20))
one_dollar_label.grid(row=13, sticky='W', padx=533)

fifty_cent_label = Label(change_return_frame, text='$00.50 coins:', bg='royalblue4', fg='snow1', font=('helvetica', 20))
fifty_cent_label.grid(row=14, sticky='W', padx=533)

twenty_cent_label = Label(change_return_frame, text='$00.20 coins:', bg='royalblue4', fg='snow1', font=('helvetica', 20))
twenty_cent_label.grid(row=15, sticky='W', padx=533)

ten_cent_label = Label(change_return_frame, text='$00.10 coins:', bg='royalblue4', fg='snow1', font=('helvetica', 20))
ten_cent_label.grid(row=16, sticky='W', padx=533)

five_cent_label = Label(change_return_frame, text='$00.05 coins:', bg='royalblue4', fg='snow1', font=('helvetica', 20))
five_cent_label.grid(row=17, sticky='W', padx=533)

# Change return Results
fifty_dollar_result = Label(change_return_frame, text='0', bg='royalblue4', fg='snow1', font=('helvetica', 20))
fifty_dollar_result.grid(row=8, sticky='W', padx=725)

twenty_dollar_result = Label(change_return_frame, text='0', bg='royalblue4', fg='snow1', font=('helvetica', 20))
twenty_dollar_result.grid(row=9, sticky='W', padx=725)

ten_dollar_result = Label(change_return_frame, text='0', bg='royalblue4', fg='snow1', font=('helvetica', 20))
ten_dollar_result.grid(row=10, sticky='W', padx=725)

five_dollar_result = Label(change_return_frame, text='0', bg='royalblue4', fg='snow1', font=('helvetica', 20))
five_dollar_result.grid(row=11, sticky='W', padx=725)

two_dollar_result = Label(change_return_frame, text='0', bg='royalblue4', fg='snow1', font=('helvetica', 20))
two_dollar_result.grid(row=12, sticky='W', padx=725)

one_dollar_result = Label(change_return_frame, text='0', bg='royalblue4', fg='snow1', font=('helvetica', 20))
one_dollar_result.grid(row=13, sticky='W', padx=725)

fifty_cent_result = Label(change_return_frame, text='0', bg='royalblue4', fg='snow1', font=('helvetica', 20))
fifty_cent_result.grid(row=14, sticky='W', padx=725)

twenty_cent_result = Label(change_return_frame, text='0', bg='royalblue4', fg='snow1', font=('helvetica', 20))
twenty_cent_result.grid(row=15, sticky='W', padx=725)

ten_cent_result = Label(change_return_frame, text='0', bg='royalblue4', fg='snow1', font=('helvetica', 20))
ten_cent_result.grid(row=16, sticky='W', padx=725)

five_cent_result = Label(change_return_frame, text='0', bg='royalblue4', fg='snow1', font=('helvetica', 20))
five_cent_result.grid(row=17, sticky='W', padx=725)
### END OF CHANGE RETURN PROGRAM TKINTER CONFIG ###


### BINARY TO DECIMAL CONVERTER TKINTER CONFIG ###
# Frame config
binary_to_decimal_frame.columnconfigure(0, weight=1)

# Title Label
binary_to_decimal_title = Label(binary_to_decimal_frame, text="Binary and Decimal Convertor", bg='royalblue4', fg='snow1', font=('helvetica', 50))
binary_to_decimal_title.grid(row=0)

# Instructions Label
binary_to_decimal_instructions = Label(binary_to_decimal_frame, text='Use the drop down menu to select conversion type, enter a figure then click submit', bg='royalblue4', fg='snow1', font=('helvetica', 20))
binary_to_decimal_instructions.grid(row=1, pady=50)

# Combobox Label
binary_to_decimal_combobox_label = Label(binary_to_decimal_frame, text='Select a conversion type:', bg='royalblue4', fg='snow1', font=('helvetica', 20))
binary_to_decimal_combobox_label.grid(row=2, sticky='w', padx=533)

# Combobox
binary_combobox = ttk.Combobox(binary_to_decimal_frame, width=24, font=('helvetica', 25))
binary_combobox['values'] = ('Decimal to Binary', 'Binary to Decimal')
binary_combobox['state'] = 'readonly'
binary_combobox.current(0)
binary_combobox.grid(row=3, pady=5)

# Conversion Label
binary_to_decimal_num_label = Label(binary_to_decimal_frame, text='Enter binary or number:', bg='royalblue4', fg='snow1', font=('helvetica', 20))
binary_to_decimal_num_label.grid(row=4, pady=(20, 0), sticky='w', padx=533)

# Conversion Entry
binary_to_decimal_entry = Entry(binary_to_decimal_frame, font=('helvetica', 25), relief=RIDGE, bd=4, bg='Dodger Blue', fg='snow2', width=25)
binary_to_decimal_entry.grid(row=5)

# Submit Button
binary_to_decimal_button = Button(binary_to_decimal_frame, text='Submit', font=('helvetica', 20), relief=RAISED, bd=4, bg='Dodger Blue', fg='snow2', command=binary_to_decimal_submit)
binary_to_decimal_button.grid(row=6, pady=2)

# Scrolled results box
binary_to_decimal_results = scrolledtext.ScrolledText(binary_to_decimal_frame, bg='royalblue4', fg='snow1', font=('helvetica', 20), height=7, wrap=WORD)
binary_to_decimal_results.grid(row=7, pady=50)
### END OF BINARY TO DECIMAL CONVERTER TKINTER CONFIG ###


### SCIENTIFIC CALCULATOR TKINTER CONFIG ###
# Title Label
calculator_title = Label(calculator_frame, text="Scientific Calculator", bg='royalblue4', fg='snow1', font=('helvetica', 50))
calculator_title.grid(row=0, columnspan=6, padx=200, sticky="nsew")

# Calculator Screen
calculator_entry = Entry(calculator_frame, font=('helvetica', 50), width=41, relief=RIDGE, justify=RIGHT, bd=10,
                         bg='Dodger Blue', fg='snow2', disabledbackground='Dodger Blue', disabledforeground='snow2',
                         state=DISABLED)
calculator_entry.grid(row=1, columnspan=6, pady=20, sticky="nsew")

# Row 2
# ABS button
calculator_abs_button = Button(calculator_frame, font=('helvetica', 25), text='Abs', relief=RAISED, bd=4,
                               bg='Dodger Blue', fg='snow2', width=4, height=1, command=calc_abs)
calculator_abs_button.grid(row=2, column=0, sticky="nsew")

# log Button
calculator_log_button = Button(calculator_frame, font=('helvetica', 25), text='log', relief=RAISED, bd=4, bg='Dodger Blue', fg='snow2', width=4, height=1, command=calc_log)
calculator_log_button.grid(row=2, column=1, sticky="nsew")

# ln Button
calculator_ln_button = Button(calculator_frame, font=('helvetica', 25), text='ln', relief=RAISED, bd=4, bg='Dodger Blue', fg='snow2', width=4, height=1, command=calc_ln)
calculator_ln_button.grid(row=2, column=2, sticky="nsew")

# e button
calculator_e_button = Button(calculator_frame, font=('helvetica', 25), text='e', relief=RAISED, bd=4, bg='Dodger Blue', fg='snow2', width=4, height=1, command=calc_e)
calculator_e_button.grid(row=2, column=3, sticky="nsew")

# x! button
calculator_factorial_button = Button(calculator_frame, font=('helvetica', 25), text='x!', relief=RAISED, bd=4, bg='Dodger Blue', fg='snow2', width=4, height=1, command=calc_factorial)
calculator_factorial_button.grid(row=2, column=4, sticky="nsew")

# ANS button
calculator_ans_button = Button(calculator_frame, font=('helvetica', 25), text='Ans', relief=RAISED, bd=4, bg='Dodger Blue', fg='snow2', width=4, height=1, command=calc_ans)
calculator_ans_button.grid(row=2, column=5, sticky="nsew")

# Row 3
# Squared button
calculator_squared_button = Button(calculator_frame, font=('helvetica', 25), text='x^2', relief=RAISED, bd=4, bg='Dodger Blue', fg='snow2', width=4, height=1, command=calc_square)
calculator_squared_button.grid(row=3, column=0, sticky="nsew")

# Cubed button
calculator_cubed_button = Button(calculator_frame, font=('helvetica', 25), text='x^3', relief=RAISED, bd=4, bg='Dodger Blue', fg='snow2', width=4, height=1, command=calc_cube)
calculator_cubed_button.grid(row=3, column=1, sticky="nsew")

# x to the power of y button
calculator_power_button = Button(calculator_frame, font=('helvetica', 25), text='x^y', relief=RAISED, bd=4, bg='Dodger Blue', fg='snow2', width=4, height=1, command=calc_power)
calculator_power_button.grid(row=3, column=2, sticky="nsew")

# square root button
calculator_sqrt_button = Button(calculator_frame, font=('helvetica', 25), text='√x', relief=RAISED, bd=4, bg='Dodger Blue', fg='snow2', width=4, height=1, command=calc_sqrt)
calculator_sqrt_button.grid(row=3, column=3, sticky="nsew")

# 3rd root button
calculator_third_root_button = Button(calculator_frame, font=('helvetica', 25), text='3√x', relief=RAISED, bd=4, bg='Dodger Blue', fg='snow2', width=4, height=1, command=calc_third_root)
calculator_third_root_button.grid(row=3, column=4, sticky="nsew")

# inverse button
calculator_inverse_button = Button(calculator_frame, font=('helvetica', 25), text='x^-1', relief=RAISED, bd=4, bg='Dodger Blue', fg='snow2', width=4, height=1, command=calc_inverse)
calculator_inverse_button.grid(row=3, column=5, sticky="nsew")

# Row 4
# sin button
calculator_sin_button = Button(calculator_frame, font=('helvetica', 25), text='sin', relief=RAISED, bd=4, bg='Dodger Blue', fg='snow2', width=4, height=1, command=calc_sin)
calculator_sin_button.grid(row=4, column=0, sticky="nsew")

# cos button
calculator_cos_button = Button(calculator_frame, font=('helvetica', 25), text='cos', relief=RAISED, bd=4, bg='Dodger Blue', fg='snow2', width=4, height=1, command=calc_cos)
calculator_cos_button.grid(row=4, column=1, sticky="nsew")

# tan button
calculator_tan_button = Button(calculator_frame, font=('helvetica', 25), text='tan', relief=RAISED, bd=4, bg='Dodger Blue', fg='snow2', width=4, height=1, command=calc_tan)
calculator_tan_button.grid(row=4, column=2, sticky="nsew")

# pi button
calculator_pi_button = Button(calculator_frame, font=('helvetica', 25), text='π', relief=RAISED, bd=4, bg='Dodger Blue', fg='snow2', width=4, height=1, command=calc_pi)
calculator_pi_button.grid(row=4, column=3, sticky="nsew")

# left bracket button
calculator_left_bracket_button = Button(calculator_frame, font=('helvetica', 25), text='(', relief=RAISED, bd=4, bg='Dodger Blue', fg='snow2', width=4, height=1, command=calc_left_bracket)
calculator_left_bracket_button.grid(row=4, column=4, sticky="nsew")

# right bracket button
calculator_right_bracket_button = Button(calculator_frame, font=('helvetica', 25), text=')', relief=RAISED, bd=4, bg='Dodger Blue', fg='snow2', width=4, height=1, command=calc_right_bracket)
calculator_right_bracket_button.grid(row=4, column=5, sticky="nsew")

# Row 5
# 7 button
calculator_7_button = Button(calculator_frame, font=('helvetica', 25), text='7', relief=RAISED, bd=4, bg='Dodger Blue', fg='snow2', width=4, height=1, command=calc_7)
calculator_7_button.grid(row=5, column=0, sticky="nsew")

# 8 button
calculator_8_button = Button(calculator_frame, font=('helvetica', 25), text='8', relief=RAISED, bd=4, bg='Dodger Blue', fg='snow2', width=4, height=1, command=calc_8)
calculator_8_button.grid(row=5, column=1, sticky="nsew")

# 9 button
calculator_9_button = Button(calculator_frame, font=('helvetica', 25), text='9', relief=RAISED, bd=4, bg='Dodger Blue', fg='snow2', width=4, height=1, command=calc_9)
calculator_9_button.grid(row=5, column=2, sticky="nsew")

# % button
calculator_percent_button = Button(calculator_frame, font=('helvetica', 25), text='%', relief=RAISED, bd=4, bg='Dodger Blue', fg='snow2', width=4, height=1, command=calc_percent)
calculator_percent_button.grid(row=5, column=3, sticky="nsew")

# AC button
calculator_ac_button = Button(calculator_frame, font=('helvetica', 25), text='AC', relief=RAISED, bd=4, bg='orange', fg='snow2', width=4, height=1, command=calc_all_clear)
calculator_ac_button.grid(row=5, column=4, columnspan=2, sticky="nsew")

# Row 6
# 4 button
calculator_4_button = Button(calculator_frame, font=('helvetica', 25), text='4', relief=RAISED, bd=4, bg='Dodger Blue', fg='snow2', width=4, height=1, command=calc_4)
calculator_4_button.grid(row=6, column=0, sticky="nsew")

# 5 button
calculator_5_button = Button(calculator_frame, font=('helvetica', 25), text='5', relief=RAISED, bd=4, bg='Dodger Blue', fg='snow2', width=4, height=1, command=calc_5)
calculator_5_button.grid(row=6, column=1, sticky="nsew")

# 6 button
calculator_6_button = Button(calculator_frame, font=('helvetica', 25), text='6', relief=RAISED, bd=4, bg='Dodger Blue', fg='snow2', width=4, height=1, command=calc_6)
calculator_6_button.grid(row=6, column=2, sticky="nsew")

# x button
calculator_x_button = Button(calculator_frame, font=('helvetica', 25), text='x', relief=RAISED, bd=4, bg='Dodger Blue', fg='snow2', width=4, height=1, command=calc_multiply)
calculator_x_button.grid(row=6, column=3, sticky="nsew")

# DEL button
calculator_del_button = Button(calculator_frame, font=('helvetica', 25), text='DEL', relief=RAISED, bd=4, bg='orange', fg='snow2', width=4, height=1, command=calc_delete_last)
calculator_del_button.grid(row=6, column=4, columnspan=2, sticky="nsew")

# Row 7
# 1 button
calculator_1_button = Button(calculator_frame, font=('helvetica', 25), text='1', relief=RAISED, bd=4, bg='Dodger Blue', fg='snow2', width=4, height=1, command=calc_1)
calculator_1_button.grid(row=7, column=0, sticky="nsew")

# 2 button
calculator_2_button = Button(calculator_frame, font=('helvetica', 25), text='2', relief=RAISED, bd=4, bg='Dodger Blue', fg='snow2', width=4, height=1, command=calc_2)
calculator_2_button.grid(row=7, column=1, sticky="nsew")

# 3 button
calculator_3_button = Button(calculator_frame, font=('helvetica', 25), text='3', relief=RAISED, bd=4, bg='Dodger Blue', fg='snow2', width=4, height=1, command=calc_3)
calculator_3_button.grid(row=7, column=2, sticky="nsew")

# ÷ button
calculator_divide_button = Button(calculator_frame, font=('helvetica', 25), text='÷', relief=RAISED, bd=4, bg='Dodger Blue', fg='snow2', width=4, height=1, command=calc_divide)
calculator_divide_button.grid(row=7, column=3, sticky="nsew")

# = button
calculator_equal_button = Button(calculator_frame, font=('helvetica', 25), text='=', relief=RAISED, bd=4, bg='Dodger Blue', fg='snow2', width=4, height=1, command=calc_equals)
calculator_equal_button.grid(row=7, column=4, columnspan=2, rowspan=2, sticky="nsew")

# Row 8
# 0 button
calculator_0_button = Button(calculator_frame, font=('helvetica', 25), text='0', relief=RAISED, bd=4, bg='Dodger Blue', fg='snow2', width=4, height=1, command=calc_0)
calculator_0_button.grid(row=8, column=0, sticky="nsew")

# . button
calculator_period_button = Button(calculator_frame, font=('helvetica', 25), text='.', relief=RAISED, bd=4, bg='Dodger Blue', fg='snow2', width=4, height=1, command=calc_decimal)
calculator_period_button.grid(row=8, column=1, sticky="nsew")

# + button
calculator_plus_button = Button(calculator_frame, font=('helvetica', 25), text='+', relief=RAISED, bd=4, bg='Dodger Blue', fg='snow2', width=4, height=1, command=calc_plus)
calculator_plus_button.grid(row=8, column=2, sticky="nsew")

# - button
calculator_minus_button = Button(calculator_frame, font=('helvetica', 25), text='-', relief=RAISED, bd=4, bg='Dodger Blue', fg='snow2', width=4, height=1, command=calc_minus)
calculator_minus_button.grid(row=8, column=3, sticky="nsew")
### END OF SCIENTIFIC CALCULATOR TKINTER CONFIG ###


### UNIT CONVERTER TKINTER CONFIG ###
# Frame config
unit_converter_frame.columnconfigure(0, weight=1)

# Title Label
unit_converter_title = Label(unit_converter_frame, text="Unit Converter", bg='royalblue4', fg='snow1', font=('helvetica', 50))
unit_converter_title.grid(row=0)

# Instructions Label
unit_converter_instructions = Label(unit_converter_frame, text="Use the drop down menu's to select conversion type, enter a figure then click submit.", bg='royalblue4', fg='snow1', font=('helvetica', 20))
unit_converter_instructions.grid(row=1, pady=50)

# Top combo box
top_combobox = ttk.Combobox(unit_converter_frame, width=20, font=('helvetica', 20))
top_combobox['values'] = ('Area', 'Energy', 'Frequency', 'Length', 'Mass', 'Pressure', 'Temperature', 'Time', 'Volume')
top_combobox['state'] = 'readonly'
top_combobox.current(0)
top_combobox.grid(row=2, pady=5, sticky='s')
top_combobox.bind('<<ComboboxSelected>>', unit_converter_top_combobox)

# Equals label
unit_converter_equals_label = Label(unit_converter_frame, text="=", bg='royalblue4', fg='snow1', font=('helvetica', 100))
unit_converter_equals_label.grid(row=3, rowspan=2)

# Left entry
unit_converter_left_entry = Entry(unit_converter_frame, font=('helvetica', 20), width=23, justify=RIGHT, relief=RIDGE, bd=5, bg='Dodger Blue', fg='snow2', disabledbackground='Dodger Blue', disabledforeground='snow2', state=NORMAL)
unit_converter_left_entry.grid(row=3, sticky='sw', padx=(200, 0))

# Left combo box
left_combobox = ttk.Combobox(unit_converter_frame, width=20, font=('helvetica', 21))
left_combobox['values'] = ('Square kilometer', 'Square meter', 'Square mile', 'Square yard', 'Square foot', 'Square inch', 'Hectare', 'Acre')
left_combobox['state'] = 'readonly'
left_combobox.current(0)
left_combobox.grid(row=4, sticky='NW', padx=(200, 0))

# Right entry
unit_converter_right_entry = Entry(unit_converter_frame, font=('helvetica', 20), width=23, relief=RIDGE, bd=5, bg='Dodger Blue', fg='snow2', disabledbackground='Dodger Blue', disabledforeground='snow2')
unit_converter_right_entry.grid(row=3, sticky='SE', padx=(0, 200))

# Right combo box
right_combobox = ttk.Combobox(unit_converter_frame, width=20, font=('helvetica', 21))
right_combobox['values'] = ('Square kilometer', 'Square meter', 'Square mile', 'Square yard', 'Square foot', 'Square inch', 'Hectare', 'Acre')
right_combobox['state'] = 'readonly'
right_combobox.current(0)
right_combobox.grid(row=4, sticky='NE', padx=(0, 200))

# Submit button
unit_converter_button = Button(unit_converter_frame, text='Submit', font=('helvetica', 20), relief=RAISED, bd=4, bg='Dodger Blue', fg='snow2', command=unit_converter_submit)
unit_converter_button.grid(row=5, pady=2)

# Internet Connection Label
unit_converter_internet_label = Label(unit_converter_frame, text="Connected to the internet", bg='royalblue4', fg='green', font=('helvetica', 20))
unit_converter_internet_label.grid(row=6, pady=50)

# Refresh Connection Button
unit_converter_button = Button(unit_converter_frame, text='Refresh', font=('helvetica', 20), relief=RAISED, bd=4, bg='Dodger Blue', fg='snow2', command=unit_converter_refresh)
unit_converter_button.grid(row=7, pady=2)
### END OF UNIT CONVERTER TKINTER CONFIG ###


### ALARM CLOCK TKINTER CONFIG ###
# Title Label
alarm_clock_title = Label(alarm_clock_frame, text="Alarm Clock", bg='royalblue4', fg='snow1', font=('helvetica', 50))
alarm_clock_title.grid(row=0, columnspan=6, padx=200, sticky="nsew")

# Clock face
alarm_clock_clockface = Entry(alarm_clock_frame, font=('helvetica', 97), width=21, relief=RIDGE, justify=CENTER, bd=10, bg='Dodger Blue', fg='snow2', disabledbackground='Dodger Blue', disabledforeground='snow2', state=NORMAL)
alarm_clock_clockface.grid(row=1, columnspan=6, pady=20, sticky="nsew")

# Set Alarm labels
set_alarm_time_label = Label(alarm_clock_frame, text="Set alarm time:", bg='royalblue4', fg='snow1', font=('helvetica', 25))
set_alarm_time_label.grid(row=2, column=0, columnspan=2, sticky='W', pady=(25, 0))

# Hour Label
set_alarm_label_hour = Label(alarm_clock_frame, text="Hour", bg='royalblue4', fg='snow1', font=('helvetica', 25))
set_alarm_label_hour.grid(row=3, column=0)

# Min Label
set_alarm_label_min = Label(alarm_clock_frame, text="Min", bg='royalblue4', fg='snow1', font=('helvetica', 25))
set_alarm_label_min.grid(row=3, column=1)

# Sec Label
set_alarm_label_sec = Label(alarm_clock_frame, text="Sec", bg='royalblue4', fg='snow1', font=('helvetica', 25))
set_alarm_label_sec.grid(row=3, column=2)

# AM/PM Label
set_alarm_label_am_pm = Label(alarm_clock_frame, text="AM / PM", bg='royalblue4', fg='snow1', font=('helvetica', 25))
set_alarm_label_am_pm.grid(row=3, column=3)

# Alarm on Button
alarm_on_button = Button(alarm_clock_frame, text='Alarm Off', font=('helvetica', 20), relief=RAISED, bd=4, bg='Dodger Blue', fg='snow2')
alarm_on_button.grid(row=3, column=4)

# Set Alarm Type Label
set_alarm_type_label = Label(alarm_clock_frame, text="Set alarm type:", bg='royalblue4', fg='snow1', font=('helvetica', 25))
set_alarm_type_label.grid(row=5, column=0, columnspan=2, sticky='W', pady=(25, 0))

# Set Alarm Message Label
set_alarm_message_label = Label(alarm_clock_frame, text="Set custom message (optional):", bg='royalblue4', fg='snow1', font=('helvetica', 25))
set_alarm_message_label.grid(row=7, column=0, columnspan=2, sticky='W', pady=(25, 0))

# MP3 Selected Label
mp3_selected_label = Label(alarm_clock_frame, text="MP3 Selected:", bg='royalblue4', fg='snow1', font=('helvetica', 25))
mp3_selected_label.grid(row=7, column=3, columnspan=2, sticky='W', pady=(25, 0))

# MP3 Selected Entry
mp3_selected_entry = Entry(alarm_clock_frame, font=('helvetica', 25), width=25, relief=RIDGE, bd=4, bg='Dodger Blue', fg='snow2')
mp3_selected_entry.grid(row=8, column=3, columnspan=2, sticky='W')
mp3_selected_entry.insert(END, 'No custom song selected')

# Hour Combo Box
hour_combobox = ttk.Combobox(alarm_clock_frame, font=('helvetica', 50), width=3)
hour_combobox['values'] = ([str(num).zfill(2) for num in range(0, 13)])
hour_combobox['state'] = 'readonly'
hour_combobox.current(0)
hour_combobox.grid(row=4, column=0)

# Min Combo Box
min_combobox = ttk.Combobox(alarm_clock_frame, font=('helvetica', 50), width=3)
min_combobox['values'] = ([str(num).zfill(2) for num in range(0, 60)])
min_combobox['state'] = 'readonly'
min_combobox.current(0)
min_combobox.grid(row=4, column=1)

# Sec Combo Box
sec_combobox = ttk.Combobox(alarm_clock_frame, font=('helvetica', 50), width=3)
sec_combobox['values'] = ([str(num).zfill(2) for num in range(0, 60)])
sec_combobox['state'] = 'readonly'
sec_combobox.current(0)
sec_combobox.grid(row=4, column=2)

# AM/PM Combo Box
am_pm_combobox = ttk.Combobox(alarm_clock_frame, font=('helvetica', 50), width=3)
am_pm_combobox['values'] = ('AM', 'PM')
am_pm_combobox['state'] = 'readonly'
am_pm_combobox.current(0)
am_pm_combobox.grid(row=4, column=3)

# Alarm Type Combo Box
alarm_type_combobox = ttk.Combobox(alarm_clock_frame, font=('helvetica', 20), width=30)
alarm_type_combobox['values'] = ('default sound only', 'custom message only', 'custom .mp3 only', 'default sound and custom message', 'custom .mp3 and custom message')
alarm_type_combobox['state'] = 'readonly'
alarm_type_combobox.current(0)
alarm_type_combobox.grid(row=6, column=0, columnspan=2, pady=10)

# Custom Message Entry
alarm_clock_entry = Entry(alarm_clock_frame, font=('helvetica', 25), width=25, relief=RIDGE, bd=4, bg='Dodger Blue', fg='snow2')
alarm_clock_entry.grid(row=8, column=0, columnspan=2)

# Alarm OFF Button
alarm_on_button = Button(alarm_clock_frame, text='Alarm Off', width=15, font=('helvetica', 20), relief=RAISED, bd=4, bg='Dodger Blue', fg='snow2', command=alarm_on_off_button)
alarm_on_button.grid(row=3, column=4)

# Select MP3 Button
select_mp3_button = Button(alarm_clock_frame, text='Select custom mp3', font=('helvetica', 20), relief=RAISED, bd=4, bg='Dodger Blue', fg='snow2', command=custom_mp3_button)
select_mp3_button.grid(row=4, column=4)

# Stop Music Button
alarm_stop_music_button = Button(alarm_clock_frame, text='Stop music', width=15, font=('helvetica', 20), relief=RAISED, bd=4, bg='Dodger Blue', fg='snow2', command=stop_music_button)
alarm_stop_music_button.grid(row=6, column=4)
### END OF ALARM CLOCK TKINTER CONFIG ###


### DISTANCE BETWEEN TWO CITIES TKINTER CONFIG ###
# Frame config
distance_two_cities_frame.columnconfigure(0, weight=1)

# Title Label
distance_two_cities_title = Label(distance_two_cities_frame, text="Distance Between Two Cities", bg='royalblue4', fg='snow1', font=('helvetica', 50))
distance_two_cities_title.grid(row=0)

# Instructions Label
distance_two_cities_instructions = Label(distance_two_cities_frame, text="Ensure you are connected to the internet, then click submit once you have made your selection", bg='royalblue4', fg='snow1', font=('helvetica', 25))
distance_two_cities_instructions.grid(row=1, pady=50)

# From Label
distance_two_cities_from_label = Label(distance_two_cities_frame, text="From:", bg='royalblue4', fg='snow1', font=('helvetica', 25))
distance_two_cities_from_label.grid(row=2, sticky='w', padx=(50, 0))

# To Label
distance_two_cities_to_label = Label(distance_two_cities_frame, text="To:", bg='royalblue4', fg='snow1', font=('helvetica', 25))
distance_two_cities_to_label.grid(row=2, sticky='w', padx=(540, 0))

# In Label
distance_two_cities_in_label = Label(distance_two_cities_frame, text="In:", bg='royalblue4', fg='snow1', font=('helvetica', 25))
distance_two_cities_in_label.grid(row=2, sticky='e', padx=(0, 500))

# Submit Button
distance_two_cities_button = Button(distance_two_cities_frame, text='Submit', width=7, font=('helvetica', 20), relief=RAISED, bd=4, bg='Dodger Blue', fg='snow2', command=distance_two_cities_calculator)
distance_two_cities_button.grid(row=4, column=0, columnspan=7)

# Results Label
distance_two_cities_results = Label(distance_two_cities_frame, text="", bg='royalblue4', fg='snow1', font=('helvetica', 25))
distance_two_cities_results.grid(row=6, pady=25)

# Internet Status Label
distance_two_cities_internet_status = Label(distance_two_cities_frame, text="Connected to the internet", bg='royalblue4', fg='green', font=('helvetica', 25))
distance_two_cities_internet_status.grid(row=3, pady=25)

# Refresh Button
distance_two_cities_refresh_button = Button(distance_two_cities_frame, text='Refresh', width=7, font=('helvetica', 20), relief=RAISED, bd=4, bg='Dodger Blue', fg='snow2', command=refresh_connection)
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
    unit_converter_internet_label.config(text='No internet connection, Please try again', fg='red')

# Entry Boxes (attempt to create these with the above list if internet is connected)
try:
    # From Entry
    from_entry = AutocompleteCombobox(distance_two_cities_frame, font=('helvetica', 20), completevalues=list_of_cities)
    from_entry.grid(row=2, sticky='W', padx=(150, 0))

    # To Entry
    to_entry = AutocompleteCombobox(distance_two_cities_frame, font=('helvetica', 20), completevalues=list_of_cities)
    to_entry.grid(row=2)

    # In Entry
    in_entry = AutocompleteCombobox(distance_two_cities_frame, font=('helvetica', 20), completevalues=['kilometers', 'miles'])
    in_entry.grid(row=2, sticky='E', padx=(0, 150))

except NameError:
    distance_two_cities_internet_status.config(text='No internet connection, Please try again', fg='red')
### END OF DISTANCE BETWEEN TWO CITIES TKINTER CONFIG ###


### CREDIT CARD VALIDATOR TKINTER CONFIG ###
# Frame config
credit_card_validator_frame.columnconfigure(0, weight=1)

# Title Label
card_validator_title = Label(credit_card_validator_frame, text="Credit Card Validator", bg='royalblue4', fg='snow1', font=('helvetica', 50))
card_validator_title.grid(row=0)

# Instructions Label
card_validator_instructions = Label(credit_card_validator_frame, text="Enter a credit card number between 13 and 16 digits and click submit", bg='royalblue4', fg='snow1', font=('helvetica', 25))
card_validator_instructions.grid(row=1, pady=50)

# Entry Box
card_validator_entry = Entry(credit_card_validator_frame, font=('helvetica', 25), width=25, relief=RIDGE, bd=4, bg='Dodger Blue', fg='snow2')
card_validator_entry.grid(row=2)

# Submit button
card_validator_button = Button(credit_card_validator_frame, text='Submit', width=7, font=('helvetica', 20), relief=RAISED, bd=4, bg='Dodger Blue', fg='snow2', command=credit_card_validation)
card_validator_button.grid(row=3, pady=2)

# Results Label
card_validator_results = Label(credit_card_validator_frame, text="", bg='royalblue4', fg='snow1', font=('helvetica', 25))
card_validator_results.grid(row=4, pady=50)

# Example Combo box
# Payment frequency Combobox
card_validator_combobox = ttk.Combobox(credit_card_validator_frame, width=24, font=('helvetica', 25))
card_validator_combobox['values'] = ('Custom', 'Visa card example', 'Master card example', 'Discover card example', 'American Express card example')
card_validator_combobox['state'] = 'readonly'
card_validator_combobox.current(0)
card_validator_combobox.grid(row=5)
### END OF CREDIT CARD VALIDATOR TKINTER CONFIG ###


### INCOME TAX CALCULATOR TKINTER CONFIG ###
# Frame config
tax_calculator_frame.columnconfigure(0, weight=1)

# Title Label
simple_tax_title = Label(tax_calculator_frame, text="Simple Tax Calculator", bg='royalblue4', fg='snow1', font=('helvetica', 50))
simple_tax_title.grid(row=0)

# Instructions Label
simple_tax_instructions = Label(tax_calculator_frame, text="Enter your total taxable income in dollars for the year and click submit", bg='royalblue4', fg='snow1', font=('helvetica', 25))
simple_tax_instructions.grid(row=1, pady=25)

# Entry Box
simple_tax_entry = Entry(tax_calculator_frame, font=('helvetica', 25), width=25, relief=RIDGE, bd=4, bg='Dodger Blue', fg='snow2')
simple_tax_entry.grid(row=2)

# Submit Button
simple_tax_button = Button(tax_calculator_frame, text='Submit', width=7, font=('helvetica', 20), relief=RAISED, bd=4, bg='Dodger Blue', fg='snow2', command=income_tax_calc)
simple_tax_button.grid(row=3, pady=2)

# Results Label
simple_tax_results = Label(tax_calculator_frame, text="", bg='royalblue4', fg='snow1', font=('helvetica', 25))
simple_tax_results.grid(row=4, pady=20)

# Further Instructions Labels
simple_tax_further_instructions_row_1 = Label(tax_calculator_frame, text="Australian Resident tax rates 2021–22", bg='royalblue4', fg='snow1', font=('helvetica', 25))
simple_tax_further_instructions_row_1.grid(row=5, sticky='W', pady=(0, 10), padx=(230, 0))

simple_tax_further_instructions_row_2 = Label(tax_calculator_frame, text="Income", bg='royalblue4', fg='snow1', font=('helvetica', 25))
simple_tax_further_instructions_row_2.grid(row=6, sticky='W', padx=(230, 0))

simple_tax_further_instructions_row_2_a = Label(tax_calculator_frame, text="Tax on this income", bg='royalblue4', fg='snow1', font=('helvetica', 25))
simple_tax_further_instructions_row_2_a.grid(row=6, sticky='W', padx=(600, 0))

simple_tax_further_instructions_row_2 = Label(tax_calculator_frame, text="--------------------------------------------------------------------------------------------------", bg='royalblue4', fg='snow1', font=('helvetica', 25))
simple_tax_further_instructions_row_2.grid(row=7, sticky='W', padx=(230, 0))

simple_tax_further_instructions_row_3 = Label(tax_calculator_frame, text="0 – $18,200", bg='royalblue4', fg='snow1', font=('helvetica', 25))
simple_tax_further_instructions_row_3.grid(row=8, sticky='W', padx=(230, 0))

simple_tax_further_instructions_row_3_a = Label(tax_calculator_frame, text="Nil", bg='royalblue4', fg='snow1', font=('helvetica', 25))
simple_tax_further_instructions_row_3_a.grid(row=8, sticky='W', padx=(600, 0))

simple_tax_further_instructions_row_4 = Label(tax_calculator_frame, text="$18,201 – $45,000", bg='royalblue4', fg='snow1', font=('helvetica', 25))
simple_tax_further_instructions_row_4.grid(row=9, sticky='W', padx=(230, 0))

simple_tax_further_instructions_row_4_a = Label(tax_calculator_frame, text="19 cents for each $1 over $18,200", bg='royalblue4', fg='snow1', font=('helvetica', 25))
simple_tax_further_instructions_row_4_a.grid(row=9, sticky='W', padx=(600, 0))

simple_tax_further_instructions_row_5 = Label(tax_calculator_frame, text="$45,001 – $120,000", bg='royalblue4', fg='snow1', font=('helvetica', 25))
simple_tax_further_instructions_row_5.grid(row=10, sticky='W', padx=(230, 0))

simple_tax_further_instructions_row_5_a = Label(tax_calculator_frame, text="$5,092 plus 32.5 cents for each $1 over $45,000", bg='royalblue4', fg='snow1', font=('helvetica', 25))
simple_tax_further_instructions_row_5_a.grid(row=10, sticky='W', padx=(600, 0))

simple_tax_further_instructions_row_6 = Label(tax_calculator_frame, text="$120,001 – $180,000", bg='royalblue4', fg='snow1', font=('helvetica', 25))
simple_tax_further_instructions_row_6.grid(row=11, sticky='W', padx=(230, 0))

simple_tax_further_instructions_row_6_a = Label(tax_calculator_frame, text="$29,467 plus 37 cents for each $1 over $120,000", bg='royalblue4', fg='snow1', font=('helvetica', 25))
simple_tax_further_instructions_row_6_a.grid(row=11, sticky='W', padx=(600, 0))

simple_tax_further_instructions_row_7 = Label(tax_calculator_frame, text="$180,001 and over", bg='royalblue4', fg='snow1', font=('helvetica', 25))
simple_tax_further_instructions_row_7.grid(row=12, sticky='W', padx=(230, 0))

simple_tax_further_instructions_row_7_a = Label(tax_calculator_frame, text="$51,667 plus 45 cents for each $1 over $180,000", bg='royalblue4', fg='snow1', font=('helvetica', 25))
simple_tax_further_instructions_row_7_a.grid(row=12, sticky='W', padx=(600, 0))
### END OF INCOME TAX CALCULATOR TKINTER CONFIG ###


### FACTORIAL FINDER TKINTER CONFIG ###
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

exponentiation_button = Button(exponentiation_frame, text='Submit', width=7, font=('helvetica', 20), relief=RAISED, bd=4, bg='Dodger Blue', fg='snow2', command=exponentiation_submit)
exponentiation_button.grid(row=3, column=0, columnspan=6, pady=2)

exponentiation_results = Label(exponentiation_frame, text="", bg='royalblue4', fg='snow1', font=('helvetica', 25), wraplength=1000, justify="center")
exponentiation_results.grid(row=4, column=0, columnspan=6, pady=50)

window.config(menu=menubar)

show_frame(welcome_screen_frame)

clock_time()

window.mainloop()
