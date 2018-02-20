def denormalizeTime(timeInMinutes):
    if(timeInMinutes < 720):
        hour = timeInMinutes // 60 #divide with integral result
        minute = timeInMinutes % 60 #Take modulo in order to get the remainder
        return ("{0:02d}{1:02d}".format(hour, minute))
    elif(timeInMinutes == 720):
        hour = 1200
        # return hour
        return ("1200")
    else:
        hour = ((timeInMinutes - 720) // 60) + 12   # divide with integral result
        minute = timeInMinutes % 60  # Take modulo in order to get the remainder
        return ("{0:02d}{1:02d}".format(hour, minute))

#Durations from one airport to another in minutes
timeAusDal = 50     #Austin to Dallas Flight time in minutes and vice versa
timeAusHou = 45     #Austin to Houston Flight time in minutes and vice versa
timeDalHou = 65     #Dallas to Houston Flight time in minutes and vice versa

#Minimum Ground Time at the Airports in minutes
groundTimeAus = 25
groundTimeDal = 30
groundTimeHou = 35

flightSchedule = []    #Declaring a list to store the flight schedule

#Tail1 Austin to Dallas and vice versa
dayStart = 360  #(6*60) Day Starts at 0600 before which flight cannot depart
dayEnd = 1320   #(22*60) Day Ends at 2200 after which flights cannot arrive

#Initializing Arrival and Departure times for the airports
depAus = 360
arrAus = 360
depDal = 360
arrDal = 360
depHou = 360
arrHou = 360

while(dayStart < dayEnd):
    # print(dayStart)
    arrDal = depAus + timeAusDal;
    flightSchedule.append(['T1', 'AUS', 'DAL', denormalizeTime(depAus), denormalizeTime(arrDal)])
    depDal = arrDal + groundTimeDal
    # print ("Dallas: " +str(arrDal) + " " + str(depDal))
    arrAus = depDal + timeAusDal;
    flightSchedule.append(['T1', 'DAL', 'AUS', denormalizeTime(depDal), denormalizeTime(arrAus)])
    depAus = arrAus + groundTimeAus
    # print("Austin: "+str(arrAus) + " " + str(depAus))
    dayStart = depAus + timeAusDal + groundTimeDal + timeAusDal


#Tail2 Dallas to Houston and vice versa
dayStart = 360  #(6*60) Day Starts at 0600 before which flight cannot depart
dayEnd = 1320   #(22*60) Day Ends at 2200 after which flights cannot arrive

#Initializing Arrival and Departure times for the airports
depAus = 360
arrAus = 360
depDal = 360
arrDal = 360
depHou = 360
arrHou = 360

while(dayStart < dayEnd):
    arrHou = depDal + timeDalHou;
    flightSchedule.append(['T2', 'DAL', 'HOU', denormalizeTime(depDal), denormalizeTime(arrHou)])
    depHou = arrHou + groundTimeHou
    arrDal = depHou + timeDalHou;
    flightSchedule.append(['T2', 'HOU', 'DAL', denormalizeTime(depHou), denormalizeTime(arrDal)])
    depDal = arrDal + groundTimeDal
    dayStart = depDal + timeDalHou + groundTimeHou + timeDalHou


#Tail3 Austin to Houston and vice versa
dayStart = 360  #(6*60) Day Starts at 0600 before which flight cannot depart
dayEnd = 1320   #(22*60) Day Ends at 2200 after which flights cannot arrive

#Initializing Arrival and Departure times for the airports
depAus = 360
arrAus = 360
depDal = 360
arrDal = 360
depHou = 360
arrHou = 360

while(dayStart < dayEnd):
    arrAus = depHou + timeAusHou;
    flightSchedule.append(['T3', 'HOU', 'AUS', denormalizeTime(depHou), denormalizeTime(arrAus)])
    depAus = arrAus + groundTimeAus
    arrHou = depAus + timeAusHou;
    flightSchedule.append(['T3', 'AUS', 'HOU', denormalizeTime(depAus), denormalizeTime(arrHou)])
    depHou = arrHou + groundTimeHou
    dayStart = depHou + timeAusHou + groundTimeHou + timeAusHou


#Tail4 Houston to Dallas and vice versa
dayStart = 360  #(6*60) Day Starts at 0600 before which flight cannot depart
dayEnd = 1320   #(22*60) Day Ends at 2200 after which flights cannot arrive

#Initializing Arrival and Departure times for the airports
depAus = 360
arrAus = 360
depDal = 360
arrDal = 360
depHou = 360
arrHou = 360

for i in range(10):
    if dayStart < dayEnd:
        arrHou = depDal + timeDalHou
        flightSchedule.append(['T4', 'DAL', 'HOU', denormalizeTime(depDal), denormalizeTime(arrHou)])
        depHou = arrHou + groundTimeHou
        dayStart = depHou + timeDalHou + groundTimeDal

    if dayStart < dayEnd:
        arrDal = depHou + timeDalHou
        flightSchedule.append(['T4', 'HOU', 'DAL', denormalizeTime(depHou), denormalizeTime(arrDal)])
        depDal = arrDal + groundTimeDal
        dayStart = depDal + timeDalHou + groundTimeHou


# Tail5 Dallas to Houston and vice versa
dayStart = 360  # (6*60) Day Starts at 0600 before which flight cannot depart
dayEnd = 1320  # (22*60) Day Ends at 2200 after which flights cannot arrive

# Initializing Arrival and Departure times for the airports
depAus = 360
arrAus = 360
depDal = 360
arrDal = 360
depHou = 360
arrHou = 360

for i in range(10):
    if dayStart < dayEnd:
        arrDal = depHou + timeDalHou
        flightSchedule.append(['T5', 'HOU', 'DAL', denormalizeTime(depHou), denormalizeTime(arrDal)])
        depDal = arrDal + groundTimeDal
        dayStart = depDal + timeDalHou + groundTimeHou

    if dayStart < dayEnd:
        arrHou = depDal + timeDalHou
        flightSchedule.append(['T5', 'DAL', 'HOU', denormalizeTime(depDal), denormalizeTime(arrHou)])
        depHou = arrHou + groundTimeHou
        dayStart = depHou + timeDalHou + groundTimeDal

# Tail6 Houston to Dallas and vice versa
dayStart = 360  # (6*60) Day Starts at 0600 before which flight cannot depart
dayEnd = 1320  # (22*60) Day Ends at 2200 after which flights cannot arrive

# Initializing Arrival and Departure times for the airports
depAus = 360
arrAus = 360
depDal = 360
arrDal = 360
depHou = 360
arrHou = 360
t6DalHou = 455

for i in range(10):
    if dayStart < dayEnd:
        arrDal = t6DalHou + timeDalHou
        flightSchedule.append(['T6', 'HOU', 'DAL', denormalizeTime(t6DalHou), denormalizeTime(arrDal)])
        depDal = arrDal + groundTimeDal
        dayStart = depDal + timeDalHou + groundTimeHou

    if dayStart < dayEnd:
        arrHou = depDal + timeDalHou
        flightSchedule.append(['T6', 'DAL', 'HOU', denormalizeTime(depDal), denormalizeTime(arrHou)])
        t6DalHou = arrHou + groundTimeHou
        dayStart = t6DalHou + timeDalHou + groundTimeDal

# sort the flight schedule according to tail number and departure time
flightSchedule = sorted(flightSchedule, key = lambda x: x[3] + x[4])

for path in flightSchedule:
    print(path)

csvFileHeader = 'tail_number,origin,destination,departure_time,arrival_time'
fileName = 'flight_schedule.csv'

def getFlightSchedule(fileName, csvFileHeader, flightSchedule):
    with open(fileName,'wt') as file1:
        print(csvFileHeader, file=file1)
        for line in flightSchedule:
            print(','.join(line), file=file1)

getFlightSchedule(fileName, csvFileHeader, flightSchedule)
