class multiplefunction():
    def oddeven():
        num=int(input("enter the Number:"))
        if (num%2==1):
            print(num," given number is even")
        else:
            print(num, "given number is odd")
        return

    def marriage_eligibility():
        gender = input("Enter your gender ('male' or 'female'): ")
        age = int(input("Enter your age: "))
        if gender.lower() == "male":
            if (age >=21):
                return "your ARe eligible to Marriage:"
            else:
                return "your are not eligible to magrrige"
        elif gender.lower() == "female":
            if(age>=18):
                return "your are eligible to marriage"
            else:
                return "your are not eligible to marriage"

    def subfields_in_ai():
        subfields = [
                "Machine Learning",
                "Neural Networks",
                "Vision",
                "Robotics",
                "Speech Processing",
                "Natural Language Processing"
                ]
        print("Sub-fields in AI are:")
        for subfield in subfields:
            print(subfield)

    def triangle_cal():
        height=float(input("Height:"))
        breadth=float(input("Breadth:"))
        print("Area formula: (Height*Breadth)/2")
        area=(height*breadth)/2
        print("area of triangle:",area)
    
        height1=float(input("Height1:"))
        height2=float(input("Height2:"))
        breadth=float(input("Breadth:"))
        print("Perimeter formula: Height1+Height2+Breadth")
        traingle = height1+height2+breadth
        print("Perimeter of Triangle:",traingle)

    def findpercent():
        subject1=int(input("Subject1 mark:"))
        subject2=int(input("Subject2 mark:"))
        subject3=int(input("Subject3 mark:"))
        subject4=int(input("Subject4 mark:"))
        subject5=int(input("Subject5 mark:"))
        total = subject1+subject2+subject3+subject4+subject5
        percent= (total/5)
        print(f"Total Marks: {total}")
        print(f"Percentage: {percent:.15f}%")