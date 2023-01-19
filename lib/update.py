import os
def start():
	print("Starting Update...")
	os.system("rm -rf ~/.cache/pdist-db; mkdir -p $HOME/.cache; cd $HOME/.cache; git clone https://github.com/pdist/pdist-db; rm -rf $HOME/.local/share/pdist; mkdir $HOME/.local/share/pdist; cp -r $HOME/.cache/pdist-db/db $HOME/.local/share/pdist")
	print("Done")
	print("Clean Cache")
	os.system("rm -rf ~/.cache/pdist-db")