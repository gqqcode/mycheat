import commands

commands.getoutput("git add .")
commands.getoutput('git commit -a -m  "update"')
commands.getoutput("git push")
print("update mycheat ok!")
