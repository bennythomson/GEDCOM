import datetime

def divorce_before_death(conn):

    divorced_after_death = []

    cur = conn.cursor()
    cur.execute("SELECT * FROM families")

    rows = cur.fetchall()

    for row in rows:

        divorce_date = row[2]
        if(divorce_date != None):
            divorce_date = datetime.datetime.strptime(divorce_date, '%Y-%m-%d').date()

        #print(row[3:])

        for indiv in row[3:]:

            indiv= indiv.strip()
            new_cur = conn.cursor()

            new_cur.execute("SELECT * FROM individuals WHERE ID = ?",(str(indiv),))
            indiv_result = new_cur.fetchall()


            if(indiv_result[0][5] != None):
                individuals_death = datetime.datetime.strptime(indiv_result[0][5], '%Y-%m-%d').date()

                if(divorce_date != None):
                    if(individuals_death < divorce_date):

                        divorced_after_death.append(indiv)
                        print("Error: " + indiv_result[0][0] + " divorced after death")

    return divorced_after_death





def mc_user_stories(conn):
    divorce_before_death(conn)
