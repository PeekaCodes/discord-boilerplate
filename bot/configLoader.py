from configparser import ConfigParser
import os 

cfg_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'config.ini'))



config = ConfigParser()
config.read(cfg_path) #path of your .ini file



# read values from a section
def getToken():
 
 return config.get("Settings","token") 


