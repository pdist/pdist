from lib import update
from lib import install
print("Welcome To PDist!")
print("""
            .___.__           __    
______    __| _/|__|  _______/  |_  
\____ \  / __ | |  | /  ___/\   __\ 
|  |_> >/ /_/ | |  | \___ \  |  |   
|   __/ \____ | |__|/____  > |__|   
|__|         \/          \/         
                                    
    """)

print("""
1. Update
2. Install
3. Uninstall
""")
choice = input("> ")
choice = choice.replace(" ", "")
if(choice == "1"):
	update.start()
if(choice == "2"):
	install.prompt()
if(choice == "3"):
	uninstall.prompt()
