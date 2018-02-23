# -*- coding: utf-8 -*-
import re
import pymysql

district_id = 0


def show_tables():
    i=1
    while(i):
        data = list_of_tables(i)
        if data is None:
            break
        print(str(i) + ":" +data)
        i = i+1


def show_queries():
    i=1
    while(i):
        data = listOfQueries(i,district_id)
        if data is None:
            break
        print(str(i) + ":" +data)
        i = i+1


def list_of_tables(x):
    return {
        1: 't_institution',
        2: 't_class',
        3: 'd_class_section',
        4: 't_district_sync_config',
        5: 't_district_taxonomy_map',
        6: 't_mastery_criteria',
        7: 't_performance_band',
        8: 't_rubric_details',
        9: 't_school_year',
    }.get(x, None)


def listOfQueries(x,district_id):
    return {

        # get all the institutions based on the district id

        1: "select distinct c.* from t_class as t , t_institution as c where t.institution_id in (select distinct c.id as institution_id from t_dn_org_reference as a INNER join t_institution_district_codes as b on b.institutionDistrict_Id=a.institution_district_id Inner join t_institution as c on c.institution_district_id=a.institution_district_id where a.institution_district_id="+str(district_id)+") and t.institution_id=c.id;",

        # select all the fields from the table

        0: "select * from "+table_name+" limit 1000;",

        # get all courses in a particular institution id in a particular district

        2: "select distinct t.* from t_class as t , t_institution as c where t.institution_id in (select distinct c.id as institution_id from t_dn_org_reference as a INNER join t_institution_district_codes as b on b.institutionDistrict_Id=a.institution_district_id Inner join t_institution as c on c.institution_district_id=a.institution_district_id where a.institution_district_id="+str(district_id)+") and t.institution_id=c.id;",

        # get all the details of table where district id = ""

        3: "select * from "+table_name+ " where district_id =" +str(district_id)+ " LIMIT 1000;",



    }.get(x, None)


def matchNumber(item):
    try:
        res = bool(re.search(r'\D+',item))
        return res
    except Exception as e:
        return True


def ordone(item):
    try:
        res = ord(item)
        return True
    except Exception as e:
        return False


def version2(results):
    content = ""
    for i in results:
        content = content + "("
        for j in i:
            if j is None:
                j = 'NULL'
            elif ordone(j):
                j = ord(j)
            elif matchNumber(str(j)):
                j = '\"' + str(j).replace("\"",'') + '\"'
            content = content + str(j) + " ,"
        content = content.rstrip(',')
        content = content + ") ,\n"
    content = content.rstrip(',')
    return content


def getSchema(cursor,table_name):

    query = "select COLUMN_NAME from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME='"+str(table_name)+"';"
    insert_query = "INSERT INTO "+str(table_name)+" ("
    cursor.execute(query)
    result = cursor.fetchall()
    for i in result:
        item = str(i)
        item = re.findall(r'\w+', item, re.I)
        item = item[0]
        if item:
            insert_query = insert_query+item+", "
    insert_query = insert_query + " ) VALUES ";
    return insert_query


def connectdb():
    try:
        conn = pymysql.connect(db="mongrel", user="dbuser", host="ec2-54-167-210-35.compute-1.amazonaws.com", passwd="dbpassword")
        conn.autocommit = True
        cursor = conn.cursor()
        return cursor
    except Exception as e:
        print("Db connection unsuccessfull!! please check the connection parameters")
        print(e)
        exit(1)


def closedbconnection(cursor):
    cursor.close()


if __name__ == "__main__":

    final_query = ""
    table_name = 't_institution'

    print("########CHOOSE THE TABLE YOU WANNA EXPORT############ ")
    show_tables()
    table_id = int(input(':'))
    table_name = list_of_tables(table_id)

    district_id = int(input("Enter the district Id :"))

    print("choose the list of queries you wanna run :")
    print("select 0 for showing all details of the table")
    show_queries()
    query_id = int(input(":"))
    query = listOfQueries(query_id,district_id)

    cursor = connectdb()
    try:
        insert_query = getSchema(cursor,table_name)
        cursor.execute(query)
        results = cursor.fetchall()
        content = version2(results)
        print(str(len(results)) + " results returned ")
        final_query = content
        final_query = insert_query + final_query
        with open('output.sql','w') as f:
            f.write(str(final_query))
        closedbconnection(cursor)
    except Exception as e:
        print(e)
        exit(1)




