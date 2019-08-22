import numpy as np

pod = "/home/kristijan/python_test-programi/test_of_words.txt"
sec = "/home/kristijan/python_test-programi/empty_file.txt"
def sort_words(file,save_file):
    f = open(file,"r")
    content = f.read()
    print("Unsordet : ",content)
    content = content.split()
    content.sort()
    print("Sorted : ",content)
    for i in range(0,len(content)):
                    print(i+1,":",content[i])

    with open(save_file, 'w') as f:
        for item in content:
            f.write("%s\n" % item)

sort_words(pod,sec)
