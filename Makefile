python-packages := rss2pdf

check: check_black check_isort check_flake8 check_pylint check_mypy check_pydocstyle

check_black:
	black --check --diff --line-length 100 $(python-packages)

check_isort:
	isort --check --diff $(python-packages)

check_flake8:
	pflake8 $(python-packages)

check_pylint:
	pylint $(python-packages)

check_mypy:
	mypy --pretty $(python-packages)

check_pydocstyle:
	pydocstyle $(python-packages)

format:
	black -l 100 $(python-packages)
	isort $(python-packages)

install_devel:
	$(MAKE) -C .config/python-style install_devel
