N = int(input("Write an integer: "))
odd_numbers = list()
even_numbers = list()
#even_numbers = [e for e in range(1, N+1) if (e % 2) == 0]
#odd_numbers = [o for o in range(1, N+1) if (o % 2) == 0]
for i in range(1, N+1):
    if (i % 2) == 0:
        even_numbers.append(i)
    else:
        odd_numbers.append(i)
sum_of_odds = 0
for m in odd_numbers:
    sum_of_odds += m
sum_of_evens = 0
for j in even_numbers:
    sum_of_evens += j
avarage_of_evens = sum_of_evens // len(even_numbers)
print("""
The sum of odd numbers = {}
The avarage of even numbers = {}

""".format(sum_of_odds,avarage_of_evens))
