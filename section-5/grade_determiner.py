score = int(input("Enter the student's score as an integer: "))

if score >= 90:
    print("The student's score of " + str(score) + " recieved an A.")
else:
    if score >= 80:
        print("The student's score of " + str(score) + " recieved a B.")
    else: 
        if score >= 70:
            print("The student's score of " + str(score) + " recieved a C.")
        else: 
            if score >= 60:
                print("The student's score of " + str(score) + " recieved a D.")
            else:
                print("The student's score of " + str(score) + " recieved an F.")