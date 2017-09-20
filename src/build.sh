if [ ! -d "../site" ]
	then
	mkdir ../site ../site/img ../site/pages ../site/css
else
	if [ ! -d "../site/css" ]; then
		mkdir ../site/img
	fi
	if [ ! -d "../site/pages" ]; then
		mkdir ../site/pages
	fi
	if [ ! -d "../site/img" ]; then
		mkdir ../site/img
	fi
fi

cp -r ../img/* ../site/img
