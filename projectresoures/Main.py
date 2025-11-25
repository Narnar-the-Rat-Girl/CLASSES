





# Ashley
class Doctor:
    def __init__(self, doc_id='', name ='', specialization='', working_time='',qualification='', room_num=''):
       self.doc_id = doc_id
       self.name = name
       self.specialization = specialization
       self.working_time = working_time
       self.qualification = qualification
       self.room_num = room_num
       
    def get_doc_id(self):
        return(self.doc_id)
    
    def get_name(self):
        return(self.name)
    
    def get_specialization(self):
        return(self.specialization)
    
    def get_working_time(self):
        return(self.working_time)
   
    def get_qualification(self):
        return(self.qualification)
    
    def get_room_num(self):
        return(self.room_num)
        


#ashley
class DoctorManager:
    pass

class Patient:
    pass

class PatientManager:
    pass

class Management:
    pass

#class 1 and 2 ashely
#class 3 
#class 4


if __name__ == "__main__":
    print("starting")
    test = Doctor(name="test")
    print(test.name)