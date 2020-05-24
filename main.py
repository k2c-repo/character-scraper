import os
import csv
import glob
import shutil

# filename = ['a','b','c','d','e']
# print(filename.index('e'))

output_file = '/home/com/Desktop/news/out.csv'
char_load_file = '/home/com/Desktop/news/output/out0.csv'

character = []



# Previous Work File Load
if os.path.exists(char_load_file):
    print("Character Load")

    char_load = open(char_load_file, 'r', encoding='utf-8')
    reader = csv.reader(char_load, delimiter=',')

    for line in reader:
        character.append(line[0])
        # print(line[0])

    # Previous Work File Copy
    shutil.copy(char_load_file, output_file)
        

# import sys; sys.exit(0)


# For Output File Save
o = open(output_file, 'a', encoding='utf-8')
wr = csv.writer(o)


# Article Load
path = "/home/com/Desktop/news/*.csv"
file_list = [file for file in glob.glob(path)]
print ("file_list: {}".format(file_list))


for list in file_list:
    print(list)
    # break

    # f = open('/home/com/Desktop/news/old/' + list + '.csv', 'r', encoding='utf-8')
    f = open(list, 'r', encoding='utf-8')
    rdr = csv.reader(f, delimiter=',')

    for line in rdr:
        
        try:
            news = line[4].replace(" ", "").replace(".", "").replace("…", "")
        except Exception as ex:
            print('error news ::: ', line)
            print(ex)
            pass
        
        # print(len(news))

        for i in range(len(news)):
            # print(news[i:i+1])
            # o.write(news[i:i+1] + '\n')
            tmp_cha = news[i:i+1]

            try:
                character.index(tmp_cha)
                # if(character.index(tmp_cha) > -1):
                    # print('Already Exist!!')
            except:                
                if(ord(tmp_cha) >= 44032 and ord(tmp_cha) <= 55215):
                    print('New Character')
                    # print(ord(tmp_cha), ' ', tmp_cha)
                    character.append(tmp_cha)
                    # o.write(tmp_cha + '\n')
                    wr.writerow([tmp_cha, line[5]])
                pass
        
        # print(news)
        # print(character)
        # break
    f.close()
o.close()