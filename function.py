def convertToMin(seconds):
     mins = str(int(seconds//60))
     secs = str(seconds%60)
     return(mins+'min'+secs)

print(convertToMin(102.3))
