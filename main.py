import mysql.connector
import random


class ticketSystem:
    def __init__(self):
        print("Ticket system has started")

    def createTicket(self):
        id = random.randint(0,999999999)
        ticketDesc = input("Why did you open a ticket?: ")
        ticketDesc = ticketDesc.replace("'","''")
        self.dbcursor.execute(f"INSERT INTO `tickets` (`ticketID`, `open`, `ticketDesc`) VALUES ('{id}', '1', '{ticketDesc}');")
        print(f"Created ticket Your ticket ID is {id} and the description of your ticket is {ticketDesc}")
        self.replyTicket() # FOR DEBUGGING


    def replyTicket(self,id=0):
        # This line of code can be modified to your liking to fetch an ID.  Otherwise it'll ask for an input
        id = int(input("What ID to fetch?"))
        self.dbcursor.execute(f"SELECT * FROM tickets WHERE ticketID = '{id}'")
        for (ticketDesc) in self.dbcursor:
            if ticketDesc[1] == 0:
                print (f"Fetched your ticket reply!  The fetched ticket description is {ticketDesc[2]} and the ticket ID is {ticketDesc[0]}")
            else: print (f"Fetched your ticket!  The fetched ticket description is {ticketDesc[2]} and the ticket ID is {ticketDesc[0]}")
        reply = input("Would you like to reply to this ticket? (Y/y)").lower()
        if reply == "Y".lower():
            ticketDesc = input("What is your reply to this ticket?: ")
            self.dbcursor.execute(f"INSERT INTO `tickets` (`ticketID`, `open`, `ticketDesc`) VALUES ('{id}', '0', '{ticketDesc}');")

# This function will fetch the SQL database
    def handleTickets(self):
        try: self.dbcursor.execute("CREATE TABLE tickets(ticketID INT, open BOOLEAN, ticketDesc TEXT)")
        except Exception as e: print(f"Table most likely already created ignore following error.  \n**IGNORE**: {e}")
        self.dbcursor.execute("SHOW TABLES")
        for x in self.dbcursor:
            print(x)
        #This line should be modified; for debugging purposes
        addTicket = input("Want to create a ticket: (Y/y)?").lower()
        if addTicket == "Y".lower():
            self.createTicket()

    def beginFunction(self):
        sqlConnection = mysql.connector.connect(user='database', password='password',
                              host='revivehost.com',
                              database='username',
                              autocommit=True)
        self.dbcursor = sqlConnection.cursor()
        self.handleTickets() # This line should be removed and changed to match your needs.


ts = ticketSystem()
ts.beginFunction()



###
# Developed by knotam
###
