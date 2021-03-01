import datetime


def divorce_after_death(individual=None, family=None):
    # for those who don't have empty information
    if individual is not None and family is not None:

        # skip those who have no death date or divorce date
        if individual[5] is None or family[2] is None:
            return None

        # set the columns to check from the two data tables and convert dates for manipulation
        divorce_date = family[2]
        divorce_date = datetime.datetime.strptime(divorce_date, '%Y-%m-%d').date()
        individuals_death = datetime.datetime.strptime(individual[5], '%Y-%m-%d').date()

        # check if divorce date is greater than death date, print the error, return the individual
        if divorce_date > individuals_death:
            print("US06 Error: ", individual[0], " got divorced after death, review Simpson Family")
            return individual[0]


    return None



def mc_user_stories(conn):
    # connect to the data base
    cur = conn.cursor()
    cur.execute("SELECT * FROM families")

    # fetch all the rows
    rows = cur.fetchall()

    for row in rows:

        # manipulate data that for individuals that have information
        for indiv in row[3:5]:
            if indiv is not None:
                indiv = indiv.strip()
                new_cur = conn.cursor()

                new_cur.execute("SELECT * FROM individuals WHERE ID = ?", (str(indiv),))
                indiv_result = new_cur.fetchall()
                # connect to the defined variable created before
                divorce_after_death(indiv_result[0], row)


