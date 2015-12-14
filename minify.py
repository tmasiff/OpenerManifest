import sys
import subprocess
import re
import os
import shutil
import json

if len(sys.argv) < 2:
    print "No path specified"
    sys.exit()
    
path = sys.argv[1]

data = json.loads(open(path).read())

# Strip unneeded keys from apps
for appIndex,app in enumerate(data['apps']):
	appKeys = app.keys()
	for keyIndex,key in enumerate(appKeys):
		if not key in ["identifier", "displayName", "storeIdentifier", "scheme", "new", "platform", "iconURL"]:
			# print "Removing " + key + " from " + app["identifier"]
			app.pop(key, None)
			
# Strip unneeded keys from actions
for actionIndex,action in enumerate(data['actions']):
	actionKeys = action.keys()
	for keyIndex,key in enumerate(actionKeys):
		if not key in ["title", "regex", "includeHeaders", "formats"]:
			# print "Removing " + key + " from action"
			action.pop(key, None)
		
	# Strip unneeded keys from formats
	for format in action['formats']:
		formatKeys = format.keys()
		for keyIndex,key in enumerate(formatKeys):
			if not key in ["appIdentifier", "format", "script"]:
				# print "Removing " + key + " from format"
				format.pop(key, None)
				
data = json.dumps(data, separators=(',',':'))
open(path.replace('.json', '-minified.json'), 'w').write(data)