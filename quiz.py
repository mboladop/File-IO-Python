
def main():
    print("Main Choice: Choose 1 of 3 choices")
    print("1. Ask Questions")
    print("2. Add a Question")
    print("3. Exit Game")
   
    choice = input ("Please make a choice: ")
    score=[]
    score= 0
    
    if choice == "1":
        
        f = open('questions.txt', 'r')
        lines = f.read().split('\n') 
        
        
        f.close()
        for line in lines:
            question, answer= line.split(',')
            guess= input(question+":").lower()
            if guess  == answer:
                print("You're right")
                score+=1
            
            else:
                print("WRONG")
        print(score)
             
        
        
        
    elif choice == "2":
        f = open('questions.txt', 'a')
        new_question = (input("Ask a question: "))
        questions = f.write('\n'+ new_question +",")
        new_answer = (input("Answer please: "))
        questions = f.write(new_answer)
        print(questions)
        f.close()
    
    elif choice == "3":
        print("Bye Bye")
        return None
    
    else: 
        print("please enter valid option")
        main()
    
    
  
main()