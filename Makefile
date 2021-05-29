BASEDIR=./

all : clean

clean :
	@rm -rf `find ./ -type d -name "*__pycache__"`
build :
	python setup.py sdist
upload :
	python setup.py sdist upload
