import os
import subprocess
import pwd
from pathlib import Path
import shutil

def user_exist(u):
    try:
        pwd.getpwnam(u)
        return True
    except KeyError:
        return False


while True:
    print("=========================")
    print("   USER MANAGEMENT TOOL  ")
    print("=========================")
    print(" 1) Shtoni User")
    print(" 2) Fshini User")
    print(" 3) Listo User-at")
    print(" 4) Login i Fundit i User-it")
    print(" 5) Krijoni File")
    print(" 6) Krijoni Directory")
    print(" 7) Fshini File")
    print(" 8) Fshini Directory")
    print(" 9) Ndryshoni Emrin e File")
    print("10) Ndryshoni Permissions e File")
    print("11) Ndryshoni Kush Ka Akses Tek Directory")
    print(" q) Dilni")
    print("")

    opsioni = input("Zgjedhni nje opsion: ")

    if opsioni == "1" or opsioni == "2":
        if os.geteuid() != 0:
            print("Ju lutem filloni si root per te shtuar ose fshire usera \" Perdoreni: sudo\"")
            break


    if opsioni == "1":
        username = input("Shenoni emrin e userit qe doni te shtoni: ")
        if username == "":
            print("Username nuk mund te jete i zbrazet.")
        elif user_exist(username):
            print("Username ekziston")

        else:
            subprocess.run(["useradd", username])
            print("Shenoni passwordin")
            subprocess.run("passwd"), username
            print(f"User: {username} u shtua me sukses.")
            print("")

    elif opsioni == "2":
        username = input("Shenoni emrin e userit qe doni te fshini: ")
        if user_exist(username):
            subprocess.run(["userdel", username])
            print(f"Useri {username} u fshi me sukses\n")
        else:
            print("Username nuk ekziston!")

    elif opsioni == "3":
        print("------- System Users -------")
        subprocess.run(["cut", "-d:", "-f1", "/etc/passwd"])

    elif opsioni == "4":
        print("Login i fundit i userit")
        username = input("Shenoni username: ")
        print("")
        if user_exist(username):
            command = "last " + username + " | head -n 1"
            print(os.system(command))

    elif opsioni == "5":
        filen = input("Shenoni emrin e file: ")
        filepath = Path(filen)
        if filepath.is_file():
            print(f"File {filepath} ekziston")
        else:
            with open(filen, "w"):
                pass
            print(f"File {filepath} u krijua me sukses.")

    elif opsioni == "6":
        dirn = input("Shenoni emrin e directory: ")
        dirpath = Path(dirn)
        if dirpath.is_dir():
            print(f"Directory {dirpath} ekziston!")
        else:
            dirpath.mkdir()
            print(f"Directory {dirpath} u krijua me sukses.")

    elif opsioni == "7":
        filen = input("Shenoni emrin e file: ")
        if os.path.exists(filen):
            os.remove(filen)
            print(f"File {filen} u fshi me sukses.")
        else:
            print("File nuk ekziston.")

    elif opsioni == "8":
        dirn = input("Shenoni emrin e directory: ")
        dirpath = Path(dirn)
        if dirpath.is_dir():
            shutil.rmtree(dirpath)
            print(f"Directory {dirpath} u fshi me sukses.")
        else:
            print("Directory nuk ekziston!")

    elif opsioni == "9":
        filen = input("Shenoni emrin e file: ")
        if os.path.exists(filen):
            filenew = input("Shenoni emrin e ri te file: ")
            subprocess.run(["mv", filen, filenew])
            subprocess.run(["ls", "-la", filenew])
            print("Emri i file u nderrua me sukses")
        else:
            print("File nuk ekziston")

    elif opsioni == "10":
        print("Read=4\tWrite=2\tExecute=1")
        filen = input("Shenoni emrin e file: ")
        if os.path.exists(filen):
            akses = input("Shenoni numrat per permissions \"Shembull 744\": ")
            subprocess.run(["chmod", akses, filen])
            subprocess.run(["ls", "-la", filen])
            print("Permissions u ndrrua me sukses")
        else:
            print("File nuk ekziston")

    elif opsioni == "11":
        dirn = input("Shenoni emrin e directory: ")
        dirpath = Path(dirn)
        if dirpath.is_dir():
            akses = input("Shenoni user dhe grupin qe doni te jepni akses \"root:root\" ")
            subprocess.run("chown", akses, dirpath)
            print("Aksesi u ndryshua me sukses.")
            subprocess.run(["ls", "-ld", dirpath])


    elif opsioni == "q":
        print("Exiting ...")
        break

    else:
        print("Ju lutem te shenoni vetem njeren nga opsionet e larte permendura")

    print("")
    input("Shtypni Enter per te vzahduar ... ")
    subprocess.run("clear")