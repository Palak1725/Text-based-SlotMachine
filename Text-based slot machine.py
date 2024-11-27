import random

MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

ROWS = 3
COLS = 3

SYMBOLS = {'A': 2, 'B': 4, 'C': 6, 'D': 7}
symb_value = {'A': 5, 'B': 4, 'C': 3, 'D': 2}

def spin(rows, cols, symbol):
    
    all_symbols = []

    for i, SYMBOLS in symbol.items():
        for _ in range(SYMBOLS):
            all_symbols.append(i)

    columns = []

    for _ in range(cols):
        coln = []
        current_symbols = all_symbols[:]

        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            coln.append(value)

        columns.append(coln)

    return columns

def check_wins(columns, lines, bet, values):
    wins = 0
    win_line = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            wins += values[symbol] * bet
            win_line.append(line+1)
    
    return wins, win_line

def print_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end = " | ")
            else:
                print(column[row], end = '\n')

def deposit():

    while True:

        amount = input("What would you like to deposit? $")

        if amount.isdigit():
            
            amount = int(amount)

            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")

        else:

            print("Enter a number.")
    return amount

def no_of_lines():
    
    while True:

        lines = input(f"Enter the no. of lines to bet on (1-{MAX_LINES})? ")

        if lines.isdigit():
            
            lines = int(lines)

            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a avlid no. of lines.")

        else:
            print("Enter a number.")

    return lines

def get_bet():

    while True:

        bet = input("What would you like to bet on each line? $")

        if bet.isdigit():
            bet = int(bet)

            if (MIN_BET <= bet <= MAX_BET):
                break
            else:
                print(f"Amount must be between ${MIN_BET} and ${MAX_BET}.")

        else:
  
            print("Enter a number.")

    return bet

def game(balance):
    lines = no_of_lines()

    while True:

        bet = get_bet()

        total_bet = bet * lines

        if total_bet > balance:
            print(f"Not enough balance. \nCurrent Balance = ${balance}.")
        else:
            break

    print(f"You're betting ${bet} on {lines} lines. Total bet = ${total_bet}")

    slots = spin(ROWS, COLS, SYMBOLS)
    print_machine(slots)
    winnings, winning_lines = check_wins(slots, lines, bet, symb_value)
    print(f"You won ${winnings}!")
    print(f"You won on lines: ", *winning_lines)

    return winnings - total_bet

def main():

    balance = deposit()

    while True:
        print(f"Current balance is: ${balance}.")
        answer = input("Press enter to play (or q to quit).")
        if answer.lower() == 'q':
            break
        balance += game(balance)
    print(f"You are left with ${balance}.")

main()