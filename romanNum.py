def romaNum(num):
    numo = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    numl = ["M", "CM", "D", "CD", "C", "XC", "L", "XL" , "X" , "IX" , "V" , "IV" , "I"]
    result = ""
    c=0;
    if(num<1 or num >4999){
        print ("Please enter an integer");
        }
    while (num>0){
        for_ in range (no//num[c]):
            result += numl[c]
            num -=numo[c]
        c++ 
        }
    return result;
print (romaNum(123))