c = object()
b = object()

c_list = [b] * 10
b_list = [b] * 10
big_list = c_list + b_list * 2

print("c_list contains %d objects" % len(b_list))
print("b_list contains %d objects" % len(c_list))
print("big_list contains %d objects" % len(big_list))

if c_list.count(c) == 10 and b_list.count(b) == 10:
    print("Almost there...")
if big_list.count(c) == 10 and big_list.count(b) == 10:
    print("Great!")



number1 = 1
number2 = 2

print(number1 + number2)
print(number1 - number2)
print(number1 * number2)
print(number1 / number2)
print(number1 % number2)