# Program that I can use as a journal
# Password protected

from dotenv import load_dotenv
import os

load_dotenv()
my_password = os.getenv('TOKEN')


def show_options():
    print('1) -----Enter new log entry-----')
    print('2) -----Read previous logs-----')
    print('3) -----Exit-----')


def starting_message():
    print('**************************')
    print("-------Ty's Journal-------")
    print('**************************')


def check_password(password):
    if password == my_password:
        return True
        print('Correct Password! Access Granted')
    else:
        return False


def change_password(password, new_password):
    if(check_password(password) == True):
        my_password = new_password
        return True
    else:
        return False


def create_new_entry(title, content, date):
    text_file = open("something.txt", "a")
    text_file.write
    ('------------------------------------\n' +
     f'{title}\n' +
     f' date: {date}\n' +
     f'{content}\n' +
     '------------------------------------\n')
    text_file.close()


def read_the_diary():
    text_file = open("something.txt", "r")
    data = text_file.read().splitlines()
    print(data)


def save_entry_num():
    text_file = open("saves.txt", "r")
    data = text_file.read()
    current_num = int(data[0])
    text_file = open("saves.txt", "w")
    res = current_num + 1
    text_file.write(str(res))
    text_file.close()


def show_num_of_entrys():
    text_file = open("saves.txt", "r")
    data = text_file.read()
    print(f'Number of entries: {data}')


enter_password = input('Whats the password?')
if check_password(enter_password) == True:
    starting_message()
    running = True
    show_options()
    print('What would you like to do?')
else:
    print('Incorrect password. Try again...')

while(running == True):
    choice = input()
    if choice == 'new entry':
        title = input('Title?\n')
        content = input('Write what you want to log\n')
        date = input('What is the date?\n')
        create_new_entry(title, content, date)
        save_entry_num()
        show_options()
    if choice == 'read prev':
        read_the_diary()
        show_num_of_entrys()
        show_options()
    if choice == 'exit':
        running = False
