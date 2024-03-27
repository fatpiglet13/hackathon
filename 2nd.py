eyes_list =["Light colors", "Blue, green, or gray", "Dark","Brown", "Black"]
hair_list =["Red", "Blond","Dark blond", "Brown", "Black"]
freckles_list= ["Many", "Several", "Few", "Rare", "None"]
duration_list=["Painful blisters", "Mild Blisters", "Mild Burns", "Rare Burns", "No Burns"]
tan_list= ["Never", "Seldom", "Sometimes", "Often", "Always"]
brown_list= ["Never", "Light tan", "Medium tan", "Dark tan", "Deep dark"]
often_list=["Never", "Seldom", "Sometimes", "Often", "Always"]
last_tan_list=["3+ months", "2-3 months", "1-2 months", "Weeks ago", "Days ago"]
skintype_list=["Type 1", "Type 2", "Type 3", "Type 4", "Type 5", "Type 6"]

def format(question):
    formatted=""
    for i in range(len(question)):
        formatted=formatted+str(i)+". "
        formatted=formatted+question[i]+"\n"
    return formatted

print('Welcome to our Tan quiz. We are here to help you decide how to tan safely. Lets find out how long to tan!')

uv_index = int(input("what is the uv?"))

eyes=int(input("What is you eye color?\n"+format(eyes_list)))
hair=int(input("What is your hair color?\n"+format(hair_list)))
freckles=int(input("How many freckles do you have?\n"+format(freckles_list)))
duration=int(input("What hppens when you are in the sun for a long time?\n"+format(duration_list)))
tan=int(input("Do you tan?\n"+format(tan_list)))
brown=int(input("How brown do you get?\n"+format(brown_list)))
often=int(input("How often do you tan?\n"+format(often_list)))
last_tan=int(input("When is the last time you tanned?\n"+format(last_tan_list)))

score=eyes+hair+freckles+duration+tan+brown+often+last_tan

if score == 0 or 1 or 2 or 3 or 4 or 5 or 6:
    print('You have skin type 1: Always Burns and never tans')
elif score == 7 or 8 or 9 or 10 or 11:
    print('You have skin type 2: Burns easily and tans minimally')
elif score == 12 or 13 or 14 or 15 or 16 or 17:
    print('You have skin type 3: Sometimes burns and tans uniformly')
elif score == 18 or 19 or 20 or 21 or 22:
    print('You have skin type 4: Burns Minimally and tans well')
elif score == 23 or 24 or 25 or 26 or 27:
    print('You have skin type 5: Rarely Burns and tans profusely')
elif score == 28 or 29 or 30 or 31 or 32:
    print('You have skin type 6: Never burns')

skintype=int(input("What is your Skin Type?\n"+format(skintype_list)))

if skintype == 0:
    if uv_index == 1 or 2 or 3 or 4:
        print('Apply Sunscreen, Tan 10 minutes in the front, and 10 minutes on the back, Reapply sunscreen, 10 minutes in the front, and 10 minutes on the back')
    elif uv_index == 5 or 6 or 7 or 8 :
        print('Apply Suncreen, Tan for 15 minutes on the front, 15 minutes on the back')
    elif uv_index == 9 or 10 or 11 or 12:
        print ('Apply Sunscreen, Tan 10 minutes in the front, and 10 minutes on the back.')
    elif uv_index == 13 or 14 or 15:
        print ('DONT TAN!!')
if skintype == 1:
    if uv_index == 1 or 2 or 3 or 4:
        print('Apply Sunscreen, Tan 15 minutes in the front, and 15 minutes on the back, Reapply sunscreen, 15 minutes in the front, and 15 minutes on the back')
    elif uv_index == 5 or 6 or 7 or 8 :
        print('Apply Suncreen, Tan for 10 minutes on the front, 10 minutes on the back, Reapply sunscreen, tan for 10 minutes on the front and 10 minutes on the back')
    elif uv_index == 9 or 10 or 11 or 12:
        print ('Apply Sunscreen, Tan 15 minutes in the front, and 15 minutes on the back.')
    elif uv_index == 13 or 14 or 15:
        print ('DONT TAN!!')
if skintype == 2:
    if uv_index == 1 or 2 or 3 or 4:
        print('Apply sunscreen, Tan for 15 minutes on front, 15 minutes on Back, Tan 15 min front, Reapply Sunscreen, 15 min on back, tan 15 min on front, and 15 min on back')
    elif uv_index == 5 or 6 or 7 or 8 :
        print('Apply sunscreen, Tan for 15 minutes on front, 15 minutes on Back,Reapply Sunscreen, Tan 15 min front, 15 min on back')
    elif uv_index == 9 or 10 or 11 or 12:
        print ('Apply Sunscreen, tan for 10 minutes on front and 10 minutes on, tan 10 min front, and 10 min back')
    elif uv_index == 13 or 14 or 15:
        print ('DONT TAN!!')
if skintype == 3:
    if uv_index == 1 or 2 or 3 or 4:
        print('Apply sunscreen, Tan for 15 minutes on front, 15 minutes on Back, Tan 15 min front, Reapply Sunscreen, 15 min on back, tan 15 min on front, and 15 min on back')
    elif uv_index == 5 or 6 or 7 or 8 :
        print('Apply sunscreen, Tan for 15 minutes on front, 15 minutes on Back,Reapply Sunscreen, Tan 15 min front, 15 min on back')
    elif uv_index == 9 or 10 or 11 or 12:
        print ('Apply Sunscreen, tan for 10 minutes on front and 10 minutes on, tan 10 min front, and 10 min back')
    elif uv_index == 13 or 14 or 15:
        print ('DONT TAN!!')
if skintype == 4:
    if uv_index == 1 or 2 or 3 or 4:
        print('Apply sunscreen, Tan for 15 minutes on front, 15 minutes on Back, Tan for 15 minutes on front, 15 minutes on Back, Re Apply Sunscreen, Tan for 15 minutes on front, 15 minutes on Back, Re Apply Sunscreen, Tan for 15 minutes on front, 15 minutes on Back,Tan for 15 minutes on front, 15 minutes on Back')
    elif uv_index == 5 or 6 or 7 or 8 :
        print('Apply Sunscreen, Tan for 15 minutes on front, 15 minutes on Back, Tan for 15 minutes on front, 15 minutes on Back, Re-Apply Sunscreen, Tan for 15 minutes on front, 15 minutes on Back,Tan for 15 minutes on front, 15 minutes on Back')
    elif uv_index == 9 or 10 or 11 or 12:
        print ('Apply Sunscreen, Tan for 15 minutes on front, 15 minutes on Back,Tan for 15 minutes on front, Apply Sunscreen, 15 minutes on Back, Tan for 15 minutes on front, 15 minutes on Back')
    elif uv_index == 13 or 14 or 15:
        print ('DONT TAN!!')
if skintype == 5:
    if uv_index == 1 or 2 or 3 or 4:
        print('Apply sunscreen, Tan for 15 minutes on front, 15 minutes on Back, Tan for 15 minutes on front, 15 minutes on Back, Re Apply Sunscreen,15 minutes on front, 15 minutes on Back,  Tan for 15 minutes on front, 15 minutes on Back, Re Apply Sunscreen, Tan for 15 minutes on front, 15 minutes on Back,Tan for 15 minutes on front, 15 minutes on Back, Re-Apply Sunscreen, 15 minutes on front, 15 minutes on back,15 minutes on front, 15 minutes on back')
    elif uv_index == 5 or 6 or 7 or 8 :
        print('Apply sunscreen, Tan for 15 minutes on front, 15 minutes on Back, Tan for 15 minutes on front, 15 minutes on Back, ReApply sunscreen, Tan for 15 minutes on front, 15 minutes on Back, Tan for 15 minutes on front, 15 minutes on Back, ReApply sunscreen, Tan for 15 minutes on front, 15 minutes on Back, Tan for 15 minutes on front, 15 minutes on Back,  ReApply sunscreen, 15 min front anf 15 min on back')
    elif uv_index == 9 or 10 or 11 or 12:
        print ('Apply sunscreen, Tan for 15 minutes on front, 15 minutes on Back, Tan for 15 minutes on front, 15 minutes on Back, ReApply sunscreen, Tan for 15 minutes on front, 15 minutes on Back, Tan for 15 minutes on front, 15 minutes on Back, ReApply sunscreen, Tan for 15 minutes on front, 15 minutes on Back, Tan for 15 minutes on front, 15 minutes on Back')
    elif uv_index == 13 or 14 or 15:
        print ('DONT TAN!!')

print("PSA: Please stop tanning if signs of burning appear like redness of skin, blistering, ect. Please know that there is no such thing as a safe tan and remember to use SPF.")