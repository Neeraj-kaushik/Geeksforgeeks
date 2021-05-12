def validate(ip):
    count=0
    address=ip.split('.')
    a=len(address)
    if a!=4:
        print('0')
    else:
        for i in range(len(address)):
            if address[i]=='':
                print('0')
                break
            else:
                address[i]=int(address[i])
        for i in range(len(address)):
            if address[i]>=0 and address[i]<=255:
                count+=1
            if count==4:
                print('1')
            else:
                print('0')
 

ip=input()
validate(ip)