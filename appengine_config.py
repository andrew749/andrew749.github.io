# [START vendor]
from google.appengine.ext import vendor

# Add any libraries installed in the "lib" folder.
vendor.add('lib')

import tempfile
tempfile.SpooledTemporaryFile = tempfile.TemporaryFile
# [END vendor]<Paste>
