import mysql.connector

db = mysql.connector.connect(
    host='192.169.144.133',
    database='sr_team_3',
    user='mcctc3',
    password='mcctcrocks'
)

print("Connection ID:", db.connection_id)
mycursor = db.cursor()

def players():
    playerssql = "SELECT FIRST_NAME FROM playerInput"
    mycursor.execute(playerssql)
    #db.commit()
    myresult = mycursor.fetchall()

    for x in myresult:
     print(x)


start = input("Want to register? ")
if start == "y":
    FirstName = input("First Name: ")
    LastName = input("Last Name: ")
    PhoneNum = input("Phone Number: ")
    DiscordID = input("Discord ID: ")
    PlayerID = input("Player ID: ")
    EsportGame = input("ESport Game: ") 

    

    sql = "INSERT INTO playerInput (FIRST_NAME,LAST_NAME,PHONE_NUMBER,DISCORD_ID,PLAYER_ID,ESPORT_GAME) VALUES (%s,%s,%s,%s,%s,%s)"
    val = (FirstName, LastName,PhoneNum,DiscordID,PlayerID,EsportGame)

    mycursor.execute(sql, val)
else:
    players()

info = input("Give name of user you want info on: ")
mycursor.execute(f"SELECT * FROM playerInput WHERE FIRST_NAME = '{info}'")
myresult = mycursor.fetchall()
print("FIRST_NAME|LAST_NAME|PHONE_NUM|DISCORD|ESPORT|PLAYER")
for x in myresult:
     print(x)




db.commit()
#print(db)