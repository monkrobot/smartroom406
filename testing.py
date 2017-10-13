#import testing2
#import time
#numbers = [x for x in range(100)]
#
#def firstfunc(numbers):
#    res = []
#    for i in numbers:
#        res.append(i**2)
#
#def secondfunc(numbers):
#    res = [x**2 for x in numbers]
#
#for function_exec in [firstfunc, secondfunc]:
#    speed = testing2.test(function_exec, numbers, number_of_use=1)
#    print(speed)
#
#start = time.clock()
#firstfunc(numbers)
#print('time: ' + str(time.clock()-start))
#
#start2 = time.clock()
#secondfunc(numbers)
#print('time: ' + str(time.clock()-start2))


#def func123(x):
#    x.append(1)
#    print(x)
#x =[4]
#xyz = func123(x)
#yz = func123(x)
#xz = func123(x)


list1 = [{1: 's'}, {2: "sld"}, {3: 'd'}]
#y = list1.index({2: "sld"})
#y = list1.remove({2: "sld"})
#print(y)
#print(list1)
#id_del = 4
#for i in list1:
#    if id_del in i:
#        print("yes")
#        list1.remove(i)
#        break
#    else:
#        print('no')
#        continue
#
#print(list1)
num = 14+1j
print(type(num))
print(2.3 // 2)
print(num.imag)

x = 23
y = 'boo'
print(x and y)
