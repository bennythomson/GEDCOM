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
