import datetime
from datetime import date

def divorce_after_death(individual=None, family=None):
    # for those who don't have empty information
    if individual and family is not None:

        # skip those who have no death date or divorce date

        # Bad Smell #1:  There is duplicated code for is None
        if individual[5] is None or family[2] is None:
            return None

        # Bad Smell #2: There is duplicated code for getting the date
        def clean_date(date_str):
            return datetime.datetime.strptime(date_str, '%Y-%m-%d').date()

        divorce_date = clean_date(family[2])
        individuals_death = clean_date(individual[5])

        # check if divorce date is greater than death date, print the error, return the individual
        if divorce_date > individuals_death:
            print("Error US06: ", individual[0], " got divorced after death, review Simpson Family")
            return individual[0]

    return None

def mc_user_stories(conn):
    # connect to the data base
    cur = conn.cursor()
    cur.execute("SELECT * FROM families")

    # fetch all the rows
    families = cur.fetchall()

    for family in families:

        # manipulate data that for individuals that have information
        for indiv in family[3:5]:
            if indiv is not None:
                indiv = indiv.strip()
                new_cur = conn.cursor()

                new_cur.execute("SELECT * FROM individuals WHERE ID = ?", (str(indiv),))
                indiv_result = new_cur.fetchall()
                # connect to the defined variable created before
                divorce_after_death(indiv_result[0], family)