import re
stringText = "Hi this is Wild on, from the Wild Wild west"
cleanString = re.sub(r"[^\w\s]", "", stringText.lower())
for word in cleanString.split():
    print (word)

