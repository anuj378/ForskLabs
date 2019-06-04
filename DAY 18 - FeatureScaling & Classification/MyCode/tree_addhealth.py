"""
For this Code Challenge, The National Longitudinal Study of Adolescent to Adult Health (Add Health) data set, an ongoing (longitudinal) survey study that began in the mid-1990s is used. The project website URL is:

http://www.cpc.unc.edu/projects/addhealth/.

This large data set is available online from the University of North Carolina's
Carolina Population Center, 
#http://www.cpc.unc.edu/projects/addhealth/data.


Import tree_addhealth.csv

 
The attributes are:

 
BIO_SEX: 1 = male 0 = female    

HISPANIC: 1=Yes,0=No    

WHITE : 1=Yes,0=No

BLACK : 1=Yes,0=No          

NAMERICAN: 1=Yes,0=No                      

ASIAN: 1=Yes,0=No                      

ALCEVR1: ever drank alcohol(1=Yes,0=No)   

marever1: ever smoked marijuana(1=Yes,0=No)    

cocever1: ever used cocaine(1=Yes,0=No)                

inhever1: ever used inhalants(1=Yes,0=No)             

cigavail: cigarettes available in home(1=Yes,0=No)

PASSIST: parents or public assistance(1=Yes,0=No)

EXPEL1: ever expelled from school(1=Yes,0=No)

TREG1: Ever smoked regularly(1=Yes,0=No)


Explanatory Variables:


Age

ALCPROBS1:alcohol problems 0-6

DEP1: depression scale

ESTEEM1: self esteem scale       

VIOL1:violent behaviour scale

DEVIANT1: deviant behaviour scale     

SCHCONN1: school connectedness scale       

GPA1: gpa scale  4 points)

FAMCONCT: family connectedness scale       

PARACTV:parent activities scale

PARPRES:parental presence scale

 

Build a classification tree model evaluating if an adolescent would smoke 
regularly or not based on: gender, age, (race/ethnicity) Hispanic, White, 
Black, Native American and Asian, alcohol use, alcohol problems, marijuana use,
cocaine use, inhalant use, availability of cigarettes in the home, depression,
and self-esteem.

Build a classification tree model evaluation if an adolescent gets expelled or
 not from school based on their Gender and violent behavior.
Use random forest in relation to regular smokers as a target and explanatory 
variable specifically with Hispanic, White, Black, Native American and Asian.

(Please make confusion matrix and also check accuracy score for each and every
section)

file_name - "tree_addhealth.py"

"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv("tree_addhealth.csv")
for i in data:
    data[i] = data[i].fillna(data[i].mode()[0])

fe = data[['BIO_SEX','age','WHITE','BLACK','HISPANIC','NAMERICAN','ASIAN',
           'ALCEVR1','ALCPROBS1','marever1','cocever1','inhever1','cigavail',
           'DEP1','ESTEEM1']].values
la = data["TREG1"].values

from sklearn.model_selection import train_test_split as tts
ftr,fte,ltr,lte = tts(fe,la,test_size=.2,random_state=0)


from sklearn.tree import DecisionTreeClassifier
classi = DecisionTreeClassifier()
classi.fit(ftr,ltr)
pred = classi.predict(fte)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(pred,lte)


from sklearn.metrics import accuracy_score as score
m1 = score(lte,pred)

print ("Accuracy Score of the Model part 1 : "+str(round(m1*100,2))+"%")




##############
fe = data[["BIO_SEX","VIOL1"]].values
la = data["EXPEL1"].values


ftr,fte,ltr,lte = TTS(fe,la,test_size=.2,random_state=0)


classi.fit(ftr,ltr)
pred = classi.predict(fte)


cm = confusion_matrix(pred,lte)

m2 = score(lte,pred)

print ("Accuracy Score of the Model part 2 : ",(round(m2*100,2)),"%")



######################
fe = data[['WHITE','BLACK','HISPANIC','NAMERICAN','ASIAN']].values
la = data["TREG1"].values

ftr,fte,ltr,lte = TTS(fe,la,test_size=.2,random_state=0)

from sklearn.ensemble import RandomForestClassifier
classi = RandomForestClassifier(n_estimators=10, 
                                random_state=0)
classi.fit(ftr,ltr)
pred = classi.predict(fte)

cm = confusion_matrix(pred,lte)

m3 = accuracy_score(lte,pred)

print ("Accuracy Score of the Model 3 : ",(round(m3*100,2)),"%")