def main(): 
    try:
        choice = int(input("Enter Choice : \n1.Record New patient details \n2.List all patient details \n3.Exit \nChoice : "))
    except:
        print("Invalid Input !! Try Agaain")
        main()    
    
    class Patient:
        def __init__(self, reg_no):
            self.reg_no = reg_no
            return
        
        def input_details(self):
            self.first_name = input("Enter First Name : ")
            self.last_name = input("Enter Last Name : ")
            self.dob = input("Enter Date of Birth : ")
            self.gender = input("Enter Gender : ")
            self.address = input("Enter Address : ")
            mob = True
            while mob:
                try:
                    self.mobile = int(input("Enter Mobile Number : "))
                    mob = False
                except:
                    print("Invalid Mobile Number (Only Numbers Accepted), Try Again !!")
            return
        
        def list_records(self):
            print("Registration Number : ", self.reg_no)
            print("First Name :",self.first_name)
            print("Last Name : ",self.last_name)
            print("Date of Birth : ",self.dob)
            print("Gender : ",self.gender)
            print("Address : ",self.address)
            print("Mobile : ",self.mobile)
            print("----------------------------------------")
            return
     
    def create_record():
        global patient_list
        reg_no = input("Enter Register Number :")
        patient_list[reg_no] = Patient(reg_no)
        patient_list[reg_no].input_details()
        return
    
    def list_records():
        global patient_list
        print("Listing records : ")
        for key in patient_list.keys():
            print(key)
            patient_list[key].list_records()
        return
        
        
    if choice == 1 :
        create_record()
        main()
    elif choice == 2 :
        list_records()
        main()
    elif choice == 3 :
        exit()
    else :
        print("Invalid Input !! Try Agaain")
        main()        
    return


patient_list = []
patient_list = dict(patient_list)

main()