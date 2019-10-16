#!/usr/bin/env python
import os


def nice_output(context,filename):
    top = '#BEGIN models/' + filename + '\n'
    top+= ('#' * 25) + '\n\n\n' 
    body = context
    bottom = '\n\n\n#END models/' + filename + '\n'
    bottom+= ('#' * 25) + '\n\n\n\n'
    return top + body + bottom

generated_FILENAME = './datamodel.prisma'
generated_FILE = open(generated_FILENAME,'w')


for file in os.listdir('models'):
    current_file = open('models/{}'.format(file),'r+')
    current_file_context = current_file.read()
    generated_FILE.write(nice_output(current_file_context,file))
    current_file.close()
    
    
generated_FILE.close()


print('Schema generated')