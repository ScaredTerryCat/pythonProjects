#i made this for windows but it can be easily extended to linux or other operating systems with some changes
import os
from subprocess import check_output
#things means files and directories
def print_all_things(path="C:/",tabs="\t"):
	try:
		for i in os.listdir(path):
			newPath=os.path.join(path,i)
			print(tabs+"|---"+i)
			print_all_things(newPath,tabs+"\t")
	except Exception as e:
		pass
def getUser():
	command="echo %USERNAME%"
	response=check_output(command,shell=True,text=True)
	return response
def getAllPathsWorker(paths,path):
	try:
		for i in os.listdir(path):
			newPath=os.path.join(path,i)
			paths.append(newPath)
			getAllPaths(newPath)
	except Exception as e:
		pass
def getAllPaths(path="C:/"):
	paths=[]
	getAllPathsWorker(paths,path)
	return paths
def findFileOrFolderWorker(path,target,result):
	try:
		for item in os.listdir(path):
			if(item==target):
				foundPath=os.path.join(path,item)
				result.append(f" '{item}' found!\t Location:{foundPath}")
				return
			print(f" '{target}' Not found yet...still searching...\tcurrent path:{os.path.join(path,item)}")
			findFileOrFolderWorker(os.path.join(path,item),target,result)
	except Exception as e:
		pass
def findFileOrFolder(path="C:/",target="example.txt"):
	result=[]
	findFileOrFolderWorker(path,target,result)
	if(result==[]):
		return f"{target} not found!"
	else:
		return result



if __name__ == "__main__":
	user=getUser()
	user=user[0:len(user)-1]#for me it also takes a space after the name,if this is not your case delete this line of code
	#or comment it lol

	#print_all_things(f"C:/users/{user}/desktop") 
	
	#paths=getAllPaths(f"C:/users/{user}/desktop")
	#print(paths)

	#targetFile="python"
	#found=findFileOrFolder(f"C:/Users/{user}/desktop",targetFile)
	#print(found[0])

	target=input("Enter the name of the file or directory for which you want to search.")
	directory=input("Enter directory from where to start searching recursively or 0 for default 'C:/' ")
	if(directory=="0"):
		directory="C:/"
	found=findFileOrFolder(directory,target)
	print(found[0])





