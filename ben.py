def marriage_before_death(conn):
    #dont fear the reaper....

    cur = conn.cursor()
    cur.execute("SELECT * FROM families")

    rows = cur.fetchall()

    for row in rows:
        pass

def ben_user_stories(conn):
 marriage_before_death(conn)
