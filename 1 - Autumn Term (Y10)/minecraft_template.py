#Pi Minecraft template (J Robinson)

#Import statements, add the minecraft api
import mcpi.minecraft as minecraft

#Find out where minecraft-pi is running, if remote IP not given then default to local machine.
host= raw_input("Enter the name of the pi where minecraft is running or press e$
if host =="":
        host="127.0.0.1"

#Connect to minecraft game and create session object mc                
mc = minecraft.Minecraft.create(host)
