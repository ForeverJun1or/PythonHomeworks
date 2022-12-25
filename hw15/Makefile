setup: ../hw15
	flake8 --ignore=E501,W605 main.py
	flake8 --ignore=E501 CurrencyExchange.py
	pip install requests
	mypy --install-types
	mypy main.py
	mypy CurrencyExchange.py

run:
	python main.py