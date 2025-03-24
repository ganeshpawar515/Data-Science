import pandas as pd

titanic  = pd.read_csv('tested.csv',index_col='PassengerId')

#@Basic
# print(titanic.columns)

# survived = titanic[titanic["Survived"]==1]["Survived"].count()
# not_survived = titanic[titanic["Survived"]==0]["Survived"].count()
# print("survived: ",survived)
# print("not survived: ",not_survived)

# print(titanic.shape)
# print(titanic[['Name','Age','Survived']].iloc[[0,1],0])
# print(titanic.loc[[0,1],['Name','Age','Survived']])

print(titanic.shape)

#@Index
# titanic.set_index('PassengerId',inplace=True)
# print(titanic[["Embarked"]].value_counts())
# print(titanic.loc[0:2,'Name':'Age'])
# print(titanic.index)
# print(titanic.loc[901,'Name'])
# titanic.reset_index(inplace=True)

titanic.sort_index(inplace=True)
df=titanic[['Name','Sex','Age','Survived']].head(10)

#@Filters
# filt2 = (df['Sex']=='male')
# filt = (df['Age']>30) & (df['Sex']=='male')
filt =  (df['Age']>30) | (df['Sex']=='male')

# print(filt)

# print(df[filt])

# print(df.loc[~filt])

'''
age_50_plus_surviver_filt=(titanic['Age']>50)&(titanic['Survived']==1)
age_50_plus_surviver_count=titanic[age_50_plus_surviver_filt]
print(age_50_plus_surviver_count.count())
'''
# print(titanic[(titanic["Age"]>30) & ( titanic["Sex"]=="male")].loc[(titanic["Embarked"] == 'S') | (titanic["Embarked"] == 'Q')]  )

#IsIn
embarks=["Q"]
filt = titanic["Embarked"].isin(embarks)
filt2=(titanic["Age"]>30) & ( titanic["Sex"]=="male")

#stringify value then check
mr_filter=titanic["Name"].str.contains('Mr', na=False)
# print(titanic.loc[mr_filter,'Name'])

#Change column Name
# titanic.columns=[col.upper() for col in titanic.columns]

# titanic.rename(columns={'Ticket':"TicketNo"},inplace=True)

# print(titanic.head(5))
# titanic.loc[892:895,["Name","Sex"]]=["Molly",'female']
# titanic.at[892,"Name"]="Molly"

# filt=(titanic["Ticket"]=="330911")

# titanic.loc[filt,"Name"]="Mot"

# titanic["Name"].str.lower()

# print(titanic["Name"].str.lower())


# .apply(func)
'''
def update_name(name):
    return name.lower()

titanic.Name=titanic.Name.apply(update_name)
titanic.Name=titanic.Name.apply(lambda x:x.upper())
'''

# print(titanic.apply(len,axis='columns'))

data = {
    "first":["John","Corey","tony"],
    "last":["Doe","Scaffer","stark"]
}

df=pd.DataFrame(data)

# print(df)
# print(df.apply(min))
# filt=df["first"].str.contains("John")
# print(df.loc[filt,"last"])

# print(df.apply(lambda x: x.min()))

# print(df.applymap(len))
# print(df.applymap(str.lower))
# print(df.apply(lambda x:x.min(),axis="columns"))

# print(titanic.applymap(lambda x:len(str(x))))

# print(df["first"].replace({"John":"hon"}))

def male_female_convertor(inp):
    if inp=="male":
        return 0
    else:
        return 1
titanic['Sex']=titanic["Sex"].replace({"male":'M',"female":'F'})

#Dataframe
# print(titanic.apply(len))
#Series
# print(titanic.Name.apply(len))
titanic.rename(columns={"Sex":"Gender"},inplace=True)


#Add column
df['email']=["a","2","3"]
df["lastEmail"]=df["last"]+' '+df["email"]

#Remove column
df.drop(columns=['email',"lastEmail"],inplace=True)

df["full_name"]=df["first"]+' '+df['last']
df["email"]=["John@email.com","Corey@email.com","tony@email.com"]
df.drop(columns=["first","last"],inplace=True)

# def get_first_name(full_name):
#     first_name = str(full_name).split(" ")[0]
#     return first_name
# df["first"]=df["full_name"].apply(get_first_name)

df[['first','last']]=df['full_name'].str.split(" ",expand=True)

#ADD Remove row
'''
person={
    "first":["Gon"],
    "last":["lisk"],
    "email":["gon@gmail.com"]
}
df2=pd.DataFrame(person)
# df.loc[len(df)]=person
df=pd.concat([df,df2],ignore_index=True,sort=True)
df=pd.concat([df,pd.DataFrame({"first":['temp'],"last":["Doe"]})],ignore_index=True)
df.drop(index=3,inplace=True)
filt=df['last']=="Doe"
# print(df[filt].index)
df.drop(index=df[filt].index,inplace=True)
'''
df=pd.concat([df,pd.DataFrame({"first":['temp',"Akash"],"last":["Doe","Doe"]})],ignore_index=True)

# print(df.sort_values(by="last", ascending=False))
# print(df.sort_values(by=["last","first"], ascending=False))
df.sort_values(by=["last","first"], ascending=[False,True],inplace=True)

# print(df.sort_index())

titanic.reset_index(inplace=True)
# titanic.sort_values(["Fare"],ascending=False,inplace=True)

# print(titanic[["PassengerId","Name","Fare"]].head(20))

# print(titanic["Fare"].nlargest(5))
# print(titanic.nlargest(5,"Fare"))
# print(titanic.nsmallest(5,"Fare"))

print(titanic.head())

