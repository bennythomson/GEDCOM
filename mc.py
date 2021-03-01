import datetime

def divorce_after_death(conn):

    # create a list where individuals who were divorced post death go
    divorced_after_death = []

    # create a connection to the data base and specific info
    connection = conn.cursor()
    connection.execute("SELECT * FROM families")

    # fetch rows from the connection
    rows = connection.fetchall()

    for row in rows:

        divorce_date = row[2]
        if(divorce_date != None):
            divorce_date = datetime.datetime.strptime(divorce_date, '%Y-%m-%d').date()

        for indiv in row[3:]:

            indiv= indiv.strip()
            anotha_one = conn.cursor()

            anotha_one.execute("SELECT * FROM individuals WHERE ID = ?",(str(indiv),))
            indiv_result = anotha_one.fetchall()


            if(indiv_result[0][5] != None):
                individual_death = datetime.datetime.strptime(indiv_result[0][5], '%Y-%m-%d').date()

                if(divorce_date != None):
                    if(individual_death < divorce_date):

                        divorced_after_death.append(indiv)
                        print("Error: Shows " + indiv_result[0][0] + " was divorced after death")

    return divorced_after_death





def mc_user_stories(conn):
    divorce_after_death(conn)
