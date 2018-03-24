import os, time
import datetime
path_to_watch = "/home/pi/.octoprint/uploads/"
queuestr = '_queue'
DBG = False

def filename_mtime_dict(path):
	return dict ([(f, os.path.getmtime(path+f)) for f in os.listdir (path)])

def appendtofile(path,src,dst):
	cmd = 'cat %s%s >> %s%s' %(path,src,path,dst)
	print datetime.datetime.now(), 'Appending file using command:',cmd
	if DBG:
		print 'Append not perfomed in debug mode'
	else:
		os.system(cmd)
	
before = filename_mtime_dict(path_to_watch)

print 'Watching directory',path_to_watch,'number of files=',len(before)

while 1:
	time.sleep (5)
	after = filename_mtime_dict(path_to_watch)
	changed = False
	for f,mtime in after.iteritems():
		if f.endswith(queuestr+'.gcode') and f.replace(queuestr,'') in before:
			if (f not in before) or (after[f] > before[f]): 
				#this is a new file, wait a couple of seconds for the uplaod to finish then append it
				print datetime.datetime.now(), 'PUSH: Detected a changed/new _queue file',f,mtime,'waiting 20 seconds for upload to finish'
				time.sleep(20)
				appendtofile(path_to_watch,f,f.replace(queuestr,''))
				time.sleep(1)
				before = filename_mtime_dict(path_to_watch)
				changed = True
		if '.gcode' in f:
			if f in before:
				if after[f] != before[f]:
					print datetime.datetime.now(), 'Detected file update:',f,'at',after[f],'from',before[f]
			else:
				print datetime.datetime.now(), 'Detected new file:',f,after[f]
				
	if DBG:
		print 'No changes'
	if not changed:
		before = after


