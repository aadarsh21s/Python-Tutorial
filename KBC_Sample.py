questions = [["What is the full form of AI?", "Artificial Intelligence", "Artic Info", "Art Info", "Arrow Intelligence", None, 1],
              ["Which language is used to create AI?", "Python", "Java", "C++", "Ruby", None, 1],
              ["Which is the first programming language?", "C", "C++", "Python", "Java", None, 1],
              ["Which command is used to push in git?", "git update", "git upload", "git push", "git pull", None, 3],
              ["Which language is to create .net", "c", "c++", "C programming", "c#", None, 4],
              ["Which command is used to print in python?", "print()", "printf()", "cout", "System.out.println()", None, 1],
              ["Which command is used to commit in git?", "git commit", "git push", "git pull", "git update", None, 1],
              ["Which programming language is used to create android apps?", "Java", "Python", "C++", "Ruby", None, 1]]

levels = [1000, 3000, 5000, 10000, 50000, 1000000, 2500000, 5000000, 10000000]
money_won = 0
for i in range(0, len(questions)):
    print(f"Question for Rs.{levels[i]}: {questions[i][0]}")
    print(f"1. {questions[i][1]}")
    print(f"2. {questions[i][2]}")
    print(f"3. {questions[i][3]}")
    print(f"4. {questions[i][4]}")
    
    answer = int(input("Enter your answer (1-4): "))
    
    if answer == questions[i][8]:
        print(f"Correct! You have won Rs.{levels[i]}.\n")
        if i == 2:
            money_won = 5000
        elif i == 4:
            money_won = 50000
        elif i == 6:
            money_won = 2500000
        elif i == 8:
            money_won = 10000000
    else:
        print("Incorrect answer. Game over.")
        break

print(f"You have won Rs.{money_won}.")