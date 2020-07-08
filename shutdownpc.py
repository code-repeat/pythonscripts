import subprocess
task = input("Digite seu comando> ")
if task == "desligar":
     subprocess.call("shutdown /s /t 0", shell=True)
 
