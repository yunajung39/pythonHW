class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    @staticmethod
    def is_time_valid(time_string):
        return int(time_string.split(':')[0])<=24 and \
            int(time_string.split(':')[1])<=59 and \
                int(time_string.split(':')[2])<=60
    @classmethod
    def from_string(cls,time_string):
        hour, minute, second = map(int, time_string.split(':'))
        time=cls(hour, minute, second)
        return time
    
time_string = input()
 
if Time.is_time_valid(time_string):
    t = Time.from_string(time_string)
    print(t.hour, t.minute, t.second)
else:
    print('잘못된 시간 형식입니다.')