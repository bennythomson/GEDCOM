import sqlite3
# Initialize variables for the individual dnd family fields (pull up fields)
# Individual's Attributes: ID, Name, sex, birth, aliveBoolean, death, child, spouse
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


# Family Attributes: ID, Marriage date, divorce date, husband ID, wife ID, children
class Family:
    def __init__(self, id, marriage, divorce, husband, wife, children):
        self.id = id
        self.marriage = marriage
        self.divorce = divorce
        self.husband = husband
        self.wife = wife
        self.children = children

        if not isinstance(husband, Individual):
            self.husband = self.get_indiv(husband)

        if not isinstance(wife, Individual):
            self.wife = self.get_indiv(wife)

    def get_indiv(self, ID):

        connection = sqlite3.connect("./family.db")
        cur = connection.cursor()
        # Query all familes in database
        cur.execute("SELECT * FROM individuals WHERE ID = ?", (str(ID).strip(),))
        indiv_result = cur.fetchall()

        if not indiv_result:
            return None

        indiv_obj = Individual(indiv_result[0][0], indiv_result[0][1], indiv_result[0][2], indiv_result[0][3],
                               indiv_result[0][4], indiv_result[0][5], indiv_result[0][6], indiv_result[0][7])

        return indiv_obj

    def get_children(self):
        #returns a list of the Individual objects, corresponding to the children in the family
        if self.children is None:
            return []
        explode = self.children.split(',')

        return map(self.get_indiv, explode[:len(explode)-1])

    def get_children_ids(self):
        #returns a list of Family's children's IDs
        if self.children is None:
            return []
        explode = self.children.split(',')

        return explode[:len(explode)-1]
