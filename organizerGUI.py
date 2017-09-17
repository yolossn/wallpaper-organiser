import os,sys,subprocess
from PIL import Image
import tkinter as tk
from tkinter import StringVar,ttk

def Bgorganizer(z):
	workDir="/"
	os.chdir(workDir)
	#check if the user provided directory exists 
	if not os.path.exists(z):
		warnPopup=tk.Toplevel()
		warnPopup.title("Directory doesn't exist")
		warnPopup.geometry("300x80")
		ttk.Label(warnPopup,text="Please check the input\nthe directory doesn't exist").pack(padx=10,pady=10)
	else:
		def organize(workDir,folderName,fileName):
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
		workDir=z
		os.chdir(workDir)
		print(workDir)
		for root,dirs,files in os.walk(workDir):
			for name in files:
				dim=getDims(name)
				if dim is not None:
					organize(workDir,"{}x{}".format(dim[0],dim[1]),name)
		
		if sys.platform.startswith('darwin'):
			subprocess.call(('open', workDir))
		elif os.name == 'nt':
			os.startfile(workDir)
		elif os.name == 'posix':
			subprocess.call(('xdg-open', workDir))
		successPopup=tk.Toplevel()
		successPopup.title("Success")
		successPopup.geometry("300x80")
		ttk.Label(successPopup,text="The images are organized").pack(padx=10,pady=10)
		ttk.Button(successPopup,text="Exit",command=lambda:sys.exit()).pack(padx=10,pady=10)





if __name__ == '__main__':
	root=tk.Tk()
	directory=StringVar()
	root.wm_title("Background organizer")
	ttk.Label(root,text="Paste the Directory where the images are stored").pack(pady=10,padx=10)
	ttk.Entry(root,textvariable=directory).pack(pady=10,padx=10)
	ttk.Button(root,text="Organize",command=lambda:Bgorganizer(directory.get())).pack(pady=10,padx=10)
	root.mainloop()




	
