def DisplayMenu():
    print("Select from the following options, or Select 3 to stop:")
    v_Options = int(input("1 - Doctors\n2 - Patients\n3 - Exit Program\n"))

    while v_Options >= 0:
        if v_Options == 1:

            v_1 = DoctorsMenu()

            if v_1 == 6:
                DisplayMenu()

        elif v_Options == 2:
            clsPatient = Patient("patients.txt")
            print("\nPatients Menu:")
            v_Patient = int(input(
                "1 - Display patient's list\n2 - Search for patient by ID\n3 - Add patient\n4 - Edit patient info\n5 - Back to the Main Menu\n"))
            if v_Patient == 1:
                print("Show Display Patient list")
                clsPatient.read_patients_file()
                clsPatient.displayPatientsList()

            elif v_Patient == 2:
                v_PatientID = str(input("Enter Patient id:\n "))

                clsPatient.read_patients_file()
                clsPatient.searchPatientById(v_PatientID)

            elif v_Patient == 3:

                clsPatient.enter_patient_info()
                clsPatient.addPatientToFile()


            elif v_Patient == 4:
                v_PatientID = str(
                    input("Please enter the id of the Patient that you want to edit their information:\n"))

                clsPatient.read_patients_file()
                clsPatient.editPatientInfo(v_PatientID)

            elif v_Patient == 5:
                DisplayMenu()

        elif v_Options == 3:
            print('Thanks for using the program. Bye!')
            exit()
            break


def DoctorsMenu():
    v_Filename = "doctors.txt"

    clsDoctor = Doctor(v_Filename)

    print("\nDoctors Menu")
    v_Doctors = int(input(
        "1 - Display Doctors list\n2 - Search for doctor by ID\n3 - Search for doctor by name\n4 - Add doctor\n5 - Edit doctor info\n6 - Back to the Main Menu\n"))
    if v_Doctors == 1:
        clsDoctor.read_doctors_file()
        clsDoctor.display_doctors_list()

    elif v_Doctors == 2:
        v_DoctorID = str(input("Enter the doctor id: \n"))
        clsDoctor.read_doctors_file()
        clsDoctor.search_doctor_by_id(v_DoctorID)

    elif v_Doctors == 3:
        v_DoctorName = str(input("Enter the doctor name:\n"))
        clsDoctor.read_doctors_file()
        clsDoctor.search_doctor_by_name(v_DoctorName)

    elif v_Doctors == 4:
        NewDoctorID = str(input("Enter the doctor's ID:\n"))
        NewDoctorName = str(input("Enter the doctor's Name:\n "))
        NewSpecialty = str(input("Enter the doctor's specialty:\n "))
        NewDoctorsTime = str(input("Enter the doctor's timing (e.g., 7am-10pm):\n "))
        NewQualification = str(input("Enter the doctor's qualification: \n"))
        NewRoomNo = str(input("Enter the doctor's room number:\n "))

        clsDoctor.enter_dr_info(NewDoctorID, NewDoctorName, NewSpecialty, NewDoctorsTime, NewQualification, NewRoomNo)
        clsDoctor.format_dr_info()
        clsDoctor.Write_list_of_doctors_to_file()

        print(f"Doctor whose ID is {NewDoctorID} has been added")

    elif v_Doctors == 5:
        v_DoctorID = str(input("Please enter the id of the doctor that you want to edit their information: "))

        clsDoctor.read_doctors_file()
        clsDoctor.edit_doctor_info(v_DoctorID)

        print(f"Doctor whose ID is {v_DoctorID} has been edited")

    return v_Doctors

print("Welcome to Alberta Hospital (AH) Management System")
DisplayMenu()