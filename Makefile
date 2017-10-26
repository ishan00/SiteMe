build:
	bash ./build.sh
tutorial:
	if [ ! -f "./pages/blog.sm" ]   \
		then                    \
		touch "./pages/blog.sm" \
	fi                              \
	python3 ./src/renderblog.py './pages/blog.sm' './Tutorial/' \
	python3 ./src/interpreter.py
clean:
	rm -r ./site/ ./tmp/
	
