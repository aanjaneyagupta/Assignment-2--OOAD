import time
#Imported time function to delay every output for third of second.
import random

#Have imported random module for random number of products sold.
#The name of the class is Inventory

class Inventory:
    #Created a method to input all the details of the product and store the same in the form of different lists so that it is easy to recall
    def var():
        global l1,l2,l3,l4,l5,l6,prmprod,prprice,prmcost,prstock

        l1=[]
        l2=[]
        l3=[]
        l4=[]
        l5=[]
        l6=[]
        print('Welcome to Programming Principles Sample Product Inventory\n')
        time.sleep(1)
        print("""
  ____                            _         ____                   _               _     ___                           _                      
 / ___|   __ _  _ __ ___   _ __  | |  ___  |  _ \  _ __  ___    __| | _   _   ___ | |_  |_ _| _ __ __   __ ___  _ __  | |_  ___   _ __  _   _ 
 \___ \  / _` || '_ ` _ \ | '_ \ | | / _ \ | |_) || '__|/ _ \  / _` || | | | / __|| __|  | | | '_ \\ \ / // _ \| '_ \ | __|/ _ \ | '__|| | | |
  ___) || (_| || | | | | || |_) || ||  __/ |  __/ | |  | (_) || (_| || |_| || (__ | |_   | | | | | |\ V /|  __/| | | || |_| (_) || |   | |_| |
 |____/  \__,_||_| |_| |_|| .__/ |_| \___| |_|    |_|   \___/  \__,_| \__,_| \___| \__| |___||_| |_| \_/  \___||_| |_| \__|\___/ |_|    \__, |
                          |_|                                                                                                           |___/ 
""")

        #This will ask the details from the user again if the user fails to enter correct type of values in the specific fields.
        try:
            prcode = int(input('Please enter the Product Code: '))
            prname = input('Please enter the Product Name: ')
            prstock = int(input('Please enter the Current Stock: '))
            prprice = float(input('Please enter the Product Sale Price: '))
            prmcost = float(input('Please enter the Product Manufacture Cost: '))
            prmprod = int(input('Please enter estimated monthly production: '))
        except:
            print("Please enter correct type of values in every field.")
            prcode = int(input('Please enter the Product Code: '))
            prname = input('Please enter the Product Name: ')
            prstock = int(input('Please enter the Current Stock: '))
            prprice = float(input('Please enter the Product Sale Price: '))
            prmcost = float(input('Please enter the Product Manufacture Cost: '))
            prmprod = int(input('Please enter estimated monthly production: '))

        #Every input is being added to a list

        l1.append(prcode)
        l2.append(prname)
        l3.append(prstock)
        l4.append(prprice)
        l5.append(prmcost)
        l6.append(prmprod)
        print('*******Programming Principles Sample Stock Statement*******')

        #To search for the product by entering product code and displaying all other details.

        p1 = int(input('Please enter the Product Code: '))
        for i in l1:
            if p1==i:
                ind = l1.index(p1)
                print('Product Name: ',l2[ind])
                print('Current Stock: ',l3[ind])
                print('Sale Price: ',l4[ind])
                print('Manufacture Cost: ',l5[ind])
                print('Monthly production: ',l6[ind],'\n')
        
                
    #This method is created to display the estimate sold products and the net profit after 1 Year.
    def estimate():
        global stock
        global sold
        global total_sold
        total_sold=0
        for i in range(1,13):

            #For Month 1 only we will also subtract from the existing units manufactured
            if i==1:
                print("Month",i,':')
                time.sleep(0.3)
                print("     Manufactured: ",prmprod)
                time.sleep(0.3)
                sold = random.randint((prmprod-10),(prmprod+10))
                print("     Sold: ", sold, "units")
                time.sleep(0.3)
                stock=(prstock+prmprod)-sold
                print('     Stock: ',stock)
                print('')
                time.sleep(0.3)
            #For months after Month 1
            else:
                print("Month",i,':')
                time.sleep(0.3)
                print("     Manufactured: ",prmprod)
                time.sleep(0.3)
                sold = random.randint((prmprod-10),(prmprod+10))
                print("     Sold: ", sold, "units")
                time.sleep(0.3)
                stock = (stock+prmprod)-sold
                print('     Stock:', stock)
                print('')
                time.sleep(0.3)
            total_sold+=sold
        

        #This is net profit which is (Total Units Sold x Selling Price) - (Total Units Manufactured x Manufacturing Cost)
        net = ((total_sold)*prprice)-(((prmprod*12)+prstock)*prmcost)
        print('Net Profit: ',net)

Inventory.var()
Inventory.estimate()



        