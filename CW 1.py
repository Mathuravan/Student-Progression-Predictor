#I declare that my work contains no examples of misconduct,such as plagiarism,or collusion.
#Any code taken from other sources is referenced within my code solution.
#IIT ID:20221696
#WOU iD:w1998740
#Name: Jeyakumar Mathuravan
#Date: 21/04/2023
# Initialize variables for histogram

#part 1


progress_count = 0
trailer_count = 0
retriever_count = 0
exclude_count = 0
list_format = []
pass_list=[]
defer_list=[]
fail_list=[]

credits_list = [0, 20, 40, 60, 80, 100, 120]


# Define function to get credits input from user and validate it
def get_credits(prompt):
    while True:
        try:
            credits = int(input(prompt))
        except ValueError:
            print("Integer required")
        else:
            if credits not in credits_list:
                print("Out of range")
            else:
                return credits

# Loop to allow staff member to predict progression outcomes for multiple students
while True:
    # Get credits input from user
    pass_credits = get_credits("Enter your total PASS credits: ")
    defer_credits = get_credits("Enter your total DEFER credits: ")
    fail_credits = get_credits("Enter your total FAIL credits: ")
    
    total_credits = pass_credits + defer_credits + fail_credits
    if total_credits != 120:
        print("Total incorrect")
        
    elif pass_credits == 120:
        print("Progress")
        progress_count += 1
        list_format.append("Progress")
        
    elif pass_credits == 100 and defer_credits <= 20:
        print("Progress (module trailer)")
        trailer_count += 1
        list_format.append("Progress (module trailer)")
        
    elif pass_credits >= 20 and defer_credits == 0:
        print("Exclude")
        exclude_count += 1
        list_format.append("Exclude")
    else:
        print("Module retriever")
        retriever_count += 1
        list_format.append("Module retriever")
        
    pass_list.append(pass_credits)
    defer_list.append(defer_credits)
    fail_list.append(fail_credits)
        
    # Ask user if they want to continue or quit
    while True:
        choice = input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ")
        if choice.lower() == "q":
            # Display histogram and quit loop
            print("---------------------------------------------------------------")
            print("Histogram")
            print("Progress  {} : {}".format(progress_count, "*"*progress_count))
            print("Trailer   {} : {}".format(trailer_count, "*"*trailer_count))
            print("Retriever {} : {}".format(retriever_count, "*"*retriever_count))
            print("Exclude   {} : {}".format(exclude_count, "*"*exclude_count))
            print("{} outcomes in total.".format(progress_count+trailer_count+retriever_count+exclude_count))
            print("---------------------------------------------------------------")
#part 2
            print("\n part 2: ")
            for i in range(len(list_format)):
                print("{} - {}, {}, {}".format(list_format[i], pass_list[i], defer_list[i], fail_list[i]))
            exit()
        elif choice.lower() == "y":
            break
        else:
            print("Please enter 'y' or 'q'")
