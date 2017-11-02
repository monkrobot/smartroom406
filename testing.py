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


#list1 = [{1: 's'}, {2: "sld"}, {3: 'd'}]
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


#Coursera homework
import csv

class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying

class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passengers_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passengers_seats_count = passengers_seats_count

class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.body_whl = body_whl
        list_body_size = self.body_whl.split('x')
        try:
            self.body_size = int(list_body_size[0])*int(list_body_size[1])*float(list_body_size[2])
        except ValueError:
            self.body_size = 0

    #def body_size(self):
    #    list_body_size = self.body_whl.split('x')
    #    return list_body_size

class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra

def get_car_list(csv_filename):
    car_list = []
    try:
        with open(csv_filename) as csv_file:
            reader = csv.reader(csv_file, delimiter=";")
            next(reader)
            for row in reader:
                #print(row)
                car_list.append(row)
    except IOError:
        result = "Error"
        return result

    return car_list


cars = []
trucks = []
spec_macs = []

car_list = get_car_list("week3_cars.csv")
print(car_list)

for i in range(len(car_list)-1):
        if car_list[i][0] == "car":
            car = Car(car_list[i][1], car_list[i][3], car_list[i][5], car_list[i][2])
            cars.append(car)
        if car_list[i][0] == "truck":
            truck = Truck(car_list[i][1], car_list[i][3], car_list[i][5], car_list[i][4])
            trucks.append(truck)
        if car_list[i][0] == "spec_machine":
            spec_mac = SpecMachine(car_list[i][1], car_list[i][3], car_list[i][5], car_list[i][6])
            spec_macs.append(spec_mac)

print("cars:", cars)
print("trucks:", trucks)
print("spec_macs:", spec_macs)

for truck in range(len(trucks)):
    print('body_size:', trucks[truck].body_size)