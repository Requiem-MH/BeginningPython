from tkinter import *  # Import tkinter


class InvestmentAmount:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("Investment Calculator")  # Set title

        Label(window, text="Investment Amount: ").grid(row=1,
                                                        column=1, sticky=W)
        Label(window, text="Annual Interest Rate: ").grid(row=2,
                                                   column=1, sticky=W)
        Label(window, text="Number of Years: ").grid(row=3,
                                               column=1, sticky=W)
        Label(window, text="Total: ").grid(row=4,
                                          column=1, sticky=W)

        self.investment = IntVar()
        Entry(window, textvariable=self.investment,
              justify=RIGHT).grid(row=1, column=2)
        self.annualInterestRate = DoubleVar()
        Entry(window, textvariable=self.annualInterestRate,
              justify=RIGHT).grid(row=2, column=2)
        self.years = IntVar()
        Entry(window, textvariable=self.years,
              justify=RIGHT).grid(row=3, column=2)
        self.futureValue = DoubleVar()
        Label(window, textvariable = self.futureValue,
              justify = RIGHT).grid(row = 4, column = 2)
        Button(window, text="Calculate", command=self.getFutureValue).grid(
            row=5, column=2, sticky=E)

        window.mainloop()  # Create an event loop


    def getFutureValue(self):
        futureVal = round((self.investment.get() * (1 + (self.annualInterestRate.get() / 12) / 100) ** (self.years.get() * 12)), 2)
        self.futureValue.set(futureVal)


InvestmentAmount() # Create GUI