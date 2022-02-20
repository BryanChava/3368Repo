#homework1-3368-19296-bryan chavarria-1657040
import mysql.connector
from mysql.connector import Error
#shown in class, connectiion to my sqlworkbench
def create_con(host_name, user_name, user_password, db_name):
    connection = None
    try: 
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to 3368 DB successful")
    except Error as e:
        print(f'the error {e} occured')
    return connection
#if connection successful will choose for table within database named'garage'
conn = create_con('database3368.chuw2jvtxam9.us-east-2.rds.amazonaws.com', 'admin', 'Admin2177', 'Database3368')
cursor = conn.cursor(dictionary = True)
csr = cursor
sql = "select * from garage"
csr.execute(sql)
rows = cursor.fetchall()


#will display menu for user to input data into terminal, 
#line 35 statements will come into effect IF choice is invalid  
def select():
    print("1. Go to Main Menu In Garage")
    print("2. Quit") #function that reveals the main menu for the use to start interacting with program in terminal
    select1 = int(input("Enter your choice: "))
    if select1 == 1:
        mainmenu()
    elif select1 == 2:
        print("Program quit successfully")
        exit()
    else:
        print("Invalid choice, try again")
        select()

#Note: Data from an .csv file was instered into my sql workbench for easier understanding
#Inserting / Adding cars to the table                                        
#source https://www.w3schools.com/sql/func_mysql_insert.asp / 
#https://www.sqlshack.com/learn-sql-insert-into-table/
def insert():
    print("Insert new car")
    sql = "select max(id) from garage"
    csr.execute(sql)
    readcsr = csr.fetchone()
    if readcsr[0] == None:
        id = 1
    else:
        id = readcsr[0] + 1
#once sucessful, program will add variable as requested into the database
    car = input("Enter type of car: ")                
    year = int(input("Enter year: "))
#error code may present itself if data type is incorrect such as year being numeric not CHAR
    color = int(input("Enter color: "))
    sql = "insert into garage values(%s,%s,%s,%s)"
    val = (id, car, year, color)
    csr.execute(sql, val)
    conn.commit()
    print("Car added successfully")
    select()

#deleting/removing car(s) from table                                 
#source http://www.edu4java.com/en/sql/sql8.html
#https://www.mysqltutorial.org/mysql-drop-table
#once user selects an ID from table, use iputs id, program then removes data from ID and is prompted with
#choice to go to main menu or exit program
def delete():
    print("Enter the ID for the car you want to delete: ")
    id = int(input("Enter Here : "))
    csr.execute("delete from garage where id=%s", (id,))
    conn.commit()
    print("Car deleted successfully")
    select()


#updating car details (model,color,year) all make is the same 
#user will be prompted to enter id for specific car / line row of data (86) the user will follow steps inorder 
# from how the collum is made to make any adjustments to database, if left blank data will not be affected   
#line 92 sql data changed is PUSHED                                   
#source https://datatofish.com/update-records-sql-server/
#https://pynative.com/python-mysql-update-data/
def update():
    id = int(input("Enter the ID for the car you want to update: "))
    print(f"Update details for ID No. {id}")
    model = input("Enter new car model: ")
    color = (input("Enter new color: "))
    year = (input("Enter new year: "))
    sql = "update garage set model=%s,color=%s, year=%s where id=%s"
    val = (id, model, color, year)
    csr.execute(sql, val)    
    conn.commit()
    print("Car details updated successfully")
    print()
    select()


#displays all og the cars in garage sorted by year in acending order 
#sort function was used to sort cars by year 
#source https://www.pythontutorial.net/python-basics/python-sort-list/#:~:text=Summary-,Use%20the%20Python%20List%20sort()%20method%20to%20sort%20a,reverse%20the%20default%20sort%20order.

def sort():
    print("displaying cars assorted by year")
    sql = "select car from garage order by yearsort"
    csr.execute(sql)
    disp = csr.fetchall()
    for i in disp:
        print(i[0])
    print()
    select()


#displays all cars of a certain color when 
#called 
#source https://www.pythontutorial.net/python-basics/python-sort-list/#:~:text=Summary-,Use%20the%20Python%20List%20sort()%20method%20to%20sort%20a,reverse%20the%20default%20sort%20order.
def sort():
    print("Displaying cars by a certain color")
    sql = "select car from garage by colorsort"
    csr.execute(sql)
    disp = csr.fetchall()
    for i in disp:
        print(i[0])
    print()
    select()


#user will navigate the main menu
#charcters within the print function will be displayed at the beginning of the code to naviagte the program 
#source https://stackoverflow.com/questions/17352630/creating-a-terminal-program-with-python
def mainmenu():
    print("Please select 1 of the following options")
    print("""+-+
1. Add car
2. Remove car
3. Update car details
4. Display cars sorted by year
5. Display cars of a certain color
6. Quit
+-+""")
    print()
    print("""Type the number below to perform the corresponding action.""")
    ch = int(input("Enter your choice : "))
    print()
    #functions used in the main menu 
    if ch == 1:
        insert()
    elif ch == 2:
        delete()
    elif ch == 3:
        update()
    elif ch == 4:
        sort()
    elif ch == 5:
        sort()
    elif ch == 6:
        print("Program quit successfully")
        exit()
    else:
        print("invalid, Retry")
    print()

print("Welcome to the garage")
mainmenu()
#end of code
