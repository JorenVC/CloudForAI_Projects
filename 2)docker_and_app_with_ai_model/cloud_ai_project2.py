################## IMPORT ##################
# This is to see which python version we are using
import pandas as pd
import joblib
import random
import csv

import sklearn

### Change variable
df_Excel_website = pd.read_csv("results.csv")
EndResults_file_path = 'Prediction_records.csv'        
model_path = 'cloud_ai_project2_model.joblib'

print(sklearn.__version__)
################## Loop through all students  ##################

AmountOfRows = len(df_Excel_website)
for i in range(AmountOfRows):
    print(f'\nProcessing line {i + 1}')
    df_Excel = df_Excel_website.iloc[i]

    ################## General info ""Naam, Email""##################
    Student_Name = df_Excel['Naam']
    Student_Email = df_Excel['Email']
    print(Student_Name)
    print(Student_Email)
    ################## Q1 ""What is your country of origin"" ##################

    # Make a new dataframe(df) with the same columns as in the AI tool
    columns = ['Austria','Bangladesh','Belgium','Bulgaria','Czech Republic','France','Greece','Israel','Moldova','Netherlands','Poland','Turkey']
    df1 = pd.DataFrame(columns=columns)

    # Read the value of the excel dataframe
    val_excel = df_Excel['What is your country of origin']

    # Initialize all columns to 0
    df1.loc[0] = [0] * len(columns)

    # Compare the answer from the excel with the list of answers
    if val_excel in columns:
        df1[val_excel] = 1
    else:
        list_length = len(columns)
        rand = random.randint(0, list_length - 1)
        item = columns[rand]
        df1[item] = 1
    
    ################## Q2 ""What score would you give yourself for your international knowledge?"" ##################

    # Make a new dataframe(df) with the same columns as in the AI tool
    columns = ['What score would you give yourself for your international knowledge?']        
    df2 = pd.DataFrame(columns=columns)

    # Read the value of the excel dataframe
    val_excel = df_Excel['What score would you give yourself for your international knowledge?']

    # Initialize all columns to 0
    df2.loc[0] = [0] * len(columns)

    # Place the right data in the right column
    df2['What score would you give yourself for your international knowledge?'] = val_excel


    ################## Q3 ""What score would you give yourself for your intercultural knowledge?"" ##################

    # Make a new dataframe(df) with the same columns as in the AI tool
    columns = ['What score would you give yourself for your intercultural knowledge?']        
    df3 = pd.DataFrame(columns=columns)

    # Read the value of the excel dataframe
    val_excel = df_Excel['What score would you give yourself for your intercultural knowledge?']

    # Initialize all columns to 0
    df3.loc[0] = [0] * len(columns)

    # Place the right data in the right column
    df3['What score would you give yourself for your intercultural knowledge?'] = val_excel


    ################## Q4 ""What score would you give yourself for handling changes?"" ##################

    # Make a new dataframe(df) with the same columns as in the AI tool
    columns = ['What score would you give yourself for handling changes?']        
    df4 = pd.DataFrame(columns=columns)

    # Read the value of the excel dataframe
    val_excel = df_Excel['What score would you give yourself for handling changes?']

    # Initialize all columns to 0
    df4.loc[0] = [0] * len(columns)

    # Place the right data in the right column
    df4['What score would you give yourself for handling changes?'] = val_excel

    ################## Q5 ""How important was it for you to learn new things?"" ##################

    # Make a new dataframe(df) with the same columns as in the AI tool
    columns = ['How important was it for you to learn new things?']        
    df5 = pd.DataFrame(columns=columns)

    # Read the value of the excel dataframe
    val_excel = df_Excel['How important was it for you to learn new things?']

    # Initialize all columns to 0
    df5.loc[0] = [0] * len(columns)

    # Place the right data in the right column
    df5['How important was it for you to learn new things?'] = val_excel

    ################## Q6 ""How open are you to new experiences?"" ##################

    # Make a new dataframe(df) with the same columns as in the AI tool
    columns = ['How open are you to new experiences?']        
    df6 = pd.DataFrame(columns=columns)

    # Read the value of the excel dataframe
    val_excel = df_Excel['How open are you to new experiences?']

    # Initialize all columns to 0
    df6.loc[0] = [0] * len(columns)

    # Place the right data in the right column
    df6['How open are you to new experiences?'] = val_excel

    ################## Q7 ""What were your feelings about studying abroad?"" ##################

    # Make a new dataframe(df) with the same columns as in the AI tool
    columns = ['Anxious','Enthusiastic','Happy','Sad','Shy']

    df7 = pd.DataFrame(columns=columns)

    # Read the value of the excel dataframe
    val_excel = df_Excel['What were your feelings about studying abroad?']
    val_excel = val_excel.item()

    # Initialize all columns to 0
    df7.loc[0] = [0] * len(columns)

    # Compare the answer from the excel with the list of answers
    if val_excel in columns:
        df7[val_excel] = 1
    else:
        list_length = len(columns)
        rand = random.randint(0, list_length - 1)
        item = columns[rand]
        df7[item] = 1

    
    ################## Q8 ""Did you like to travel in your free time?"" ##################

    # Make a new dataframe(df) with the same columns as in the AI tool
    columns = ['No','Yes']

    df8 = pd.DataFrame(columns=columns)

    # Read the value of the excel dataframe
    val_excel = df_Excel['Did you like to travel in your free time?']

    # Initialize all columns to 0
    df8.loc[0] = [0] * len(columns)

    # Compare the answer from the excel with the list of answers
    if val_excel in columns:
        df8[val_excel] = 1
    else:
        list_length = len(columns)
        rand = random.randint(0, list_length - 1)
        item = columns[rand]
        df8[item] = 1

    ################## Q9 ""Did previous experience abroad influence your decision to study abroad?"" ##################

    # Make a new dataframe(df) with the same columns as in the AI tool
    columns = ["Maybe",'No','Yes']

    df9 = pd.DataFrame(columns=columns)

    # Read the value of the excel dataframe
    val_excel = df_Excel['Did previous experience abroad influence your decision to study abroad?']

    # Initialize all columns to 0
    df9.loc[0] = [0] * len(columns)

    # Compare the answer from the excel with the list of answers
    if val_excel in columns:
        df9[val_excel] = 1
    else:
        list_length = len(columns)
        rand = random.randint(0, list_length - 1)
        item = columns[rand]
        df9[item] = 1

    ################## Q10 ""Do you have a desire to experience an international career and gain experience in the labor market abroad?"" ##################

    # Make a new dataframe(df) with the same columns as in the AI tool
    columns = ["Maybe",'No','Yes']

    df10 = pd.DataFrame(columns=columns)

    # Read the value of the excel dataframe
    val_excel = df_Excel['Do you have a desire to experience an international career and gain experience in the labor market abroad?']

    # Initialize all columns to 0
    df10.loc[0] = [0] * len(columns)

    # Compare the answer from the excel with the list of answers
    if val_excel in columns:
        df10[val_excel] = 1
    else:
        list_length = len(columns)
        rand = random.randint(0, list_length - 1)
        item = columns[rand]
        df10[item] = 1

    ################## Q11 ""Which family member do you feel closest to?"" ##################

    # Make a new dataframe(df) with the same columns as in the AI tool
    columns = ["Other",'Parent(s)','Sibling(s)']

    df11 = pd.DataFrame(columns=columns)

    # Read the value of the excel dataframe
    val_excel = df_Excel['Which family member do you feel closest to?']

    # Initialize all columns to 0
    df11.loc[0] = [0] * len(columns)

    # Compare the answer from the excel with the list of answers
    if val_excel in columns:
        df11[val_excel] = 1
    else:
        list_length = len(columns)
        rand = random.randint(0, list_length - 1)
        item = columns[rand]
        df11[item] = 1

    ################## Q12 ""How close are you to your family?"" ##################

    # Make a new dataframe(df) with the same columns as in the AI tool
    columns = ['How close are you to your family?']        
    df12 = pd.DataFrame(columns=columns)

    # Read the value of the excel dataframe
    val_excel = df_Excel['How close are you to your family?']

    # Initialize all columns to 0
    df12.loc[0] = [0] * len(columns)

    # Place the right data in the right column
    df12['How close are you to your family?'] = val_excel

    ################## Q13 ""What is your family income/month in EUR?"" ##################

    # Make a new dataframe(df) with the same columns as in the AI tool
    columns = ['What is your family income/month in EUR?']        
    df13 = pd.DataFrame(columns=columns)

    # Read the value of the excel dataframe
    val_excel = df_Excel['What is your family income/month in EUR?']

    # Initialize all columns to 0
    df13.loc[0] = [0] * len(columns)

    # Place the right data in the right column
    df13['What is your family income/month in EUR?'] = val_excel

    ################## Q14 ""What is your field of study?"" ##################

    # Make a new dataframe(df) with the same columns as in the AI tool
    columns = ['Agriculture and nature','Art and culture','Computer science','Economy and Business','Healthcare','Industrial sciences and technology','Language and Communication']        
    df14 = pd.DataFrame(columns=columns)

    # Read the value of the excel dataframe
    val_excel = df_Excel['What is your field of study?']

    # Initialize all columns to 0
    df14.loc[0] = [0] * len(columns)

    # Compare the answer from the excel with the list of answers
    if val_excel in columns:
        df14[val_excel] = 1
    else:
        list_length = len(columns)
        rand = random.randint(0, list_length - 1)
        item = columns[rand]
        df14[item] = 1

    ################## Q15 ""What is your highest level of education?"" ##################   omvormen naar index

    # Make a new dataframe(df) with the same columns as in the AI tool
    columns = ['What is your highest level of education?']

    df15 = pd.DataFrame(columns=columns)

    # Read the value of the excel dataframe
    val_excel = df_Excel['What is your highest level of education?']

    # Initialize all columns to 0
    df15.loc[0] = [0] * len(columns)

    # Compare the answer from the excel with the list of answers
    edu_list = ['Diploma of higher education','Bachelor degree','Master degree','Doctorate degree','None of the above']

    if val_excel in edu_list:
        index = edu_list.index(val_excel)
        df15['What is your highest level of education?'] = index
    else:
        list_length = len(edu_list)
        rand = random.randint(0, list_length - 1)
        df15['What is your highest level of education?'] = rand


    ################## Q16 ""In what study cycle did you have chance to go abroad?"" ##################   one hot

    # Make a new dataframe(df) with the same columns as in the AI tool
    columns = ['First','None of the above','Other cycle','Second','Third']

    df16 = pd.DataFrame(columns=columns)

    # Read the value of the excel dataframe
    val_excel = df_Excel['In what study cycle did you have chance to go abroad?']

    # Initialize all columns to 0
    df16.loc[0] = [0] * len(columns)

    # Compare the answer from the excel with the list of answers
    if val_excel in columns:
        df16[val_excel] = 1
    else:
        list_length = len(columns)
        rand = random.randint(0, list_length - 1)
        item = columns[rand]
        df16[item] = 1

    ################## Q17 ""How well do you understand English?"" ##################   direct

    # Make a new dataframe(df) with the same columns as in the AI tool
    columns = ['How well do you understand English?']

    df17 = pd.DataFrame(columns=columns)

    # Read the value of the excel dataframe
    val_excel = df_Excel['How well do you understand English?']

    # Initialize all columns to 0
    df17.loc[0] = [0] * len(columns)

    # Place the right data in the right column
    df17['How well do you understand English?'] = val_excel

    ################## Q18 ""Did your university inform you about studying abroad?"" ##################         one hot

    # Make a new dataframe(df) with the same columns as in the AI tool
    columns = ['No','Yes']

    df18 = pd.DataFrame(columns=columns)

    # Read the value of the excel dataframe
    val_excel = df_Excel['Did your university inform you about studying abroad?']

    # Initialize all columns to 0
    df18.loc[0] = [0] * len(columns)

    # Compare the answer from the excel with the list of answers
    if val_excel in columns:
        df18[val_excel] = 1
    else:
        list_length = len(columns)
        rand = random.randint(0, list_length - 1)
        item = columns[rand]
        df18[item] = 1

    ################## Q19 ""Does your university have international teachers?"" ##################

    # Make a new dataframe(df) with the same columns as in the AI tool
    columns = ["I don't know",'No','Yes']

    df19 = pd.DataFrame(columns=columns)

    # Read the value of the excel dataframe
    val_excel = df_Excel['Does your university have international teachers?']

    # Initialize all columns to 0
    df19.loc[0] = [0] * len(columns)

    # Compare the answer from the excel with the list of answers
    if val_excel in columns:
        df19[val_excel] = 1
    else:
        list_length = len(columns)
        rand = random.randint(0, list_length - 1)
        item = columns[rand]
        df19[item] = 1

    ################## Q20 ""Does your university have an international office?"" ##################

    # Make a new dataframe(df) with the same columns as in the AI tool
    columns = ["I don't know",'No','Yes']

    df20 = pd.DataFrame(columns=columns)

    # Read the value of the excel dataframe
    val_excel = df_Excel['Does your university have an international office?']

    # Initialize all columns to 0
    df20.loc[0] = [0] * len(columns)

    # Compare the answer from the excel with the list of answers
    if val_excel in columns:
        df20[val_excel] = 1
    else:
        list_length = len(columns)
        rand = random.randint(0, list_length - 1)
        item = columns[rand]
        df20[item] = 1

    ################## Q21 ""Does your fields of study in your university have internationalization options?"" ##################

    # Make a new dataframe(df) with the same columns as in the AI tool
    columns = ["I don't know",'No','Yes']

    df21 = pd.DataFrame(columns=columns)

    # Read the value of the excel dataframe
    val_excel = df_Excel['Does your fields of study in your university have internationalization options?']

    # Initialize all columns to 0
    df21.loc[0] = [0] * len(columns)

    # Compare the answer from the excel with the list of answers
    if val_excel in columns:
        df21[val_excel] = 1
    else:
        list_length = len(columns)
        rand = random.randint(0, list_length - 1)
        item = columns[rand]
        df21[item] = 1

    ################## Q22 ""Does your university have option for you to do a long term mobility abroad? (more than 3 months)"" ##################

    # Make a new dataframe(df) with the same columns as in the AI tool
    columns = ["I don't know",'Yes']

    df22 = pd.DataFrame(columns=columns)

    # Read the value of the excel dataframe
    val_excel = df_Excel['Does your university have option for you to do a long term mobility abroad? (more than 3 months)']

    # Initialize all columns to 0
    df22.loc[0] = [0] * len(columns)

    # Compare the answer from the excel with the list of answers
    if val_excel in columns:
        df22[val_excel] = 1
    else:
        list_length = len(columns)
        rand = random.randint(0, list_length - 1)
        item = columns[rand]
        df22[item] = 1

    ################## Q23 ""Does your university have a system where you can help a foreign student?"" ##################

    # Make a new dataframe(df) with the same columns as in the AI tool
    columns = ["I don't know",'No','Yes']

    df23 = pd.DataFrame(columns=columns)

    # Read the value of the excel dataframe
    val_excel = df_Excel['Does your university have a system where you can help a foreign student?']

    # Initialize all columns to 0
    df23.loc[0] = [0] * len(columns)

    # Compare the answer from the excel with the list of answers
    if val_excel in columns:
        df23[val_excel] = 1
    else:
        list_length = len(columns)
        rand = random.randint(0, list_length - 1)
        item = columns[rand]
        df23[item] = 1

    ################## Q24 ""Do you have connections with people from other nationalities?"" ##################

    # Make a new dataframe(df) with the same columns as in the AI tool
    columns = ['No','Yes']

    df24 = pd.DataFrame(columns=columns)

    # Read the value of the excel dataframe
    val_excel = df_Excel['Do you have connections with people from other nationalities?']

    # Initialize all columns to 0
    df24.loc[0] = [0] * len(columns)

    # Compare the answer from the excel with the list of answers
    if val_excel in columns:
        df24[val_excel] = 1
    else:
        list_length = len(columns)
        rand = random.randint(0, list_length - 1)
        item = columns[rand]
        df24[item] = 1

    ################## Q25 ""Have you spoken with any alumni or current student who have participated in mobility programs? If so, what insights did they share?"" ##################

    # Make a new dataframe(df) with the same columns as in the AI tool
    columns = ['No','Yes']

    df25 = pd.DataFrame(columns=columns)

    # Read the value of the excel dataframe
    val_excel = df_Excel['Have you spoken with any alumni or current student who have participated in mobility programs? If so, what insights did they share?']

    # Initialize all columns to 0
    df25.loc[0] = [0] * len(columns)

    # Compare the answer from the excel with the list of answers
    if val_excel in columns:
        df25[val_excel] = 1
    else:
        list_length = len(columns)
        rand = random.randint(0, list_length - 1)
        item = columns[rand]
        df25[item] = 1

    ####################################################################################################################################################################################
    ####################################################################################################################################################################################

    ################## Concat all datasets and change panda dataset to Numpy-array  ##################
    df_list = [df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12,df13,df14,df15,df16,df17,df18,df19,df20,df21,df22,df23,df24,df25]
    concat_result = pd.concat(df_list, axis=1)
    # to numpy array 
    result_np = concat_result.values

    ################## Get prediction and save it in a CSV file ##################

    model = joblib.load(model_path)

    predicted_probabilities = model.predict_proba(result_np)
    probabilities_rate_go_Abroad = predicted_probabilities[:, 0].tolist()[0]
    Percentage = round(probabilities_rate_go_Abroad*100,2)

    # To csv file
    data_For_client_CSV = f"{Student_Name} has a {Percentage}% chance to go abroad. ---> ( {Student_Email} )"
    print(data_For_client_CSV)
    

    # Open the file in append mode ('a') and create a csv writer object
    with open(EndResults_file_path, mode='a', newline='') as file:
        writer = csv.writer(file, delimiter='|')  # Use a delimiter that won't appear in your strings
        writer.writerow([data_For_client_CSV])  # Write the string as a single column

    if i + 1 == AmountOfRows:
        print(f'\nAll {AmountOfRows} students have been processed.')
        break