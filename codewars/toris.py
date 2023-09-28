'''

https://www.codewars.com/kata/55e2adece53b4cdcb900006c/train/python

Two tortoises named A and B must run a race. A starts with an average speed of 720 feet per hour. Young B knows she runs faster than A, and furthermore has not finished her cabbage.

When she starts, at last, she can see that A has a 70 feet lead but B's speed is 850 feet per hour. How long will it take B to catch A?

More generally: given two speeds v1 (A's speed, integer > 0) and v2 (B's speed, integer > 0) and a lead g (integer > 0) how long will it take B to catch A?

The result will be an array [hour, min, sec] which is the time needed in hours, minutes and seconds (round down to the nearest second) or a string in some languages.

If v1 >= v2 then return nil, nothing, null, None or {-1, -1, -1} for C++, C, Go, Nim, Pascal, COBOL, Erlang, [-1, -1, -1] for Perl,[] for Kotlin or "-1 -1 -1" for others.

'''

def race(v1, v2, g):
    t = g / (v2 - v1)  # 追上所花的時間
    print(t)
    if  t >= 1:
        h = t//1
        m = (t-h)*60
        s = t * 3600 - h*3600 - m*60
    else:
        h = 0
        m = (t*60)
        s = t * 3600 - h*3600 - m*60
    
    if v1 >= v2 :
        return None
    else:
        return [int(h), int(m), round(s)]
    
 
test = race(80, 91, 37) 
print(test)