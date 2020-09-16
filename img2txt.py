from PIL import Image
import sys
import os
from pathlib import Path
import pyocr
import pyocr.builders
import shutil
import glob

# Image file path
image_file_folder = Path(str(Path.home())+"/Desktop/")
image_file_name = input("enter image file name>> ")
image_file_path = os.path.join(image_file_folder,image_file_name)

# Text file path (for saving text)
txt_file_folder = Path(str(Path.home())+"/Desktop/")
txt_file_name = input("enter text file name>> ")
txt_file_path = os.path.join(txt_file_folder,txt_file_name)

# Process start
tools = pyocr.get_available_tools()
if len(tools) == 0:
	print("No OCR tool found")
	sys.exit(1)
tool = tools[0]
print("Will use tool {}".format(tool.get_name()))

# Get available language
langs = tool.get_available_languages()
print(langs)

# Copy training data from /data/tessdata/ to /data/
dest = os.environ.get("TESSDATA_PREFIX")
#print(dest)
src = os.path.join(dest,"tessdata")
for f in glob.glob(src+'/**/*', recursive=True):
        shutil.copy(f,dest)

print("Available languages: "+", ".join(langs))

lang_selected = input('select language>> ')

# Extract text from image
txt = tool.image_to_string(
	Image.open(image_file_path),
	lang = lang_selected,
	builder = pyocr.builders.TextBuilder()
	)

# Output text to txt file
print(txt)
f = open(txt_file_path, "w")
f.write(txt)
print("Text file has been written in {}".format(txt_file_path))
f.close()

