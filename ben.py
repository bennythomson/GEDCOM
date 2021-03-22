import datetime


#Objects to represent individuals and familes
class Individual:

    def __init__(self, id, name, sex, birthday, alive, death, children, spouse):

        self.id = id
        self.name = name
        self.sex = sex
        self.birthday = birthday
        self.alive = alive
        self.death = death
        self.children = children
        self.spouse = spouse

class Family:
    def __init__(self, id, marriage, divorce, husband, wife, children):
        #ID, marriage, divorce, husband, wife, children
        self.id = id
        self.marriage = marriage
        self.divorce = divorce
        self.husband = husband
        self.wife = wife
        self.children = children


def format_date(date_str):
    #takes in a string repreenting a date in Y-m-d format and returns a datetime object
    return datetime.datetime.strptime(date_str, '%Y-%m-%d').date()

def marriage_after_death(individual=None, family=None):
    #dont fear the reaper....


    '''This method returns the ID of the individual if their marriage date occurs
    after their death date'''
    if(individual != None and family != None):
        #check if the death date or marriage date are none
        if(individual.death == None or family.marriage == None):
            return None


        #print("death " + individual.death)
        #print(" ind: " + individual)
        #print("fam : " + family)

        marriage_date = format_date(family.marriage)
        individuals_death = format_date(individual.death)

        if(individuals_death <= marriage_date):
            print("Error US05: " + individual.id + " marriage after death")
            return individual.id

    return None

def marriage_before_divorce(family=None):

    if(family.marriage == None or family.divorce == None):
        return None

    marriage_date = format_date(family.marriage)
    divorce_date = format_date(family.divorce)

    if(marriage_date >= divorce_date):
        print("Error US04: " + family.id + " divorce date after marriage")
        return family.id

    return None



def ben_user_stories(conn):

    cur = conn.cursor()
    #Query all familes in database
    cur.execute("SELECT * FROM families")

    familes = cur.fetchall()

    for family in familes:
        #loop through each family, checking the divorce/marriage dates
        fam_obj = Family(family[0], family[1], family[2],family[3],family[4],family[5],)

        marriage_before_divorce(fam_obj)

        #loop through each individual in the family
        for indiv in family[3:5]:

            if indiv != None:
                indiv = indiv.strip()
                new_cur = conn.cursor()

                new_cur.execute("SELECT * FROM individuals WHERE ID = ?",(str(indiv),))
                indiv_result = new_cur.fetchall()

                indiv_obj = Individual(indiv_result[0][0], indiv_result[0][1], indiv_result[0][2], indiv_result[0][3], indiv_result[0][4], indiv_result[0][5], indiv_result[0][6], indiv_result[0][7])

                marriage_after_death(indiv_obj, fam_obj)
