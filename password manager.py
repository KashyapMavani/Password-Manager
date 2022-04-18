from audioop import add


print("Welcome to the Password Manager")
your_name = input("Enter your name : ")
print("Hello",your_name,"Let's get started saving passwords.")


def view():
        with open('Password.txt','r') as f:
            for line in f.readlines():
                data = line.rstrip()
                user,passw = data.split("|")
                print("User :", user , "Password : ",passw)


def add():
        user_id = input("User ID : ")
        pwd = input("Password : ")

        with open('Password.txt','a') as f:
            f.write(user_id + "|" + pwd + "\n")


while True:

        mode = input(" To Add  New password type (Add) or To view existing passwords type (View) or press (q) to quite? : ").lower()

        if mode == "q":
            print("Thank you",your_name,"for visiting")
            break

        if mode == "add":
            add()
        elif mode == "view":
            view()
        else:
            print("Invalid Mode") 
            continue