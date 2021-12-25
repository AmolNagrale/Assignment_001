# from logging import*
# debug("This is Debug")
# info("This is Info")
# warning("This is Warning")    # By default warning display on console
# error("This is Error")
# critical("This is Critical")

# How to create logging file

from logging import*

# if we want to declare specific path.
# basicConfig(filename = 'logfile.log', level = DEBUG) #by default it has work on append mode 
# 
# debug("This is Debug")
# info("This is Info")
# warning("This is Warning")     
# error("This is Error")
# critical("This is Critical")


# How to change append mode to write mode

# basicConfig(filename = 'logfile.log', level = DEBUG, filemode = 'w') 
# 
# debug("This is Debug in w mode")
# info("This is Info in w mode")
# warning("This is Warning in w mode")     
# error("This is Error in w mode")
# critical("This is Critical in w mode")

# How to use format stored data into log file

LOG_FORMAT = '(% asctime)s//(% message)s//(% lineno)d'

basicConfig(filename = 'logfile.log', level = DEBUG, filemode = 'w', format = LOG_FORMAT) 

debug("This is Debug in w mode")
info("This is Info in w mode")
warning("This is Warning in w mode")     
error("This is Error in w mode")
critical("This is Critical in w mode")





