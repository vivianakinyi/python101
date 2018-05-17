## File Input and output
#Open a file
file = open("rawAddresses.csv", 'r')

print file.name
addr = []

for l in file:
    addr.append(l)

for ad in addr:
    print ad


file.close() # Got practice
    


