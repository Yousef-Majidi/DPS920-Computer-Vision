import os

def rename_files():
    #rename all the files in negative folder to negative1.jpg, negative2.jpg, negative3.jpg, etc.
    # i = 1
    # for file_type in ['negative']:
    #     for img in os.listdir(file_type):
    #         os.rename(file_type+'/'+img, file_type+'/'+file_type+str(i)+'.jpg')
    #         i += 1
    #rename all the files in positive folder to positive1.jpg, positive2.jpg, positive3.jpg, etc.
    # x = 1
    # for file_type in ['positive']:
    #     for img in os.listdir(file_type):
    #         os.rename(file_type+'/'+img, file_type+'/'+file_type+str(x)+'.jpg')
    #         x += 1

    i = 1
    for file_type in ['testpics']:
        for img in os.listdir(file_type):
            os.rename(file_type+'/'+img, file_type+'/'+file_type+str(i)+'.jpg')
            i += 1
rename_files()
            