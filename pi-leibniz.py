''' Calculate pi using leibniz algorithm'''
# Initialize denominator
k = 1

# Initialize sum
s = 0

for i in range(10000000):

    # even index elements are positive
    if i % 2 == 0:
        s += 4/k
    else:

        # odd index elements are negative
        s -= 4/k

    # denominator is odd
    k += 2

print(s)

filename = 'piTon.txt'
with open(filename, 'w') as file_object:
    file_object.write(str(s))
