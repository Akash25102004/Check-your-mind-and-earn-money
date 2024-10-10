questions = [
    [
        "Which of the following is a popular Python library for data analysis?",
        "JavaFX", "Numpy", "C++ STL", "Flask", 2
    ],
    [
        "In machine learning, what does overfitting refer to?",
        "The model performs well on training data but poorly on unseen data",
        "The model performs equally well on both training and test data",
        "The model is too simple", "The model has too many features", 1
    ],
    [
        "Which of the following is a characteristic of C++?",
        "It is an interpreted language", "It supports object-oriented programming",
        "It is primarily used for web development", "It has automatic garbage collection", 2
    ],
    [
        "Which SQL command is used to retrieve data from a database?",
        "READ", "GET", "FETCH", "SELECT", 4
    ],
    [
        "In React, what is the purpose of the useState hook?"," To manage side effects","To manage component state",
        " To handle API requests","To render components",1
    ],
    [
        "Which of the following is NOT a machine learning algorithm?","Linear Regression",
        "Decision","Tree","HTML",4
    ],
    [
        "What is the output of the following Python code: print(2 ** 3)?", 
        "5", "6","8","9",3
    ],
    [
        "Which of the following is used to visualize data in Python?", "Matplotlib",
        "PyGame","Django","Flask",1
    ],
    [
        "What does SQL stand for?","simple Query language"" Structured Query Language",
        "Standard Query Language","Scripting Query Language",2
    ],
    [
        "In React, what is the purpose of props? ","To store state",
        "To pass data to components"," To manage events"," To create hooks",2
    ],
    [
        "What is the primary use of TensorFlow?","Web development",
        "Data visualization","Machine learning","Game development",3
    ],
    [
        "Which keyword is used to define a function in Python?",
        "function","def","define","func",2
    ],
    [
        "What does the acronym API stand for?",
        "Application Programming Interface",
        "Advanced Programming Interface",
        "Application Program Interface",
        "Automatic Programming Interface",1
    ],
    [
       "Which C++ feature allows the creation of multiple functions with the same name?", 
       "Inheritance","Encaplulation","Polymorphism","Overloading",2
    ],
    [
        "In machine learning, what is a common technique to improve model performance?", "Feature selection",
        "Data deletion",
        "Code optimization",
        "System reboot",1
    ]

]

levels = [1000, 2000, 3000, 5000,10000,20000,40000,80000,1600000,3600000,720000,1250000,2500000,5000000,10000000]
money=0
for i in range(len(questions)):
    q = questions[i]
    print(f"{q[0]} (\nThis question is for {levels[i]} points)")
    print(f"a. {q[1]}")
    print(f"b. {q[2]}")
    print(f"c. {q[3]}")
    print(f"d. {q[4]}")

    try:
        rep = int(input("\nEnter the option (1-4) or enter 0 to quit::"))
        if rep==0:
            break
        if rep == q[-1]:
            print(f"\nCorrect! You've won.{levels[i]}")
            if i==4:
                money=10000
            elif i==9:
                money=360000
            elif i==13:
                money=5000000
            elif i==14:
                money=10000000        
        else:
            print("\nWrong answer. Game over.")
            break
    except ValueError:
        print("\nPlease enter a valid option (1-4).")
        break
print(f"Toatlly you have won is :",money)