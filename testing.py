import testing2
import time
numbers = [x for x in range(100)]

def firstfunc(numbers):
    res = []
    for i in numbers:
        res.append(i**2)

def secondfunc(numbers):
    res = [x**2 for x in numbers]

for function_exec in [firstfunc, secondfunc]:
    speed = testing2.test(function_exec, numbers, number_of_use=1)
    print(speed)

start = time.clock()
firstfunc(numbers)
print('time: ' + str(time.clock()-start))

start2 = time.clock()
secondfunc(numbers)
print('time: ' + str(time.clock()-start2))


#def func123(x):
#    x.append(1)
#    print(x)
#x =[4]
#xyz = func123(x)
#yz = func123(x)
#xz = func123(x)
