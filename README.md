# OctoPrint_Cura_Queue
This small scripts allows you to queue additional prints from Cura into octoprint without having to start new jobs
It works with perfectly with Raspberry Pi Octoprint hosts.
It watches the /home/pi/.octoprint/uploads/ directory for new/modified files that end in [anything]_queue.gcode, when it sees one, it will wait for the upload to finish then append the contents of [anything]_queue.gcode to [anything].gcode. 
Thus if [anything].gcode is a file under printing, it will also print the new file appended to it. 


How to install: 
1. copy octoqueue.py onto the raspi, e.g. to /home/pi
2. optionally add 
(sleep 10; python /home/pi/octoqueue.py >> /home/pi/octoqueue.log)&
to your /etc/rc.local file to make the script run from start up

How to use:
Start any print, and remember the filename. If you upload/update a new file to octoprint (either through cura's queue job button or through the interface) with the name [filename]_queue.gcode, then it will append all the commands and print those as well.

WARNING:
This will not clear the build plate on its own. You are responsible for making sure the head does not collide with existing prints on the bed or anything. Use at your own risk. 

