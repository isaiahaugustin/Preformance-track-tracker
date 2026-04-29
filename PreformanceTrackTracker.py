# Isaiah Augustin

#Class: Computer Science

# Date: 4/28/2026

#Preformance Track Tracker





preformance = [] 



print("=== Basic track performance ===")

print("Type 'exit' at any time to finish, and results will be saved, performances.text\n")

#This is the beging of the while statment, that is looking for the word "exit" by the user

while True:

    Isaiah = input("Please enter name: ")

    if Isaiah.lower() == "exit":

       break

#Again the user can write whatever they want so they can add whatever they want the program will accept it

    event = input("Enter envent (100m, long jump, high jump, and notes can be added):")

    if event.lower() == "exit":

       break

#One agan here the user can write whatever they want so they can add whatever they want the program will accept it

    performance = input("Enter performance [time/distance]:")

    if performance.lower() == "exit":

        break



    entry = {

        "Isaiah": Isaiah,

        "event": event,

        "performance": performance

    }
    performance.append(entry)




    print("\nEntry added! Current results:")

    #This is where the for loop runs untile the user types "exit"

    for i in performances:

        print(f"- {i['Isaiah']}) | {i['event']} | {i['performance']}")

        #what this does breaks the line after each entry

    print("\n##############Starting New Entry below + previous entry for tracking#####################################\n")



    #This saves the results to a local file wheere that .py is saved, this will take all the results entered so it can be save

with open("performances.txt", "w") as file:

    file.write("******* Final Results *****\n______________________________\n\n")

    for i in performances:

        file.write(f"{i['Isaiah']} - {i['event']} - {i['performance']}\n -------------------------------------------------\n")



print("n=== Final Results ===")

for i in performances:

    print(f"{i['Isaiah']} - {I['event']} - {I['performance']}")



 #This is what will save the result after the word "exit" is typed

    print("\nResults saved to 'performances.txt'.")



 #This will be the final message to show the while loop works when the user types in exit and then prints it

    print("tracking complete, after user type exit.")