import os

# to run any linux commands or os specific commands
os.system("ls -l")
os.system("pwd")

# x = os.system("pwd")
# print(x)

# to run any os module specific commands for linux
# show present dir
os.getcwd()

# to change dir
os.chdir("path")

# to list dir
os.listdir()

# To create a file
os.mknod("testfile.sh")

# To create a dir
os.mkdir("testdir")

# to create dir recurively similar to 'mkdir -p '
os.makedirs("test1dir/test2dir")

# to print all env variables
os.environ

# to get specific env variable
os.environ.get("HOME")

# get id
os.getuid()
os.getgid()

# to remove dir
os.rmdir("testdir")
os.removedirs("test1dir/test2dir")