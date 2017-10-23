def main():
    value = [4,8,12,25,20]
    nlen = len(value)
    n = 5

    count = 0
    for i in range(nlen):
        if value[i]%n==0:
            count+=1

    print(count)

main()
        
    
