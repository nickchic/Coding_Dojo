

class Patient(object):
    def __init__(self, id_num, name, allergies):
        self.id_num = id_num
        self.name = name
        self.allergies = allergies
        self.bed_number = None


class Hospital(object):
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.patients = []
        #array of beds False meaning empty
        self.beds = []
        for x in range(0,capacity):
            self.beds.append(False)
    def admit(self, new_patient):
        if len(self.patients) >= self.capacity:
            print "Hospital full."
        else:
            self.patients.append(new_patient)
            #gives the 1st available bed to new patient
            for index, bed in enumerate(self.beds):
                if bed == False:
                    new_patient.bed_number = index+1
                    self.beds[index] = True
                    break
            print "Patient added."
        return self
    def discharge(self, patient_to_discharge):
        # empties the bed the discharged patient was in
        self.beds[patient_to_discharge.bed_number-1] = False
        patient_to_discharge.bed_number = None
        for index, patient in enumerate(self.patients):
            if patient.id_num == patient_to_discharge.id_num:
                self.patients.pop(index)
        return self

nick = Patient(1, "Nick", "Sulfa Drugs")
lindsey = Patient(2, "Lindsey", "None")
mary = Patient(3, "Mary", "Peanuts")
ryan = Patient(4, "Ryan", "None")

penn_hospital = Hospital("Pennsylvania Hospital", 3)

penn_hospital.admit(nick).admit(lindsey).admit(mary).admit(ryan)

print "-- take one ---"
for patient in penn_hospital.patients:
    print patient.name, patient.bed_number

penn_hospital.discharge(nick).admit(ryan)

print "-- take two ---"
for patient in penn_hospital.patients:
    print patient.name, patient.bed_number
