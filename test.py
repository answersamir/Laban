from pprint import pprint
import yaml
from yaml import dump,load 
from pykwalify.core import Core

#mydic->dictionary of entire .yml file

def func_write(mydic,f):
     for key, value in mydic.iteritems() :
    	f.write(str(key)+" ")
	for x in range(0,len(value)):
		f.write(str(value[x])+" ")
	f.write("\n")


if __name__== '__main__':
#schema validation code
        c=Core(source_file="sample.yaml",schema_files=["schema.yaml"])
        try: 
             c.validate(raise_exception = True)
             print "Perfectly valid yaml file"
        except:
             print "Problem in validating"
        f1=open("sample.yaml")
        sample=yaml.load(f1)
        f2=open("sample.lbn","w+")
        f2.seek(0)
        func_write(sample,f2)
        f1.close()
        f2.close()    


