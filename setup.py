import os
import sys

os.system('clear')
print()
print("""

████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█░░░░░░░░░░░░███░░░░░░░░░░░░░░█░░░░░░██████████░░░░░░█░░░░░░██░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░███████
█░░▄▀▄▀▄▀▄▀░░░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░░░░░░░░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░███████
█░░▄▀░░░░▄▀▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░░░░░▄▀░░░░░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░░░███████
█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█████░░▄▀░░█████░░▄▀░░██░░▄▀░░█░░▄▀░░███████████████
█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█████░░▄▀░░█████░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░███████
█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█████░░▄▀░░█████░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░███████
█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█████░░▄▀░░█████░░▄▀░░██░░▄▀░░█░░░░░░░░░░▄▀░░███████
█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░█████░░▄▀░░█████░░▄▀░░██░░▄▀░░█████████░░▄▀░░███████
█░░▄▀░░░░▄▀▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░░░░░▄▀░░█████░░▄▀░░█████░░▄▀░░░░░░▄▀░░█░░░░░░░░░░▄▀░░███████
█░░▄▀▄▀▄▀▄▀░░░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░░░░░░░░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█████░░▄▀░░█████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░███████
█░░░░░░░░░░░░███░░░░░░░░░░░░░░█░░░░░░██████████░░░░░░█░░░░░░░░░░░░░░█████░░░░░░█████░░░░░░░░░░░░░░█░░░░░░░░░░░░░░███████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████
█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██░░░░░░█░░░░░░░░░░░░░░█
█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█░░░░░░▄▀░░░░░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░█
█░░▄▀░░█████████░░▄▀░░█████████████░░▄▀░░█████░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█
█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█████░░▄▀░░█████░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░█
█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█████░░▄▀░░█████░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
█░░░░░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█████░░▄▀░░█████░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█
█████████░░▄▀░░█░░▄▀░░█████████████░░▄▀░░█████░░▄▀░░██░░▄▀░░█░░▄▀░░█████████
█░░░░░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█████░░▄▀░░█████░░▄▀░░░░░░▄▀░░█░░▄▀░░█████████
█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█████░░▄▀░░█████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░█████████
█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█████░░░░░░█████░░░░░░░░░░░░░░█░░░░░░█████████
████████████████████████████████████████████████████████████████████████████ DOSST 1.1
""")
print()
print("Welcome to DonutOS 1.1 BeggorraBear")
print('DOSST')
print()
print("To install DonutOS to your PC type `install`, to view basic information type `about, to quit DOSST type `exit`.")
print()
installer = ""
while installer != "exit":
   installer = input("DOSST #1.1 :> ").lower()
   if installer == "install":
      print()
      print("Starting the Installer....")
      print("Preparing the Installer...")
      print()
      print("Getting Critical Updates... Checking Network...")
      print("Connecting to the server...")
      for ch in "DonutOS Setup DOSST 1.1 https://sites.google.com/view/donutlinux/   " :
         print(ch)
      os.system('clear')
      print("Detecting Disks...")
      print("#"*80)
      os.system('clear')
      print("LICENSE AGREEMENT")
      os.system('less license')
      print()
      os.system('clear')
      print("LICENSE AGREEMENT")
      print()
      print("Do you agree the license terms?")
      confirm = input("yes/no :> ")
      if confirm == "yes":
         print("Preparing for Installation..")
         os.system('clear')
         print("SELECT DRIVE TO INSTALL")
         print()
         os.system('sudo fdisk -l')
         print()
         idr = input("Enter installation source (e.g. /dev/sdb) : ")
         dd = input("Enter destination drive (e.g. /dev/sda or /dev/nvme) : ")
         print()
         print("Your installation medium : ",idr," and you destination drive : ",dd)
         print()
         sttmt = str("if="+idr)
         sttmt_2 = str(" bs=64k of="+dd)
         statement = "sudo dd "+sttmt+sttmt_2
         proceed = input("Are you sure you want to install /!\ Your entire drive will be formatted (yes/no): ")
         if proceed == "yes":
            os.system('clear')
            print("INSTALLATION")
            print()
            print("\t FORMATTING")
            formatv = str("sudo wipefs -a "+dd+" --force")
            os.system(formatv)
            print("\t CREATING EXT4 FILESYSTEM")
            format_ext4 = str("sudo mkfs -t ext4 "+dd)
            print("\t INSTALLING")
            os.system(statement)
            print("Installation Finished....")
            print()
            reboot = input("Do you want to reboot your system now? (yes/no) ? : ")
            if reboot == "yes":
               print("Rebooting to your new OS")
               print("The DonutOS")
               os.system('sudo reboot')
            else:
               break
         else:
            print("Installation Abort..!")

      else:
         print("Installation Abort..!")

   elif installer == "about":
      print()
      print("DonutOS 1.1 BeggorraBear Setup")
      print("Setup UI : DOSST (DonutOS Setup Tool)")
      print("v1.1")
      print("Gautham Nair")
      print()
   elif installer == "exit" or installer == "quit":
      break
   else:
      print("Invalid command..!")
