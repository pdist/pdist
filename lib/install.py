import os
def clear():
	os.system("clear")
def prompt():
	print("Please Choose A Distro")
	os.system("ls ~/.local/share/pdist/db/")
	distro = input("> ")
	distro = distro.replace(" ", "")
	os.system("clear")
	print("Starting Install")
	os.system("bash ~/.local/share/pdist/db/" + distro + "/install.sh")