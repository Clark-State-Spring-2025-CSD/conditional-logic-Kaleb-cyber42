#Updated 1 Feb 2025
#Create a program that will ask the user for a number between 1 and 12. You may assume the input is correct.
#After getting the number display which season it is. The ranges are:
#Spring: 3,4,5
#Summer: 6,7,8
#Fall: 9,10,11
#Winter 12,1,2
#Here is a sample output:
#What month is it? (1-12): 2
#The current season is Winter.
#For an extra 2 points, display the month as all. So the output becomes:
#What month is it? (1-12): 2
#The month is February and the current season is Winter.
#Remember to also complete the flowchart. It is strongly advised that you do the flowchart first,
#as this will help you write the code.

x = int(input("What month is it? (1-12): "))


if x == 3 or x == 4 or x == 5: 
    print("The current season is Spring.")

if x == 6 or x == 7 or x == 8:
    print("The current season is Summer.")

if x == 9 or x == 10 or x == 11:
    print("The current season is Fall.")

if x == 12 or x == 1 or x == 2:
    print("The current season is Winter.")
    
