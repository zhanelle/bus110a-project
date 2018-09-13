# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 10:47:08 2017

@author: Zhanelle
"""

import sqlite3
import seaborn
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats


conn = sqlite3.connect('LeVinEmployee.db')

# *Employee Registration Check method=====================================================================*
def PKCheck():
    EmpID = input("To register a new employee, first enter his or her 4-digit EmployeeID: ").strip()

    StripEmpID = EmpID.strip()

    while not StripEmpID:
        StripEmpID = input("EmployeeID cannot be blank. Please provide a 4-digit EmployeeID: ")

    while not StripEmpID.isdigit():
        StripEmpID = input("Sorry, only digits are allowed. Please enter a 4-digit EmployeeID: ").strip()





    while len(StripEmpID) < 4 or len(StripEmpID) > 4:
        StripEmpID = input("EmployeeID cannot be greater or less than 4 digits. Please provide a 4-digit EmployeeID: ")

    with conn:
        cur = conn.cursor()
        try:
            cur.execute("SELECT COUNT (*) FROM Employee WHERE(EmployeeID = '" + StripEmpID + "')")
            results = cur.fetchone()
            while results[0] == 1:
                EmpID = input("That EmployeeID is already in use. Please enter a different one:  ")
                StripEmpID = EmpID.strip()
                cur.execute("SELECT COUNT (*) FROM Employee WHERE(EmployeeID = '" + StripEmpID + "')")
                results = cur.fetchone()
            print("EmployeeID, " + StripEmpID + ", is accepted")

            firstName = input("Please enter first name: ")
            while not firstName:
                firstName = input("First name cannot be blank. Please provide a first name: ")

            lastName = input("Please enter last name: ")
            while not lastName:
                lastName = input("Last name cannot be blank. Please provide a last name: ")

            streetAddress = input("Please enter street address: ")
            while not streetAddress:
                streetAddress = input("Street address cannot be blank. Please provide a street address: ")

            city = input("Please enter city: ")
            while not city:
                city = input("City cannot be blank. Please provide a city: ")

            state = input("Please enter state: ")
            while not state:
                state = input("State cannot be blank. Please provide a state: ")

            zipcode = input("Please enter zipcode: ")
            while not zipcode:
                zipcode = input("Zipcode cannot be blank. Please provide a zipcode: ")

            email = input("Please enter email: ").lower()

            while not email:
                email = input("Email can not be blank. Please provide an email: ")

            with conn:
                cur = conn.cursor()
                try:
                    cur.execute("SELECT COUNT (*) FROM Employee WHERE(Email = '" + email.lower() + "')")
                    results = cur.fetchone()

                    while results[0] == 1:
                        email = input("That email has already been registered. Please enter a different email: ").lower()
                        while not email:
                            email = input("Email cannot be blank. Please provide an email: ").lower()
                        cur.execute("SELECT COUNT (*) FROM Employee WHERE(Email = '" + email + "')")
                        results = cur.fetchone()



                except:
                    print("Connection failed")
            password = input("Please enter password: ").strip()
            while not password:
                password = input("Password cannot be blank. Please provide a password: ").strip()

            cur.execute("Insert INTO Employee values (?,?,?,?,?,?,?,?,?)", (EmpID,firstName, lastName, streetAddress, city,state,zipcode,email,password))

            cur.execute("SELECT * FROM Employee WHERE(EmployeeID = '" + StripEmpID + "')")
            results2 = cur.fetchall()
            print ("Registration Successful")

        except:
            print("Connection Failed")
# *=======================================================================================*

# *Employee Login method==================================================================*
def login():
    userEmail = input("Please enter your registered employee email to log in: ")

    StripUserEmail = userEmail.strip().lower()

    while not StripUserEmail:
        StripUserEmail = input("Email cannot be blank. Please provide an email: ").lower()

    with conn:
        cur = conn.cursor()
        try:
            # belle.bristow@gmail.com
            cur.execute("SELECT COUNT (*) FROM Employee WHERE(Email = '" + StripUserEmail + "')")
            results = cur.fetchone()

            while results[0] !=1:
                StripUserEmail = input ("There is no employee associated with that email. Please enter your registered employee email: ").lower()
                while not StripUserEmail:
                    StripUserEmail = input("Email cannot be blank. Please provide an email: ")
                cur.execute("SELECT COUNT (*) FROM Employee WHERE(Email = '" + StripUserEmail + "')")
                results = cur.fetchone()


            if results[0] == 1:
                password = input("Please enter your password(CaSeSeNsItIvE): ").strip()

                while not password:
                    password = input("Password cannot be blank. Please provide a password: ").strip()

                cur.execute("SELECT COUNT (*) FROM Employee WHERE(Password = '" + password + "' AND Email = '"+ StripUserEmail + "')   ")
                results = cur.fetchone()

                while results[0] != 1:
                    password = input("Password is incorrect. Please try again:  ")
                    while not password:
                        password = input("Password cannot be blank. Please provide a password: ")
                    cur.execute("SELECT COUNT (*) FROM Employee WHERE(Password = '" + password + "' AND Email = '"+ StripUserEmail + "')   ")
                    results = cur.fetchone()

                if results[0] == 1:
                    print("Login Successful")
                    register = input("Would you like to register a user? Please enter 'yes' or 'no': ").strip()

                    while not register:
                        register = input("Response cannot be blank. Please respond 'yes' or 'no': ").strip().lower()

                    while register.lower() != "yes" and register.lower() !="no":
                        register = input("Sorry, please try again.\nIf you would like to register a user, please enter 'yes'.\nEnter 'no' to log out. ").strip()

                    if register.lower() == "yes":
                        PKCheck()
                    elif register.lower() == "no":
                        testquestion = input("Would you like to test wines?\nPlease type '1' to test wine association or '2' to test attribute frequency.\n").strip().lower()
                        while not testquestion:
                            testquestion = input("Response cannot be blank. Please respond with '1' or '2'")
                            
                        while testquestion != "1" and testquestion !="2":
                            testquestion = input("Sorry, please try again.\nType '1' to test wine association or '2' to test attribute frequency.\n").strip().lower()
                            
                        if testquestion == '1':
                            typeOfWine = input("Which wine would you like to test?\nPlease type 'r' for red wine or 'w' for white wine: ")
                            stripTypeOfWine = typeOfWine.strip().lower()
                            
                            while not stripTypeOfWine:
                                stripTypeOfWine = input("Your response was blank. Please provide a response by typing 'r' or 'w': ").strip().lower()
                                
                            while stripTypeOfWine != "r" and testquestion !="w":
                                stripTypeOfWine = input("Sorry, please try again.\nProvide a response by typing 'r' or 'w': \n").strip().lower()
    
                            if stripTypeOfWine == "r":
                                QualityTestRed()
        
                            elif stripTypeOfWine == "w":
                                QualityTestWhite()
                            
                        if testquestion == '2':
                            typeOfWine = input("Which wine would you like to test?\nPlease type 'r' for red wine or 'w' for white wine: \n")
                            stripTypeOfWine = typeOfWine.strip().lower()
    
                            while not stripTypeOfWine:
                                stripTypeOfWine = input("Your response was blank. Please provide a response by typing 'r' or 'w': \n").strip().lower()
    
                            if stripTypeOfWine == "r":
                                RedFrequency()
        
                            elif stripTypeOfWine == "w":
                                WhiteFrequency()


        except:
            print("Connection Failed")
            
# *=======================================================================================*
            
#Test associations for any wine characteristic by using wine characteristic variables
try:
    
    # Use pandas to read the full winequality.csv file
    # sep = ',', tells pandas the files are separated by commas
    # header = 0 tells pandas the header row is the first row of the file
    allWines = pd.read_csv('winequality-both.csv', sep = ',', header = 0)

    # loc function allows us to select specific rows and columns
    # Rows listed first, columns listed second

    # Call the full database and ask it to look for rows
    # Partion into two lists
    red = allWines.loc[allWines['type'] == 'red', :]
    white = allWines.loc[allWines['type'] == 'white', :]
    
    def QualityTestRed():

        WineCharX = "quality"
        testChar = input("You chose to test red wine.\nWhat wine characteristic would you like to test?\nPlease type one of the following:\n'v' for volatile acidity\n'f' for fixed acidity\n'a' for alcohol percent\n'r' for residual sugar").strip().lower()
            
        while not testChar:
            testChar = input("Your response was blank. Please provide a response by typing 'v', 'f', 'a', or 'r': ").strip().lower()
            
        while testChar != "v" and testChar !="f" and testChar !="a" and testChar !="r":
            testChar = input("Sorry, please try again.\nProvide a response by typing 'v', 'f', 'a', or 'r': \n").strip().lower()
            
        if testChar == "v":
            WineCharY = "volatile acidity"
        elif testChar == "f":
            WineCharY = "fixed acidity"
        elif testChar == "a":
            WineCharY = "alcohol"
        elif testChar == "r":
            WineCharY = "residual sugar"
        else:
            print("Please type 'v', 'f', 'a', or 'r': ")
            
        # *Red Wine Correlations ==================================================*
    
        getCorr = scipy.stats.pearsonr(red[WineCharX], red[WineCharY])
    
        #Create string versions to print concatenation
        correlation = str(getCorr[0])
        pValue = str(getCorr[1])
        print("For red wine, the correlation between " + WineCharX + " and " + WineCharY + " is: " + correlation)
        print("With p value of: " + pValue)
    
        seaborn.lmplot(x = WineCharX, y = WineCharY, data = red)
    
        # Create label for chart
        plt.xlabel(WineCharX)
        plt.ylabel(WineCharY)
    
        # Create title for chart
        plt.title("Red Wine: " + WineCharX + " X " + WineCharY)
        
        FaQ()
    
        # *========================================================================*             
            
    def QualityTestWhite():
        WineCharX = "quality"
        testChar = input("You chose to test white wine.\nWhat wine characteristic would you like to test?\nPlease type one of the following:\n'v' for volatile acidity\n'f' for fixed acidity\n'a' for alcohol percent\n'r' for residual sugar").strip().lower()
        
        while not testChar:
            testChar = input("Your response was blank. Please provide a response by typing 'v', 'f', 'a', or 'r': ").strip().lower()
            
        while testChar != "v" and testChar !="f" and testChar !="a" and testChar !="r":
            testChar = input("Sorry, please try again.\nProvide a response by typing 'v', 'f', 'a', or 'r': \n").strip().lower()
        
        if testChar == "v":
            WineCharY = "volatile acidity"
        elif testChar == "f":
            WineCharY = "fixed acidity"
        elif testChar == "a":
            WineCharY = "alcohol"
        elif testChar == "r":
            WineCharY = "residual sugar"
        else:
            testChar = input("Please type 'v', 'f', 'a', or 'r': ").strip().lower()
            
        # White Wine Correlations =================================================*
        
        getCorr = scipy.stats.pearsonr(white[WineCharX], white[WineCharY])
        correlation = str(getCorr[0])
        pValue = str(getCorr[1])
        print("For white wine, the correlation between " + WineCharX + "and " + WineCharY + " is: " + correlation)
        print("With p value of: " + pValue)
        
        seaborn.lmplot(x = WineCharX, y = WineCharY, data = white)
        
        plt.xlabel(WineCharX)
        plt.ylabel(WineCharY)
        
        plt.title("White Wine: " + WineCharX + " X " + WineCharY)
        
        FaQ()
        
        # =========================================================================*
        
    def RedFrequency():
        
        WineChar2 = "quality"
        print("We are going to test the frequency of red wine attributions.")
        TestWineChar = input("What attribution would you like to test?\nPlease type one of the following:\n'v' for volatile acidity\n'f' for fixed acidity\n'a' for alcohol percent\n'r' for residual sugar\n").strip().lower()
        
        while not TestWineChar:
            TestWineChar = input("Your response was blank. Please provide a response by typing 'v', 'f', 'a', or 'r': \n").strip().lower()
            
        while TestWineChar != "v" and TestWineChar !="f" and TestWineChar !="a" and TestWineChar !="r":
            TestWineChar = input("Sorry, please try again.\nProvide a response by typing 'v', 'f', 'a', or 'r': \n").strip().lower()
            
        if TestWineChar == "v":
            WineChar = "volatile acidity"
            WineCharValue = input("To test wine quality freqency, enter a number between " + str(red['volatile acidity'].min()) + " and " + str(red['volatile acidity'].max()) + ": ").strip()
            while not red['volatile acidity'].min() <= float(WineCharValue):
                WineCharValue = input("The value you entered was not within range. Please enter a number between " + str(red['volatile acidity'].min()) + " and " + str(red['volatile acidity'].max()) + ": ").strip()
            while not float(WineCharValue) <= red['volatile acidity'].max():
                WineCharValue = input("The value you entered was not within range. Please enter a number between " + str(red['volatile acidity'].min()) + " and " + str(red['volatile acidity'].max()) + ": ").strip()
                
        elif TestWineChar == "f":
            WineChar = "fixed acidity"
            WineCharValue = input("To test wine quality frequency, enter a number between " + str(red['fixed acidity'].min()) + " and " + str(red['fixed acidity'].max()) + ": ").strip()
            while not red['fixed acidity'].min() <= float(WineCharValue):
                WineCharValue = input("The value you entered was not within range. Please enter a number between " + str(red['fixed acidity'].min()) + " and " + str(red['fixed acidity'].max()) + ": ").strip()
            while not float(WineCharValue) <= red['fixed acidity'].max():
                WineCharValue = input("The value you entered was not within range. Please enter a number between " + str(red['fixed acidity'].min()) + " and " + str(red['fixed acidity'].max()) + ": ").strip()
        
        elif TestWineChar == "a":
            WineChar = "alcohol"
            WineCharValue = input("To test wine quality frequency, enter a number between " + str(red['alcohol'].min()) + " and " + str(red['alcohol'].max()) + ": ").strip()
            while not red['alcohol'].min() <= float(WineCharValue):
                WineCharValue = input("The value you entered was not within range. Please enter a number between " + str(red['alcohol'].min()) + " and " + str(red['alcohol'].max()) + ": ").strip()
            while not float(WineCharValue) <= red['alcohol'].max():
                WineCharValue = input("The value you entered was not within range. Please enter a number between " + str(red['alcohol'].min()) + " and " + str(red['alcohol'].max()) + ": ").strip()
                
        elif TestWineChar == "r":
            WineChar = "residual sugar"
            WineCharValue = input("To test wine quality frequency, enter a number between " + str(red['residual sugar'].min()) + " and " + str(red['residual sugar'].max()) + ": ").strip()
            while not red['residual sugar'].min() <= float(WineCharValue):
                WineCharValue = input("The value you entered was not within range. Please enter a number between " + str(red['residual sugar'].min()) + " and " + str(red['residual sugar'].max()) + ": ").strip()
            while not float(WineCharValue) <= red['residual sugar'].max():
                WineCharValue = input("The value you entered was not within range. Please enter a number between " + str(red['residual sugar'].min()) + " and " + str(red['residual sugar'].max()) + ": ").strip()
            
        else:
            print("Please type 'v', 'f', 'a', or 'r': \n")
 
        # *Red Wine Correlations ==================================================*
        
        InputAttribute = red.loc[red[WineChar]==float(WineCharValue),:]
        WineCharValueDataSet = InputAttribute.loc[:,WineChar2]
    
        seaborn.distplot(WineCharValueDataSet, bins = 10, kde = False)
        plt.title(WineChar + " value " + str(WineCharValue) + " frequencies by " + WineChar2)
        plt.ylabel('Number of Wines')
        plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    
        # *========================================================================*
        
        FaQ()
    
    def WhiteFrequency():
        
        WineChar2 = "quality"
        print("We are going to test the frequency of white wine attributions.")
        TestWineChar = input("What attribution would you like to test?\nPlease type one of the following:\n'v' for volatile acidity\n'f' for fixed acidity\n'a' for alcohol percent\n'r' for residual sugar\n").strip().lower()
        
        while not TestWineChar:
            TestWineChar = input("Your response was blank. Please provide a response by typing 'v', 'f', 'a', or 'r': \n").strip().lower()
            
        while TestWineChar != "v" and TestWineChar !="f" and TestWineChar !="a" and TestWineChar !="r":
            TestWineChar = input("Sorry, please try again.\nProvide a response by typing 'v', 'f', 'a', or 'r': \n").strip().lower()
            
        if TestWineChar == "v":
            WineChar = "volatile acidity"
            WineCharValue = input("To test wine quality freqency, enter a number between " + str(white['volatile acidity'].min()) + " and " + str(white['volatile acidity'].max()) + ": ").strip()
            while not white['volatile acidity'].min() <= float(WineCharValue):
                WineCharValue = input("The value you entered was not within range. Please enter a number between " + str(white['volatile acidity'].min()) + " and " + str(white['volatile acidity'].max()) + ": ").strip()
            while not float(WineCharValue) <= white['volatile acidity'].max():
                WineCharValue = input("The value you entered was not within range. Please enter a number between " + str(white['volatile acidity'].min()) + " and " + str(white['volatile acidity'].max()) + ": ").strip() 
        
        elif TestWineChar == "f":
            WineChar = "fixed acidity"
            WineCharValue = input("To test wine quality freqency, enter a number between " + str(white['fixed acidity'].min()) + " and " + str(white['fixed acidity'].max()) + ": ").strip()
            while not white['fixed acidity'].min() <= float(WineCharValue):
                WineCharValue = input("The value you entered was not within range. Please enter a number between " + str(white['fixed acidity'].min()) + " and " + str(white['fixed acidity'].max()) + ": ").strip()
            while not float(WineCharValue) <= white['fixed acidity'].max():
                WineCharValue = input("The value you entered was not within range. Please enter a number between " + str(white['fixed acidity'].min()) + " and " + str(white['fixed acidity'].max()) + ": ").strip()    
            
        elif TestWineChar == "a":
            WineChar = "alcohol"
            WineCharValue = input("To test wine quality freqency, enter a number between " + str(white['alcohol'].min()) + " and " + str(white['alcohol'].max()) + ": ").strip()
            while not white['alcohol'].min() <= float(WineCharValue):
                WineCharValue = input("The value you entered was not within range. Please enter a number between " + str(white['alcohol'].min()) + " and " + str(white['alcohol'].max()) + ": ").strip()
            while not float(WineCharValue) <= white['alcohol'].max():
                WineCharValue = input("The value you entered was not within range. Please enter a number between " + str(white['alcohol'].min()) + " and " + str(white['alcohol'].max()) + ": ").strip()    
            
        elif TestWineChar == "r":
            WineChar = "residual sugar"
            WineCharValue = input("To test wine quality freqency, enter a number between " + str(white['residual sugar'].min()) + " and " + str(white['residual sugar'].max()) + ": ").strip()
            while not white['residual sugar'].min() <= float(WineCharValue):
                WineCharValue = input("The value you entered was not within range. Please enter a number between " + str(white['residual sugar'].min()) + " and " + str(white['residual sugar'].max()) + ": ").strip()
            while not float(WineCharValue) <= white['residual sugar'].max():
                WineCharValue = input("The value you entered was not within range. Please enter a number between " + str(white['residual sugar'].min()) + " and " + str(white['residual sugar'].max()) + ": ").strip()    
            
        else:
            print("Please type 'v', 'f', 'a', or 'r': \n")
        
            
        # *White Wine Correlations ==================================================*
    
        InputAttribute = white.loc[white[WineChar]==float(WineCharValue),:]
        WineCharValueDataSet = InputAttribute.loc[:,WineChar2]
    
        seaborn.distplot(WineCharValueDataSet, bins = 10, kde = False)
        plt.title(WineChar + " value " + str(WineCharValue) + " frequencies by " + WineChar2)
        plt.ylabel('Number of Wines')
        plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    
        # *========================================================================*
        
        FaQ()
        
    def FaQ():
        question = input("3 additional questions: If you want to learn about volatile acidity concentration, type '1'\nIf you want to learn about correcting overly sweet wines, type '2'\nIf you want to learn about fixed acidity, type '3'\n").strip()
        
        while not question:
            question = input("Your response was blank. Please provide a response by typing '1', '2', or '3': \n").strip()
        
        while question != "1" and question != "2" and question != "3":
            question = input("Sorry, please try again.\nProvide a response by typing '1', '2', or '3': \n").strip().lower()
                
        if question == "1":
            print("Volatile acidity concentration is regulated by the federal Tax and Trade Bureau, \nand allowable levels for various wine styles can be found in the Code of Federal Regulations (CFR). In general, per the CFR: \n'The maximum volatile acidity, calculated as acetic acid and exclusive of sulfur di- oxide, \nis 0.14 g/100 mL for red wine and 0.12 g/100 mL for white wines.' \nThis is equivalent to 1.4 and 1.2 g/L acetic acid for red and white wines, respectively")
            
        elif question == "2":
            print("Overly Sweet Wine: This is the bane of the beginning winemaker and by far the most common wine\nproblem. An overly sweet wine can be corrected in two ways; you can restart fermentation and convert\nthe residual sugar into alcohol or you can blend the sweet wine with a like wine that is bone dry, if you\nhave it. In the first case, restarting fermentation may be a problem in itself. Use a fresh yeast with a high\nalcohol tolerance and sprinkle it over a sample of 1/2 cup of the overly sweet wine mixed with one cup\nof warm water into which 1/2 teaspoon of yeast nutrient has been dissolved. When fermentation begins\nin the sample and becomes very active, add 1/4 cup more wine. Wait 6-8 hours and add another 1/4 cup\nof the wine. Repeat this two more times. After another 6-8 hours, assuming the fermentation is still\ngoing strong, add the sample to the bulk of the overly sweet wine, stir in another 1/2 teaspoon of yeast\nnutrient, and fit the airlock in place. Rack after fermentation has ceased and again after 30 days. The\nresulting wine will contain more alcohol than before, but the excessive sweetness will be gone.")
        
        elif question == "3":
            print("The predominant fixed acids found in wines are tartaric, malic, citric, and succinic. Their respective\nlevels found in wine can vary greatly but in general one would expect to see 1,000 to 4,000 mg/L\ntartaric acid, 0 to 8,000 mg/L malic acid, 0 to 500 mg/L citric acid, and 500 to 2,000 mg/L succinic\nacid. All of these acids originate in grapes with the exception of succinic acid, which is produced by\nyeast during the fermentation process. Grapes also contain ascorbic acid (Vitamin C), but this is lost\nduring fermentation. It is also legal to add fumaric acid as a preservative.")
        
except (KeyError, ZeroDivisionError) as e:
    print (e)

login()
