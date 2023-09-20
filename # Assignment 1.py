# Assignment 1 
# Name: Mikayla Morrison
# Student ID: 501182358

#For this assignment, I wanted to create a program that would calculate some form of 
#credit to help students understand how loans, interest, and payments can become vital and costly aspects of funding a post-secondary education. 

#The following program determines the student's total tuition for their first year of university,maccording to faculty and eligbilibity for entrance scholarships. 
#The figures used pertain only to full-time domestic students (in-province and out of province). 

#It is assumed that the student is unable to pay their tuition in full; so, the program helps students start a line of credit, 
#take out a loan, and begin to pay off their loan over the course of 365 days (interest compounded daily). 

#All of the figures and amounts used in this program are based on the latest information from TMU and several banks/private institutions. 


def faculty_tuition(faculty): 
    #This function calculates the user's tuition/payments to the university based on the faculty defined in the main function. 
    tuition_fee = {"ARTS":7084.00, "COMMUNITY SERVICES":7341.00, "ENGINEERING":10749.50, "SCIENCE":8313.00, "CREATIVE SCHOOL":7462.00, "TED ROGERS SCHOOL OF MANAGEMENT":9226.00}
    #A dictionary; this was used to find the tuition based on the user's faculty. 
    #These figures are based on average costs as defined by the TMU website; https://www.torontomu.ca/current-students/tuition-fees/
    global tuition_base
    #A variable that has been assigned global status using the global keyword: this makes the tuition base (the value of the element in the dictionary) accesible to every function in the program. 
    #This is necessary as the tuition_base becomes essential to the calculation of loan in the function loan_calculation
    tuition_base = float(tuition_fee[faculty.upper()]) #.....not sure if i need to convert this to a float......
    #Retrieves the value based on the key (faculty) in the dictionary. 
    #Converts the value of the key to a float type, and assigns this value to the variable tuition_base. 
    #The variable has now been assigned a value that we will use for other calculations in different functions of the program. 
    
    canada = ["ontario","quebec","alberta","saskatchewan","british colombia","manitoba","new brunwick","newfoundland and labrador","nova scotia","prince edward island","northwest territories","nunavut","yukon"]
    #A list of all the canadian provinces/territories; this will be used to determine whether or not the user will face any additional tuition costs. 
    domestic_response = input("*** In what province/territory in Canada did you graduate from high school?: ")
    #Asks the user for their location; their response will determine whether or not there will be additiona changes to their tuition
    while domestic_response.lower() not in canada: 
        #A while loop that will keep running as so long as the user's response is not in the list Canada 
        print ("***Sorry, that province/territory doesn't seem to exist in Canada...***")
        domestic_response = (input("\n*** To continue, please enter a valid province/territory: "))
        #Loop asks the user for another input (under the same variable name, so that the condition can be checked and so repeatedly and so the loop isn't infinite)
        #Same variable assigned a new value based on new user input; condition is checked again to determine if the loop can be broken/the program continued 
    
    if domestic_response.lower() in canada and domestic_response.lower() != "ontario": 
        #A condition; if the user's response is valid (if the response can be found in the list Canada) and if that response is not Ontario...
        tuition_base += 645.92
        #As per the same TMU tuition fee website, students pay an average of $645.92 more if they are from out-of-province. 
        #This cost is added to tuition_base based on the user's input, and the condition defined in the if statement 
   
    entrance_scholarship = float((input("*** What was your average at the end of your last year in highschool (please enter a number grade with no percent sign): ")))
    #Takes the user's grade as a float point; this value is then stored for use in the following conditions. 
    #The following conditions determine the student's entrance scholarship amount based on their highschool grade. 
    if entrance_scholarship < 70:
        print ("\n*** Hmm, it seems like this average is below a 70%, which means you didn't maintain the average required to enter your program...Sorry, and best of luck with your studies ***")
        quit()
        #If the user's grade is less than 70%, then it is assumed that the student did not maintain the grade necessary to enter their program. 
        #As per the TMU website, the average grade necessary to maintain an offer of entrance into any program is a 70%.
        #At this point, there is basically nothing that we can do for the user; so, the quit() function is used to terminate the rest of the program
    elif entrance_scholarship >= 86.00 and entrance_scholarship < 90.00: 
        #Although it is discouraged, the float point value entered by the user is being directly compared to an integer. 
        #This is due to issues with accuracy/precision errors in regards to floating point values and integers (ex. 95.000000000001(float) does not equal 95 (int))
        tuition_base -= 750
    elif entrance_scholarship >= 90.00 and entrance_scholarship < 95.00: 
        tuition_base -= 1500
    elif entrance_scholarship >= 95.00: 
        tuition_base -= 3000
    #Given that the student had over an 86%, the student is entitled to an entrance scholarship as per the TMU wesbite
    #https://www.torontomu.ca/admissions/scholarships-awards/
    #The conditions above define the grade boundaries for the scholarships and deducts the amount corresponding to the condition, 
    #from the student's total tuition cost.
    
    residence = input("*** Do you plan to live on residence in your first year? (yes/no): ")
    if "y" in residence.lower(): 
        #A "y" indicates that the user said yes (or at least we assume); if the user answers yes, a series of calculations
        #are run to determine how much residence will cost the user. If the answer is not yes, this condition is skipped and so 
        #is the body of code withtin it. 
        tuition_base += 3134.89 + (2454.83*3) + (1434.25*3)
        #If the student plans to live on residence, then another payment is added to their tuition base
        #These figures were based on the average cost of the first payment, the average cost of the other 3 residence charges 
        #during the school year, and the average cost of the meal plan (charged 3 times per year). 
        #https://www.torontomu.ca/calendar/2022-2023/policies-and-procedures/fees-financial/tuition_fees/
   
    print (f"\n*** It looks like your tuition will cost you a total of ${round(tuition_base, 2)} during your first year ***")
    #A formatted string. Contains the total tuition cost and prints it for the user. 
    #The element to be formatted (tuition_base) also uses the round funtion to return a floating point value
    #with a certain number of decimal points. The first value in the bracket is the number that is to be rounded (tuition_base), 
    #and the second value is the number of decimals/points that the float will be rounded two (in this case it will be rounded to 2 decimal points). 

    #End of function. 


def loan_account():
    #This function allows the user to set-up their "account"; this information will be used to access all info regarding their line of credit. 
    print ("\n*** Let's open up a line of credit for you. Please fill out the following information to continue: ***")
    global name 
    #Global keyword is used to make the variable 'name' available throughout the entire program (not local, not just limited to the scope of this function).
    #This variable is not particularly important, but we do call on it in the next function as an interactive compoenent of this program
    name = (input("*** Name: "))
    student_number = (input("*** Student Number: "))
    #The student inputs their student number, and the variable is stored
    while len(student_number) != 9: 
        #The len() function is used to return the number of characters in the string; this value is then used as apart of the condition in the loop 
        print ("\n*** Hm, that doesn't seem to be a valid student number. Your student number should be 9 characters long... ***")
        student_number = (input("*** Please enter a valid student number: "))
        #This loop also gives the user another opporuntity to re-enter a student number that is 9 characters long 
        #This loop will continue to run as so long as the length of the user input for the student number is not equal to 9. 

    #This part of the program was again, intended to be more interactive, so there it is mostly just comparison of strings. 
    
    global password
    #Another global keyword; used to make the variable password global 
    password = (input("*** Please create a password (must include at least one special character and one number): "))
    #User input, gets a password from the user. This password will be used to allow the user to access the informatino they need to 
    #facilitate a loan. You'll notice that the password has a set of conditions; these will be tested in the next lines of code. 
    no_digits = True
    #For now, we use a variable and a boolean to determine that the password has "no digits". This will be checked with the 
    #for statement below. This for statement, filters through each element (x) in the password. 
    for x in password: 
        if x.isdigit(): 
            #If the element of the password at index x (ex. password[0] = the first charcater in the password) is a digit 
            #(tested for using the isdigit() method) then we set no digits to False; this tells us that the password has a digit. 
            no_digits = False
    if no_digits == True: 
        #If the password has no digit (if the boolean value remains true), then we add a digit to the end of the password. 
        #Strings are not mutable, so we use the addition operator to concatenate the string (essentially add a character to it).
        password += "6"
    #The same logic is the code used to check for a digit; there is only a slight difference. 
    special = False
    for y in password: 
        #Again, the for loop filters through each character in the password (y). Here, we use a slightly different method:
        special_characters = ["@","#","$","%","!","?"]
        #A list was created that consisted of all the characters deemed 'special'; the strings in this list will be used 
        #for comparison purposes. 
        if y in special_characters: 
            #If the character in the password at index y, is in the list of special characters, then the 
            #boolean 'special' is set to true. This tells us that special character are present (therefore, the user 
            # password meets this requirement/condition). 
            special = True 
    if special == False: 
    #This condition is tested for once the loop has run through each character in the password; if no special characters are
    #present (if the boolean 'special' is still false), then a special character (in this case, $) is concatenated to the end of the password. 
            password += "$"
        
    #The condition below, was simply meant to notify the user of the modifications to their password; 
    #if the boolean values are False for special, and/or True for no digits, then the "modified" password (that includes the addition of a 
    #digit and/or special character) is printed on the screen. 
    if special == False or no_digits == True: 
        print ("\n*** It looks like your password did not contain a number and/or a special character, so we had to adjust it ***")
        print (f"*** Please make note of your new password: {password}")
    
    #End of function. 


def loan_calculation(tuition_base): 
    #This function serves as the meat of the program; here we will determine a set of values relating to loans, 
    #interest, payments, that ultimately form the user's transaction history. 
    print ("\n" + "*" * 58 + "\n\t*** Welcome to the Bank! ***\n" + "*" * 58)

    password_please = input ("\n*** Please input your password to continue: ")
    #Interactuve; the user inputs the password that they entered (or the password that was modified to meet requirements 
    #as per the conditionals in the function loan_account) so that they can begin to access information related to their loan. 
    while password_please != password: 
        print ("\n*** Password invalid")
        password_please = input ("*** Please try again: ")
    #This loop is meant to run only if the user inputs the wrong password; it will continue to run until the user inputs the corret password. 
    #It will break when password_please (user input) is equal to the password (global variable, inputted by the user earlier on). 
    
    print (f"\n*** Hello {name}! We're delighted to be able to help you fund your first year of education ***")
    #Remember how we made the variable name global? We did it so that we could call it here (in a different function). 
    #Again, this was more for interactive purposes; the variable 'name' isn't particulary important. 
    
    loans = [] 
    payments = []
    #Two empty lists; these lists will have elements added to them later on. Lists are muteable, therefore, we 
    #are able to add/delete/manipulate certain elements within it. Lists are also iterable (we will use this feature 
    # to out advantage in the latter part of this function). 
    loan_paid = 0
    paid = 0
    #Two variables that have been given a value of 0. This value will be manipulated (added onto, or subtracted from)
    #when we begin to run out calculations. 

    run_it = True
    #Another boolean; we will use this value to drive the while loop that allows the user to perform a set of transactions. 
    while run_it == True: 
        service = input ("\n*** Are you here to take out a loan (withdraw) or pay off a loan/pay off tuition (deposit)?: ")
        #The user is asked what action they would like to perform; based on their response, the 2 variables with 
        #a value of 0, and the 2 lists are modified. 
        if service.lower() == "withdraw": 
            #This set of code is run if the user chooses to take out a loan. 
            outstanding_loan = 0
            loan_base = 0
            #Another 2 variables (local variables) are defined here; this will become the base for the calculation of the student loan. 
            #It is defined here and not at the very top of the function due to the nature of the for loop used to calculate the interest 
            #rate/loan payments. If this variable had been put into the for loop, the value would always be equal to 0, as it would be reset 
            #with each iteration. Therefore it needed to be defined outside of the for loop. 
            #It could not go at the top of the function with the other variables either. This is because all values within the list
            #would be added to this variable with each transaction (ex. [1000] + [1000,1000], = 3000; not the intended 2000). 
            remaining_tuition = tuition_base
            #The same logic as above, applies to this variable here; this variable will be used to keep track of how much tution the user 
            #has left to oay after each transaction. 
            #Therefore, the variable had to be defined within the while loop in order for it to work properly.
            credits = float(input ("*** Please enter the amount that you would like to loan: "))
            while credits > tuition_base:
                #This while loop is here to ensure that the user does not take out a loan that is greater than the user's tuition. 
                #This was done so that the loan would be exclusive to the student's tuition payment. This was done mostly for 
                #demonstrative purposes; in real life, the student can borrow up to $60,000 at a time from a private institution. 
                #https://wowa.ca/line-of-credit-canada
                credits = float(input ("*** This amount is greater than your tuition payment...please enter a new loan amount: "))
                #User asked to input another amount, converts string to float; loop is not broken until the loan amount entered is less than the tuition_base. 
            loans.append(credits)
            #The loan value that the user inputs is added to the empty list of loans (given that it meets the requirement as per the condition 
            #defined in the while loop); this list becomes a very important part of the for loop below. 
            for i in range(len(loans)): 
                loan_base += loans[i]
                #This for loop is driven by a range; that range being the length of the list. It will filter through each individual 
                #element (each of the user's loans). The body of the loop calculates the user's loan plus the interest accumulated over the course 
                #of one year (the time until the start if the next school year). 
                outstanding_loan += round((loans[i] * (6.45/100)), 2) 
                #Lets break this calculation down from the inside out. First, in the purple brackets, we divide the interest percentage by 100; this 
                #gives us the interest rate. In the next set of brackets, the loan at the index i (from the list of loans) is multiplied by the interest rate. 
                #This gives us the total amount of interest on the loan. In the next set of brackets, the amount of interest is added to the loan amount 
                #at index i. This gives us the total value of the loan including interest. Finally, the round() method is used to round the result to 
                #2 decimal places. 
                #This calculation then adds the total value of the loan to the variable we defined as 0 earlier on. This variable is called later on in the program to 
                #show the user a record of their debts and payments. 

                #It is also to be noted that while the interest rate is typically fixed for federal loans as well as student loan,
                #the rate (6.45% in this case) can be variable depending on the private institution. 
                #https://www.credible.com/blog/refinance-student-loans/student-loans-compound-interest/
                #https://wowa.ca/line-of-credit-canada
                #In this instance, I used a fixed rate to better reflect a more accurate calculation of a student loan/line of credit. 
                remaining_tuition -= loans[i]
                #This line deducts the loan amount from the tuition; this line basically assumes that the user can only pay their tuition through a loan. 
                #While this is not always the case in real life, this was done for the program, as it is assumed that most students will take out a loan
                #to pay their tuition before the a certain deadline (given that they often do not have the money to do so immediately). 
            outstanding_loan += loan_base
            #The loan_base calculated is added to the outstanding loan; this was done here and not in the loop, because the loop would have kept adding the same value more than once;
            #this means that it would yield a wrong result (a result that would be too large). 

        else: 
            #If the user is not here to take out a loan, the following condition (and the body of code within in) assumes that the user
            #is here to pay off their loan/pay off their tuition. 
            paid = float(input ("*** Please enter the amount that you would like to pay: "))
            #Asks the user for an number; converts the string entered to a float point value. 
            loan_paid += (paid) 
            #Total amount of the loan paid is updated; amount that the user entered is added to it. 
            outstanding_loan -= paid
            #To show that the user is paying off their loan, the amount they paid is deducted from their total loan debt. 
            payments.append(paid)
            #The user that the amount entered is added to the list of payments. 

        print (f"*** Outstanding loan amount: ${round(outstanding_loan, 2)}\n" + f"*** Total amount of loan paid: ${round(loan_paid, 2)}\n" + f"*** Total owed: ${round((outstanding_loan + remaining_tuition), 2)}\n" + f"*** Remaining Tuition: ${round(remaining_tuition,2)}")
        #Formatted strings that are printed to the screen to show the user their balances once their transaction has been completed. 
        #You'll notice that there are a few formatted strings that seem to be using arithmetic operations; this was done as opposed to 
        #storing values in variables as the value would have no other use other than as a display. Therefore, it would be more simple to 
        #just run the calculation in the formatted string. 
        
        run_again = input ("Would you like to perform another transaction? (yes/no): ")
        #Once a single transaction has been performed, the user has the option to continue to make another transaction. 
        #If the user chooses not to, then the function prints the lists (loans and payments; both of which are modified with each transaction) 
        #of the user's transactions before ending completely. 
        if "n" in run_again.lower(): 
            run_it = False
            print ("\n" + "*" * 58 + "\n\t\t*** Transaction History ***" + "\n" + "*" * 58)
            print ("\nLoans: " + f"{loans}")
            print ("Payments: " + f"{payments}")
        #At this point, the function returns to the main function. 
        #At this point, the function returns to the main function.
     
     #End of function. 


if __name__ == "__main__": 
    print ("*" * 58 + "\n*** Welcome to the TMU Undergraduate Loan Calculator! ***\n" + "*" * 58)
 
    faculty_list = ["ARTS", "COMMUNITY SERVICES", "ENGINEERING", "SCIENCE", "CREATIVE SCHOOL", "TED ROGERS SCHOOL OF MANAGEMENT"]
    #A list of strings containing all of the faculties at TMU; the user will have the option to display the list of faculties. 
    #This list will also serve as a tool for comparison to determine the user's faculty (the faculty will also be used in the faculty_tuition function). 
    response = (input("\n*** Before we get started, would you like to see a list of TMU's faculties? (yes/no): "))
    if "y" in response.lower(): 
        #If statement; body of code within it is executed if the user's answer contains y (assumed that if it contains y, then the user is saying yes). 
        print (f"\n{faculty_list}")
        #Formatted string; simply prints the list of faculties for the user on a new line. 
    
    faculty = (input("\n*** To start, please enter your current/intended faculty: "))
    #String from the user input it stored and compared to the elements in the list of faculties.
    while faculty.upper() not in faculty_list: 
        #While loop runs as so long as the user input does not correspond with any of the elements in the list of faculties. 
        print ("\n*** Sorry, this faculty doesn't seem to exist at TMU...***")
        faculty = (input("*** To start, please enter a valid faculty: "))
        #Will continue to loop as so long as the user does not input a faculty within the list of faculties at TMU. 
    
    #After essential information (faculty; a global variable directly used in the first function and essential to the execution of 
    #all other functions) has been collected, all of the functinos in this program are called in the order that they are to be executed. 

    faculty_tuition (faculty) 
    #Uses the parameter of the faculty (value assigned here in the main function) in order to execute find the base tuition fee for the user. 
    loan_account()
    #Loan account was a more interacive section of code; there were no previous parameters that needed to be defined in order for 
    #the function to perform it's operations. Therefore, the parameters were was left blank. 
    loan_calculation (tuition_base)
    #Uses the parameter tuition_base (assigned global status in faculty_tuition function so that it could be accessed here, as well as
    # in the loan_account function) to calculate loans, payments, and interest according to user input. 
    
    #End of function. 

    print ("\n" + "*" * 58 + "\n\t*** Best of luck in your studies! ***\n" + "*" * 58)
    #One final message printed to the user once the entire program has been executed.

    #End of program. 

