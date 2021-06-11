from buaa_login import BuaaLogin

if __name__ == '__main__':
    username = str(input('Input username:'))
    passwd = str(input('Input password: '))
    a = BuaaLogin(username=username,
                   password=passwd)
    while 1:
        print('\n{: ^28}'.format('Input order'))
        print('{:-^31}'.format(''))
        print('{: ^15}'.format('1') + '-' + '{: ^15}'.format('Login'))
        print('{: ^15}'.format('2') + '-' + '{: ^15}'.format('Logoff'))
        print('{: ^15}'.format('3') + '-' + '{: ^15}'.format('Status'))
        print('{: ^15}'.format('4') + '-' + '{: ^15}'.format('Quit'))
        print('{:-^31}\n'.format(''))
        command = str(input(''))
        if command == '1':
            a.log_in()
        elif command == '2':
            a.log_out()
        elif command == '3':
            a.get_login_info()
        elif command == '4':
            exit()
        else:
            print('\n{: ^28}'.format('Wrong formation'))



