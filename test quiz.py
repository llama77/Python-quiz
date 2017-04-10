def main():
    global sys
    import sys
    global time
    import time
    print("Loading Quiz")
    time.sleep(0.4)
    print("10%")
    time.sleep(0.4)
    print("20%")
    time.sleep(0.4)
    print("30%")
    time.sleep(0.4)
    print("40%")
    time.sleep(0.4)
    print("50%")
    time.sleep(0.4)
    print("60%")
    time.sleep(0.4)
    print("70%")
    time.sleep(0.4)
    print("80%")
    time.sleep(0.4)
    print("90%")
    time.sleep(0.4)
    print("100%")
    time.sleep(0.4)
    print("Loading Compleat")

    time.sleep(1.5)
    print("Welcome To The Quiz!")
    time.sleep(1.5)
    begin = input("would you like to take the quiz?.\n")
    if begin == "yes":
        print("Awsome lets get started")
    else:
        print("Well that sucks")
        time.sleep(0.5)
        print("Terminating program")
        sys.exit()
    time.sleep(1.5)
    name = input("First off lets get your name.\n")
    print("Hello, {}".format(name))
    time.sleep(1.5)
    print("Ok lets get this started....")
    time.sleep(1.5)
    print("What category would you like")
    time.sleep(1.0)
    print("A, Animals")
    print("B, Food")
    type = input("C, Linux.\n")
    if type == "A":
       animal_quiz()
    if type == "B":
        food_quiz 
    if type == "C":
        linux_quiz

def animal_quiz():
    score = 0
    print("Animals it is")
    time.sleep(1.5)
    print("Question 1")
    time.sleep(1.5)
    print("What is animal likes to climb trees")
    time.sleep(1.0)
    print("A. Cat")
    print("B. squirrel")
    question1 = input("C. Llama.\n")
    if question1 == "B":
        print("Correct!")
        score = score + 1
        time.sleep(1.5)        
    else:
        print("Wrong")
        score = score + 0
    time.sleep(1.5)     
    print("Question 2")
    time.sleep(1.5)
    print("What animal has a long neck")
    time.sleep(1.0)
    print("A. Frog")
    print("B. Giraffe")
    question2 = input("C. Toad.\n")
    if question2 == "B":
        print("Correct!")
        score = score + 1
    else:
        print("Wrong")
        score = score + 0
    print("Question 3")
    time.sleep(1.5)
    print("What animal has wings")
    time.sleep(1.0)
    print("A. Frog")
    print("B. Tiger")
    question3 = input("C. Bird.\n")
    if question3 == "C":
        print("Correct!")
        score = score + 1
    else:
        print("Wrong")
        score = score + 0
        
    End()
    
 
    

def food_quiz():
    print("test")

def linux_quiz():
    print("test")

def End():
    print("test")
if __name__ == "__main__": main()
