import datetime
def marriage_before_death(conn):
    #dont fear the reaper....

    married_after_death = []

    cur = conn.cursor()
    cur.execute("SELECT * FROM families")

    rows = cur.fetchall()

    print(rows)
    for row in rows:

        marriage_date = row[1]
        print(marriage_date)
        marriage_date = datetime.datetime.strptime(marriage_date, '%Y-%m-%d').date()

        #print(row[3:])

        for indiv in row[3:]:

            indiv= indiv.strip()
            new_cur = conn.cursor()

            new_cur.execute("SELECT * FROM individuals WHERE ID = ?",(str(indiv),))
            indiv_result = new_cur.fetchall()


            if(indiv_result[0][5] != None):
                individuals_death = datetime.datetime.strptime(indiv_result[0][5], '%Y-%m-%d').date()

                if(individuals_death < marriage_date):

                    married_after_death.append(indiv)
                    print("Error: " + indiv_result[0][0] + " marriage after death")

    return married_after_death





def ben_user_stories(conn):
    marriage_before_death(conn)
