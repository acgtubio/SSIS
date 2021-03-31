import csv

def getData():
    #Retrieves data from csv file.

    stList = []
    with open('students.csv','r') as file:
        reader = csv.reader(file)

        for row in reader:
            stList.append(row)
    
    #Returns list of students of format [id, last name, first name, middle name, year, course, gender].
    return stList

def pushData(info):
    #Sends data back to csv file.
    #Info is of format [id, last name, first name, middle name, year, course, gender].

    with open('students.csv','a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(info)

if __name__ == '__main__':
    #For testing purposes.

    print(getData())
    pushData(['2','Doe II','John','Doge','2','ME','idk'])
    print(getData())