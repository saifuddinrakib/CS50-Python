filename =input(("file name:"))
new_filename=filename.lower()
#if gif or png or jpg, print "image/type"
if '.gif'   in  new_filename:
    print ("image/gif")
elif '.png' in  new_filename:
    print ("image/png")
elif '.jpg' in  new_filename:
    print ("image/jpeg")
elif '.jpeg'in  new_filename:
    print ("image/jpeg")
elif '.pdf' in  new_filename:
    print ("application/pdf")
elif '.zip' in  new_filename:
    print ("application/zip")
elif '.txt' in  new_filename:
    print ("text/plain")
else:
    print("application/octet-stream")

