# Ashley
class Doctor:
    def __init__(
        self,
        doc_id="",
        name="",
        specialization="",
        working_time="",
        qualification="",
        room_num="",
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
    
    
    #TODO __str__()
    def __str__():
        pass


# ashley
class DoctorManager:
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
        return f"Name: Patient ID: {self.pid}, {self.pat_name}, Disease: {self.disease}, Gender:{self.gender}, Age: {self.age}"
    

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

        new_patient = Patient(pid, pat_name, disease, gender, age)
        return new_patient

    #
    def read_patients_file(self):
        with open("patients.txt", "r") as patient_data:
            for line in patient_data:
                pid, pat_name, disease, gender, age = line.split(",")
                patient = Patient(pid, pat_name, disease, gender, age)
                self.patient_list.append(patient)

    def search_patient_by_id():
        pass

    def display_patient_info():
        pass

    def edit_patient_info_by_id():
        pass

    def display_patients_list():
        pass

    def write_list_of_patients_to_file():
        pass

    def add_patient_to_file():
        pass


class Management:
    pass


# class 1 and 2 ashely
# class 3
# class 4


if __name__ == "__main__":
    print("starting")
    test = Doctor(name="test")
    print(test.name)
