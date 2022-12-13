setup: requirements.txt
	@echo 'setup has started'
	pip install -r requirements.txt
	flake8 --ignore=E501 homework13.py
	flake8 --ignore=E501 Figures.py
	mypy homework13.py
	mypy Figures.py
	pytest
	@echo 'setup has ended'
run:
	python homework13.py