#open the text file  
with open('curaminputdata', 'r') as f: 
  #read the text file into a list of lines 
  lines = f.readlines() 
 
#create an empty dictionary 
file_dict = {} 
 
#loop through the lines in the text file  
for line in lines: 
  #split the line on ':' 
  key, value = line.split('|') 
  #strip the whitespace 
  key = key.strip() 
  value = value.strip() 
  #add the key, value pair to the dictionary 
  file_dict[key] = value 
   
#print the dictionary 
print(file_dict)