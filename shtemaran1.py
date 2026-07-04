a = input("please enter some text") #Մուտքագրել տողը և տպել դրա երկարությունը
print(f"the length of the text you\'ve entered is {len(a)}")

a = input("please enter some text") #Մուտքագրել տեքստ և կրկնապատկել այն
print(a * 2)

n = input("please enter some text") #Մուտքագրել տեքստ և հաշվել դրա a և b տառերի քանակը։
n.lower()
a= n.count("a")
b = n.count("b")
print(f"the number of letter \"a\" encountered in the text is {a} ")
print(f"the number of letter \"b\" encountered in the text is {b}")

n = input("please enter some text") #Մուտքագրել տեքտ և դրա միջի բոլոր a տառերը փոխարինել #-ով։
a = n.replace("a",("#"))
print(a)

n = input("please enter some text")# Մուտքագրել տեքստ և ջնջել բոլոր ա երը 
a = n.replace(("a"),(" ")).replace(("A"),(" "))
print(a)

n = float(input("enter any real number")) #Մուտքագրել ցանկացած իրական թիվ, անջատել տասնորդական մասը և տպել։
i = int(n)
print(f"decimal part of {n} is {n-i}")

n = input("please enter some text "" ")# Մուտքագրել տեքստ և տպել 1-ին ու վերջին տառեևը։
print(n[0],n[-1])

n = input("please enter some text") # Մուտքագրել տող և այն գրել ամբողջությամբ մեծատառերի ու փոքրատառերի փոխած։
a= n.lower()
b = n.upper()
print(a,b)

n = input("please, enter some text") #Մուտքագրել տեքստ և որոշել արդյոք այն վերջանում է վերջակետով։
if n.endswith(":"):
    print("Yes")
else:
    print("No") 

n = input("please, enter some text "" ") #Մուտքագրել տող, եթե այն սկսվում է Hello -։
if n.startswith("Hello"):
    print("Yes")
else:
    print("No") 

n = input("please, enter some text "" ") #Մուտքագրել տող,և այն տպել հակադարձված։
print(n[::-1])

n = int(input("please, enter a number "" ") )#Մուտքագրել թիվ և տպել հակառակը։
a = str(n)
print(a[::-1])

n = int(input("please enter a number")) # Մուտքագրել թիվ և տպել դրա հակադիրը։
print(-1*n)

n = float(input("please enter a real number")) # Մուտքագրել 2 իրական թիվ և հաշվել դրանց գումարը։
b = float(input("please enter a real number"))
print(f" the sum of real the number {n} and the real number {b } is {n+b}")

m = float(input("please enter your weight")) #Մուտքագրել մարդւո քաշն ու հասակը և հաշվել BMI -ը։
h = float(input("please enter your height"))
BMI = m/h**2
print(f" Your BMI is {BMI}")

n = input("please enter some text").replace(" ","").lower() #Մուտքագրել 2 տող և պարզել, արդյոք դրանք անագրամներ են ,թե՝ ոչ։
m = input("please enter some text").replace(" ","").lower()
if sorted(m) == sorted(n):
    print("They are anagrams")
else:
    print("They are not anagrams")   

n = float(input("please enter the length of the road in kilometers "))  #Գրելմծրագիր որը մուտքագրված թիվը կփոխարինի հռոմեական լիգայի և ապա ֆրանսիական լիգայի։
h = n /2.2
f = h/4.6
print(f" the length of the road in Rome league is {h} and in French league is {f}")

l = int(input("Please enter the number of coins")) #ՀՀ 200 դրամանոց մետաղադրամը պատրաստված է պղնձի ալյումինի ու նիկելի համաձուլվածքից,որոնք ունեն 
#մոտավորապես 14։1։5 հարաբերակցությունը։ Գրել ծրագիր ,որը կստանա200 դրամանոցների քանակը  և կհաշվի թե քանի գրամ պղինձ,նիկելևալյումին է այն 
#պարունակում։Մեկ մետաղադրամի քաշը 4,5 գրամ է
x = 4.5/20
p = 14 * x * l
a = x * l
n = 5 * x * l
print(f"the amount of Copper in {l} coins is {p}, the amount of Aluminum is {a}, and the amount of Nickel is {n}")
