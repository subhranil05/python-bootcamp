import os

# To check a path exists or not, it will return True/False in response
os.path.exists("/etc/hosts")

os.path.isfile("/etc/hosts")

os.path.isdir("/etc/hosts")

os.path.islink("pathtofile")

os.path.getsize("/etc/hosts")

os.path.basename("/etc/hosts")

os.path.dirname("/etc/hosts")

os.path.join("path1", "path2")