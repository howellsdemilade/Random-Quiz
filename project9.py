#Quiz Program
quiz = {
    "Question1": {
        "question": "What is the capital of France?" ,
        "answer": "Paris"
    },
    "Question2": {
        "question": "What is the capital of Germany?" ,
        "answer": "Berlin"
    },
    "Question3": {
        "question": "What is the capital of Italy?" ,
        "answer": "Rome"
    },
    "Question4": {
        "question": "What is the capital of Spain?" ,
        "answer": "Madrid"
    },
    "Question5": {
        "question": "What is the capital of Portugal?" ,
        "answer": "Lisbon"
    },
    "Question6": {
        "question": "What is the capital of Switzerland?" ,
        "answer": "Bern"
    },
    "Question7": {
        "question": "What is the capital of Austria?" ,
        "answer": "Vienna"
    }
}


score = 0

for key, value in quiz.items():
    print(value["question"])
    answer = input("The Answer is: ")
    
    if answer.lower() == value["answer"].lower():
        print("You are Correct...Hurray!!!")
        score+=1
        print("Your score is: " + str(score))
        print("")
        print("")
        
    else:
        print("You are Wrong...Shame on You!!!")
        print("The Answer is: " + value["answer"])
        print("Your score is: " + str(score))
        print("")
        print("")
        


print("You got " + str(score) + " out of 7 questions correctly!")
print("Your Percentage is "+ str(int(score/7 * 100)) + "%")


    


























