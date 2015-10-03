from setuptools import setup, find_packages
setup(
	name="Hello",
        version="0.1",
 	scripts=["hello.py"],
	install_requires=['pbr>=1.8.0',
			  'python>=2.7',
			  'nova'],
	package_data = {
		'': ['*.txt', '*.rst'],
		'hello': ['*.msg'],
		},
	author = "Me",
    	author_email = "me@example.com",
    	description = "This is an Example Package",
    	license = "PSF",
    	keywords = "hello world example examples",
    	url = "http://example.com/HelloWorld/",   # project home page, if any
)
