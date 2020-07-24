echo -n "Round Name:"
read round
mkdir $round 
touch $round/A.py
touch $round/B.py
touch $round/C.py
echo "for _ in range(int(input())):
    n = int(input())
    s = input()
    n,m = map(int,input().split())
    ar = list(map(int,input().split()))
" > $round/A.py
echo "for _ in range(int(input())):
    n = int(input())
    s = input()
    n,m = map(int,input().split())
    ar = list(map(int,input().split()))
" > $round/B.py
echo "for _ in range(int(input())):
    n = int(input())
    s = input()
    n,m = map(int,input().split())
    ar = list(map(int,input().split()))
" > $round/C.py

code $round/.