import os


def create_neg():
    for file_type in ['negative']:
        for img in os.listdir(file_type):
            if file_type == 'negative':
                line = file_type+'/'+img+'\n'
                with open('neg.txt', 'a') as f:
                    f.write(line)


def create_pos():
    for file_type in ['positive']:
        for img in os.listdir(file_type):
            if file_type == 'positive':
                line = file_type+'/'+img+'\n'
                with open('pos.txt', 'a') as f:
                    f.write(line)


create_neg()
create_pos()
