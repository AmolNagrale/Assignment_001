from logging import*

''' Important note :- by default warning level has set, hence we are shown
only below of this level but above of this level has not show'''

basicConfig(filename = "mylogs.log", level = DEBUG, filemode = "w",)

debug("This is debug")

info("This is Info")

warning("This is warning")

error("This is error")

critical("This is critical")

