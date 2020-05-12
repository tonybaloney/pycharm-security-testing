import os
import stat
from os import chmod

os.chmod('x', 777)

os.chmod('x', 0o777)

os.chmod('x', 0o300)

os.chmod('x', stat.S_IXOTH | stat.S_IXGRP)
os.chmod('x', stat.S_IXOTH)
os.chmod('x', stat.S_IRUSR | stat.S_IRGRP | stat.S_IWUSR | stat.S_IXOTH)

chmod('x', 777)