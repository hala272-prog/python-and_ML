import random

MAX_LINES = 3 
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}

symbol_values = {
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2
}
def check_winning(colomns, lines, bet, values) :
    winning_lines = []
    winning = 0 
    for line in range(lines):
        symbol = colomns[0][line]
        for column in colomns :
            symbol_to_check = column[line]
            if symbol != symbol_to_check :
                break
        else :
            winning += values[symbol] * bet 
            winning_lines.append(lines + 1)
    return winning , winning_lines      

def get_slot_machine_spin(rows,cols,symboles):
    all_symbols =[]
    for symbol, symbol_count in symboles.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    colomns =[]
    for _ in range (cols):
        coloms = []
        current_symbols = all_symbols[:]
        for _ in range (rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            coloms.append(value)
        colomns.append(coloms)  
    return colomns  



def print_slot_machine(colomns):
    for row in range (len(colomns[0])):
        for i, colom in enumerate(colomns):
            if i!= len(colomns) - 1 :
                print(colom[row], end =" | ")
            else:
                print(colom[row] , end ="")
        print()        

def deposit():
    while True :
        amount = input("what would you like to desposit? $ ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0 :
                break 
            else:
                print("amount must be greater than 0")
        else:
            print("please ennter a number")
    return amount 

def get_number_of_lines():
        while True :
            lines = input("Enter the number of lines (1 -" + str(MAX_LINES ) + ")? ")
            if lines.isdigit():
                lines = int(lines)
                if  1 <= lines <= MAX_LINES :
                    break 
                else:
                    print("Enter a valide number of lines ")
            else:
                print("please ennter a number")
        return lines 

def get_bet():
      while True :
          amount  = input("what would you like to bet ? $ ")
          if amount.isdigit():
               amount = int(amount)
               if  MIN_BET <= amount <= MAX_BET :
                   break 
               else:
                    print(f" amount must be beween {MIN_BET} and {MAX_BET} ")
          else:
              print("please ennter a number")
      return amount

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total = bet * lines 
        if total >= balance :
            print(f"you do not have enough to bet that amount , your cuurent balence is {balance}")
        else:
            break 
    print(f"you are betting ${bet} on {lines} lines . total bet is {total}")
    slot = get_slot_machine_spin(ROWS , COLS , symbol_count )
    print_slot_machine(slot)
    winning, winning_lines = check_winning(slot, lines, bet, symbol_values)
    print(f"you won {winning}")
    print(f"you won on lines : ", *winning_lines)
    return winning - total

def main():
    balance = deposit()
    while True :
        print(f"current balence is ${balance}")
        answer = input("prees enter to spin (q to quit)")
        if answer == "q" :
            break 
        balance += spin(balance)
    print (f"you left with ${balance}")
    
main()