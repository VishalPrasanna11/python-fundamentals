import sqlite3 as lite

class DatabaseManage(object):
    
    def __init__(self):
        global con
        try:
            con = lite.connect('courses.db')
            with con:
                cur = con.cursor()
                cur.execute("""
                CREATE TABLE IF NOT EXISTS course(
                    Id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    name TEXT, 
                    description TEXT, 
                    price TEXT, 
                    is_private BOOLEAN NOT NULL DEFAULT 1
                )""")
        except Exception:
            print("Unable to create a DB!")
            
    # Insert data into the database
    def insert_data(self, data):
        try:
            with con:
                cur = con.cursor()
                cur.execute("INSERT INTO course(name, description, price, is_private) VALUES(?,?,?,?)", data)
                return True
        except Exception:
            return False
    
    # Fetch data from the database
    def fetch_data(self):
        try:
            with con:
                cur = con.cursor()
                cur.execute("SELECT * FROM course")
                return cur.fetchall()
        except Exception:
            return False
        
    # Delete data from the database
    def delete_data(self, id):
        try:
            with con:
                cur = con.cursor()
                sql = "DELETE FROM course WHERE Id = ?"
                cur.execute(sql, [id])
                return True
        except Exception:
            return False
        
    # Update data in the database
    def update_data(self, id, updated_fields):
        """
        Update only the fields provided in updated_fields. Leave other fields unchanged.
        :param id: Course ID to update.
        :param updated_fields: Dictionary of fields to update.
        """
        try:
            with con:
                cur = con.cursor()

                # Build the dynamic SQL query
                fields_to_update = []
                values = []
                for field, value in updated_fields.items():
                    fields_to_update.append(f"{field} = ?")
                    values.append(value)

                # Ensure there's something to update
                if not fields_to_update:
                    print("No fields to update!")
                    return False

                values.append(id)  # Add ID to the values list for the WHERE clause
                sql = f"UPDATE course SET {', '.join(fields_to_update)} WHERE Id = ?"
                cur.execute(sql, values)
                return True
            
        except Exception as e:
            print("Error updating data:", e)
            return False

# Interface to the database

def main():
    print("*" * 40)
    print("\n:: COURSE MANAGEMENT ::\n")
    print("*" * 40)
    print("\n")
    
    db = DatabaseManage()
    
    print("#" * 40)
    print("\n:: User Manual ::\n")
    print("#" * 40)
    
    while True:
        print('\nPress 1. Insert a new course\n')
        print('Press 2. Show all courses\n')
        print('Press 3. Update a course (NEED ID OF COURSE)\n')
        print('Press 4. Delete a course (NEED ID OF COURSE)\n')
        print('Press 5. Exit\n')
        
        print("#" * 40)
        
        choice = input("\nEnter a choice: ")
        
        if choice == "1":
            name = input("\nEnter course name: ")
            description = input("\nEnter course description: ")
            price = input("\nEnter course price: ")
            private = input("\nIs this course private (0/1): ")
            
            if db.insert_data([name, description, price, private]):
                print("Course was inserted successfully!")
            else:
                print("OOPS! Something went wrong!")
        
        elif choice == "2":
            print("\n:: Course List ::")
            
            for index, item in enumerate(db.fetch_data()):
                print("\nSl no: " + str(index + 1))
                print("Course ID: " + str(item[0]))
                print("Course Name: " + str(item[1]))
                print("Course Description: " + str(item[2]))
                print("Course Price: " + str(item[3]))
                private = 'Yes' if item[4] else 'No'
                print("Is Private: " + private)
                print("\n")
        
        elif choice == "3":
            record_id = input("\nEnter the course ID to update: ")
            
            print("\nLeave fields blank to keep the current values.")
            name = input("\nEnter updated course name: ")
            description = input("\nEnter updated course description: ")
            price = input("\nEnter updated course price: ")
            private = input("\nIs this course private (0/1) (leave blank to keep current): ")
            
            # Build the dictionary of fields to update
            fields_to_update = {}
            if name.strip():
                fields_to_update["name"] = name
            if description.strip():
                fields_to_update["description"] = description
            if price.strip():
                fields_to_update["price"] = price
            if private.strip():
                fields_to_update["is_private"] = int(private)

            # Call update_data with the fields to update
            if db.update_data(record_id, fields_to_update):
                print("Course was updated successfully!")
            else:
                print("OOPS! Something went wrong!")
                        
        elif choice == "4":
            record_id = input("\nEnter the course ID to delete: ")
                
            if db.delete_data(record_id):
                print("Course was deleted successfully!")
            else:
                print("OOPS! Something went wrong!")
                
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("\nBAD CHOICE!")
            
if __name__ == '__main__':
    main()
