import multiprocessing
import ast
from win10toast import ToastNotifier as tn
import time
from multiprocessing import process
import datetime


toast = tn()

input_string = f"{datetime.datetime.now()}"
input_format = "%Y-%m-%d %H:%M:%S.%f"
datetime_obj = datetime.datetime.strptime(input_string, input_format)
year = datetime_obj.year
month = datetime_obj.month
day = datetime_obj.day
hour = datetime_obj.hour
minute = datetime_obj.minute
sec = datetime_obj.second
timeI = f"{year}-{month}-{day} {hour}:{minute}:{sec}"
print(timeI)

s = 1
a = []
number = 0
timeStringI = timeI

"""
def todos():
    while s == 1:
        #it = input('Please enter Todo\n')
        t#i = input('Please enter due date\n')

        ts = datetime.datetime.strptime(ti, '%Y-%m-%d %H:%M:%S')
        year = ts.year
        month = ts.month
        day = ts.day
        hour = ts.hour
        minute = ts.minute
        sec = ts.second
        timeStringI = f"{year}-{month}-{day} {hour}:{minute}:{sec}"

        global g
        g = a
        g.append(it)

        for i in g:
            number1 = number
            print(number1, i)
            number1 = number1 +1
            #print(timeStringI)
            #print( timeI)
"""

def notifications(timeI, timeStringI, g):

    #n = map(ast.literal_eval, g)
    n = [x.encode('UTF8') for x in g]
    #y = [i.decode('utf-8') if isinstance(i, list) else i for i in g]
    #timeII = ast.literal_eval(timeI)
    #timeStringII = ast.literal_eval(timeStringI)

    while(timeI != timeStringI ):

        #print('a')

        input_string = f"{datetime.datetime.now()}"
        input_format = "%Y-%m-%d %H:%M:%S.%f"

        datetime_obj = datetime.datetime.strptime(input_string, input_format)

        year = datetime_obj.year
        month = datetime_obj.month
        day = datetime_obj.day
        hour = datetime_obj.hour
        minute = datetime_obj.minute
        sec = datetime_obj.second

        timeI = f"{year}-{month}-{day} {hour}:{minute}:{sec}"

    toast.show_toast(
                "Mitteilung",
                g[0],
                duration= 20,
                threaded= True,
                icon_path="img/icon.ico"
    )


### Start Multiprocessing
### if var g has a value, give it to the Notifications function
### else don't. Not working right now which's why I had to get g a value
### maybe start later?
if __name__ == '__main__':
    #while s == 1:
    it = input('Please enter Todo\n')
    ti = input('Please enter due date\n')

    ts = datetime.datetime.strptime(ti, '%Y-%m-%d %H:%M:%S')
    year = ts.year
    month = ts.month
    day = ts.day
    hour = ts.hour
    minute = ts.minute
    sec = ts.second
    timeStringI = f"{year}-{month}-{day} {hour}:{minute}:{sec}"

    g = a
    g.append(it)

    for i in g:
        number1 = number
        print(number1, i)
        number1 = number1 + 1
        # print(timeStringI)
        # print( timeI)

    queue = multiprocessing.Queue()

    #p1 = multiprocessing.Process(target=todos)
    #p1.start()
    #p1.join()
    p2 = multiprocessing.Process(target=notifications, args=(timeI, timeStringI, g))
    p2.start()
    p2.join()

