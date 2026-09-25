# დავალებაში ეწერა, რომ უნდა დავითვალოთ ჯამი n-მდე, თუმცა მაგალითი მოყვანილი იყო n-ის ჩათვლით.
# ამიტომ მეც n-ის ჩათვლით დავწერე.

#  ვარიანტი N1

total = 0
n = int(input("Enter a positive number: "))
for i in range(2, n+1, 2):
    total += i
print ("Total:", total)


#  ვარიანტი N2

total = 0
n = int(input("Enter a positive number: "))
for i in range(2, n+1):
    if i  % 2 == 1:
         continue
    total += i
print ("Total:", total)

   
   
    



