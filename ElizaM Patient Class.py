class Patient:
    def __init__(self, pFileName):
        self.pFileName = pFileName

    def format_patient_Info_for_file(self):
        self.NewValue = self.NewPatientID + "_" + self.NewPatientName + "_" + self.NewPatientDisease + "_" + self.NewPatientGender + "_" + self.NewPatientAge

    def enter_patient_info(self):
        self.NewPatientID = input("Enter Patient id:\n")
        self.NewPatientName = input("Enter Patient Name: \n")
        self.NewPatientDisease = input("Enter Patient disease: \n")
        self.NewPatientGender = input("Enter Patient Gender: \n")
        self.NewPatientAge = input("Enter Patient age: \n")

        print(f"Patient whose ID is {self.NewPatientID} has been added.")

    def read_patients_file(self):
        self.myPatients = open(self.pFileName, 'r')

    def searchPatientById(self, pPatientID):
        new = []

        v_Found = False
        for line in self.myPatients:
            new = line.split("_")
            if new[0] == pPatientID:
                print("ID".ljust(5), "Name".ljust(10), "Disease".ljust(10), "Gender".ljust(10), "Age".ljust(15))
                self.displayPatientInfo(new)
                v_Found = True
                break
        if v_Found == False:
            print("Can't find the Patient with the same id on the system\n")

    def displayPatientInfo(self, pInfo):
        print(pInfo[0].ljust(5), pInfo[1].ljust(10), pInfo[2].ljust(10), pInfo[3].ljust(10), pInfo[4].ljust(10))

    def editPatientInfo(self, pPatientID):

        self.NewPatientID = pPatientID
        self.NewPatientName = input("Enter New Name: \n")
        self.NewPatientDisease = input("Enter New disease: \n")
        self.NewPatientGender = input("Enter New Gender:\n")
        self.NewPatientAge = input("Enter New age: \n")

        print(f"Patient whose ID is {self.NewPatientID} has been edited.")

        new = []

        self.myPatientsFileWrite = open('Patient_temp.txt', 'w')

        for line in self.myPatients:
            new = line.split("_")

            if new[0] == pPatientID:
                self.format_patient_Info_for_file()
                self.myPatientsFileWrite.write(self.NewValue + "\n")
            else:
                self.myPatientsFileWrite.write(line)

        self.myPatientsFileWrite.close()
        self.myPatients.close()

        os.remove('patients.txt')
        os.rename('Patient_temp.txt', 'patients.txt')

    def displayPatientsList(self):
        for line in self.myPatients:
            new = line.split("_")
            print(new[0].ljust(5), new[1].ljust(10), new[2].ljust(10), new[3].ljust(10), new[4].ljust(10))

    def writeListOfPatientsToFile(self):
        self.myPatients = open(self.pFileName, 'a')
        self.myPatients.write("\n" + self.NewValue)
        self.myPatients.close()

    def addPatientToFile(self):
        self.myPatients = open(self.pFileName, 'a')

        self.format_patient_Info_for_file()

        self.myPatients.write("\n" + self.NewValue)

        self.myPatients.close()
