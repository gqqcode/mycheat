#coding:utf-8

# export EDITOR=/usr/bin/vim
# export DEFAULT_CHEAT_DIR='/home/gqq/mycheat/cheat/myman'

import os

import commands

# _basedir = os.path.join(os.path.abspath(__file__), "..")
# print _basedir
cheat_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "mycheat"))
print cheat_dir

content = """
export EDITOR=/usr/bin/vim
export DEFAULT_CHEAT_DIR='{0}'
""".format(cheat_dir)

with open("~/.bashrc", "a") as f:
    f.write(content)
commands.getoutput("source ~/.bashrc")
print("set env ok!")


