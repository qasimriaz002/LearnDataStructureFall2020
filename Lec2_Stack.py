#   In this lecture we are going to implement Last in first out --- Stack based data strcutrue
#   Here we will use the list for the implementation of stacks in Python

foldersList = []

foldersList.append("mangoFolder")
foldersList.append("oranageFolder")
foldersList.append("bannanaFolder")
foldersList.append("guavaFolder")
foldersList.append("cherryFolder")

print(foldersList)

foldersList.pop()       # at this point cherryFolder will be removed
print(foldersList)

foldersList.pop()       # at this point guavaFolder will be removed
print(foldersList)

foldersList.pop()       # at this point bannanaFolder will be removed
print(foldersList)

foldersList.pop()       # at this point orangeFolder will be removed
print(foldersList)

foldersList.pop()       # at this point mangoFolder will be removed
print(foldersList)

foldersList.pop()

