

FORCE:

tests: FORCE
	nosetests --cover-package=src

prod: tests
	git commit -a
	git push origin main

dev_env: FORCE
	pip install -r requirements/dev.txt
