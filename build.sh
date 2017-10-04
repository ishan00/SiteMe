if [ ! -d "./site" ]
	then
	mkdir ./site ./site/img ./site/pages ./site/css
else
	if [ ! -d "./site/css" ]; then
		mkdir ./site/img
	fi
	if [ ! -d "./site/pages" ]; then
		mkdir ./site/pages
	fi
	if [ ! -d "./site/img" ]; then
		mkdir ./site/img
	fi
fi

cp -r ./img/* ./site/img
if [ -f "./site/css/style.css" ]
	then
	rm ./site/css/style.css
fi

#touch ./site/css/style.css

# The Following Lines needs to be removed later
cp ./layout/slideshow.css ./site/css/style.css
cp ./layout/slideshow.js ./site/css/slideshow.js
cp ./layout/footer_basic.css ./site/css/footer_basic.css
cp ./layout/navbar_orange.css ./site/css/navbar_orange.css

if [ ! -d './tmp' ]
	then
	mkdir tmp
fi

#python3 ./src/parser.py ./pages/index.siteme >./tmp/index.tmp
#python3 ./src/interpreter.py >./site/index.html

python3 ./src/interpreter.py ./pages/index.siteme ./config.siteme > ./site/index.html
if [ -f "./tmp/*.plot" ]
	then gnuplot ./tmp/*.plot
fi
