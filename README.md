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

E.g.:
1. Start a print from cura with the name e.g. 'box'
2. Rename the job in cura to box_queue
3. Reposition the item or add a different item on the build plate to prevent collision, change some settings around (as you wish)
4. Hit print with octoprint, then when Cura complains that octoprint is busy, click the queue job button. 
5. Your box_queue will be printed after the 'box' was finished
6. Repeat steps 3-5 as desired for unlimited queued objects only limited by your ability to aviod collisions. 

Caveats:
Your time remaining counter in octoprint will not update correctly after the first job, and the progress bar will not work correctly. 

WARNING:
This will not clear the build plate on its own. You are responsible for making sure the head does not collide with existing prints on the bed or anything. Use at your own risk. 

