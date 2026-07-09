#n = int(input("Enter a number:"))#Տրված է n բնական թիվը։ Տպել 1-ից n բոլոր թվերը։
#for i in range(n):
#    print(i)

#n = int(input("Enter a number:"))#Տրված է n բնական թիվը։ Տպել n-ից 1 բոլոր թվերը։
#for i in range(n, 0, -1):
#    print(i)

#n = int(input("Enter a number:"))# Տրված է n թիվը։ Տպել 1-ից n բոլոր զույգ թվերը։
#for i in range(2, n, 2):
#    print(i)

#a = int(input("Enter a number:"))#Տրված է n թիվը։ Տպել 1-ից n բոլոր կենտ թվերը։
#for i in range(1, a, 2):
#    print(i)

#n = int(input("Enter a number:"))#Տրված է n թիվը։ Հաշվել 1-ից n թվերի գումարը։
#a = 1
#for i in range(1, n):
#    i += 1
#    a += i
#print(a)    

#n = int(input("Enter a number:"))# Տրված է n թիվը։ Հաշվել 1-ից n թվերի արտադրյալը։
#a = 1
#for i in range(1, n):
#    i += 1
#    a *= i
#print(a)    

#n = int(input("Enter a number:"))#Տրված է n թիվը։ Տպել նրա բազմապատիկները 1-ից 100 միջակայքում։
#for i in range(1,101):
#    if i % n ==0:
#        print(i)

#n = int(input("Enter tne number:"))#Տրված է n թիվը։ Հաշվել, թե քանի թիվ է 1-ից n միջակայքում բաժանվում 3-ի։   
#i = 0
#for k in range(1, n+1):
#    if k %3 == 0:
#        i +=1
#print(i)

#n = int(input("Enter a number:"))#Տրված է n թիվը։ Տպել 5-ի բոլոր բազմապատիկները մինչև n։
#i = 0
#for l in range(1, n+1):
#    if l%5 == 0:
#        i += 1
#print(i)        

#n = int(input("Enter a number:"))# Տրված է n թիվը։ Տպել յուրաքանչյուր թվի քառակուսին 1-ից n։
#for i in range(1, n+1):
#   i **=2
#    print(i)

#n = int(input("Enter a number:"))#Տրված է n թիվը։ Տպել յուրաքանչյուր թվի խորանարդը 1-ից n։
#for i in range(1, n+1):
#    i **=3
#    print(i)

#n = int(input("Enter a number:"))# Տրված է n թիվը։ Հաշվել բոլոր զույգ թվերի գումարը։
#a = 0
#for t in range(1, n+1):
#    if t%2 == 0:
#        a +=t
#print(a)       

#n = int(input("Enter a number:"))# Տրված է n թիվը։ Հաշվել բոլոր կենտ թվերի գումարը։
#a =0
#for i in range(1, n+1):
#    if i %2 == 1:
#        a +=i
#print(a)        

#n = int(input("Enter a number:"))#Տրված է n թիվը։ Գտնել ամենամեծ թիվը, որը փոքր է կամ հավասար n-ին և բաժանվում է 7-ի։
#for i in range(n, 1, -1):
#    if i %7 == 0:
#        print(i) 
#        break

#n = int(input("Enter a number:"))#Տրված է n թիվը։ Տպել բոլոր թվերը, որոնք բաժանվում են և՛ 3-ի, և՛ 5-ի։
#for i in range(1, n+1):
#    if i %5 ==0 and i %3 ==0:
#        print(i)

#n = int(input("Enter a number:")) #Տրված է n թիվը։ Գտնել 1-ից n թվերի միջինը։
#a = 0
#for i in range(1, n+1):
#    a += i 
#    b = a/n
#print(b)    

#n = int(input("Enter a number:"))#Տրված է n թիվը։ Հաշվել, թե քանի թիվ է բաժանվում 2-ի կամ 5-ի։
#a = 0
#for i in range(1, n+1):
#    if i % 5 ==0 or i %2 == 0:
#        a +=1
#print(a)        

#n = int(input("Enter a number:")) #Տրված է n թիվը։ Տպել միայն այն թվերը, որոնք չեն բաժանվում 3-ի։
#for i in range(1, n+1):
#    if i %3 != 0:
#        print(i)

#n = int(input("Enter a number:"))#Տրված է n թիվը։ Տպել բոլոր թվերը հակառակ հերթականությամբ։
#for i in range(n, 0, -1):
#    print(i)

#n = int(input("Enter a number:")) #Տրված է n թիվը։ Հաշվել 1² + 2² + ... + n²։
#a = 0
#for i in range(1, n+1):
#    a +=i**2
#print(a)    

#n = int(input("Enter a number:"))#Տրված է n թիվը։ Հաշվել 1³ + 2³ + ... + n³։
#a = 0
#for i in range(1, n+1):
#    i **=3
#    a += i
#print(a)    

#n = int(input()) #Տրված է n թիվը։ Գտնել նրա բոլոր բաժանարարները։
#i = 1
#while n >= 1:
#    if n % i == 0:
#        print(i)
#    i +=1    

#n= int(input("Enter a number:"))# Տրված է n թիվը։ Հաշվել նրա բաժանարարների քանակը։
#a =0
#for i in range(1, n+1):
#    if n %i == 0:
#        a +=1
#print(a)    

#n = int(input("Enter a number:"))#Տրված է n թիվը։ Որոշել՝ այն պարզ թիվ է, թե ոչ։
#i = 1
#a = 0
#while i <= n:
#    if n % i ==0:
#        a +=1
#    i +=1
#if a == 2:
#    print("The number is prime.")        
#else:
#    print("The number is not prime.")    
     
n = int(input("Enter a number:"))#Տրված է n թիվը։ Գտնել նրանից փոքր ամենամեծ պարզ թիվը։    
for i in range(1, n, 1):
    if n %i ==0:
        print(i)
        
        
        