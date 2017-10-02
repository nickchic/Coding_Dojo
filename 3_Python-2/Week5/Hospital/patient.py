class Patient(object):
    def __init__(self, id_num, name, allergies):
        self.id_num = id_num
        self.name = name
        self.allergies = allergies
        self.bed_number = None
    def __repr__(self):
        return "-- Name: {}, ID: {}, Allergies:{}, Bed: {} --".format(self.name, self.id_num, self.allergies, self.bed_number)
