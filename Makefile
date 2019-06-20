deps:
	pip install -r test_requirements.txt
test:
	PYTHONPATH= py.test
