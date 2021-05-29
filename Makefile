BASEDIR=./

all : clean

clean :
	@rm -rf `find ./ -type d -name "*__pycache__"`
	@rm -rf ./dist/ ./stringcheese*.egg-info/

build :
	python setup.py sdist
	
testupload :
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*
upload :
	twine upload dist/*
