import random
exercises = [i for i in range(4)]
user_input = int(input("whats the highest number?: "))
a = random.randint(0, user_input)
b = random.randint(0, user_input)
op = random.choice(exercises)
while True:

    if op == 0:
        print(f"{a}+{b}=")
        c = a + b
        math = int(input("answer: "))
        if math == c:
            print("correct")
            a = random.randint(0, user_input)
            b = random.randint(0, user_input)
            op = random.choice(exercises)
            
        elif math != c:
            print("try again")
            print(f"{a}+{b}=") 
            math = int(input("answer: "))                   
            if math == c:
                print("correct")
                a = random.randint(0, user_input)
                b = random.randint(0, user_input)
                op = random.choice(exercises)
               
    elif op == 1:
        print(f"{a}-{b}=")
        c = a - b
        math = int(input("answer: "))
        if math == c:
            print("correct")
            a = random.randint(0, user_input)
            b = random.randint(0, user_input)
            op = random.choice(exercises)
           
        elif math != c:
            print("try again")
            print(f"{a}-{b}=")
            math = int(input("answer: "))                   
            if math == c:
                print("correct")
                a = random.randint(0, user_input)
                b = random.randint(0, user_input)
                op = random.choice(exercises)
                   
    elif op == 2:
        print(f"{a}*{b}=")
        c = a * b
        math = int(input("answer: "))
        if math == c:
            print("correct")
            a = random.randint(0, user_input)
            b = random.randint(0, user_input)
            op = random.choice(exercises)
           
        elif math != c:
            print("try again")
            print(f"{a}*{b}=")
            math = int(input("answer: "))                   
            if math == c:
                print("correct")
                a = random.randint(0, user_input)
                b = random.randint(0, user_input)
                op = random.choice(exercises)
               
    elif op == 3:
        print(f"{a}:{b}=")
        c = a // b
        math = int(input("answer: "))
        if math == c:
            print("correct")
            a = random.randint(0, user_input)
            b = random.randint(0, user_input)
            op = random.choice(exercises)
           
        elif math != c:
            print("try again")
            print(f"{a}:{b}=") 
            math = int(input("answer: "))                   
            if math == c:
                print("correct")
                a = random.randint(0, user_input)
                b = random.randint(0, user_input)
                op = random.choice(exercises)
               
