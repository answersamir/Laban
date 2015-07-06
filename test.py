from pprint import pprint
import yaml
from yaml import dump,load 

#mydic->dictionary of entire .yml file

def func_write(mydic,f):
     for key, value in mydic.iteritems() :
    	f.write(str(key)+" ")
	for x in range(0,len(value)):
		f.write(str(value[x])+" ")
	f.write("\n")


if __name__== '__main__':

        f1=open("sample.yml")
        sample=yaml.load(f1)
        f2=open("sample.lbn","w+")
        f2.seek(0)
        func_write(sample,f2)
        f1.close()
        f2.close()    

'''# print li (just to test)
   for x in range(0,len(li)):
      f.write(str(li[x])+" ")
   f.write("\n")'''
