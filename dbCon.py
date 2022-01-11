import sqlite3
con = sqlite3.connect("users.db" ,check_same_thread=False)
cur=con.cursor()
def addUser(id ,name,ref,lang ):
    cur.execute(f"INSERT INTO users VALUES ({id},'{name}',{ref},'{lang}')")
    con.commit()

def setLang(lang , id):
    #UPDATE "main"."users" SET "ref"=? WHERE "_rowid_"='1';
    cur.execute(f'UPDATE "main"."users" SET "lang"="{lang}" WHERE "id"="{id}"')
    con.commit()

def getLang (id):
    cur.execute(f'SELECT lang FROM users WHERE id={id} ')
    return cur.fetchone()[0]

def setRef(id , ref):
    cur.execute(f'UPDATE "main"."users" SET "ref"={ref} WHERE "id"="{id}"')
    con.commit()

def getRef(id):
    cur.execute(f'SELECT ref FROM users WHERE id={id} ')
    return cur.fetchone()[0]

def setStep(id , step):
    cur.execute(f'UPDATE "main"."users" SET "step"={step} WHERE "id"="{id}"')
    con.commit()

def getStep(id):
    cur.execute(f'SELECT step FROM users WHERE id={id} ')
    return cur.fetchone()[0]

def setWallet(id , wallet):
    cur.execute(f'UPDATE "main"."users" SET "wallet"={wallet} WHERE "id"="{id}"')
    con.commit()

def getWallet(id):
    cur.execute(f'SELECT wallet FROM users WHERE id={id} ')
    return cur.fetchone()[0]

def setPrim(id , prim):
    cur.execute(f'UPDATE "main"."users" SET "prim"={prim} WHERE "id"="{id}"')
    con.commit()

def getPrim(id):
    cur.execute(f'SELECT prim FROM users WHERE id={id} ')
    return cur.fetchone()[0]

def setReflaed(id ,  refraled):
    cur.execute(f'UPDATE "main"."users" SET "refraled"={refraled} WHERE "id"="{id}"')
    con.commit()

def getRefraled(id):
    cur.execute(f'SELECT refraled FROM users WHERE id={id} ')
    return cur.fetchone()[0]

	