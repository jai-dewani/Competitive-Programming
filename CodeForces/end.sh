git status
git add . 
echo -n "Commit message: "
read com 
echo $com
git commit -m "${com}"
git push origin master