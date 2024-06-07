# -*- coding: utf-8 -*-
"""
@author: Joren

Pyton for AI Project: Exams
De bedoeling is om te voorspellen wat de score gaat zijn van het wiskunde examen voor een student.

df = De dataset zonder aanpassingen
df2 = De dataset met zonder NaN values (ingevuld met random values)

# 50 random value pakken om lege value in dataset te steken
# print(dfnp.shape) #(1000,8) # dfnp[0] tot dfnp[999]

df = pd.read_csv("exams.csv")
for n in range(50):
    rand = random.randint(0, 999)
    rand_feature = random.randint(0, 7)
    print(f"Prev {n+1}: plaats {rand} \n{df.iloc[rand]}\n")
    df.iloc[rand,rand_feature] = "NA"
    df.to_csv("exams.csv", index=False)
    print(f"New {n+1}: plaats {rand} \n{df.iloc[rand]}\n")
"""


"""
######################## 1. Import ########################
"""
from joblib import dump
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OrdinalEncoder
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error,confusion_matrix
from sklearn import preprocessing
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
import random



"""
######################## 2. Dataset importeren + histograms ########################
"""
df = pd.read_csv("exams.csv")
feature_names = df.columns

# Histograms
hist_readingScore = df["reading score"]
hist_writingScore = df["writing score"]
hist_math = df["math score"]
n_bins = 10

# Histogram hist_readingScore
# plt.subplots(1)
# plt.hist(hist_readingScore,n_bins,color = "red", ec="black")
# plt.ylabel("Count")
# plt.xlabel("Reading score")

# # Histogram hist_Writing score
# plt.subplots(1)
# plt.hist(hist_writingScore,n_bins, color = "green", ec="black")
# plt.ylabel("Count")
# plt.xlabel("Writing score")

# # Histogram hist_math
# plt.subplots(1)
# plt.hist(hist_math,n_bins,ec="black")
# plt.ylabel("Count")
# plt.xlabel("Math score")

# plt.show()


"""
######################## 3. Preparing data / Feature engeneering ########################

# Hier wordt de dataset klaar gemaakt zodat een model er mee kan werken.
#   3.1) MISSING DATA handeling
#   3.2) Encoding categorical features
#   3.3) Split data
#   3.4) Min-max scaling
"""
## 3.1 MISSING DATA handeling

df_isnull = df.isnull()
index_NaN_arr = np.argwhere(df_isnull.values == 1)  # Zoek naar de indexen waar er een NaN value is
len_index = len(index_NaN_arr)                      # Totaal aantal missing data
Colm_Name_Incl_NaN = []                             


# Zoeken naar missing data
print(f"\nLijst van Missing data per feature: {len_index} missing values\n")
for n in df:
    val_unique_arr = pd.unique(df_isnull[n])        # Zet alle unique values van een kolom in een array.
    nr_nan = (df_isnull[n] == True).sum()           # Tel de True waardes in de kolom True == NaN
    if True in val_unique_arr:                      # Geef alle kolommen die een Nan waarde hebben
        print(f"{n} heeft {nr_nan} NaN values")
        Colm_Name_Incl_NaN.append(n)                # Kolom namen opslagen waar Nan in voorkomt

# Invullen van missing data (random gekozen)
print(f"\nLijst van gecorrigeerde data per feature: {len_index} gecorrigeerde values\n")
df2 = df.values
teller = 0

for index_val in index_NaN_arr:
    teller = teller + 1
    colomn = index_val[1]                           # kolom index van de NaN values
    row = index_val[0]                              # rij index van de NaN values
    feature_title = feature_names[colomn]           # kolom naam van de NaN values
    colm_nonNaN = df[feature_title].dropna()        # NaN values verwijderen in kolom
    unique_vals = pd.unique(colm_nonNaN)            # alle unique values van de kolom zonder NaN
    rand_nr = random.randint(0, len(unique_vals)-1) # random
    new_val = unique_vals[rand_nr]                  # random value gekozen uit de lijst van unieke values van een bepaalde kolom
    print(f"{teller: 3}: In {index_val} is {df2[row][colomn]} veranderd naar {new_val} {type(new_val)}")
    df2[row][colomn] = new_val

print("---------------------------------------------\n\n")
df3_npToPd = pd.DataFrame(df2,columns=feature_names)
df3 = df3_npToPd.astype({"math score": 'float64', "reading score": 'float64', "writing score": 'float64'})


"""
######################## 3.2) Encoding categorical features ########################
"""
# Selecteren van de categorical kolommen
CatCol = df3.select_dtypes("object")
CatCol_featureNames = CatCol.columns
NumCol = df3.select_dtypes("float64")
arr_CatCol = CatCol.values

# Categorical kolommen omvormen naar numerical kolommen
enc = OrdinalEncoder()
enc.fit(arr_CatCol)
enc_cat = enc.categories_
df3_CatCol_to_num = enc.transform(arr_CatCol)

#concat df3_CatCol_to_num met df3 numerical kolommen
df3_CatCol_to_num_pd = pd.DataFrame(df3_CatCol_to_num,columns=CatCol_featureNames)
df4 = pd.concat([df3_CatCol_to_num_pd,NumCol], axis='columns')

print("Dit is de dataset VOOR feeature engeneering:\n")
print(f"{df.info()}\n\n")
print("Dit is de dataset NA feeature engeneering:\n")
print(f"{df4.info()}")
print("---------------------------------------------\n\n")


"""
######################## 3.3) Split data ########################
"""
x_pd = df4.drop(columns=['math score'])
y_pd = df4['math score']

x = df4.drop(columns=['math score']).values
y = df4['math score'].values


"""
######################## 3.4) Min-max scaling ########################
"""
# x scaling
scaler_minmax = preprocessing.MinMaxScaler()
x_minmax = scaler_minmax.fit_transform(x)

print("Min-max scaling:\n")
print(f"min_max_scaler.scale_ : {scaler_minmax.scale_}\n")

print("x_minmax:\n")
print(f"{x_minmax}\n\n")
print("---------------------------------------------\n\n")


"""
######################## 4. plotting ########################
Aan de hand van de heatmap zie je welke features een correlatie hebben 
met de "math score" feature. Een waarde boven de 0,2 en onder de -0,2 beschouw 
ik als een feature dat invloed heeft op de eind waarde. Je kan dan 
de feature "parental lvl of education" en "test prep course" verwijderen. 
Dit zou normaal weinig invloed mogen geven op het eind resultaat.
"""

# heatmap correlation van scaling df
x_minmax_df = pd.DataFrame(x_minmax,columns=x_pd.columns)
heatmap_scal = pd.concat([x_minmax_df,y_pd], axis='columns')

# sns.heatmap(heatmap_scal.corr(),cmap="YlGnBu", annot=True, fmt=".2f", linewidth=.5)

# Reading score plot
# plt.subplots(1)
# plt.scatter(x_minmax_df["reading score"],y_pd)
# plt.ylabel("math score")
# plt.xlabel("reading score")

# # Writing score plot
# plt.subplots(1)
# plt.scatter(x_minmax_df["writing score"],y_pd)
# plt.ylabel("math score")
# plt.xlabel("writing score")

# plt.show

# verwijderen onnodige features voor dimensionality reduction
x_minmax = x_minmax_df.drop(columns=['parental level of education','test preparation course']).values


"""
######################## 5. Bouw model ########################
"""
#Linear Regression model

x_train,x_test,y_train,y_test = train_test_split(x_minmax,y,test_size=0.2)

linreg = LinearRegression()
linreg.fit(x_train,y_train)
y_pred = linreg.predict(x_test)

dump(linreg, 'Cloud_AI_Project1_model.joblib')

print(f"De score van het LinReg model 3 (Accuracy): {linreg.score(x_test, y_test)}")
print(f"De score van het LinReg model 3 (MSE): {mean_squared_error(y_test, y_pred)}")
print(f"De score van het LinReg model 3 (MAE): {mean_absolute_error(y_test, y_pred)}")
print(f"De score van het LinReg model 3 (r2_score): {r2_score(y_test, y_pred)}")
print("---------------------------------------------\n\n")


# y_test, y_pred plot
# x_line = np.linspace(20,100)
# y_line = x_line
# plt.subplots(1)
# plt.scatter(y_test, y_pred)
# plt.plot(x_line,y_line,"r")
# plt.xlabel("y_test")
# plt.ylabel("y_pred")
# plt.show