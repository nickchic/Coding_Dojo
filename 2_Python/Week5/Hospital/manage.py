from patient import Patient
from hospital import Hospital

nick = Patient(1, "Nick", "Sulfa Drugs")
lindsey = Patient(2, "Lindsey", "None")
mary = Patient(3, "Mary", "Peanuts")
ryan = Patient(4, "Ryan", "None")

penn_hospital = Hospital("Pennsylvania Hospital", 3)

penn_hospital.admit(nick).admit(lindsey).admit(mary).admit(ryan)

print "-- take one ---"
print penn_hospital

penn_hospital.discharge(nick).admit(ryan)

print "-- take two ---"
print penn_hospital
