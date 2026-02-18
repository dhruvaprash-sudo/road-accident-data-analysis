#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#class~~>12
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Topic~>ROAD ACCIDENTS DATA ANALYSIS
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#IMPORTING LIBRARIES
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
#DATAFRAME USED
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
df=pd.read_csv('C:\\Users\\IT-LAB\\Downloads\\DTA 12 D ROAD ACCIDENTS.csv')
pd.set_option('display.max_columns',None)

#FUNCTION FOR THE MAIN MENU
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
def menu():
ans=True
while ans:
print("""
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
1-Data Visualisation
2-Data Analysis
3-Read CSV/EXCEL File
4-Data Manipulation
5-Exit
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::""")
inp=int(input('enter your choice:'))
if inp==1:
datavisual()
elif inp==2:
raanalysis()
elif inp==3:
read_csv_excel()
elif inp==4:
manuplt()
elif inp==5:
ex=input('Are you sure you want to exit?(y/n)')
if ex=='y'or ex=='Y':
print("Exiting now........Done!\nHave A Nice Day!")

sys.exit()
else:
print("\nInvalid Input Try Again")
#FUNCTION FOR PLOTTING GRAPHS/CHARTS
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
def datavisual():
ans=True
while ans:
print("""
======================================================
DATA VISUALISATION
======================================================
1. lINE CHART~> POPULATION OF INDIA VS TOTAL NUMBER OF PERSONS INJURED
2. lINE CHART~> POPULATION OF INDIA VS TOTAL NUMBER OF PERSONS KILLED
3. BAR CHART~> POPULATION OF INDIA VS NO. OF ACCIDENTS PER LAKH POPULATION
4. BAR CHART~> POPULATION OF INDIA VS NO. OF ACCIDENTS PER TEN THOUSAND VEHICLES
5. HISTOGRAM~> TOTAL NUMBER OF ROAD ACCIDENTS
6. EXIT TO MAIN MENU
======================================================
======================================================""")
ans = input("Please enter your choice:")

if ans == '1':
line_chart1()
elif ans == '2':
line_chart2()
elif ans == '3':
bar_chart1()
elif ans == '4':
bar_chart2()
elif ans == '5':
dhistogm()
elif ans == '6':
menu()
else:
print("\nInvalid choice.Try again")
continue
#PLOT LINE CHART~> POPULATION OF INDIA VS TOTAL NUMBER OF PERSONS INJURED
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
def line_chart1():
df=pd.read_csv("C:\\Users\\IT-LAB\\Downloads\\DTA 12 D ROAD ACCIDENTS.csv")
df.sort_values(by='Persons_Injured',ascending=False,
inplace=True)
df=df.loc[:,['Population','Persons_Injured']]

df1=df.head(10)
population_of_india=df1['Population']
total_no_of_persons_injured=df1['Persons_Injured']
plt.plot(population_of_india,total_no_of_persons_injured,
linestyle=':',color='green', marker='.')
x=np.arange(len(population_of_india))
#plt.xticks(x,population_of_india,rotation=30)
plt.xlabel('Population~ ~ ~~~~~>', fontsize=18,color='r')
plt.ylabel('Persons Injured', color='r', fontsize=18)
plt.title('Population vs Persons Injured',color = 'dimgrey',fontsize = 18)
plt.show()
#PLOT LINE CHART~> POPULATION OF INDIA VS TOTAL NUMBER OF PERSONS KILLED
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
def line_chart2():
df=pd.read_csv("C:\\Users\\IT-LAB\\Downloads\\DTA 12 D ROAD ACCIDENTS.csv")
df.sort_values(by= 'Persons_Killed',ascending = False, inplace = True)
df = df.loc[:,['Population','Persons_Killed']]
df1 = df.head(10)
population_of_india=df1['Population']
total_no_of_persons_killed=df1['Persons_Killed']
plt.plot(population_of_india,total_no_of_persons_killed,
linestyle='dashed',color='orange',marker='+')
x=np.arange(len(population_of_india))
#plt.xticks(x,population_of_india)

plt.xlabel('Population~ ~ ~~~~~>', fontsize=18,color='blue')
plt.ylabel('Persons Killed', color='blue', fontsize=18)
plt.title('Population vs Persons Killed',color = 'dimgrey',fontsize = 18)
plt.show()
#PLOT BAR CHART~> POPULATION OF INDIA VS NO. OF ACCIDENTS PER LAKH POPULATION
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
def bar_chart1():
df=pd.read_csv("C:\\Users\\IT-LAB\\Downloads\\DTA 12 D ROAD ACCIDENTS.csv")
df.sort_values('Accidents_Per_Lakh',ascending = False)
df1 = df.head(n=10)
x = np.arange(len(df1))
population_of_india=df1['Population']
accidents_per_lakh_population=df1['Accidents_Per_Lakh']
plt.bar(x+0.25,accidents_per_lakh_population,width = 0.6, label = 'No. Of Accidents Per Lakh Population',color = 'gold')
plt.xticks(x,population_of_india,rotation = 30)
plt.title('Population vs No. Of Accidents Per Lakh Pop',color = 'dimgrey',fontsize = 18)
plt.xlabel('Population~ ~ ~~~~~>',fontsize = 18, color = 'r')
plt.ylabel('No. Of Accidents Per Lakh Population',fontsize = 18, color = 'r')
plt.legend()
plt.show()
#PLOT BAR CHART~> POPULATION OF INDIA VS NO. OF ACCIDENTS PER TEN THOUSAND VEHICLES

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
def bar_chart2():
df=pd.read_csv("C:\\Users\\IT-LAB\\Downloads\\DTA 12 D ROAD ACCIDENTS.csv")
df.sort_values('Accidents_per_TenThousand_Vehicles',ascending = False)
df1 = df.head(n=10)
x = np.arange(len(df1))
population_of_india=df1['Population']
accidents_per_tenthousand_vehicles=df1['Accidents_per_TenThousand_Vehicles']
plt.bar(x+0.25,accidents_per_tenthousand_vehicles,width = 0.6, label = 'Accidents Per Ten Thousand Vehicles',color = 'cyan')
plt.xticks(x,population_of_india,rotation = 30)
plt.title('Population vs No. Of Accidents Per Ten Thousand Vehicles',color = 'dimgrey',fontsize = 18)
plt.xlabel('Population~ ~ ~~~~~>',fontsize = 18, color = 'blue')
plt.ylabel('No. Of Accidents Per Ten Thousand Vehicles',fontsize = 18, color = 'blue')
plt.legend()
plt.show()
#PLOT HISTOGRAM~> TOTAL NUMBER OF ROAD ACCIDENTS
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
def dhistogm():

df=pd.read_csv("C:\\Users\\IT-LAB\\Downloads\\DTA 12 D ROAD ACCIDENTS.csv")
i = df['Persons_Injured']
k = df['Persons_Killed']
dat = ['Injured','Killed']
plt.hist([i,k],rwidth=0.9,color=['pink','purple'],label=dat)
plt.title('Total Number Of Road Accidents',color = 'dimgrey', fontsize = 18)
plt.xlabel('Injured/Killed',fontsize=18,color='r')
plt.ylabel('Total Road Accidents',fontsize=18,color='r')
plt.legend()
plt.show()
#FUNCTION FOR ANALYSIS OF ROAD ACCIDENTS
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
def raanalysis():
while True:
print('<------------------->')
print('Data Frame Analysis')
print('<------------------->')
mn = """ 1) To print records of population in terms of number of accidents per lakh
2) To print records of bottom most population in terms of number of persons injured
3) To print records of column specified by the user
4) To print records of persons killed for specific years
5) To go back to the main menu"""
print(mn)

x = int(input("Enter your choice : "))
print("---------x-------------------x-------------------x-------------------x")
df = pd.read_csv("C:\\Users\\IT-LAB\\Downloads\\DTA 12 D ROAD ACCIDENTS.csv")
if x ==1:
df = df.sort_values('Accidents_Per_Lakh',ascending = False, ignore_index=True)
df = df.loc[:,['Population','Accidents_Per_Lakh']]
nok = int(input('Enter the number of records to be displayed : '))
print('Top',nok,'records from dataframe')
print(df.head(nok))
print("---------x-------------------x-------------------x-------------------x")
elif x ==2 :
df = df.sort_values('Persons_Injured',ascending = False, ignore_index=True)
df = df.loc[:,['Population','Persons_Injured']]
noi = int(input('Enter the number of records to be displayed : '))
print('Bottom',nok,'records from dataframe')
print(df.tail(noi))
print("---------x-------------------x-------------------x-------------------x")
elif x ==3 :
print('Name of the columns~~>',df.columns)
clm = eval(input('Enter the column names in a list in quotes :'))
print(df[clm])
print("---------x-------------------x-------------------x-------------------x")
elif x ==4 :

print('Years')
print(df['Years'].values)
entry = eval(input('Enter year in the form of list in quotes:'))
print('Total number of persons killed in years :')
for ent in entry :
print(df.loc[df['Years']==ent,['Years','Persons_Killed']])
print("---------x-------------------x-------------------x-------------------x")
elif x ==5 :
menu()
break
#READING CSV FILE/EXCEL FILE AND DISPLAYING DATAFRAME
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
def read_csv_excel():
ans = True
while ans:
print("""1) Read csv file and display DataFrame
2) Press 2 to go back to main menu""")
ans = int(input('Enter your choice:'))
if ans ==1:
df = pd.read_csv("C:\\Users\\IT-LAB\\Downloads\\DTA 12 D ROAD ACCIDENTS.csv")
print(df)
print('Done!')
elif ans ==2:

menu()
#MANIPULATION OF DATA
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
def manuplt():
df = pd.read_csv("C:\\Users\\IT-LAB\\Downloads\\DTA 12 D ROAD ACCIDENTS.csv")
ans = True
while ans:
print("""DATA MANIPULATION\n
~~~~~~~~~~~~~~~~~~
1) Inserting a row
2) Deleting a row
3) Inserting a column
4) Deleting a column
5) Renaming a column
6) Exit to main menu""")
ans = int(input('Enter your choice[12 columns/30 rows]:'))
pd.set_option('display.max_columns',None)
if ans ==1:
print('Enter the input in following format:')
col = df.columns
print(col)
lst = eval(input('Enter the row values in list:'))
sr = pd.Series(lst,index=col)
row_df1 = pd.DataFrame([sr])

df = pd.concat([row_df1,df],ignore_index = True)
print(df.loc[[0,1,2]])
print('Row Added Successfully!!')
print('~'*30)
elif ans ==2:
print('DataFrame before deleting the row')
print(df)
inp = int(input("Enter the row's index you want to be deleted :"))
df1 = df.drop(inp,axis=0)
print("~"*30)
print("DataFrame after row index no.",inp,"is deleted-->")
print("~"*30)
print(df1.loc[[0,1,2]])
print("~"*30)
elif ans ==3:
pd.set_option('display.width',500)
pd.set_option('display.max_columns',None)
clname = input('Enter the column name :')
inp = int(input('Enter where you want to put the column (column index):'))
df.insert(inp,clname,'Nan')
print(df.loc[[0,1,2]])
print("~"*30)
elif ans ==4:
pd.set_option('display.width',500)
pd.set_option('display.max_columns',None)
print('DataFrame before deleting the column')
print(df)

inp = input('Column name you want to delete :')
df = df.drop(inp,axis=1)
print('DataFrame after deleting the column',inp,':')
print(df.loc[[0,1,2]])
print("~"*30)
elif ans ==5:
pd.set_option('display.width',500)
pd.set_option('display.max_columns',None)
print("~"*30)
print('DataFrame before changing the column name')
print('~'*30)
print(df)
oldclm = input('Enter the column name you want to rename :')
newclm = input('Enter the new column name :')
df = df.rename(columns={oldclm:newclm})
print("~"*30)
print('DataFrame after changing the column name')
print("~"*30)
print(df.loc[[0,1,2]])
print("~"*30)
elif ans ==6:
print('Returning to main menu.....Done!!')
menu()
menu()
#<~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~END OF PROGRAM~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>#
