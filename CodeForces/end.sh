git status
flag="1"
while flag=="1"; do
    echo -n "Add files: "
    read FILES 
    git add $FILES && flag="0"
    echo -n "Done? [Y/N]: "
    read ans 
    if $ans=="Y"; then 
        flag="1"
    fi 
done 
echo -n "Commit message: "
read commit 
git commit -m $commit
git push origin master