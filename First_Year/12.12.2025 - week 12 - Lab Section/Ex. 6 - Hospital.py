#Ex. 6
'''
Да се състави програма за управление на данните на пациентите в една болница. 
За целта създайте клас Patient с полета: first_name (име), last_name (фамилия), age (възраст), room_num
(номер на стая), diagnosis (диагноза).

В класа са дефинирани и методи:

- patient information(self), който показва сцялата информация за пациента.
- change_diagnosis (self), който дава възможност потребителя (доктора) да въведе нова диагноза.

Всички пациенти се съхраняват в списък patient_list, като информацията за всеки пациент се въвежда от клавиатурата.

Да се дефинира функция search_by_lname(last_name, lname), който търси пациент по неговото 
фамилно име (името се въвежда от потребителя).
Функцията принтира в конзолата съобщение с текст, „Found" и номера на стаята (room_num),
ако има пациент с това име, в противен случай принтира „Not Found"

Да се дефинира функция search_by_room(patient_list, roomnumb, където потребителя въвежда 
номер на стая, а функцията връща като резултат и принтира в конзолата списък с всички пациенти, 
които са в тази стая.

Да се дефинира функция add_patient(patient_list, newpatient), която да добавя 
информация за нов пациент в списъка patient_list.

Да се дефинира функция remove_patient(patient_list, fname, lname, която изтрива информацията за 
пациент по зададени име и фамилия (въвеждат се от потребителя). Като резултат се 
принтира в конзолата съобщение с текст "Deleted!!!", ако има пациент със зададените имена, 
в противен случай се принтира "Patient not found!!!".
'''

# --- Class Definition ---
class Patient:
    def __init__(self, first_name, last_name, age, room_num, diagnosis):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.room_num = room_num
        self.diagnosis = diagnosis

    def patient_information(self):
        print(f"\n--- Patient Info ---")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Room: {self.room_num}")
        print(f"Diagnosis: {self.diagnosis}")
        print("--------------------")

    def change_diagnosis(self):
        print(f"Current Diagnosis: {self.diagnosis}")
        new_diag = input("Enter new diagnosis: ")
        self.diagnosis = new_diag
        print("Diagnosis updated successfully!")

# --- Helper Functions ---

def add_patient(patient_list, newpatient):
    patient_list.append(newpatient)
    print("Success: Patient added to the list.")

def search_by_lname(patient_list, lname):
    found = False
    print(f"\nResults for last name '{lname}':")
    for patient in patient_list:
        if patient.last_name == lname:
            print(f"Found! Name: {patient.first_name} {patient.last_name} | Room: {patient.room_num}")
            found = True
    
    if not found:
        print("Not Found")

def search_by_room(patient_list, roomnum):
    print(f"\n--- Patients in Room {roomnum} ---")
    patients_in_room = []
    for patient in patient_list:
        if patient.room_num == roomnum:
            patients_in_room.append(patient)
            print(f"- {patient.first_name} {patient.last_name} (Diagnosis: {patient.diagnosis})")

    if len(patients_in_room) == 0:
        print("No patients found in this room.")
    
    return patients_in_room

def remove_patient(patient_list, fname, lname):
    patient_to_remove = None
    
    for patient in patient_list:
        if patient.first_name == fname and patient.last_name == lname:
            patient_to_remove = patient
            break
    
    if patient_to_remove:
        patient_list.remove(patient_to_remove)
        print("Deleted!!!")
    else:
        print("Patient not found!!!")

# --- Main Program (Interactive Menu) ---

patient_list = []

while True:
    print("\n=== HOSPITAL MANAGEMENT MENU ===")
    print("1. Add New Patient")
    print("2. Search by Last Name")
    print("3. Search by Room Number")
    print("4. Change Diagnosis")
    print("5. Remove Patient")
    print("6. Show All Patients")
    print("0. Exit")
    
    choice = input("Select an option: ")

    # --- Add Patient ---
    if choice == "1":
        print("\n-- Enter Patient Details --")
        f_name = input("First Name: ")
        l_name = input("Last Name: ")
        
        # Validation for age
        try:
            age = int(input("Age: "))
            room = int(input("Room Number: "))
        except ValueError:
            print("Error: Age and Room must be numbers!")
            continue # Go back to menu start
            
        diagnosis = input("Diagnosis: ")
        
        # Create object and add it
        new_p = Patient(f_name, l_name, age, room, diagnosis)
        add_patient(patient_list, new_p)

    # --- Search by Last Name ---
    elif choice == "2":
        search_lname = input("Enter Last Name to search: ")
        search_by_lname(patient_list, search_lname)

    # --- Search by Room ---
    elif choice == "3":
        try:
            search_room = int(input("Enter Room Number: "))
            search_by_room(patient_list, search_room)
        except ValueError:
            print("Error: Room number must be an integer.")

    # --- Change Diagnosis ---
    elif choice == "4":
        # First we need to find the specific patient object
        target_fname = input("Enter First Name of patient: ")
        target_lname = input("Enter Last Name of patient: ")
        
        found_patient = False
        for patient in patient_list:
            if patient.first_name == target_fname and patient.last_name == target_lname:
                # We found the object, now we call the method ON that object
                patient.change_diagnosis() 
                found_patient = True
                break
        
        if not found_patient:
            print("Patient not found.")

    # --- Remove Patient ---
    elif choice == "5":
        del_fname = input("Enter First Name to delete: ")
        del_lname = input("Enter Last Name to delete: ")
        remove_patient(patient_list, del_fname, del_lname)

    # --- Show All ---
    elif choice == "6":
        if not patient_list:
            print("List is empty.")
        else:
            for p in patient_list:
                p.patient_information()

    # --- Exit ---
    elif choice == "0":
        print("Exiting program...")
        break

    else:
        print("Invalid choice, please try again.")