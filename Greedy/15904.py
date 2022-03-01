n = input()
check = 0
wu = n.find("U")
wfc = n.find("C", wu+1)
wp = n.find("P",wfc+1)
wsc = n.find("C",wp+1)
if wu != -1 and wfc != -1 and wp != -1 and wsc != -1:
  if wu < wfc and wfc < wp and wp < wsc:
    check = 1
if check == 1:
  print("I love UCPC")
else:
  print("I hate UCPC")