'''
https://www.codewars.com/kata/55b3425df71c1201a800009c/train/python
Statistics for an Athletic Association



'''

import statistics

def stat(s):
    each = s.split(",")
    runner= [e.split("|") for e in each]
    total_sec =[sec(run) for run in runner]
    median_sec = statistics.median(total_sec)
    avg_sec = sum(total_sec)/len(total_sec)
    rang = max(total_sec) - min(total_sec)
    print(avg_sec, median_sec, rang)
    
def sec(runner):
    return (3600*int(runner[0]))+60*int(runner[1])+int(runner[2])
    

def time_format(sec):
    h = sec // 3600
    m = (sec - (h*3600))//60
    s = sec - (h*3600) - (m*60)
    return f"{h}|{m}|{s}"

#test = stat("01|15|59, 1|47|16, 01|17|20, 1|32|34, 2|17|17")
test = time_format(5554)
print(test)