# Define default target
.PHONY: all
all: update

# Define variables
INPUT :=

# Define targets
.PHONY: update
update:
	python PyMDwriter.py
	git add .
	git commit -m "$(INPUT)"
	git push
