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


class Patient:
    pass


class PatientManager:
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
