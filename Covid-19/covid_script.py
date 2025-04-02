import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mticker

covid = pd.read_csv("covid_worldwide.csv")

# print(covid)
#@Visualize:Pie avg total deaths/total recovered
country=["Japan","China","India","USA"]

death_recovered_df = covid.dropna()
death_recovered_df["Total Deaths"]=death_recovered_df["Total Deaths"].str.replace(",","").astype(int)
death_recovered_df["Total Recovered"]=death_recovered_df["Total Recovered"].str.replace(",","").astype(int)

total_deaths=death_recovered_df["Total Deaths"].sum()
total_recovered=death_recovered_df["Total Recovered"].sum()
print(total_deaths)
print(total_recovered)
slices=[total_deaths,total_recovered]
labels=[f"Total Deaths\n{total_deaths}",f"Total Recovered\n{total_recovered}"]
colors=["#ff9999","#99ff99"]

plt.title("Total Covid Death and Recovered Cases World Wide")
plt.pie(slices,labels=labels,colors=colors,autopct="%1.1f%%")
plt.show()

#@Visualize:Bar covid cases in countries
total_cases=[]

covid_cases=covid[covid["Country"].isin(country)]
covid_cases["Country"]=pd.Categorical(covid_cases["Country"],categories=country,ordered=True)
covid_cases = covid_cases.sort_values("Country")
print(covid_cases.info())

covid_cases["Total Cases"]=covid_cases["Total Cases"].str.replace(",","").astype(int)
print(covid_cases)
plt.gca().yaxis.set_major_formatter(mticker.StrMethodFormatter('{x:,.0f}'))
plt.bar(covid_cases["Country"],covid_cases["Total Cases"])
plt.grid(True)
plt.title("Covid Cases By Countries")
plt.ylabel("Total Cases")
plt.xlabel("Country")
plt.tight_layout()
plt.show()




