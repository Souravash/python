alcoholic=False
tatoo="nil"
donor="eligible"
if (alcoholic == True) and (tatoo=="nil"):
	donor="not eligible"
elif alcoholic== False and tatoo=="yes":
	donor="not eligible"
else:
        donor="eligible"
print(donor)
