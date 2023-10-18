#open and read
file=open("Textfile.txt",'r')

# r - read
# a - append
# w - write
# x - create
# t - text mode - DEFAULT VALUE
# b - binary mode (eg, images)

count=0
for line in file:
    # Split the line into words
    words = line.split()
    # Print each word
    for word in words:
        count+=1
        print(words)

print("Number of words in a file are",count)
#close file
file.close()
