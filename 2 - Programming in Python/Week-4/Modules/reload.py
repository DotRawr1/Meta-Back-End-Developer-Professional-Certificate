# import only works once
# reload can reload at any time

#import importlib
#import importSample
#importlib.reload(importSample)

import importlib
import importSampleFileChange

def changes():
    try:
        importlib.reload(importSampleFileChange)
        importSampleFileChange.print_changes()
    except:
        pass

for i in range(3):
    changes()
    input("Hit enter to reload...")