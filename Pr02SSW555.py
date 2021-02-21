import sys

print("\nSSW 555: Project 02")
print("\nRun by MariaCristina Todaro\n")

gedcomfile = open('testged.ged', 'r')
sys.stdout = open("Project02Results.txt", "w")


supported_tags = [ "NAME", "SEX", "BIRT", "DEAT", "FAMC", "FAMS", "MARR", "HUSB", "WIFE",
                  "CHIL", "DIV", "DATE", "HEAD", "TRLR", "NOTE"]
caution = ["INDI", "FAM"]

for line in gedcomfile:
    # print input line
    print("-->",line)
    level = line[:1]
    # print(level)
    splitting = line.split()
    # print(splitting)
    indices = [1]
    tag = [splitting[index] for index in indices]
    # print(tag)
    arguments = line[6:]
    argue = arguments.split()
    for word in argue:
        if word in caution:
            valid = "Y"
            splitting[1], splitting[2] = splitting[2], splitting[1]
            tag = splitting[1]
            argue = splitting[2]
        else:
            for word in tag:
                if word in supported_tags:
                    valid = "Y"
                else:
                    valid = "N"
    print("<--", level, "|", tag, "|", valid, "|", argue,"\n")


sys.stdout.close()
