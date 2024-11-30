import data 

data=data.question_data
score=0
question=0
for i in data:
    user_answer=input(f"Q.{question+1} {i["text"]} (True/False)?:").lower()
    question+=1
    answer=i["answer"].lower()
    if user_answer==answer:
        print("You got that Correct")
        print(f"The correct answer was:{answer}")
        score+=1
        print(f"Your Correct Score is {score}/{question}")
        print("\n")
    else:
        print("It's Incorrect")
        print(f"The correct answer was{answer}")
        print(f"Your Correct Score is {score}/{question}")
        print("\n")


print(f"Final score = {score}/{question}")