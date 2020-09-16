from PIL import Image
import sys
import os
from pathlib import Path
import pyocr
import pyocr.builders

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
langs_extract = [l for l in langs if "tessdata/" in l]
#print('List of languages: {}'.format(langs_extract))
langs_formatted = [m.split('/')[1] for m in langs_extract]
#print('List of languages_formatted: {}'.format(langs_formatted))

print("Available languages: "+", ".join(langs_formatted))

lang_selected = input('select language>> ')
#print('selected language is: {}'.format(lang_selected))
lang_selected = langs_extract[langs_formatted.index(lang_selected)]
#print('selected (formatted) language is: {}'.format(lang_selected))

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

