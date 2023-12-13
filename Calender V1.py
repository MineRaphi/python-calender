import time
from datetime import datetime
import os
#print("   21   22  [23]  24   25   26   27   ")
#print("--------------------------------------")
#print("   01    02    03    04    05    06   ")
#print("   07    08    09    10    11    12   ")
#print("--------------------------------------")
#print("   01   02   03   04   05   06   07   ")
#print("   08   09   10   11   12   13   14   ")
#print("   15   16   17   18   19   20   21   ")
#print("   22   23   24   25   26   27   28   ")
#print("   29   30   31                       ")

monthline1 = [  "   01    02    03    04    05    06   ",
                "  [01]   02    03    04    05    06   ",
                "   01   [02]   03    04    05    06   ",
                "   01    02   [03]   04    05    06   ",
                "   01    02    03   [04]   05    06   ",
                "   01    02    03    04   [05]   06   ",
                "   01    02    03    04    05   [06]  "]

monthline2 = [  "   07    08    09    10    11    12   ",
                "  [07]   08    09    10    11    12   ",
                "   07   [08]   09    10    11    12   ",
                "   07    08   [09]   10    11    12   ",
                "   07    08    09   [10]   11    12   ",
                "   07    08    09    10   [11]   12   ",
                "   07    08    09    10    11   [12]  "]

dayline1 = ["   01   02   03   04   05   06   07   ",
            "  [01]  02   03   04   05   06   07   ",
            "   01  [02]  03   04   05   06   07   ",
            "   01   02  [03]  04   05   06   07   ",
            "   01   02   03  [04]  05   06   07   ",
            "   01   02   03   04  [05]  06   07   ",
            "   01   02   03   04   05  [06]  07   ",
            "   01   02   03   04   05   06  [07]  "]

dayline2 = ["   08   09   10   11   12   13   14   ",
            "  [08]  09   10   11   12   13   14   ",
            "   08  [09]  10   11   12   13   14   ",
            "   08   09  [10]  11   12   13   14   ",
            "   08   09   10  [11]  12   13   14   ",
            "   08   09   10   11  [12]  13   14   ",
            "   08   09   10   11   12  [13]  14   ",
            "   08   09   10   11   12   13  [14]  "]

dayline3 = ["   15   16   17   18   19   20   21   ",
            "  [15]  16   17   18   19   20   21   ",
            "   15  [16]  17   18   19   20   21   ",
            "   15   16  [17]  18   19   20   21   ",
            "   15   16   17  [18]  19   20   21   ",
            "   15   16   17   18  [19]  20   21   ",
            "   15   16   17   18   19  [20]  21   ",
            "   15   16   17   18   19   20  [21]  "]

dayline4 = ["   22   23   24   25   26   27   28   ",
            "  [22]  23   24   25   26   27   28   ",
            "   22  [23]  24   25   26   27   28   ",
            "   22   23  [24]  25   26   27   28   ",
            "   22   23   24  [25]  26   27   28   ",
            "   22   23   24   25  [26]  27   28   ",
            "   22   23   24   25   26  [27]  28   ",
            "   22   23   24   25   26   27  [28]  "]

dayline5 = ["   29   30   31                       ",
            "  [29]  30   31                       ",
            "   29  [30]  31                       ",
            "   29   30  [31]                      "]

def prt_calander():
    day = datetime.now().day
    month = datetime.now().month
    year = datetime.now().year
    hour = datetime.now().hour
    minute = datetime.now().minute
    second = datetime.now().second
    while year > 99:
        year-=100
    
    print("--------------------------------------")
    print("   "+str(year-2)+"   "+str(year-1)+"  ["+str(year)+"]  "+str(year+1)+"   "+str(year+2)+"   "+str(year+3)+"   "+str(year+4)+"   ")
    print("--------------------------------------")

    if month <= 6:
        print(monthline1[month])
        print(monthline2[0])
    elif month > 6: 
        print(monthline1[0])
        print(monthline2[month -6])
    print("--------------------------------------")

    if day < 8:
        print(dayline1[day])
        print(dayline2[0])
        print(dayline3[0])
        print(dayline4[0])
        print(dayline5[0])
    elif day < 15:
        print(dayline1[0])
        print(dayline2[day-7])
        print(dayline3[0])
        print(dayline4[0])
        print(dayline5[0])
    elif day <22:
        print(dayline1[0])
        print(dayline2[0])
        print(dayline3[day-14])
        print(dayline4[0])
        print(dayline5[0])
    elif day < 29:
        print(dayline1[0])
        print(dayline2[0])
        print(dayline3[0])
        print(dayline4[day -21])
        print(dayline5[0])
    elif day < 32:
        print(dayline1[0])
        print(dayline2[0])
        print(dayline3[0])
        print(dayline4[0])
        print(dayline5[day -28])
        
    print("--------------------------------------")
    print("              "+str(hour)+":"+str(minute)+":"+str(second)+"                 ")
    time.sleep(1)
    #os.system('cls')   #use only on windows
    #os.system('clear') #use only on linux
    prt_calander()

prt_calander()