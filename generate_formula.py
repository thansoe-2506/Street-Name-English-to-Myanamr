import clipboard
import sys
'''
=CONCATENATE(
"A2=",char(34),A1,CHAR(34),",",CHAR(34),B1,CHAR(34),",",
"A2=",char(34),A2,CHAR(34),",",CHAR(34),B2,CHAR(34),",",
"A2=",char(34),A3,CHAR(34),",",CHAR(34),B3,CHAR(34),",",)
'''

cmd_arg1 = sys.argv[1]
cmd_arg2 = sys.argv[2]
cmd_arg3 = sys.argv[3]

first_column = cmd_arg1[0]
second_column = cmd_arg2[0]
applied_cell = cmd_arg3
# total_row = sys.argv[3]
string = "\""+applied_cell+"=\",CHAR(34),"+first_column+"%s,CHAR(34),\",\",CHAR(34),"+second_column+"%s,CHAR(34)"
generated_formula = "=CONCATENATE("
start = int(cmd_arg1[1:])
end = int(cmd_arg2[1:])+1
for i in range(start,end):
      if i == end - 1:
            generated_formula += (string % (i,i))
      else:
            generated_formula += (string % (i,i)) + ",\",\","

clipboard.copy(generated_formula)
print("You can paste now!(Ctrl+V)",len(generated_formula))
