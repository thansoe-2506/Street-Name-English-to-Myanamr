import csv

# to_translate = ["ABGH98$CD009","ERT23NS","KKST34#9"]

ABC = {'A': ['U+1021', 'U+1031'],
 'B': ['U+1018', 'U+102E'],
 'C': ['U+1005', 'U+102E'],
 'D': ['U+1012', 'U+102E'],
 'E': ['U+1021', 'U+102E', 'U+1038'],
 'F': ['U+1021', 'U+1000', 'U+103A', 'U+1016', 'U+103A'], 
 'G': ['U+1002', 'U+103B', 'U+102E'], 
 'H': ['U+1021', 'U+102D', 'U+1010', 'U+103A', 'U+1001', 'U+103B', 'U+103A'], 
 'I': ['U+1021', 'U+102D', 'U+102F', 'U+1004', 'U+103A'], 
 'J': ['U+1031', 'U+1002', 'U+103B'], 
 'K': ['U+1000', 'U+1031'], 
 'L': ['U+1021', 'U+101A', 'U+103A'], 
 'M': ['U+1021', 'U+1019', 'U+103A'], 
 'N': ['U+1021', 'U+1014', 'U+103A'], 
 'O': ['U+1021', 'U+102D', 'U+102F'], 
 'P': ['U+1015', 'U+102E'], 
 'Q': ['U+1000', 'U+103B', 'U+1030'], 
 'R': ['U+1021', 'U+102C'], 
 'S': ['U+1021', 'U+1000', 'U+103A', 'U+1005', 'U+103A'], 
 'T': ['U+1010', 'U+102E'], 
 'U': ['U+101A', 'U+1030'], 
 'V': ['U+1017', 'U+103D', 'U+102E'], 
 'W': ['U+1012', 'U+1017', 'U+101C', 'U+1030'], 
 'X': ['U+1021', 'U+102D', 'U+1010', 'U+103A', 'U+1005', 'U+103A'], 
 'Y': ['U+101D', 'U+102D', 'U+102F', 'U+1004', 'U+103A'], 
 'Z': ['U+1007', 'U+1010', 'U+103A']}

ZEROTONINE = {'0':'U+1040','1':'U+1041','2':'U+1042','3':'U+1043','4':'U+1044','5':'U+1045','6':'U+1046','7':'U+1047','8':'U+1048','9':'U+1049'}

with open("csv_f/eng_house_number_003.csv") as enghnfile:
      enghnfileReader = csv.reader(enghnfile, delimiter=",")
      outputFile = open('csv_f/myanmar_house_number0000', 'w', encoding='utf-8', newline='')
      enghnData = list(enghnfileReader)
      for i in range(len(enghnData)):
            tempstr = str(enghnData[i])
            tempstr = tempstr.replace("['", "")
            tempstr = tempstr.replace("']", "")
            # print(tempstr)
            for i in range(len(tempstr)):
                  if tempstr[i] in ABC:
                        tlist = ABC[tempstr[i]]
                        for i in range(len(tlist)):
                              outputFile.write(chr(int(tlist[i][2:],16)))
                  elif tempstr[i].isnumeric():
                        index = ZEROTONINE[tempstr[i]]
                        outputFile.write(chr(int(index[2:],16)))           
                  else:
                        outputFile.write(tempstr[i])
            outputFile.write("\n")

print("all completed!!, find your text in csv_f/myanmar_house_number0000")
enghnfile.close()
outputFile.close()

'''
for k,v in ABC.items():
      print(k," ",end="")
      for i in range(len(v)):
            print(chr(int(v[i][2:],16)), end='')       
      print()
      # print(unicodeData)
      # ii = 65
      # for var in unicodeData:
      #       templist = []
      #       for i in range(len(var)):
      #             if var[i] == "": break
      #             templist.append("U+"+var[i])
      #       ABC[chr(ii)] = templist
      #       ii += 1           
      # print(ABC)
'''