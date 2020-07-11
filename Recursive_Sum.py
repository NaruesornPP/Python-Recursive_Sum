def sum(num):
    if(num!=1):
        return (num+sum(num-1));
    else :
        return 1;
    
num = int(input("Input a number : "));
print(sum(num));
