from APIs.file_handler import *

def test():
    
    object = {
        "id" : 1,
        "data" : {
            "name" : "Sukhdev Singh",
            "age" : 22
        }
    }

    output_fp = "C:\\Users\\Sukhdev Singh\\Documents\\repos\\Big-File-Processing\\output.txt"

    m = TextFileWriter(output_fp)
    for i in range(10):
        object["id"] = i
        m.write(str(object)+"\n")
    for i in range(10):
        object["id"] = i+10
        m.write(str(object)+"\n")
    m.close()
    
    for line in open(output_fp,'r'):
        print(line)

test()