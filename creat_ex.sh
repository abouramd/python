i=1
while [ $((i)) -le 5 ]
do
mkdir exercie\ $((i)) && sleep 1
touch ./exercie\ $((i))/main.py ./exercie\ $((i))/README.md
i=$((i+1))
done