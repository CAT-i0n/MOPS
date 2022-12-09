import os

if __name__ == "__main__":
    os.system('cls')
    while(True):
        print(">>>", end=" ")
        command = input()
        if command == 'exit':
            break
        os.system("python CLI.py " + command)
