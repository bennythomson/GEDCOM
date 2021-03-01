import datetime
def marriage_after_death(individual=None, family=None):
    #dont fear the reaper....
    if(individual != None and family != None):

        #check if the death date or marriage date are none
        if(individual[5] == None or family[1] == None):
            return None

        marriage_date = family[1]
    #    print(marriage_date)
        marriage_date = datetime.datetime.strptime(marriage_date, '%Y-%m-%d').date()
        individuals_death = datetime.datetime.strptime(individual[5], '%Y-%m-%d').date()

        if(individuals_death <= marriage_date):


            print("Error US05: " + individual[0] + " marriage after death")
            return individual[0]

    return None





def ben_user_stories(conn):

    cur = conn.cursor()
    cur.execute("SELECT * FROM families")

    rows = cur.fetchall()

#    print(rows)
    for row in rows:


        for indiv in row[3:5]:
            if indiv != None:
                indiv= indiv.strip()
                new_cur = conn.cursor()

                new_cur.execute("SELECT * FROM individuals WHERE ID = ?",(str(indiv),))
                indiv_result = new_cur.fetchall()

                marriage_before_death(indiv_result[0], row)