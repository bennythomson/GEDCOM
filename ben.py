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

def marriage_before_divorce(family=None):

    if(family[1] == None or family[2] == None):
        return None

    marriage_date = datetime.datetime.strptime(family[1], '%Y-%m-%d').date()
    divorce_date = datetime.datetime.strptime(family[2], '%Y-%m-%d').date()

    if(marriage_date >= divorce_date):
        print("Error US04: " + family[0] + " marriage before divorce")
        return family[0]

    return None





def ben_user_stories(conn):

    cur = conn.cursor()
    cur.execute("SELECT * FROM families")

    rows = cur.fetchall()

#    print(rows)
    for row in rows:

        marriage_before_divorce(row)
        for indiv in row[3:5]:
            if indiv != None:
                indiv= indiv.strip()
                new_cur = conn.cursor()

                new_cur.execute("SELECT * FROM individuals WHERE ID = ?",(str(indiv),))
                indiv_result = new_cur.fetchall()

                marriage_after_death(indiv_result[0], row)
