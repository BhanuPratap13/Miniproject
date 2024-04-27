start = int(input("Enter starting no.: "))
end = int(input("Enter the ending no.: "))

if start > end:
    start, end = end, start
order = input("Press 1 for 'forward' or 2 for 'backward' for order: ")
display = input("Press 3 for 'horizontal' or 4 'vertical' for the display: ")

print("\nPrinting the numbers:")

if order == '1':
   for num in range(start, end + 1):
       print(num, end=' ' if display == '3' else '\n')
else:
   for num in range(end, start - 1, -1):
       print(num, end=' ' if display == '3' else '\n')