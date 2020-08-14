.PHONY: clean release

clean:
	find -name '*.pyc' -delete
	find -name '*.swp' -delete

release:
	git push; git push --tags; python3 setup.py clean sdist upload
