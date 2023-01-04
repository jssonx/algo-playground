# make run 19
NUMBER = $(filter-out $@,$(MAKECMDGOALS))

run:
	python3 auto_md_writer.py
	git add .
	git commit -m "$(NUMBER)"
	git push


