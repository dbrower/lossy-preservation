import csv
import numpy as np
#read csv file into a dictionary. read file_id into a list
with open("test_data_updated.csv", "r") as file:
    reader = csv.DictReader(file)
    file_list = [row for row in reader]
    dic={}
    id_list=[]
    for i in file_list:
        id_list.append(i['file_id'])
        dic[(i['file_id'])] = i
        del dic[(i['file_id'])] ['access_times']
        del dic[(i['file_id'])] ['file_id']

# a mru database. use dictionary to record content. use list to record order
class database :
    def __init__(self,Maxsize=10240):
        self.Maxsize = Maxsize
        self.content = {}
        self.order =[]
        self.size = 0
        self.pushtime = 0

#delect most recent accessed file, decrease its size
    def pop(self):
        file_id = self.order.pop()
        file_size = int(self.content[str(file_id)]['size'])
        self.size -= file_size
        del self.content[str(file_id)]

    
# add a new file. add its size, increase 1 to pushtime
    def push(self,file_id):
       self.order.append(str(file_id))
       file_size = int((dic[str(file_id)])['size'])
       self.size += file_size
       self.content[str(file_id)] = dic[str(file_id)]
       self.pushtime +=1

# access a file. If the file in the database, change the order of that to the most recent place.
#if not, pop most recent accessed file until there is enough space to add the file.
    def access(self,file_id):
        assert (str(file_id)  in dic)
        file_size = int((dic[str(file_id)])['size'])
        if str(file_id) in self.content:
            self.order.remove(str(file_id))
            self.order.append(str(file_id))
        else:
            while self.size + file_size > self.Maxsize:
                self.pop()
            self.push(str(file_id))


    def clear(self):
        self.content = {}
        self.order =[]
        self.size = 0
        self.pushtime = 0

            

# evaluate the accuracy of mru database. mistake is defined that a file_id is not found in the database when it is not the first time to be accessed.
#generate a random access sequence
#use set to count how many uinque ids are there in the sequence.
# then # of mistakes = pushtime - cata_num
# acc_rate = 1-mistakes / length of sequence.
def evaluate(db,se_num,idlist):
    assert type(db) == database

    idxs =np.random.randint(0,len(idlist),size=se_num)
    set_idxs = set(idxs)
    cata_num = len(set_idxs)
    randm_list = []
    for i in idxs:
        randm_list.append(idlist[i])

    for i in randm_list:
        db.access(i)
    point = 1-((db.pushtime-cata_num)/se_num)
    db.clear()
    return point