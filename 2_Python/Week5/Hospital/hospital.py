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
    def __repr__(self):
        return "Name: {}, Capacity: {}, Patients: {}".format(self.name, self.capacity, self.patients)
