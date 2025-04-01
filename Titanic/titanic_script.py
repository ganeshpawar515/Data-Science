import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
titanic = pd.read_csv('tested.csv')
plt.style.use("fivethirtyeight")
print(titanic.columns)
print(titanic)

male_count_filt = titanic.Sex=="male"
female_count_filt = titanic.Sex=="female"
male_count = titanic[male_count_filt]["Sex"].size
female_count = titanic[female_count_filt]["Sex"].size
total_passenger_count=titanic.index.size
# print(total_passenger_count)

#@Visualize::male and female percentage on ship (pie chart)
male_pct=(male_count/total_passenger_count)*100
female_pct=(female_count/total_passenger_count)*100
# print('Males on ship: ',male_pct.__round__(2))
# print('Females on ship: ',female_pct.__round__(2))

#@Visualize::distribution of people on ship by age (Bar chart)
titanic.dropna(subset=["Age"],inplace=True)

age_upto_20_count=(titanic["Age"]<=20).sum()
age_upto_20_filt=(titanic["Age"]<=20)

survived_filt = titanic["Survived"]==1

age_upto_20_survived=((age_upto_20_filt) & survived_filt).sum()
print("age upto 20: ",age_upto_20_count," survived: ", age_upto_20_survived)

age_21_30_filt=((titanic["Age"]>20) & (titanic["Age"]<=30))
age_21_30_count=age_21_30_filt.sum()
age_21_30_survived=((age_21_30_filt)&survived_filt).sum()
print("age 21 to 30: ",age_21_30_count," survived: ",age_21_30_survived)

age_31_50_filt=((titanic["Age"]>30) & (titanic["Age"]<=50))
age_31_50_count =age_31_50_filt.sum()
age_31_50_survived=((age_31_50_filt)&survived_filt).sum()
print("age 31 to 50: ",age_31_50_count," Survived: ",age_31_50_survived)

age_51_more_filt=(titanic["Age"]>50)
age_51_more_count=age_51_more_filt.sum()
age_51_more_survived=((age_51_more_filt)&survived_filt).sum()
print("age 51 and more: ",age_51_more_count," survived: ",age_51_more_survived)

print("Data not available: ",titanic.Age.isna().sum())

print((titanic["Survived"]==1).sum())

#@Bar Graph: survivors by age group
#passengers Distribution by age
width=0.25
x_labels=["upto_20","21_30","31_50","51_more"]
x_indexes=np.arange(len(x_labels))

passengers_distribution=[age_upto_20_count,age_21_30_count,age_31_50_count,age_51_more_count]
plt.bar(x_indexes,passengers_distribution,width=width, label="Total Passengers")
#Survived
y_survived=[age_upto_20_survived,age_21_30_survived,age_31_50_survived,age_51_more_survived]
plt.bar(x_indexes+width,y_survived,width=width,label="Survived")
plt.xticks(ticks=x_indexes,labels=x_labels)
plt.title("survivors by age group")
plt.xlabel("Age Groups")
plt.ylabel("Number of Passengers")
plt.legend()
plt.tight_layout()
plt.show()

#@Visualize:Pie Passenger Distribution by embarking port
labels,values = titanic["Embarked"].value_counts().index, titanic["Embarked"].value_counts().values
print(labels,values)
colors = ["#ff9999","#66b3ff","#99ff99"]
plt.title("Passengers by Embarking Port")
plt.pie(values, labels=labels,wedgeprops={"edgecolor":"black"},autopct="%1.1f%%",shadow=True,explode=[0.1,0,0],colors=colors    )
plt.show()