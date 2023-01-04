# e.g. make run n=19
# NUMBER = $(filter-out $@,$(MAKECMDGOALS))

run:
	python3 auto_md_writer.py
	git add .
	git commit -m "update $(n)"
	git push