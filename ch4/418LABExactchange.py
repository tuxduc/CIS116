#exact_change function definition
def exact_change(user_total):   
    num_dollars= user_total// 100
    user_total =user_total% 100
    num_quarters = user_total // 25    
    user_total = user_total% 25    
    num_dimes = user_total // 10    
    user_total =user_total% 10    
    num_nickels = user_total // 5    
    user_total =y=user_total% 5    
    num_pennies = user_total   
    #returning the values
    return num_dollars, num_quarters, num_dimes, num_nickels, num_pennies
    
if __name__ == '__main__':  
    #integer input
    input_val = int(input())
    #call the functions
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val) 
    #if the entered amount is zero or less than zero
    if(input_val <= 0):    
        #printing no change
        print('No change')     
    else:   
        #dollars
        if num_dollars==1:
            print('%d Dollar'%num_dollars)
        elif num_dollars>1:
                print ('%d Dollars'%num_dollars)
        #quarters 
        if num_quarters == 1:             
            print('%d Quarter' % num_quarters) 
        elif num_quarters > 1:    
            print('%d Quarters' % num_quarters) 
        
        #dimes 
        if num_dimes == 1:             
            print('%d Dime' % num_dimes)      
        elif num_dimes > 1:             
            print('%d Dimes' % num_dimes)
        
        #nickels
        if num_nickels == 1:             
            print('%d Nickel' % num_nickels)
        elif num_nickels > 1:             
            print('%d Nickels' % num_nickels) 
        
        #pennies
        if num_pennies == 1:             
            print('%d Penny' % num_pennies)       
        elif num_pennies > 1:             
            print('%d Pennies' % num_pennies)  