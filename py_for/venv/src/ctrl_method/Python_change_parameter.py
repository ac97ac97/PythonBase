def sum(*numbers,multiple=1.0):
    total = 0.0
    for number in numbers:
        total += number
    return total * multiple
print(sum(100,20,30))
print(sum(80,30))
print(sum(80,30,multiple=2))
double_tuple={50.0,60.0,0.0,110}
print(sum(80,30,*double_tuple))