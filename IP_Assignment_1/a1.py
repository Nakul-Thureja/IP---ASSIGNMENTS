'''
- This is the skeleton code, wherein you have to write the logic for each of the
functions defined below.

- Feel free to add new helper functions, but DO NOT modify/delete the given functions. 

- You MUST complete the functions defined below, except the ones that are already defined. 
'''

item=[[0,'Tshirt','Apparels',500],[1,'Trousers','Apparels',600],
      [2,'Scarf','Apparels',250],[3,'Smartphone','Electronics',20000],
      [4,'iPad','Electronics',30000],[5,'Laptop','Electronics',50000],
      [6,'Eggs','Eatables',5],[7,'Chocolate','Eatables',10],
      [8,'Juice','Eatables',100],[9,'Milk','Eatables',45]]

def show_menu():
    '''
	Description: Prints the menu as shown in the PDF
	
	Parameters: No paramters
	
	Returns: No return value
    '''
    print('\n')
    print('-' * 80)
    print('-' * 80)
    print('\t\t\t\t MY BAZAAR')	
    print('-' * 80)
    print('-' * 80)
    print('Hello! Welcome to my grocery store!')
    print('Following are the products available in the shop : ')
    print('\n')
    print('CODE | DESCRIPTION |   CATEGORY   | COST (Rs)')
    print('-' * 80)
    for i in range(len((item))):
        print('{0:<5}| {1:<12}|  {2:<11} | {3}'.format(item[i][0],item[i][1],item[i][2],item[i][3]))
                   
    print('-' * 80)
    print('\n')

  
def get_regular_input():
    '''
	Description: Takes space separated item codes (only integers allowed). 
	Include appropriate print statements to match the output with the 
	screenshot provided in the PDF.
	
	Parameters: No parameters
	
	Returns: Returns a list of integers of length 10, where the i_th
	element represents the quantity of the item with item code i. 
    '''
    print('\n')
    print('-' * 80)
    print('ENTER ITEMS YOU WISH TO BUY')
    print('-'*80)
    t=True
    a=input('Enter the item codes (space-separated) : ')
    print('\n')
    list1=[0,0,0,0,0,0,0,0,0,0]
    a=a.split()
    
    for i in range(len(a)):
        if(a[i].isnumeric()):
            a[i]=int(a[i])
        
      
    j=0

    while(j<len(a)):
        f=True
        for i in range(10):
            if(a[j]==item[i][0]):
                f=False
                list1[i]+=1
        if f:
            print('{0} Code is Invalid.'.format(a[j]))
        j+=1

    print('Your Order has been Finalised ')
            
    return list1


def get_bulk_input():
    '''
	Description: Takes inputs (only integers allowed) from a bulk buyer. 
	For details, refer PDF. Include appropriate print statements to match 
 	the output with the screenshot provided in the PDF.
	
	Parameters: No parameters
	
	Returns: Returns a list of integers of length 10, where the i_th
	element represents the quantity of the item with item code i.
    '''
    print('\n')
    print('-' * 80)
    print('ENTER ITEM AND QUANTITIES')
    print('-'*80)
    list1=[0,0,0,0,0,0,0,0,0,0]
    while(True):
        t1=True
        t2= True
        x=input('Enter code and quantity (press Enter to stop) : ')
        if(not x):
            print('Your order has been finalized.')
            break
        
        c=0
        for i in x:
            if i==' ':
                c+=1
        if ' ' not in x:
            pass
        elif c>1:
            pass          
        else:
            a,b = x.split()
            t2 = b.isnumeric()
            if t2:
                b=int(b)
            if a.isnumeric() :
                a = int(a)
                for i in range(10):
                    if(a==item[i][0] ):
                        t1=False
                        if(t2):
                            print('You added', b , item[i][1])
                            list1[i]=list1[i]+b
                
        if t1 and not t2:
            print('Invalid code and quantity. Try again.')
        
        elif t1:
            print('Invalid code. Try again.')
        
        elif not t2:
            print('Invalid quantity. Try again.')
        
    return list1


def print_order_details(quantities):
    '''
	Description: Prints the details of the order in a manner similar to the
	sample given in PDF.
	
	Parameters: Takes a list of integers of length 10, where the i_th
	element represents the quantity of the item with item code i.
	
	Returns: No return value
    '''
    print('\n')
    print('-' * 80)
    print('ORDER DETAILS')
    print('-'*80)
    j=1
    for i in range(len(quantities)):
        if(quantities[i]>0 and i<10):
            print("[{0:2}] {1:10} * {2:3} = Rs {3:<5} * {2:<3} = Rs {4:<10}".format(j,item[i][1],quantities[i],item[i][3],item[i][3]*quantities[i]))
            j+=1
    print('\n')


def calculate_category_wise_cost(quantities):
    '''
	Description: Calculates the category wise cost using the quantities
	provided. Include appropriate print statements to match the output with the
	screenshot provided in the PDF.
	
	Parameters: Takes a list of integers of length 10, where the i_th
	element represents the quantity of the item with item code i.
	
	Returns: A 3-tuple of integers in the following format: 
	(apparels_cost, electronics_cost, eatables_cost)
    '''
    print('\n')
    print('-' * 80)
    print('CATEGORY-WISE COST')
    print('-'*80)
    a=[0,0,0]
    for i in range(len(quantities)):
        if(item[i][2]=='Apparels'):
            a[0]+=item[i][3]*quantities[i]
        
        if(item[i][2]=='Electronics'):
            a[1]+=item[i][3]*quantities[i]
        
        if(item[i][2]=='Eatables'):
            a[2]+=item[i][3]*quantities[i]
        
    print('Apparels    = Rs {}'.format(a[0]))
    print('Electronics = Rs {}'.format(a[1]))
    print('Eatables    = Rs {}'.format(a[2]))
    print('\n')
   
    return (a[0],a[1],a[2])


def get_discount(cost, discount_rate):
    '''
	Description: This is a helper function. DO NOT CHANGE THIS. 
	This function must be used whenever you are calculating discounts.
	
	Parameters: Takes 2 parameters:
	- cost: Integer
	- discount_rate: Float: 0 <= discount_rate <= 1

	Returns: The discount on the cost provided.
    '''
    return int(cost * discount_rate)


def calculate_discounted_prices(apparels_cost, electronics_cost, eatables_cost):
    '''
	Description: Calculates the discounted category-wise price, if applicable. 
	Include appropriate print statements to match the output with the
	screenshot provided in the PDF.
	
	Parameters: Takes 3 integer parameters:
	- apparels_cost: 	cost for the category 'Apparels'
	- electronics_cost: cost for the category 'Electronics'
	- eatables_cost: 	cost for the category 'Eatables'
	
	Returns: A 3-tuple of integers in the following format: 
	(discounted_apparels_cost, discounted_electronics_cost, discounted_eatables_cost). 
    '''
    print('\n')
    print('-' * 80)
    print('DISCOUNTS')
    print('-'*80)
    discounted_apparels_cost = apparels_cost
    discounted_electronics_cost = electronics_cost
    discounted_eatables_cost = eatables_cost

    cost = apparels_cost + electronics_cost + eatables_cost
    if(apparels_cost>=2000):
        discounted_apparels_cost = apparels_cost - get_discount(apparels_cost,0.1)
        print('[APPAREL]     Rs {0} - Rs {1} = Rs {2}'.format(apparels_cost,get_discount(apparels_cost,0.1),discounted_apparels_cost))
                
    if(electronics_cost>=25000):
        discounted_electronics_cost = electronics_cost - get_discount(electronics_cost,0.1)
        print('[ELECTRONICS] Rs {0} - Rs {1} = Rs {2}'.format(electronics_cost,get_discount(electronics_cost,0.1),discounted_electronics_cost))
        
    if(eatables_cost>=500):
        discounted_eatables_cost = eatables_cost - get_discount(eatables_cost,0.1)
        print('[EATABLES]    Rs {0} - Rs {1} = Rs {2}'.format(eatables_cost,get_discount(eatables_cost,0.1),discounted_eatables_cost))
        
    discount = cost - (discounted_apparels_cost + discounted_electronics_cost + discounted_eatables_cost)
    cost = discounted_apparels_cost + discounted_electronics_cost + discounted_eatables_cost
    print()
    print('TOTAL DISCOUNT = Rs ',discount)
    print('TOTAL COST     = Rs ',cost)
    print('\n')
 
    return (discounted_apparels_cost, discounted_electronics_cost, discounted_eatables_cost)


def get_tax(cost, tax):
    '''
	Description: This is a helper function. DO NOT CHANGE THIS. 
	This function must be used whenever you are calculating discounts.
	
	Parameters: Takes 2 parameters:
	- cost: Integer
	- tax: 	Float: 0 <= tax <= 1

	Returns: The tax on the cost provided.
    '''
    return int(cost * tax)


def calculate_tax(apparels_cost, electronics_cost, eatables_cost):
    '''
	Description: Calculates the total cost including taxes.
	Include appropriate print statements to match the output with the
	screenshot provided in the PDF.
	
	Parameters: Takes 3 integer parameters:
	- apparels_cost: 	cost for the category 'Apparels'
	- electronics_cost: cost for the category 'Electronics'
	- eatables_cost: 	cost for the category 'Eatables' 
	
	Returns: A 2-tuple of integers in the following format: 
	(total_cost_including_tax, total_tax)
    '''
    print('\n')
    print('-' * 80)
    print('TAX')
    print('-'*80)
    total_tax=0
    print('[APPAREL]     Rs {0} * {1} = Rs {2}'.format(apparels_cost,0.10,get_tax(apparels_cost,0.1)))
    total_tax += get_tax(apparels_cost,0.10)
    print('[ELECTRONICS] Rs {0} * {1} = Rs {2}'.format(electronics_cost,0.15,get_tax(electronics_cost,0.15)))
    total_tax += get_tax(electronics_cost,0.15)
    print('[EATABLES]    Rs {0} * {1} = Rs {2}'.format(eatables_cost,0.05,get_tax(eatables_cost,0.05)))
    total_tax += get_tax(eatables_cost,0.05)
    
    total_cost = apparels_cost + electronics_cost + eatables_cost + total_tax
    print()
    print('TOTAL TAX  = Rs',total_tax)
    print('TOTAL COST = Rs',total_cost)
    print('\n')

    return (total_cost,total_tax)


def apply_coupon_code(total_cost):
    '''
	Description: Takes the coupon code from the user as input (case-sensitive). 
	For details, refer the PDF. Include appropriate print statements to match 
	the output with the screenshot provided in the PDF.
	
	Parameters: The total cost (integer) on which the coupon is to be applied.
	
	Returns: A 2-tuple of integers:
	(total_cost_after_coupon_discount, total_coupon_discount)
    '''
    print('\n')
    print('-' * 80)
    print('COUPON CODE')
    print('-'*80)
    total_cost_after_coupon_discount = total_cost
    total_coupon_discount = 0
    t = True
    while(t):
        code=input('Enter coupon code (else leave blank) : ')
        if(code==''):
            t=False
        
        elif(code == 'HELLE25'):
            if(total_cost >= 25000):
                t=False
                if(get_discount(total_cost,0.25) <= 5000):
                    total_cost_after_coupon_discount = total_cost - get_discount(total_cost,0.25)
                    total_coupon_discount = get_discount(total_cost,0.25)
                else:
                    total_cost_after_coupon_discount = total_cost - 5000
                    total_coupon_discount = 5000
                print('[HELLE25] min(5000, Rs {0} * 0.25) = Rs {1}'.format(total_cost,total_coupon_discount))
            else:
                print('[HELLE25] Coupon Code can only be applied if Total Cost is greater than 25000')
            
            

        elif(code == 'CHILL50'):
            if(total_cost >= 50000):
                t=False
                if(get_discount(total_cost,0.50) <= 10000):
                    total_cost_after_coupon_discount = total_cost - get_discount(total_cost,0.50)
                    total_coupon_discount = get_discount(total_cost,0.50)
                else:
                    total_cost_after_coupon_discount = total_cost - 10000
                    total_coupon_discount = 10000
                print('[CHILL50] min(10000, Rs {0} * 0.50) = Rs {1}'.format(total_cost,total_coupon_discount))
            else:
                print('[CHILL50] Coupon Code can only be applied if Total Cost is greater than 50000')
                           
         
        
        else:
            print('Invalid coupon code. Try again.')
            
    
    print('\n')        
    print('TOTAL COUPON DISCOUNT = Rs',total_coupon_discount)
    print('TOTAL COST = Rs',total_cost_after_coupon_discount)
    print('\nThank you for visiting!')
    
    return (total_cost_after_coupon_discount, total_coupon_discount)


def main():
    '''
	Description: This is the main function. All production level codes usually
	have this function. This function will call the functions you have written
	above to design the logic. You will see how splitting your code into specialised
	functions makes the code easier to read, write and debug. Include appropriate 
	print statements to match the output with the screenshots provided in the PDF.
	
	Parameters: No parameters
	
	Returns: No return value
    ''' 
    show_menu()
    quantities = []
    while(True):
        key = input('Would you like to buy in bulk? (y or Y / n or N): ')
        if(key=='n' or key=='N'):
            quantities = get_regular_input()
            break
        
        elif(key=='y' or key=='Y'):
            quantities = get_bulk_input()
            break
           
    print_order_details(quantities)
    category_cost = calculate_category_wise_cost(quantities)
    discount_cost = calculate_discounted_prices(category_cost[0], category_cost[1], category_cost[2])
    discount_cost = calculate_tax(category_cost[0], category_cost[1], category_cost[2])
    apply_coupon_code(discount_cost[0])



if __name__ == '__main__':
	main()




