from scrapy.http import HtmlResponse
import requests
from random import randint
import MySQLdb
import pymysql

def displayAll():
    #display all customers from db
    print("Showing all the Customers")
    try:
        cursor, db = connectusingpymysql()
        query = "SELECT * FROM customers;"
        cursor.execute(query)
        list = cursor.fetchall()
        if not list:
            print("Empty customer's DB")
        else:
            for i in list:
                print i


    except Exception as e:
        print("Something went wrong with sql while displaying")
        print(e)
    print("\nShowing all the Hairstyles available")
    try:
        cursor, db = connectusingpymysql()
        query = "SELECT * FROM haircut;"
        cursor.execute(query)
        list = cursor.fetchall()
        if not list:
            print("The Haircut DB is empty")
        else:

            for i in list:
                print i
    except Exception as e:
        print("Something went wrong with sql while displaying")
        print(e)

    userui()



def populatehaircut():
    haircutdict = {}
    print("Make sure the device is Connected to internet")
    try:
        url = "https://en.wikipedia.org/wiki/List_of_hairstyles"
        response = getresponseobj(url)

        query = "INSERT INTO haircut(type, price) VALUES ( %s, %s)"

        lst = response.xpath('//table[@class="wikitable"]/tr/td/a/text()').extract()

        cursor, db = connectusingpymysql()

        for i in lst:
            temp = randint(100, 1000)
            haircutdict[i] = temp
            data = (i, int(temp))
            cursor.execute(query, data)

        print haircutdict
        db.commit()
        closedb(cursor, db)

    except Exception as e:
        print("Something went wrong in fetching or SQl")
        print(e)


def closedb(cursor,db):
    cursor.close()
    db.close()

def getresponseobj(url):
    body = requests.get(url).text
    response = HtmlResponse(url=url, body=body, encoding='utf-8')
    return response

def connectusingpymysql():
    try:
        db = MySQLdb.connect(user="root", passwd="", db="Saloon", unix_socket="/opt/lampp/var/mysql/mysql.sock")
        db.autocommit = True
        cursor2 = db.cursor()
        return cursor2, db
    except Exception as e:
        print "pymysql also failed"
        print e

def erasedb():
    try:
        cursor,db=connectusingpymysql()
        query = "DELETE FROM haircut;"
        cursor.execute(query)
        db.commit()
        query = "DELETE FROM customers;"
        cursor.execute(query)
        db.commit()
        closedb(cursor,db)
    except Exception as e:
        print("Something went wrong with sql query while erasing")
        print e

    userui()


def selectcustomer():
    #choosing the customer from db
    choice ='y'
    while choice=='y' or choice =='Y':
        name = raw_input("Please enter the name of the user you wanna view :")
        cursor,db = connectusingpymysql()
        query ="SELECT * FROM customer where name=%s"
        data = (name,)
        cursor.execute(query,data)
        details = cursor.fetchall()
        for i in details:
            print i
        choice = raw_input("Do You wanna view anyone else's data(y/n) ??")

    closedb(cursor,db)
    userui()


def newCustomer():
    # Entering new customer into db
    choice = 'y'
    while choice == 'y' or choice == 'Y':
        print "Enter the details of the new customer"
        name = raw_input("Enter the name of the customer :")
        age = input("Enter the age of the customer :")
        prefered_style = raw_input("Enter the prefered style of the customer :")
        query = "INSERT INTO customers(name, age, preferred_style) values (%s,%s,%s);"
        try :

            cursor, db =connectusingpymysql()
            data = (name,int(age),prefered_style)
            cursor.execute(query,data)
            db.commit()
        except Exception as e:
            print("SQL queries caused this")
            print(e)
        choice = raw_input("Do You wanna enter anyone else's data(y/n) ??")

    closedb(cursor, db)
    userui()


def searchhairstyle():
    cursor, db = connectusingpymysql()
    choice = 'y'
    while choice == 'y' or choice == 'Y':
        name = raw_input("Enter the type of the hair style :")
        query = "SELECT * FROM haircut where type=%s;"
        name = (name,)
        try:
            cursor.execute(query,name)
            data = cursor.fetchall()
        except Exception as e:
            print("SQL caused this")
            print(e)
        for i in data:
            print i
        choice = raw_input("Do you wanna search more (y/n)?? ")

    closedb(cursor,db)





def editDb():
    # edit the db
    print""
    name = raw_input("Enter the hairstyle first name to edit :")
    query="SELECT * FROM haircut where type=%s ;"
    name = (name,)
    try:

        cursor, db = connectusingpymysql()
        cursor.execute(query, name)
        data = cursor.fetchall()
    except Exception as e:
        print("SQL queries went wrong")
        print(e)
    for i in data:
        print i
    choice = raw_input("Is this the Item you wanted to edit ?? (y/n) :")
    if choice=='y' or choice == 'Y':
        query="DELETE FROM haircut where type=%s"
        try:

            cursor.execute(query, name)
            db.commit()
        except Exception as e:
            print("Something went wrong in sql")
            print(e)
        name = raw_input("Enter the new name you wanna give to that style :")
        price = input("Enter the revised price :")
        data = (name, price)
        query = "INSERT INTO haircut (type,price) VALUES (%s,%s);"
        try:

            cursor.execute(query,data)
            db.commit()
            print("Successfully Edited")
        except Exception as e:
            print("Inserting in db went wrong")
            print(e)



def newEntry():
    #new entry in hairstyle table
    print ""
    choice = 'y'
    while choice == 'y' or choice == 'Y':
        name = raw_input("Enter the name of the new hairstyle :")
        price = input("Enter the price of the new hairstyle :")
        query = "INSERT INTO haircut(type, price) values(%s, %s);"
        data = (name, price)
        try:
            cursor,db =connectusingpymysql()
            cursor.execute(query,data)
        except Exception as e:
            print("Problem in SQL")
            print(e)
        db.commit()
        choice = raw_input("Do You wanna view anyone else's data(y/n) ??")
    closedb(cursor, db)
    userui()


def userui():
    print("****************************************SALOON DATABASE****************************************")
    print("1. Search Customer from DB ")
    print("2. Enter a new customer ")
    print("3. Display all customers ")
    print("4. Edit hairstyle prices or names ")
    print("5. Enter new hairstyle")
    print("6. Search Hairstyle")
    print("7. Erase DB")
    print("8. Fetch Haircut prices from WEB")
    print("9. Quit")
    #print("Populating DB")
    #populatehaircut()
    choice = input("Choose any one of the above choices:")
    choice = int(choice)
    if choice==9:
        exit(0)

    elif choice==1:
        selectcustomer()

    elif choice == 2:
        newCustomer()

    elif choice == 3:
        displayAll()

    elif choice == 4:
        editDb()
        userui()
    elif choice==5:
        newEntry()

    elif choice==7:
        erasedb()

    elif choice==8:
        populatehaircut()
        userui()

    elif choice == 6:
        searchhairstyle()
        userui()

    else:
        print("Wrong choice, Choose again")
        userui()







"""
def connectdb():
    try:
        connect_str = "dbname='saloon' user='root' host='127.0.0.1' password=''"
        conn = psycopg2.connect(connect_str)
        conn.autocommit = True
        cursor = conn.cursor()
        return cursor
    except Exception as e:
        print "cant connect to db, some local host problem"
        print e
"""


if __name__== '__main__':
    userui()






