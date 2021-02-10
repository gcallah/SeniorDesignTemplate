

FORCE:


tests: FORCE
	nosetests --cover-package=src

prod: tests
	git commit -a
	git push origin main
