# Health Management System
# 3 clients - Rahul,Sony,Harry
# Total 6 files
# write a function that when executed takes as input client name
# One more function to retrieve exercise or food for any client

Client_list = {1: "Rahul", 2: "Sony", 3: "Harry"}
Log_list = {1: "Exercise", 2: "Diet"}


def gettime():
    import datetime
    return datetime.datetime.now()
# Data = 'y'
# while Data !='n':
try:
    print("\nSelect Client name:")
    for key, value in Client_list.items():
        print("press", key, "for", value, "\n", end="")
    client_name = int(input())
    print("Selected", Client_list[client_name], "\n", end="")

    print("press 1 to log")
    print("press 2 to retrive")
    do = int(input())
    if do == 1:
        print("Select the Log name:")
        for key, value in Log_list.items():
            print("press", key, "for", value, "\n", end="")
        log_name = int(input())
        print("Selected", Client_list[client_name], "for logging", Log_list[log_name], "\n", end="")

        f = open(Client_list[client_name] + "_" + Log_list[log_name] + ".txt", "a")
        k = 'y'
        while (k != 'n'):
            print("Enter", Log_list[log_name], "\n", end="")
            mytext = input()
            f.write("[" + str(gettime()) + "]" + mytext + "\n")
            k = input("Add more?(y/n)")
            continue

        f.close()
    elif do == 2:
        for key, value in Log_list.items():
            print("press", key, "for", value, "\n", end="")
        log_name = int(input())
        print("Selected", Client_list[client_name], "for retriving", Log_list[log_name], "\n", end="")
        f = open(Client_list[client_name] + "_" + Log_list[log_name] + ".txt", "rt")
        content = f.readlines()
        for line in content:
            print(line, end="")
        # Data = input("Want to continue ?? (y/n)")
        f.close()
    else:
        print("Invalid input credentials")
except Exception as e:
    print("Invalid Input Credential")

