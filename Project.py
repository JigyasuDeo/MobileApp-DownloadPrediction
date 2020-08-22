import os
import sys
import time
import pandas
import sklearn
import joblib
import warnings

# About Menu
def AboutUsMenu():
    os.system("cls")
    print("\n\n                                                                        ")
    print("\t\t ---------------------------------------------------------------------- ")
    print("\n                                                                          ")
    print("\t\t                            About US                                    ")
    print("\t\t                         ---------------                                ")
    print("\n                                                                          ")
    print("\t\t        This is about us sections we will have details about us         ")
    print("\t\t                      here is our window                                ")
    print("                                                                            ")
    print("\t\t            Socials                                                     ")
    print("\t\t               1. Dhruv Saini      [ Design and Architeture ]           ")
    print("\t\t               1. Divyansh Gautam  [ Innovator and Testor ]             ")
    print("\t\t               1. Jigyasu Deo      [ Backend and development ]          ")
    print("                                                                            ")
    print("\n\t\t              -------------------------------------                   ")
    print("\t\t                      Press Enter to return                             ")
    print("\t\t ---------------------------------------------------------------------- ")
    print("\t\t                                      - Developed by TechNostalgia      ")

    sys.stdin.read(1)

# Help Menu
def HelpMenu():
    os.system("cls")
    print("\n\n                                                                                  ")
    print("\t\t -------------------------------------------------------------------------------- ")
    print("\n                                                                                    ")
    print("\t\t                                       Help                                       ")
    print("\t\t                                 ---------------                                  ")
    print("\n                                                                                    ")
    print("\t\t                 This is help section here you will find details of               ")
    print("\t\t                          functions and what they do.                             ")
    print("\n                                                                                    ")
    print("\t\t         Prediction Feature :                                                     ")
    print("\t\t     -> This feature based upon user's input predicts number of downloads         ")
    print("\t\t        for their applications.                                                   ")
    print("\t\t               - On platform such as - Google playstore                           ")
    print("                                                                                      ")
    print("\t\t         FeedBack Feature :                                                       ")
    print("\t\t     -> This feature take feedback from the user.                                 ")
    print("                                                                                      ")
    print("\t\t         About US Feature :                                                       ")
    print("\t\t     -> This feature give information of creaters of the application.             ")
    print("                                                                                      ")
    print("\t\t         Credit Feature:                                                          ")
    print("\t\t     -> This feature give credits and links of important information.             ")
    print("\n\n                                                                                  ")
    print("\n\t\t                    -------------------------------------                       ")
    print("\t\t                            Press Enter to return                                 ")
    print("\t\t -------------------------------------------------------------------------------- ")
    print("\t\t                                                - Developed by TechNostalgia      ")

    sys.stdin.read(1)
    
def TakeFeedback():
    os.system("cls")
    num_lines = 1
    with open("Feedback.txt", 'r') as f:
        for line in f:
            num_lines += 1
    line = 1
    f.close()
    if num_lines > 1:
        num_lines = (num_lines // 8) + line
    
    localtime = time.localtime()
    result = time.strftime("%I:%M:%S %p", localtime)
    
    os.system("cls")
    print("\n\n\n\n")
    print("\t\t                        Feedback Form                                 \n")
    print("\t\t ---------------------------------------------------------------------- ")
    print("\n                                                                        ")
   
    FeedbackName = input("\t\t\tEnter Name : ")
    FeedbackEmail = input("\t\t\tEnter Email : ")
    Feedback = input("\t\t\tEnter Feedback : ")
    FeedbackRating = input("\n\t\t\tGive Rating out of 5 : ")
    FileName = open("Feedback.txt", "a")
    FileName.write("[%s] FeedBack No.%d :\n\tName : %s\n\tE-mail Address : %s\n\n\tFeedback : \n\t-> %s\n\n\tRating : %s out of 5 \n\n"%(result,num_lines, FeedbackName, FeedbackEmail, Feedback, FeedbackRating))

    print("\n                                                                         ")
    print("\t\t ---------------------------------------------------------------------- ")
    print("\n\t\t Processing . . . ", end='')
    time.sleep(1.50)

# Feedback Menu
def FeedbackMenu():
    # Menu Design and layout
    os.system("cls")
    print("\n\n                                                                        ")
    print("\t\t ---------------------------------------------------------------------- ")
    print("\n                                                                          ")
    print("\t\t                         Enter Feedback                                 ")
    print("\t\t                      ---------------------                             ")
    print("\n                                                                          ")
    print("\t\t       Thank you for taking this feedback and help us improve           ")
    print("\t\t                          our product.                                  ")
    print("\t\t                                                                        ")
    print("\t\t                 _________________________________                      ")
    print("\t\t                |                                 |                     ")
    print("\t\t                |                                 |                     ")
    print("\t\t                |            Thank You            |                     ")
    print("\t\t                |            Thank You            |                     ")
    print("\t\t                |            Thank You            |                     ")
    print("\t\t                |                                 |                     ")
    print("\t\t                |                                 |                     ")
    print("\t\t                 _________________________________                      ")
    print("\t\t                                 |                                      ")
    print("\t\t                         _________________                              ")
    print("\t\t                                                                        ")
    print("\n                                                                          ")
    print("\t\t ---------------------------------------------------------------------- ")
    print("\t\t                                      - Developed by TechNostalgia      ")    
    print("\t\t                                                                        ",end = " ") 
    print("\n\t\t Press enter to continue . . . ",end = " ")
    # Read a character till it continues
    sys.stdin.read(1)
    TakeFeedback()
    
def CategoryMenu():
    os.system("cls")
    List = ['1. Art and Design','2. Auto and Vehicals', '3. Beauty', '4. Book and Reference',
            '5. Business', '6. Comics', '7. Communication', '8. Dating', '9. Education',
            '10. Entertainment', '11. Events', '12. Finance', '13. Food and Drinks', 
            '14. Game - Action', '15. Game - Adventure', '16. Game - Arcade', '17. Game - Board',
            '18. Game - Card', '19. Game - Casino', '20. Game - Casual', '21. Game - Educational',
            '22. Game - Music', '23. Game - Puzzle', '24. Game - Racing', '25. Game - Roleplaying',
            '26. Game - Simulation', '27. Game - Sports', '28. Game - Strategy', '29. Game - Trivia',
            '30. Game - Word', '31. Health and Fitness', '32. House and Home', '33. Libraries and Demo',
            '34. Lifestyle ','35. Maps and Navigation', '36. Medical', '37. Music and Audio',
            '38. News and Magazines', '39. Parenting', '40. Personalization', '41. Photography', 
            '42. Productivity', '43. Shopping', '44. Social', '45. Sports', '46. Tools',
            '47. Travel and Local', '48. Video Player', '49. Weather'
        ]
    print("\n\n\t\tSelect a category -\n")
    for i in range(0, 48, 3):
        print("\t\t\t {:25} {:25} {:25}" .format(List[i], List[i + 1], List[i + 2]))
    print('\t\t\t',List[48])

# Prediction
def Prediction(res):
    # Take input from user and save that input in user.csv file
    x = pandas.read_csv("user.csv")

    # Loading our model
    
    warnings.filterwarnings("ignore")
    model = joblib.load("App_prediction.pk1")

    # Predicting result
    res = model.predict(x)
    predicted_output = (int)(res[0] * 10000)
    os.system("cls")
    print("\n\n                                                                        ")
    print("\t\t ---------------------------------------------------------------------- ")
    print("\n                                                                          ")
    print("\t\t                             Result                                     ")
    print("\t\t                      ---------------------                             ")
    print("\n                                                                          ")
    print("\n\t\t            Congratualation we have an estimation                     ")
    print("\n\t\t     Predicted Downloads of Application : ",predicted_output           )
    print("\n                                                                          ")
    print("\n                                                                          ")
    print("\t\t ---------------------------------------------------------------------- ")
    print("\t\t                                      - Developed by TechNostalgia      ")

# Prediction
def PredictionMenu():
    os.system("cls")
    print("\n\n\n\n")
    print("\t\t                        Prediction Form                               \n")
    print("\t\t ---------------------------------------------------------------------- ")
    print("\n                                                                          ")
    Size = float(input("\t\t\tEnter size (in MBs): "))
    Price = float(input("\t\t\tEnter price (in ₹) : "))
    Rating = float(input("\t\t\tEnter Rating (out of 5.0): "))

    # Preparing File
    FileName = open("user.csv", "w")
    FileName.write("0")
    for i in range(1, 52):
        FileName.write(",0")
    FileName.close()

    CategoryMenu()
    var = int(input("\n\n\t\t\tEnter your choice : "))
    FileName = open("user.csv", "a")
    FileName.write("\n%.2f,%.2f,%.1f"%(Size, Price, Rating))

    for i in range(1, 50):
        if i == var:
            FileName.write(",1")
        else:
            FileName.write(",0")
    FileName.write("\n")
    FileName.close()

    Prediction(var)

# Credit
def Credit():
    os.system("cls")
    print("\n\n                                                                        ")
    print("\t\t ---------------------------------------------------------------------- ")
    print("\n                                                                          ")
    print("\t\t                             Credits                                    ")
    print("\t\t                      ---------------------                             ")
    print("\n                                                                          ")
    print("\t\t          1. LinkedIN Profiles                                          ")
    print("\t\t          2. Github  [URL]                                              ")
    print("\t\t          3. Dataset [URL - Kagggle]                                    ")
    print("\n                                                                          ")
    print("\t\t          9. Select ALL                                                 ")
    print("\n                                                                          ")
    print("\n                                                                          ")
    print("\t\t ---------------------------------------------------------------------- ")
    print("\t\t                                      - Developed by TechNostalgia      ")

    var = int(input("\t\t Enter your choice : "))
    print("\n\t\t Processing . . . ", end='')
    time.sleep(1.50)

    if var == 1 :
        # Contributers
        os.system("start \"\" https://www.linkedin.com/in/dhruv73")
        os.system("start \"\" https://www.linkedin.com/in/divyansh-g-b00a191a2")
        os.system("start \"\" https://www.linkedin.com/in/jigyasu-d-b5861011a")

    elif var == 2 :
        #Github 
        os.system("start \"\" https://github.com/DS-73/MobileApp-DownloadPrediction")

    elif var == 3 :
        # Dataset 
        os.system("start \"\" https://www.kaggle.com/gauthamp10/google-playstore-apps?select=Google-Playstore-Full.csv")
    
    elif var == 9:
        # Contributers
        os.system("start \"\" https://www.linkedin.com/in/dhruv73")
        os.system("start \"\" https://www.linkedin.com/in/divyansh-g-b00a191a2")
        os.system("start \"\" https://www.linkedin.com/in/jigyasu-d-b5861011a")

        #Github 
        os.system("start \"\" https://github.com/DS-73/MobileApp-DownloadPrediction")
        
        # Dataset 
        os.system("start \"\" https://www.kaggle.com/gauthamp10/google-playstore-apps?select=Google-Playstore-Full.csv")

# First Menu after Loading Screen
def MainMenu():
    flag = 'Y'
    while flag == 'Y' or flag == 'y':
        os.system("cls")
        print("                                                                            ")
        print("\n\n                                                                        ")
        print("\t\t ---------------------------------------------------------------------- ")
        print("\n\n                                                                        ")
        print("\t\t                 Main Menu                                              ")
        print("\t\t                    1. Prediction                                       ")
        print("\t\t                    2. Give Feedback                                    ")
        print("\t\t                    3. Help                                             ")
        print("\t\t                    4. About US                                         ")
        print("\t\t                    5. Credit                                           ")
        print("\n\t\t              -------------------------------------                   ")
        print("\n\n                                                                        ")
        print("\t\t ---------------------------------------------------------------------- ")
        print("\t\t                                      - Developed by TechNostalgia      ")

        var = int(input("\n\n\t         Enter your choice : "))
        
        if var == 1:
            PredictionMenu()
        elif var == 2:
            FeedbackMenu()
        elif var == 3:
            HelpMenu()
        elif var == 4:
            AboutUsMenu()
        elif var == 5:
            Credit()
        else:
            print("\n                 Wrong Input ")
            time.sleep(1.00)
        
        print("\n\n\t         Enter Y to continue to Main Menu : ", end='')
        flag = input().split()[0]
        

if __name__ == "__main__":
    os.system("cls")
    print("\n\n                                                                        ")
    print("\t\t ---------------------------------------------------------------------- ")
    print("\n                                                                          ")
    print("\t\t                             Welcome                                    ")
    print("\t\t                    <--------------------->                             ")
    print("\n                                                                          ")
    print("\t\t               A Product Developed by TechNostalgia                     ")
    print("\t\t                                        - With Love                     ")
    print("\n                                                                          ")
    print("\t\t        Loading Program . . .                                           ")
    print("\n                                                                          ")
    print("\t\t ---------------------------------------------------------------------- ")
    print("\n\n                                                                        ")
    time.sleep(7.00)
    MainMenu()

