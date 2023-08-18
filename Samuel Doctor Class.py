import os


class Doctor:
    def __init__(self, pFileName):
        self.pFileName = pFileName

    def read_doctors_file(self):
        self.myDoctorsFile = open(self.pFileName, 'r')

        self.myDoctorsFile.close

    def display_doctors_list(self):

        print("ID".ljust(5), "Name".ljust(15), "Specialty".ljust(15), "Timing".ljust(10), "Qualification".ljust(20),
              "Room Number".ljust(10))
        for i in self.myDoctorsFile:
            NewValue = i.split("_")
            v_results = ""
            if NewValue[0] != "id":
                self.display_doctor_info(NewValue)

    def enter_dr_info(self, p_NewDoctorID, p_NewDoctorName, p_NewSpecialty, p_NewDoctorsTime, p_NewQualification,
                    p_NewRoomNo):
        self.DoctorID = p_NewDoctorID
        self.DoctorName = p_NewDoctorName
        self.Specialty = p_NewSpecialty
        self.DoctorsTime = p_NewDoctorsTime
        self.Qualification = p_NewQualification
        self.RoomNo = p_NewRoomNo

    def format_dr_info(self):
        self.NewValue = self.DoctorID + "_" + self.DoctorName + "_" + self.Specialty + "_" + self.DoctorsTime + "_" + self.Qualification + "_" + self.RoomNo

    def Write_list_of_doctors_to_file(self):

        self.myDoctorsFile = open(self.pFileName, 'a')
        self.myDoctorsFile.write("\n" + self.NewValue)

    def search_doctor_by_id(self, pDoctorID):

        new = []
        v_Found = False


        for line in self.myDoctorsFile:
            new = line.split("_")
            if new[0] == pDoctorID:
                print("ID".ljust(5), "Name".ljust(15), "Specialty".ljust(15), "Timing".ljust(10),
                      "Qualification".ljust(20),
                      "Room Number".ljust(10))
                v_Found = True
                self.display_doctor_info(new)
                break

        if v_Found == False:
            print("Can't find the doctor with the same ID on the system\n")

    def search_doctor_by_name(self, pDoctorName):
        new = []

        v_Found = False


        for line in self.myDoctorsFile:
            new = line.split("_")
            if new[1] == pDoctorName:
                print("ID".ljust(5), "Name".ljust(15), "Specialty".ljust(15), "Timing".ljust(10),
                      "Qualification".ljust(20),
                      "Room Number".ljust(10))
                self.display_doctor_info(new)
                v_Found = True
                break
        if v_Found == False:
            print("Can't find the doctor with the same name on the system\n")

    def edit_doctor_info(self, pDoctorID):
        self.DoctorID = pDoctorID
        self.DoctorName = str(input("Enter new Name:\n"))
        self.Specialty = str(input("Enter new Specialist in:\n "))
        self.DoctorsTime = str(input("Enter new Timing:\n "))
        self.Qualification = str(input("Enter new Qualification:\n "))
        self.RoomNo = str(input("Enter new Room number:\n "))

        new = []

        self.myDoctorsFileWrite = open('doctors_temp.txt', 'w')

        for line in self.myDoctorsFile:
            new = line.split("_")

            if new[0] == pDoctorID:
                self.format_dr_info()
                self.myDoctorsFileWrite.write(self.NewValue + "\n")
            else:
                # print (new)
                self.myDoctorsFileWrite.write(line)

        self.myDoctorsFileWrite.close()
        self.myDoctorsFile.close()

        os.remove('doctors.txt')
        os.rename('doctors_temp.txt', 'doctors.txt')

    def display_doctor_info(self, pInfo):
        vDisplay = [s.strip() for s in pInfo]
        print(pInfo[0].ljust(5), pInfo[1].ljust(15), pInfo[2].ljust(15), pInfo[3].ljust(10), pInfo[4].ljust(20),
              pInfo[5].ljust(10))