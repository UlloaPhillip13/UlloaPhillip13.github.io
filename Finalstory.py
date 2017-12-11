

def greeting():
    print("Hello ")
    response=input('Can I ask you some questions? (yes/no) ')
    return response

def second_choice():
    print ("Great.....")
    print ("First question:")
    response=input('Do you like Star Wars? (yes/no) ')
    return response

def haters():  #exits the game
    print ("Be gone brainlet")
    print ("*Fire burns you to death*")

def opened():
    print('Nice ')
    print('Another question :)')
    response=input('Are you going to see Episode 8? (yes/no) ')
    return response

def haters():  #exits the gamevndjvnuiaoshuidhauiwvyauidbwandnawnduwadhuwdiwajbuiabwvtyvbefgbswfevbesufnwdbsaiwodauwbdyawnduhawudy8gfueiyfbhsefbseifnbsdhvbwaljhdkbseifjeqfuqwhduaebwfjkrbgbdbgdrbgunsaefunsurgfuwanfkjdnjkwandjabwfbhugbaiuefhuiebgsguibsgeubghbsguiuiebuiadbuiwduabwduibawduibawdbwabduwabduwabduibsakdbksjdjgvdhtytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytytyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
    print ("Be gone brainlet")
    print ("*Fire burns you to death*")
    
def second_choice():
    print ("Great.....")
    print ("First question:")
    response=input('Do You like Star Wars? (yes/no) ')
    return response

    #Enter your code here
def not_opened():
    print("Be gone ")
    print ("*Spikes inpale you causing to bleed out till death slowly*")
    #Enter your code here

    
x = greeting()
if x=="yes":
    y = second_choice()
    if y=="yes":
        opened()
    else:
        not_opened()
else:
    haters()
