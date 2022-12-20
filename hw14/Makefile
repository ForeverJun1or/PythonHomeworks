setup: ../hw14/requirements.txt
	@echo 'setup has started'
	pip install -r requirements.txt
	flake8 --ignore=E501 main.py
	flake8 --ignore=E501 logic.py
	mypy main.py
	mypy logic.py
	@echo 'setup has ended'
run:
	python main.py