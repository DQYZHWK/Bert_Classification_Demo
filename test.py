batches=[1,2,3,4,5,6,7,8,9,0,11,22,33,44,55]
batch_size=4

class MyIterator(object):
    def __init__(self, batches, batch_size):
        self.batches = batches
        self.batch_size = batch_size
        self.num_batch_size = len(batches) // batch_size
        self.len=len(batch_size)
        if len(batches) % self.num_batch_size !=0 :
            self.residue = True
        self.index=0

    def __next__(self):
        if(self.index<self.len-1):
            one_batch = self.batches[self.index*self.batch_size:min((self.index+1)*self.batch_size,self.len)]
            return one_batch
        else:
            self.index = 0
            return StopIteration

    def __iter__(self):
        return self
    
    def __len__(self):
        if(self.residue):
            return self.num_batch_size+1
        else:
            return self.num_batch_size





it=MyIterator(batches, batch_size)


for i in it:
    print(i)
    print("\n")

