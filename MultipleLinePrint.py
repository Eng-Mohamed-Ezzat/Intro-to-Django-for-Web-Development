
'''
Multiple Lines Print
'''
inputNum = int(input("Type number of rows:"))
inputText = str(input("Type Text:"))

for i in range(1, inputNum+1):
  print(("[{0}] : {1}").format(i,inputText))
