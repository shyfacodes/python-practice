import random
from datetime import datetime
import time
import math
import os
import shutil


#-----------PROJECT 10-----------#
#--------GRADE CALCULATOR--------#



marks ={
    "Safa":{"math":95,
             "english":80,
             "ordu":80,
             "russian":80},
    "Marwa":{"math":75,
             "english":67,
             "ordu":80,
             "russian":54},
    "Aruba":{"math":65,
             "english":80,
             "ordu":43,
             "russian":80},
    "Anaya":{"math":89,
             "english":64,
             "ordu":40,
             "russian":86},


}






#----------PROJECT  9-----------#
#---------GUESS NUMBER----------#
def load_attempts():
    
    if os.path.exists("guess.txt"):
        with open("guess.txt", "r") as high:
            content =high.read().strip()
        try:
            old = int(content)
            print(f"Best score is {old}")
        except ValueError:
            print("Old score file has invalid/empty data, ignoring it")
            old = None

    else:
        old = None
        print("No old score recorded yet")
    return old

old = load_attempts()



guess = random.randint(1,100)
count_no = 0
while True:
    attempt =int( input("Guess the number (1-100): "))
    count_no += 1
    if attempt == guess:
        print("you guessed correctly")
        break
    elif attempt > guess:
        print("Wrong , your guess is too high")
    elif attempt < guess:
        print("Wrong , your guess is too low")

print(f"You made {count_no} attempts")


if old is None or old > count_no :
    print("new best score!....YOU WIN")
    with open("guess.txt", "w") as num:
        num.write(str(count_no))
else:
    print("old score is best!")


#----------PROJECT  8-----------#
#--------EXPENSE TRACKER--------#

now = datetime.now()
today_date =now.date()

expenses = []
def load_expenses ():
    if not os.path.exists('expenses.txt'):
        return
    with open("expenses.txt", "r") as me:
        for line in me:
            line = line.strip()
            if not line:
                continue
            exp_date ,exp_name, exp_category,exp_amount = line.split(":")
            expenses.append({
                "date" :exp_date.strip(),
                "name": exp_name.strip(),
               "category" : exp_category.strip(),
                "amount" :float( exp_amount.strip())

                })
load_expenses ()
print("="*25)
print("\tEXPENSE TRACKER")
print("="*25)
print("1. Add Expense")
print("2. Search Expense")
print("3. Show All Expense")
print("4. Exit")

while True:
    wish = input("Enter your choice(1-4): ")
    if wish == "1":
        print("you are adding your expenses")
        expense_name = input("Enter Expense Name: ")
        expense_category = input("Enter Expense Category: ")
        expense_amount = float(input("Enter Expense Amount: "))
        with open("expenses.txt", "a") as exp:
            exp.write(f"{today_date} :{expense_name} :{expense_category} :{expense_amount}\n")
            expenses.append({
                "date" :today_date,
                "name" :expense_name,
                "category" : expense_category,
                "amount" : expense_amount

            })
        print("expenses added")
    elif wish == "2":
        print("showing all your expenses by category")
        category = input("Enter Expense Category: ")

        cag_total = 0
        found = False
        for data in expenses:
            if data["category"].lower() == category.lower():
                cag_total =cag_total + data['amount']
                found = True
        if found:
            print(f"Total {category} expense   : {cag_total} ")
        else:
            print(f"NO, expenses found for category {category}")
    elif wish == "3":
        print("All your expenses")
        if not expenses:
            print("no, expenses recorded yet")
        for data in expenses:
            print(f"{data['date']} | {data['name']} | {data['category']} | {data['amount']}")
    elif wish == "4":
        print("Exiting... goodbye!")
        break
    else:
        print("Invalid Choice")
        print("Enter a valid choice")






#----------PROJECT  7-----------#
#---------CONTACT BOOK----------#


print("="*25)
print("\tCONTACT BOOK")
print("="*25)
print("1. Add Contact")
print("2. Search Contact")
print("3. Show All Contact")
print("4. Exit")
contacts = {}
def load_contact ():
    with open("contacts.txt", "r") as me:
        for line in me:
            con_name, con_phone_no = line.strip().split(":")
            contacts[con_name.strip()] = con_phone_no.strip()
load_contact()

while True:
    choice = input("Enter your choice(1-4): ")
    if choice == "1":

        name = input("Enter Contact Name: ")
        phone_no = input("Enter Contact Number: ")
        contacts[name] = phone_no
        with open("contacts.txt", "a") as mobile:
            mobile.write(f"{name} :{phone_no}\n")

    elif choice == "2":
        search = input("Enter Contact Name: ")
        if search in contacts:
            print(f"{search} : {contacts[search]} ")
        else:
            print("contact not found")
    elif choice == "3":
        for name ,phone_no in contacts.items():
            print(f"{name} :{phone_no}")
    elif choice == "4":

        print("Exit")
        break
    else:
        print("Invalid Choice")
        print("Enter a valid choice")


print("="*25)
print()


#-----------PROJECT 6----------#
#-----------QUIZ GAME----------#

score =0
Pyt_info ={


    "Q1":
        {"Question":"What is Python?",
         "answer":"Programming language"},
    "Q2":
        { "Question":"What is a variable in Python?",
          "answer":"Stores data"},
    "Q3":
        { "Question":"What is the difference between a list and a tuple?",
          "answer":"Mutable, Immutable"},
    "Q4":
        { "Question":"What is the purpose of the if statement?",
          "answer":"Decision making"},
    "Q5":
        { "Question":"What is a for loop used for?",
          "answer":"Repeat code"},
    "Q6":
        { "Question":"What is a function in Python?",
          "answer":"Reusable code"},
    "Q7":
        { "Question":"What is the difference between == and =?",
          "answer":"Compare, Assign"},
    "Q8":
        { "Question":"What is a dictionary in Python?",
          "answer":"Key value pairs"},
    "Q9":
        { "Question":"What does the len() function do?",
          "answer":"Counts items"},
    "Q10":
        { "Question":"What is the purpose of the input() function?",
          "answer":"User input"}



}
print("enter your ans of question")

for key in Pyt_info:
    print(key)
    print( Pyt_info [key] ["Question"])
    ans = input("")

    if ans.lower() == Pyt_info[key]["answer"].strip().lower():
         score +=1
    else:
        print ("wrong answer")

total_score = len(Pyt_info)
print(f" TOTAL SCORE  : {total_score}")
print(f" OBTAIN SCORE : {score}")
if score == 10:
    status = "too amazing"
elif score >= 8:
    status = "excellent"
elif score >= 7:
    status = "good"
elif score >= 6:
    status = "star"
else:
    status = "bad"
print(f" STATUS \t  : {status}")
if os.path.exists("result.txt"):
    with open("result.txt", "a") as result:
        result.write(f" TOTAL SCORE :\n{total_score}\n")
        result.write(f"OBTAIN SCORE : {score}\n")
        result.write(f"STATUS : {status}\n")


print("="*25)
print()

#-----------PROJECT 5----------#
#------------PART 5------------#
#--------FOLDER ANALYZER-------#


total = r"C:\Users\Pc\PycharmProjects\PythonProject5"
count_FO =0
count_FI =0
count_IM =0
count_VD =0
count_DC =0
if  os.path.exists(total):
    print("path is here")
    analyzer = os.listdir(total)
    for element in analyzer:
        way = os.path.join(total, element)
        if os.path.isdir(way):
            count_FO += 1
        elif os.path.isfile(way):
            count_FI += 1
        im_ext = ['.jpg', '.jpeg', '.png']
        vd_ext = ['.mp4', '.webm', '.avi']
        dc_ext = ['.pdf']
        file , ext = os.path.splitext(element)
        ext = ext.lower()



        if ext in im_ext:
            count_IM += 1

        elif ext in vd_ext:
            count_VD += 1

        elif ext in dc_ext:
            count_DC += 1
print("="*25)
print("\t   SUMMARY")
print("\tFolder Report")
print("="*25)
print()
print(f"FILES\t    : {count_FI}")
print(f"FOLDER\t    : {count_FO}")
print(f"IMAGES\t    : {count_IM}")
print(f"VIDEOS\t    : {count_VD}")
print(f"DOCUMENTS\t: {count_DC}")
print("="*25)








#-----------PROJECT 5----------#
#------------PART 4------------#
#-----EMPTY FOLDER CLEANER-----#



file_nam = input("enter file name :")
search = r"C:\Users\Pc\PycharmProjects\PythonProject5"
found =False
for  root , dirs, files in os.walk(search):
    if file_nam in files:
        path = os.path .join(root, file_nam)
        print(path)
        found = True
        print(found)

        print("folder or file  is  found")
        break

    elif file_nam in dirs:
        path = os.path .join(root, file_nam)
        print(path)
        found = True
        print(found)
        print("folder or file  is  found")

        break



if not found:
    print(found)
    print("folder or file  is not found")





print("="*25)

#-----------PROJECT 5----------#
#------------PART 3------------#
#-----EMPTY FOLDER CLEANER-----#


empty_folder = r"C:\Users\Pc\PycharmProjects\PythonProject5\download"
del_count = 0
skip_count = 0
if os.path.exists(empty_folder):
    print("folder exists")
    Resources = os.listdir(empty_folder)
    print(Resources)
    for item in Resources:
        article = os.path.join(empty_folder, item)
        if not os.path.isdir(article):
            continue

        if os.listdir(article) is None:
            os.rmdir(article)
            del_count += 1
        else:
            skip_count += 1
    print("="*25)
    print(f"DELETED FOLDER = {del_count}")
    print(f"SKIPPED FOLDER = {skip_count}")
    print("="*25)
else:
    print("folder is not available")
    print("="*25)


#-----------PROJECT 5----------#
#------------PART 2------------#
#------FILE BACKUP MANAGER-----#


bac_folder = r"C:\Users\Pc\PycharmProjects\PythonProject5\Images"
count = 0
print("="*25)
print("FILE BACKUP REPORT")
print("="*25)
if os.path.exists(bac_folder):
    print("folder exists")
    context = os.listdir(bac_folder)

    back_up = os.path.join(bac_folder, "back_up")
    os.makedirs(back_up, exist_ok=True)
    for item in context:
        fl_name = os.path.join(bac_folder, item)
        if os.path.isdir(fl_name):
            continue

        shutil.copy (fl_name, back_up)
        count += 1
        print(f"copied = {item}")
print("="*25)
print(f"total file copied = {count}")
print("back up complete")




print("=" *25)
print()
#-----------PROJECT 5----------#
#------------PART 1------------#
#---AUTOMATIC FILE ORGANIZER---#


my_folder = r"C:\Users\Pc\PycharmProjects\PythonProject5\download"
img_ext = ['.jpg', '.jpeg', '.png']
video_ext = ['.mp4', '.webm', '.avi']
doc_ext = ['.pdf']



Images = os.path.join(my_folder, "image")
Videos = os.path.join(my_folder, "video")
Documents = os.path.join(my_folder, "document")
Others = os.path.join(my_folder, "other")

os.makedirs(Images,exist_ok=True)
os.makedirs(Videos,exist_ok=True)
os.makedirs(Documents,exist_ok=True)
os.makedirs(Others,exist_ok=True)
if os.path.exists(my_folder):
    print("folder is...")

    content = os.listdir(my_folder)
    print(content)

    for item in content:
        name, ext = os.path.splitext(item)
        ext = ext.lower()
        file_name = os.path.join(my_folder, item)
        if os.path.isdir(file_name):
            continue

        if ext in img_ext:
            shutil.move(file_name, Images)
        elif ext in video_ext:
            shutil.move(file_name, Videos)
        elif ext in doc_ext:
            shutil.move(file_name, Documents)
        else:
            shutil.move(file_name, Others)

else:
    print("folder does not exist")
print("="*25)
print()


#-----PROJECT 4-----#
#--FOLDER ANALYZER--#

source_folder =r"C:\Users\Pc\PycharmProjects\PythonProject5\download"

if os.path.exists(source_folder):
    print("folder exists")

    with os.scandir(source_folder) as entries:


        count_folder = 0
        count_file = 0
        count_vid = 0
        count_img = 0
        for entry in entries:
            Img_ext = ['.jpg', '.jpeg', '.png']
            vid_ext = ['.mp4', '.webm', '.avi']
            if entry.is_file():
                count_file += 1
            elif entry.is_dir():
                count_folder += 1

            file_name, ext = os.path.splitext(entry.name)
            ext = ext.lower()
            if ext in Img_ext:
                count_img += 1
            elif ext in vid_ext:
                count_vid += 1

                if os.path.isdir(file_name):
                    continue

    print("="*25)
    print ("summary")
    print(f"{count_file} files")
    print(f"{count_folder} folders")
    print(f"{count_img} images")
    print(f"{count_vid} videos")
    print("="*25)
    print()
else:
    print("folder does not exist")
    print("="*25)
    print()


#-----PROJECT 3-----#
#---PERSONAL DIARY---#

diary = [
    'Write Diary',
    'Read Diary',
    'Exit'
]

now = datetime.now()
today = now.strftime("%d / %m / %Y")
current_time = now.strftime("%H:%M:%S")

for item in diary:
    print(item)


choices =input ("enter your choice :").lower()

if choices == "read diary":
    with open ("diary.txt","r")as journal:
         data = journal.read()
         print(data)
         print("In diary ,I am reading.")

elif choices == "write diary":
    entry = input("enter for diary :")
    with open ("diary.txt","a")as journal:
        journal.write(f"{today}\n{current_time}")
        journal.write("\n")
        journal.write(f"{entry}\n\n")
        print("In diary , I am writing.")

elif choices == "exit":
    print("Diary closed")
else:
    print("invalid choice")

print("="*25)
print()


#-----PROJECT 2-----#
#-----PASSWORD-----#

while True :
    length    = input("Enter password's length : ")
    character = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+-=~`<>?,./:';"
    PASSWORD  =""
    for x in range(int(length)):
        PASSWORD +=random.choice(character)
    print(f"PASSWORD GENERATED :{PASSWORD}")
    with open ("password.txt","a") as password :
        password.write(PASSWORD +"\n")
        print ("password is ready")
    choice = input ("you need more passwords YES / NO ? ")
    if choice.lower() != "yes" :
        break
print("="*25)
print()


#-----PROJECT 1-----#
#----REPORT CARD----#

name = input("enter your name :")

print(f"REPORT CARD OF {name}")
print("="*25)
print("enter your subject marks")
print("="*25)

math_marks = int(input("enter math marks     :"))
eng_marks  =int( input("enter english marks  :"))
comp_marks = int(input("enter computer marks :"))
phy_marks  = int(input("enter physics marks  :"))
urdu_marks = int(input("enter ordu marks     :"))

print("="*25)
print("SUBJECT \t\t MARKS")
print(f"MATH \t\t\t  {math_marks}")
print(f"ENGLISH \t\t  {eng_marks}")
print(f"COMPUTER \t\t  {comp_marks}")
print(f"PHYSICS \t\t  {phy_marks}")
print(f"URDU \t\t\t  {urdu_marks}")

total = math_marks + eng_marks + comp_marks + phy_marks + urdu_marks
total_marks = 500
print("="*25)
print(f"TOTAL MARKS \t  {total}")
print("="*25)

average = total / 5

if average > 90:
    GRADE = 'A'
elif  average  > 80 :
    GRADE = 'B'
elif average > 70:
    GRADE = 'C'
elif average > 60:
    GRADE = 'D'
else:
    GRADE = 'F'

percentage = total/ total_marks * 100

print(f"GRADE \t\t\t {GRADE}")
print(F"average \t\t {average}")
print(f"percentage \t\t {percentage:.2f}")

if GRADE == 'F':
    STATUS = 'FAILED'
else:
    STATUS = 'PASSED'

print(f"STATUS \t\t\t {STATUS}")
print("="*25)
if   os.path.exists ("text.txt"):
    with open("text.txt","a")as data :
        data.write(f'TOTAL          {total}\n')
        data.write(f'AVERAGE        {average}\n')
        data.write(f'PERCENTAGE     {percentage}\n')
        data.write(f'GRADE          {GRADE}\n')
        data.write(f'STATUS         {STATUS}\n')
        print("shy fa")

    print ("you are succeed")

    print("=" * 25)
    print()