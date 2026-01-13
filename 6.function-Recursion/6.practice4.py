# waf to convert usd to inr 

usd_val = int(input("Enter Your USD :"))

def convertor(usd_val):
    inr_val = usd_val * 90
    print (usd_val , "USD =", inr_val,"INR")

convertor(usd_val)