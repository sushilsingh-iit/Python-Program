# create a class called order which stores item & its price.
# use dunder function __get__ () to convey that.
#   order1 > order2 if price of order > price of order2



class order:
    def __init__(self,item,price):        
        self.item = item 
        self.price = price

        # The __gt__ dunder method handles the '>' operator

    def __gt__(self,ord2):
        return self.price > ord2.price
        

ord1 = order("chips",20)
ord2 = order ("tea ",15)
print(ord1 > ord2) # give output True 



        

