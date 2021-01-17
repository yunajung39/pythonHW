class TimeIterator:
    def __init__(self, start, stop):
        self.start=start
        self.stop=stop

    def __getitem__(self,index):
        if index<self.stop-self.start: #stop-start보다작을때
            time=self.start+index
            hour=time//3600
            time%=3600
            minute=time//60
            time%=60
            return"%02d:%02d:%02d"%(hour%24, minute, time)
        else:
            raise IndexError
        
start, stop, index = map(int, input().split())
 
for i in TimeIterator(start, stop):
    print(i)
 
print('\n', TimeIterator(start, stop)[index], sep='')