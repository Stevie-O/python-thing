from random import randint
f = open('<file path here>', 'r')
output = f.readlines()
with open('<file path here>') as fin:
    lines = sum(1 for line in fin)
i = randint(0,lines-1)
print output[i]
print lines

##Optional part; Writes the output string to a new file;
f = open('<file path here>', 'w')
f.write(output[i])