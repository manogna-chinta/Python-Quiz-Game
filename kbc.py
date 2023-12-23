questions=[
  'who is the developer of python language?',
  'when did India get independence?',
  'what is the currency in India?',
  'which state does hyderabad belong to?',
  'what is the latest iphone ?'
  ]
answers=['Guido van',
   '1947',
   'INR',
   'Telangana',
   'iphone 14'
]
options=[
   ['Dennis Ritchi','Alan Frank','Guido van','Albert'],
   ['1947','1995','2001','1950'],
   ['Pounds','INR','Euros','Dollars'],
   ['oddisa','rajasthan','Bangalore','Telangana'],
   ['iphone 14','iphone se','iphone 13','iphone 8'],
   ]

def play_game(username,questions,answers,options):
    print("Hello",username,"to the KBC game")
    score=0
    for i in range(len(questions)):
        current_question=questions[i]
        correct_answer=answers[i]
        current_question_options=options[i]
        print("Question :",current_question)
        for index,each_option in enumerate(current_question_options):
            print(index+1,")",each_option,sep='')
        user_answer_index=int(input("Enter your choice(1,2,3 or 4):"))
        user_answer=current_question_options[user_answer_index-1]
        if user_answer==correct_answer:
            print("Correct Answer")
            score=score+100
        else:
            print("Wrong Answer")
            break
    print("Your final score is ",score)
    return username,score
def view_scores(names_and_scores):
    for name,score in names_and_scores.items():
        print(name,"has scored",score)
def KBC(questions,answers,options):
    names_and_scores={}
    while True:
        print("welcome to the KBC game!")
        print("1) Play Game\n2)View Scores\n3)Exit")
        choice=int(input("Please enter your choice:"))
        if choice==1:
            username=input("Please enter your name:")
            username,score =play_game(username,questions,answers,options)
            names_and_scores[username]=score
        elif choice==2:
            view_scores(names_and_scores)
        elif choice==3:
            break
        else:
            print("your choice is not valid")
KBC(questions,answers,options)
