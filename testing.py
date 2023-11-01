print('Welcome to Craftofia Creations')
a={}
option=input('r/l')
if option=='r':
    first_name=input('Enter your first name')
    phone_number=int(input('Enter your phone number'))
    user_name=input('Enter your user_name')
    password=input('Enter your password')
    print('your account was registered successfully' + user_name)
    a[user_name] = password
elif option== 'l':
    user_name=input('Enter your user_name')
    password=input('Enter your password')
    if user_name in a and a[user_name]==password:
        print('login successfully')
    else:
        print('Incorrect username and password')
else:
    print('Choose r for registration')