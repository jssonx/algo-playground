# e.g. make update n=19
# NUMBER = $(filter-out $@,$(MAKECMDGOALS))

update:
	python auto_md_writer.py
	git add .
	git commit -m "update $(n)"
	git push