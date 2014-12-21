clean:
	@find . -name "*.pyc" -delete

release:
	@git add setup.py VERSION uikit_editor/__init__.py
	@git commit -m "setup: bump to `cat VERSION`"
	@git tag $(version)
	@git push --tags
	@git push origin master
	@make clean
	@python setup.py sdist upload