# Prompt user for information

name = str(input("Enter employee's name: "))
hoursWorked = float(input("Enter number of hours worked in a week: "))
hourRate = float(input("Enter hourly pay rate: "))
fedTax = float(input("Enter federal tax withholding rate(in decimal form): "))
stateTax = float(input("Enter state tax withholding rate (in decimal form): "))

#Calculations
grossPay = hoursWorked * hourRate
fedWithhold = round((grossPay * fedTax), 2)
stateWithhold = round((grossPay * stateTax), 2)
totalDeduction = fedWithhold + stateWithhold
netPay = grossPay - totalDeduction
percentFed = str(format(fedTax, ".0%"))
percentState = str(format(stateTax, ".0%"))


#Show Results
print("\n\n\nEmployee Name: %s" %name)
print("Hours Worked: ", hoursWorked)
print("Pay Rate: $%s" %hourRate)
print("Gross Pay: $%s" %grossPay)
print("Deductions: ")

print("\t\b\b\b\b\bFederal Withholding (%s): $%s" %(percentFed, fedWithhold))
print("\t\b\b\b\b\bState Withholding (%s): $%s" %(percentState, stateWithhold))
print("\t\b\b\b\b\bTotal Deductions: $%s" %totalDeduction)

print("Net Pay: $%s"%(netPay))












