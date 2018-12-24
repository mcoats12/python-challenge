#PyBank File

# import the preliminary packages
import os
import csv
# path for Budget Data
BudgetCSV = os.path.join('..', 'Resources', 'budget_data.csv')

with open(BudgetCSV) as csvfile:
    #Read and delimit the data
    csvreader=csv.reader(csvfile,delimiter=',')
    #Define the variables
    months=0
    revenue=0
    # Counts the Total Rows
    rows=[r for r in csvreader]
    #Defaulting to the First Value available in the Sheet
    change_revenue=int(rows[1][1])
    max = rows[1]
    min=rows[1]
    #Looping through Data
    for i in range(1,len(rows)):
        
        months=months+1
        row=rows[i]
        revenue= int(row[1]) + revenue
        
        #Excluding the Header Row
        if i > 1:
            change_revenue=change_revenue + int(row[1])-int(rows[i-1][1])
        #Finding and Max Revenue
        if int(max[1]) < int(row[1]):
            max=row
        #Finding and Min Revenue
        if int(min[1]) > int(row[1]):
            min=row
#Calculating Average Revenue Change
average= int(revenue /months)

#Printing the Outputs
print("Financial Analysis")
print("------------------")
print("Total Months: " + str(months))
print("Total Revenue: " +"$" +str(revenue))       
print("Average Revenue Change: " +"$"+ str(average))
print("Greatest Increase in Revenue:" + str(max[0])+" ($" + str(max[1])+")")
print("Greatest Decrease in Revenue:" + str(min[0])+" ($" + str(min[1])+")")

# Save the Outputs to txt
output_file = os.path.join("Budget.txt")
with open(output_file, "w") as text:
    text.write("Financial Analysis" + "\n")
    text.write("----------------------------------------" + "\n")
    text.write(f"Total Months: {months}" + "\n")
    text.write(f"Total Revenue: ${revenue}" + "\n")
    text.write(f"Average Revenue Change: ${average}" + "\n")
    text.write(f"Greatest Increase in Revenue: {max[0]} (${max[1]})" + "\n")
    text.write(f"Greatest Decrease in Revenue: {min[0]} (${min[1]})" + "\n")
