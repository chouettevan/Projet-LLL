for i in `ls *.py`
do
	python3 $i || exit 1
done
