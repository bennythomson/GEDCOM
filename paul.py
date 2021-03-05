import datetime


def birth_after_marriage(individual=None, family=None):

    if individual is not None and family is not None:

        # Check if the birth date or marriage date are empty
        if individual[3] is None or family[1] is None:
            return None

        marriage_date = datetime.datetime.strptime(family[1], '%Y-%m-%d').date()
        birth_date = datetime.datetime.strptime(individual[3], '%Y-%m-%d').date()

        if birth_date >= marriage_date:

            print("Error US02: " + individual[0] + " marriage before birth")
            return individual[0]

    return None


def birth_before_death(individual=None):
    if individual is not None:
        if individual[3] is None or individual[5] is None:
            return None
    birth_date = datetime.datetime.strptime(individual[3], '%Y-%m-%d').date()
    death_date = datetime.datetime.strptime(individual[5],'%Y-%m-%d').date()

    if birth_date >= death_date:

        print("Error US03: " + individual[0] + "death before birth")
        return individual[0]

    return None



def paul_user_stories(conn):

    cur = conn.cursor()
    cur.execute("SELECT * FROM families")

    families = cur.fetchall()

    for family in families:

        for indiv in family[3:5]:
            if indiv is not None:
                indiv = indiv.strip()
                new_cur = conn.cursor()

                new_cur.execute("SELECT * FROM individuals WHERE ID = ?", (str(indiv), ))
                indiv_result = new_cur.fetchall()

                birth_after_marriage(indiv_result[0], family)
                birth_before_death(indiv_result[0])
