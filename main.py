# copy the otter to the output
# deterministic, no network
import shutil, os
os.makedirs('/output', exist_ok=True)
shutil.copyfile('otter.jpg', '/output/entry.png')
