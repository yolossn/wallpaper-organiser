import os,sys,subprocess
from PIL import Image
if(len(sys.argv)<2):
	print('provide the directory or enter "s" to selct the current directory')
	sys.exit()
if(sys.argv[1]=='s'):
	workDir=os.getcwd();
else:
	homeDir='/'
	os.chdir(homeDir)
	#check if the user provided directory exists 
	if not os.path.exists(sys.argv[1]):
		print("The directory doesn't exist")
		sys.exit()
	else:
		workDir=homeDir+sys.argv[1]
		os.chdir(workDir)
print(workDir)

def organize(folderName,fileName):
	sizeFolder=workDir+"/"+folderName
	if not os.path.exists(sizeFolder):
		os.makedirs(sizeFolder)
	os.rename("{}".format(fileName),"{}/{}".format(sizeFolder,fileName)) #move files to corresponding folders
def getDims(filename):
	try: #to handle non image files in the directory
		im=Image.open(filename)
		return im.size
	except IOError:
		return None

for root,dirs,files in os.walk(workDir):
	for name in files:
		dim=getDims(name)
		if dim is not None:
			organize("{}x{}".format(dim[0],dim[1]),name)
if sys.platform.startswith('darwin'):
	subprocess.call(('open', workDir))
	sys.exit()
elif os.name == 'nt':
	os.startfile(workDir)
	sys.exit()
elif os.name == 'posix':
	subprocess.call(('xdg-open', workDir))
	sys.exit()



	
