from modules import Employees, Managers, Session, Base, engine
import sys

local_session = Session()
""" # Create instances of Managers and Employees
employee1 = Employees(name="Samson")
employee2 = Employees(name="John")

manager1 = Managers(name="Sam")
manager2 = Managers(name="Muchiri")

# Add employees to managers and vice versa (many-to-many relationship)
manager1.employees.append(employee1)
manager2.employees.append(employee2)

# Commit to the database
session = Session()
session.add_all([employee1, employee2, manager1, manager2])
session.commit()

# Querying the relationships
print("Managers of Samson:")
for manager in employee1.managers:
    print(manager.name)

print("Employees of Sam:")
for employee in manager1.employees:
    print(employee.name) """

if __name__ == "__main__":
    # Creating tables
    Base.metadata.create_all(engine)


manager1 = Managers(name="Arumba")
manager2 = Managers(name="Luke")
manager3 = Managers(name="kate")

current_managers = local_session.query(Managers.name).all()
print(current_managers)
if current_managers == []:
    local_session.add_all([manager1, manager2, manager3])
    local_session.commit()
    print("Managers added successfully.")
else:
    print("Managers already exist in the database.")


# handling commands
if len(sys.argv) > 1:
    if sys.argv[1] == "employees":
        manager_name = input("What is your name? ")
        manager = local_session.query(Managers).filter(
            Managers.name == manager_name).first()
        print([name.name for name in manager.employees])


else:
    print("Welcome to employee manager")
    user_type = input(
        "Please tell us how you are? (manager, employee, new employee): ")
    if user_type == "manager":
        manager_list = [manager[0] for manager in current_managers]
        manager_name = input("What is your name?s: ")
        if manager_name in manager_list:
            print(
                f"Hello employee, run 'managers' to see all the managers you work under.")
        else:
            print(f"No manager found with the name {manager_name}")

    elif user_type == "employee":
        employee_name = input("What is your name?: ")
        employee = local_session.query(Employees).filter(
            Employees.name == employee_name).first()
        print(employee)
        if employee:
            print(
                f"Hello employee, run 'managers' to see all the managers you work under.")
        else:
            want_to_add = input(
                "Do you want to become an employee? (yes/no): ")
            if want_to_add.lower() == "yes":
                new_employee_name = input("What are your full names?: ")
                add = Employees(name=new_employee_name)
                local_session.add(add)
                local_session.commit()
                manager_list = [manager[0] for manager in current_managers]
                print(manager_list)

                pick_manager = input(f"Pick a manager from {manager_list}: ")
                while True:
                    if pick_manager in manager_list:

                        chosen_manager = local_session.query(Managers).filter(
                            Managers.name == pick_manager).first()

                        if chosen_manager:
                            last_record = local_session.query(
                                Employees).order_by(Employees.id.desc()).first()

                            if last_record:
                                last_record.managers.append(chosen_manager)
                                local_session.commit()
                                print(last_record.id)
                                print(
                                    f"Employee '{last_record.name}' has been assigned to manager '{chosen_manager.name}' successfully.")
                            break
                        else:
                            print(f"Manager '{pick_manager}' not found.")
                    else:
                        print(
                            "Invalid manager choice. Please select a manager from the list.")
                    pick_manager = input(
                        f"Pick a manager from {manager_list}: ")

        local_session.close()
    elif user_type == "new employee":
        eployee_name = input("What is your name? : ")
        manager_list = [manager[0] for manager in current_managers]
        print(manager_list)

        pick_manager = input(f"Pick a manager from {manager_list}: ")
        while True:
            if pick_manager in manager_list:

                chosen_manager = local_session.query(Managers).filter(
                    Managers.name == pick_manager).first()

                if chosen_manager:
                    last_record = local_session.query(
                        Employees).order_by(Employees.id.desc()).first()

                    if last_record:
                        last_record.managers.append(chosen_manager)
                        local_session.commit()
                        print(last_record.id)
                        print(
                            f"Employee '{last_record.name}' has been assigned to manager '{chosen_manager.name}' successfully.")
                    break
                else:
                    print(f"Manager '{pick_manager}' not found.")
            else:
                print(
                    "Invalid manager choice. Please select a manager from the list.")
            pick_manager = input(
                f"Pick a manager from {manager_list}: ")
