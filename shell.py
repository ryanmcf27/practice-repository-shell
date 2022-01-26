#shell for practice-repository-shell

print('Hello There!')

print("     Respond with 'Hi!' 'Nice to meet you!' or 'Go Away!'")

while 1:
    x = input(">>>")
    if x == 'exit':
        break
    
    if x == 'Hi!':
        print('What can I do for you?')
        print("     Respond with 'Quik Maths' 'Just saying hi!' or 'Leave!'")
    if x == 'Quik Maths':
        print("I'll do my best!")            
        while 1:
            a = input(">>>")
            if a == 'exit':
                print('back to main loop')
                print('')
                print('What can I do for you?')
                print("     Respond with 'Quik Maths' 'Just saying hi!' or 'Leave!'")
                break
        
            try: 
                y = eval(a)
                if y: print(y)
            except Exception as e:
                print('error:', e)
    if x == 'Nice to meet you!':
        print("Nice to meet you too!")
        print('What can I do for you?')
        print("     Respond with 'Quik Maths' 'Just saying hi!' or 'Leave!'")

    if x == 'Go Away!':
        print("Well that wasn't very nice but okay")
        break

    if x == 'Just saying hi!':
        print("Okey Dokey! Nice to meet you!")
        break
    if x == 'Leave!':
        print("Jeez you're a little rude")
        break


    

 