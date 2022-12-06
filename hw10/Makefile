setup: requirements.txt
	@echo 'setup has started'
	pip install -r requirements.txt
	flake8 --ignore=E501 library.py
	flake8 --ignore=E501 main.py
	mypy library.py
	mypy main.py
	pytest
	@echo 'setup has started'
run:
	python main.py
