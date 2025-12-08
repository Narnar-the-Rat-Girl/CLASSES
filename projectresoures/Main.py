# Ashley
from turtle import pen


class Doctor:
    def __init__(
        self,
        doc_id="",
        name="",
        specialization="",
        working_time="",
        qualification="",
        room_num= "",
    ):
        self.doc_id = doc_id
        self.name = name
        self.specialization = specialization
        self.working_time = working_time
        self.qualification = qualification
        self.room_num = room_num

    def get_doc_id(self):
        return self.doc_id

    def get_name(self):
        return self.name

    def get_specialization(self):
        return self.specialization

    def get_working_time(self):
        return self.working_time

    def get_qualification(self):
        return self.qualification

    def get_room_num(self):
        return self.room_num

    def set_doc_id(self, new_id):
        self.doc_id = new_id

    def set_name(self, new_name):
        self.name= new_name

    def set_specialization(self, new_specialization):
        self.doc_specialization = new_specialization

    def set_working_time(self, new_working_time):
        self.working_time = new_working_time

    def set_qualification(self, new_qualification):
        self.doc_qualification = new_qualification

    def set_room_num(self, new_room_num):
        self.room_num = new_room_num
    


# ashley & Nikki
class DoctorManager:
    def __init__(self):
        self.doctor_list = []

        self.read_doctors_file()
        
    #method to format patient object info to match the infor from the doctors.txt file
    def format_doctor_info_for_file(self, doctor):
        #underscores to separate properties instead of commas
        return f"{doctor.doc_id}_{doctor.name}_{doctor.specialization}_{doctor.working_time}_{doctor.qualification}_{doctor.room_num}"
        
    #method for user to add patient info
    def enter_doctor_info(self):
        print("Enter Doctor Information")

        #gets the patient info from user
        doc_id = input("Enter Doctor ID: ")
        doctor_name = input("Enter Doctor Name: ")
        working_time = input("Enter Doctor Timing Disease: ")
        specialization = input("Enter Doctor Specialization ")
        room_num = input("Enter Doctor Room Number: ")
        qualification = input("Enter Doctor qualification: ")

        new_doctor = Doctor(doc_id, doctor_name, specialization, working_time, qualification, room_num)
        return new_doctor

    #
    def read_doctors_file(self):
        with open("doctors.txt", "r") as doctor_data:
            for line in doctor_data:
                try:
                    doc_id, doctor_name, specialization, working_time, qualification, room_num = line.split("_")
                    doctor = Doctor(doc_id, doctor_name, specialization, working_time, qualification, room_num)
                    self.doctor_list.append(doctor)
                except ValueError as e:
                    print(f"Skipping malformed line: {line}- Error: {e}")
                    


    def search_doctor_by_id(self):

        search_doc_id = input("Enter the Doctor ID: ")

        for doctor in self.doctor_list:

            if doctor.get_doc_id() == search_doc_id:
                print(doctor)
                break


        else:
            print("Can't find the Doctor with the same ID in the system")


    def search_doctor_by_name(self):
        search_doc_name = input("Enter the Doctor ID: ")

        for doctor in self.doctor_list:

            if doctor.get_name() == search_doc_name:
                print(doctor)
                break


        else:
            print("Can't find the Doctor with the same name in the system")
            pass

    def display_doctor_info(self):
        pass

    def edit_doctor_info(self):
        pass
    
    
    def display_doctors_list(self):
        pass
    

    def write_list_of_doctors_to_file(self):
        pass

    def add_dr_to_file(self):
        pass










#chloe
class Patient:
    #initializes the properties for each patient object
    def __init__(self, pid="", pat_name="", disease="", gender="", age=""):
        self.pid = pid
        self.pat_name = pat_name
        self.disease = disease
        self.gender = gender
        self.age = age

    #patient ID
    def get_pid(self):
        return self.pid
    def set_pid(self, new_pid):
        self.pid = new_pid
        
    #patient name
    def get_pat_name(self):
        return self.pat_name
    def set_name(self, new_pat_name):
        self.pat_name = new_pat_name
        
    #patient's disease
    def get_disease(self):
        return self.disease
    def set_disease(self, new_disease):
        self.disease = new_disease

    #patient's gender
    def get_gender(self):
        return self.gender
    def set_gender(self, new_gender):
        self.gender = new_gender

    #patient age
    def get_age(self):
        return self.age
    def set_age(self, new_age):
        self.age = new_age

    #returns the patient objects as a formatted string
    def __str__(self):
        return f"Name: {self.pat_name}, Patient ID: {self.pid}, Disease: {self.disease}, Gender:{self.gender}, Age: {self.age}"
    

#chloe
class PatientManager:

    #constructor method to make empty patient list
    #calls read_patients_file() to get patient data from patients.txt file
    def __init__(self):
        self.patient_list = []
        
        self.read_patients_file()
        
    #method to format patient object info to match the infor from the patients.txt file
    def format_patient_info_for_file(self, patient):
        #underscores to separate properties instead of commas
        return f"{patient.pid}_{patient.pat_name}_{patient.disease}_{patient.gender}_{patient.age}"
        
    #method for user to add patient info
    def enter_patient_info(self):
        print("Enter Patient Information")

        #gets the patient info from user
        pid = input("Enter Patient ID: ")
        pat_name = input("Enter Patient Name: ")
        disease = input("Enter Patient Disease: ")
        gender = input("Enter Patient Gender: ")
        age = input("Enter Patient Age: ")

        new_patient = Patient(pid , pat_name , disease , gender , age)
        return new_patient

    #
    def read_patients_file(self):
        with open("patients.txt", "r") as patient_data:
            for line in patient_data:
                try:
                    pid, pat_name, disease, gender, age = line.split('_')
                    patient = Patient(pid, pat_name, disease, gender, age)
                    self.patient_list.append(patient)
                except ValueError as e:
                    print(f"Skipping malformed line: {line}- Error: {e}")

    #method that seaches for a patient using a patient id entered by the user
    def search_patient_by_id(self):
        #asks the user to enter the patient id
        search_pid = input("Enter the Patient ID: ")

        #loop to look through the list to check if there is a patient with a matching id
        for patient in self.patient_list:
            #uses get() to search through patient list
            #if there is a matching pid, displays patient info
            if patient.get_pid() == search_pid:
                #calls the display_patient_info method to display the patient info
                self.display_patient_info(patient)
                break

        #if the patient id is not found, displays this instead
        else:
            print("Can't find the Patient with the same ID in the system")

    #method that displays patient information
    def display_patient_info(self, patient):
        print(patient)

    #method that allows the user to edit the information of the patient whose id is specified
    def edit_patient_info_by_id(self):
        #asks user to input the patient id
        find_patient = input("Please enter the ID of the Patient you want to edit their information: ")

        #loop to look through the list to check if there is a patient with a matching id
        for patient in self.patient_list:
            #uses get() to search through patient list
            #if there is a matching pid, allows user to change the patient info
            if patient.get_pid() == find_patient:
                #gets the new patient information from the user
                new_pat_name = input("Enter new Name: ")
                new_disease = input("Enter new Disease: ")
                new_gender = input("Enter new Gender: ")
                new_age = input("Enter new Age: ")

                #updates the patient object with the new values
                patient.set_pat_name(new_pat_name)
                patient.set_disease(new_disease)
                patient.set_gender(new_gender)
                patient.set_age(new_age)

                #writes the updated patient information in the patients.txt file
                with open("patients.txt", "w") as data:
                    for patient_data in self.patient_list:
                        data.write(self.format_patient_info_for_file(patient_data))
                return
        
        #displays this if the patient id does not exist in the system
        print("Can't find the Patient with the same ID in the system")

    def display_patients_list(self):
        pass

    def write_list_of_patients_to_file(self):
        pass

    def add_patient_to_file(self):
        pass

pm = PatientManager()
dm = DoctorManager()

# Nikki
class Management:
    def __innit__(self):
        pass
    def display_menu(self):
        print("Welcome to Alberta Hospital (AH) Managment system\nSelect from the following options, or select 3 to stop:\n1 - 	Doctors\n2 - 	Patients\n3 -	Exit Program  ")
        menu1=int(input(">>> "))
        if menu1 == 1:
            self.doctors_menu()
        if menu1 == 2:
            self.patients_menu()
        if menu1 == 3:
            print("Thanks for using the program. Bye!")
            quit()
    def doctors_menu(self):
        print("Doctors Menu:\n1 - Display Doctors list\n2 - Search for doctor by ID\n3 - Search for doctor by name\n4 - Add doctor\n5 - Edit doctor info\n6 - Back to the Main Menu")
        menu2=int(input(">>> "))
        if menu2 == 1:
            print("Id   Name                   Speciality      Timing          Qualification   Room Number")
            dm.read_doctors_file
            self.doctors_menu
        if menu2 == 2:
            dm.search_doctor_by_id
        if menu2 == 3:
            dm.search_doctor_by_name
        if menu2 == 4:
            dm.enter_doctor_info
        if menu2 == 5:
            dm.edit_doctor_info
        if menu2 == 6:
            self.display_menu()
    def patients_menu(self):
        print("Patients Menu:\n1 - Display patients list\n2 - Search for patient by ID\n3 - Add patient\n4 - Edit patient info\n5 - Back to the Main Menu")
        menu3=int(input(">>> "))
        if menu3 == 1:
            print("ID   Name		    Disease	    Gender	    Age")
            pm.read_patients_file
            self.patients_menu
        if menu3 == 2:
            print("ID   Name		    Disease	    Gender	    Age")
            pm.search_patient_by_id
        if menu3 == 3:
            pm.enter_patient_info
        if menu3 == 4:
            pm.edit_patient_info_by_id
        if menu3 == 5:
            self.display_menu()
    pass

menu = Management()



if __name__ == "__main__":
    print("starting")
    test = Doctor(name="test")
    print(test.name)
    menu.display_menu()

