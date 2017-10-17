if [ ! -d "./site" ]
	then
	mkdir ./site ./site/img ./site/pages ./site/css
else
	if [ ! -d "./site/css" ]; then
		mkdir ./site/img
	fi
	#if [ ! -d "./site/pages" ]; then
	#	mkdir ./site/pages
	#fi
	if [ ! -d "./site/img" ]; then
		mkdir ./site/img
	fi
fi

cp -r ./img/* ./site/img
if [ -f "./site/css/style.css" ]
	then
	rm ./site/css/style.css
fi

touch ./site/css/style.css

if [ ! -d './tmp' ]
	then
	mkdir tmp
fi

### This function makes a list of page specified in pages directory and calls interpreter for each such page with the config file
pages=$(find pages/*.siteme)
for page in $pages
do
	#echo $page
	FULL_PATH=$(echo $page | cut -d'.' -f1)
	#echo $FULL_PATH
	NAME=$(echo $FULL_PATH | cut -d'/' -f2)
	#echo $NAME
	OUTPUT_FILE="./site/$NAME.html"
	#echo $OUTPUT_FILE
	python3 ./src/interpreter.py $page ./config.siteme > $OUTPUT_FILE 
done

if [  -f  ./tmp/*.plot ]
	then 
	gnuplot -p ./tmp/*.plot
fi

if [ -f ./site/index.html ]
	then
	xdg-open ./site/index.html
	#subl ./site/index.html
fi

