echo -n "Round Name:"
read round
mkdir $round 

template="for _ in range(int(input())):
    n = int(input())
    s = input()
    n,m = map(int,input().split())
    ar = list(map(int,input().split()))"

touch $round/A.py
touch $round/B.py
touch $round/C.py
echo "${template}" > $round/A.py
echo "${template}" > $round/B.py
echo "${template}" > $round/C.py

code $round/.