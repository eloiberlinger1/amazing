PROGRAM = a_maze_ing.py

run:
	python $(PROGRAM)

lint:
	flake8 ./

install:
	echo install

debug:
	echo debug

lint-strict:
	echo lint_strict
