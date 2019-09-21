import os, sys
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np


###PURCHASE PRICE
while True:
    try:
        purchase_price = int(raw_input("What is the Purchase Price in Rands? "))
        print("Thank you.")
        break
    except ValueError:
        print("Something went wrong?")
        print("Try again but this time don't put any letters or commas. Only Integers are allowed!!")
###DEPOSIT
while True:
    try:
        initial_deposit = int(raw_input("What is your Deposit in Rands? "))
        print("Thank you.")
        break
    except ValueError:
        print("Something went wrong?")
        print("Try again but this time don't put any letters or commas and only Integers.")

###YEARS
while True:
    try:
        duration_years = int(raw_input("What is your Payment Term in Years? "))
        print("Thank you.")
        break
    except ValueError:
        print("Something went wrong?")
        print("Try again but this time don't put any Letters, Commas and use only WHOLE Numbers.")

###INTEREST
while True:
    try:
        interest_rate = float(raw_input("What is the Interest Rate? "))
        print("Thank you.")
        break
    except ValueError:
        print("Something went wrong?")
        print("Try again but this time don't put any letters or commas. Don't be cheeky!")

###USER
while True:
    try:
        current_user = str(raw_input("What is your First Name? "))
        print("Thank you.")
        break
    except ValueError:
        print("Something went wrong?")
        print("Try again but this time make sure you use letters.")

###This is the actual calculation
def formula(purchase,deposit,years,interest,individual):
    read_history()
    purch = float(purchase)
    dep = float(deposit)
    P = purch - dep
    N = int(years)* 12
    r = float(interest)/100/12
    user = str(individual)
    
    INPUTS = "Purchase Price: R"+str(purchase)+"; Deposit: R"+str(deposit)+"; Bond Term: "+str(years)+" years; Fixed Interest Rate: "+str(interest)+"%"
    value = (r * P)/(1 - (1 + r)**(-N))

    print "Your monthly payment will be R", round(value,2)," \n"
    total_amount = value*N  ## How much is owed in total.
    total_interest = total_amount - purch ## How much is paid to the bank.
    current_interest = 0 #how much has been paid to bank as interest so far.
    stop = years 
    
    annual_payment = value*12
    year_interest_capital = {} 
    for i in range(1,stop+1):
        d = 12*i
        cumulative_interest = (P*r - value)*((((1 + r)**d)-1)/r)+value*d
        interest_outstanding = total_interest - current_interest
        annual_interest = cumulative_interest - current_interest
        percent_of_annual_payment_to_interest = round((annual_interest/annual_payment)*100,2)
        percent_of_annual_payment_to_capital = round(((annual_payment - annual_interest)/annual_payment)*100,2)
        current_interest = cumulative_interest
        year_interest_capital[i] = (percent_of_annual_payment_to_interest,percent_of_annual_payment_to_capital)
    
    record(user,year_interest_capital,INPUTS)

def record(individual,thedata,parameters):
    output_name = now.strftime("bank_interest_%d%m%Y.txt")
    output = open("bond_calculations/"+output_name,"a")
    thetime = now.strftime("%d/%m/%Y,%H:%M:%S")
    output.write(individual+","+thetime+"\n")
    output.write(parameters+"\n")
    title_csv = "Year,Interest%,Capital%"
    output.write(title_csv+"\n")
    interest_list = []
    capital_list = []
    year_list = [] 
    for year in thedata:
        pos1 = str(thedata[year][0])
        pos2 = str(thedata[year][1])
        data_entry = str(year)+","+pos1+","+pos2
        output.write(data_entry+"\n")
         ####print "{:<8} {:<15} {:<10}".format(year,pos1,pos2)
        interest_list.append(thedata[year][0])
        capital_list.append(thedata[year][1])
        year_list.append(str(year))
    
    plot_scatter(year_list,interest_list,capital_list)

    output.write("#####\n")    
    output.close()    
    print individual,"did some helpful bond calculations and saved them too."

def read_history():
    date = now.strftime("bank_interest_%d%m%Y.txt")
    history = open("bond_calculations/"+date,"r")
    print "The calculations done TODAY %s are: \n" %(now.strftime("%d/%m/%Y"))
    for line in history:
        print line[:-1]    
 
    history.close()

def plot_scatter(size,interest,capital):
    N = len(size)
    y1 = interest
    y2 = capital

    xvalues = np.arange(N)
    
    plt.bar(xvalues,y1,align='center', color='b', label = 'Interest')
    plt.bar(xvalues,y2,align='center', color='r', bottom =y1, label = 'Capital')
    plt.xticks(xvalues, size)
    plt.xlabel('Years')
    plt.ylabel('Percentage (%)')
    plt.title('Stacked Bar Graph of Repayment Splits')
    plt.legend()
    plt.show()
    


now = datetime.now()
os.system('mkdir bond_calculations')
formula(purchase_price,initial_deposit,duration_years,interest_rate,current_user)
####formula(200000,0,30,6.5,'Lester')

listofy1 = [3,9,11,2,6,4]
listofy2 = [6,4,7,8,3,4]
size = 6
##plot_scatter(size,listofy1,listofy2)
