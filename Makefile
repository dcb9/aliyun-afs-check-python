install:
	pip install aliyun-python-sdk-afs -t `pwd`
	cp -n .envrc_template .envrc || :
	cp -n event_template.json event.json || :

build:
	zip -r ~/Downloads/afsCheckPython.zip *
	aws s3 cp ~/Downloads/afsCheckPython.zip s3://aliyunsdkafs/afsCheckPython.zip

clean:
	rm -rf __pycache__/ Crypto/ aliyun_python_sdk_*/ aliyunsdk* integration/ pycryptodome*/

