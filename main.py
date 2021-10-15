class Bookmyshow:
    
    @staticmethod
    def menu():
        print("1.Show the seats")
        print("2.Buy a Ticket")
        print("3.Statistics")
        print("4.Show Booked Ticket user Info")
        print("5.Exit")

    @staticmethod
    def seats():
        for i in range(row):
            row_list = []
            for j in range(col):
                row_list.append("S")
            column_list.append(row_list)
        return column_list

    @staticmethod
    def show_the_seats():
        print("cinema:")
        print(" ", end="  ")
        for seat in range(1, col + 1):
            if seat <= 9:
                print(seat, " ", end="")
            else:
                print(f'{seat:}', "", end="")
        print()
        for k in range(row):
            if k <= 9:
                print(f'{k + 1:=2}', end=" ")
            else:
                print(k + 1, end=" ")
            for seat in range(col):
                print(column_list[k][seat], "", end=" ")
            print()

    @staticmethod
    def percentage():
        per = (Booked_seats / Total_seats) * 100
        return per


if __name__ == '__main__':
    row = int(input("Enter the number of rows:"))
    col = int(input("Enter the number of seats in each row:"))
    column_list = []
    Total_seats = row * col
    Ticket = Bookmyshow()
    Ticket.seats()
    Audience_list = [[None for j in range(col)] for i in range(row)]
    Booked_seats = 0
    Ticket_price = 0
    if Total_seats<=60:
        Total_income=Total_seats * 10
    else:
        Total_income=(Total_seats * 10)-(row*col)
    row_no = 0
    col_no = 0

    c = 0
    while c == 0:
        Ticket.menu()
        x = int(input())
        if x == 1:
            Ticket.show_the_seats()
            vacant_seats = Total_seats - Booked_seats
            if vacant_seats == Total_seats:
                print()
                print(" ", "ALL SEATS ARE VACANT")
                print()
            else:
                print(f"Row {row_no}'s seat no.{col_no} Booked")
            c = 0
        elif x == 2:
            seat_row = int(input("Enter the row number:"))
            if seat_row in range(1, row + 1):
                seat_col = int(input("Enter the column number:"))
                if seat_col in range(1, col + 1):
                    if column_list[seat_row - 1][seat_col - 1] == "S":
                        row_no = seat_row
                        col_no = seat_col
                        if row * col <= 60:
                            Ticket_price = 10
                        elif seat_row <= int(row / 2):
                            Ticket_price = 10
                        else:
                            Ticket_price = 8
                        print("Your Ticket Price -", "$", Ticket_price)
                        confirmation = input("Yes for Booking and No for exit(Yes/No):")
                        Person_dict = {}
                        if confirmation == "Yes":
                            Person_dict['Name'] = input("Enter Your Name:")
                            Person_dict['Gender'] = input("Gender(M/F/O):")
                            Person_dict['Age'] = int(input("Your Age:"))
                            Person_dict['Phone_no'] = int(input("Your Phone no:"))
                            Person_dict["Ticket_Price"] = Ticket_price
                            column_list[seat_row - 1][seat_col - 1] = "B"
                            Booked_seats += 1
                        else:
                            continue
                        Audience_list[seat_row - 1][seat_col - 1] = Person_dict
                        print("Your Ticket is successfully Booked")
                        print()
                    else:
                        print("Seat is already Booked By someone")
                        print()
                else:
                    print("Sorry,You Have entered invalid Seat Column")
                    print("  Seat col must be atmost:", col)
                    print("  Try again with valid data")
                    print()
            else:
                print("Sorry,You Have entered invalid Seat Row")
                print("   Seat Row must be atmost:", row)
                print("  Try again with valid data")
                print()
            c = 0

        elif x == 3:
            Ticket.show_the_seats()
            print()
            print("Number of Purchased Ticket:", Booked_seats)
            print("Percentage-", Ticket.percentage())
            print("Current Income-", "$", Ticket_price)
            print("Total Income-", "$", Total_income)
            print()
            c = 0

        elif x == 4:
            r = int(input("enter which row you want to check"))
            c = int(input("enter which seat number you want to check"))
            if r in range(1, row + 1) and c in range(1, col + 1):
                if column_list[r - 1][c - 1] != "B":
                    print("Seat is unocuupied U can book it")
                    print()
                    c = 0
                else:
                    person: None = Audience_list[r - 1][c - 1]
                    print("Name:", person["Name"])
                    print("Gender:", person["Gender"])
                    print("Age:", person["Age"])
                    print("Ticket Price:", person["Ticket_Price"])
                    print("Phone No:", person["Phone_no"])
                    print()
                    c = 0
            else:
                print("Invalid Entry please type valid row and col to check")
                print()
                c = 0
        elif x == 5:
            break
