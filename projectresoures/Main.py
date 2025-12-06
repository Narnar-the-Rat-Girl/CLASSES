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


# ashley & Nikki
class DoctorManager:
    pass

#chloe
class Patient:
    def __innit__(self, name="", age="", pid="", disease="", gender=""):
        self.name = name
        self.age = age
        self.pid = pid
        self.disease = disease
        self.gender = gender

    def get_name(self):
        return self.name
    def set_name(self, new_name):
        self.name = new_name

    def get_age(self):
        return self.age
    def set_age(self, new_age):
        self.age = new_age

    def get_pid(self):
        return self.pid
    def set_pid(self, new_pid):
        self.pid = new_pid

    def get_disease(self):
        return self.disease
    def set_disease(self, new_disease):
        self.disease = new_disease

    def get_gender(self):
        return self.gender
    def set_gender(self, new_gender):
        self.gender = new_gender

    #
    def __str__():
        pass
    

#chloe
class PatientManager:
    pass

# Nikki
class Management:
    def display_menu(self):
        print("Welcome to Alberta Hospital (AH) Managment system\nSelect from the following options, or select 3 to stop:\n1 - 	Doctors\n2 - 	Patients\n3 -	Exit Program  ")
        menu1=int(input(">>> "))
        if menu1 == 1:
            self.doctors_menu()
        if menu1 == 2:
            pass
        if menu1 == 3:
            quit()
    def doctors_menu(self):
        print("Doctors Menu:\n1 - Display Doctors list\n2 - Search for doctor by ID\n3 - Search for doctor by name\n4 - Add doctor\n5 - Edit doctor info\n6 - Back to the Main Menu")
        menu2=int(input(">>> "))
        if menu2 == 1:
            pass
        if menu2 == 2:
            pass
        if menu2 == 3:
            pass
        if menu2 == 4:
            pass
        if menu2 == 5:
            pass
        if menu2 == 6:
            Management.display_menu
            
    pass


# class 1 and 2 ashely
# class 3 
# class 4


if __name__ == "__main__":
    print("starting")
    test = Doctor(name="test")
    print(test.name)
    Management.display_menu()

