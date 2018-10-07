
import os, shutil, glob

src_fldr = r"C:\Users\Neil Dahiya\Downloads" ## Edit this

# Moving txt files
dst_fldr_txt = r"C:\Users\Neil Dahiya\Downloads\txt" ## Edit this
try:
  os.makedirs(dst_fldr_txt); ## it creates the destination folder
except:
  print ("Folder already exist or some error")
for txt_file in glob.glob(src_fldr+"\\*.txt"):
    shutil.move(txt_file, dst_fldr_txt);


# Moving jgp files
dst_fldr_jpg = r"C:\Users\Neil Dahiya\Downloads\IMG" ## Edit this
try:
  os.makedirs(dst_fldr_jpg); ## it creates the destination folder
except:
  print ("Folder already exist or some error")

for txt_file in glob.glob(src_fldr+"\\*.jpg"):
    shutil.move(txt_file, dst_fldr_jpg);
for txt_file in glob.glob(src_fldr+"\\*.png"):
    shutil.move(txt_file, dst_fldr_jpg);
for txt_file in glob.glob(src_fldr+"\\*.jpeg"):
    shutil.move(txt_file, dst_fldr_jpg);


# Moving exe files
dst_fldr_exe = r"C:\Users\Neil Dahiya\Downloads\EXE" ## Edit this
try:
  os.makedirs(dst_fldr_exe); ## it creates the destination folder
except:
  print ("Folder already exist or some error")

for exe_file in glob.glob(src_fldr+"\\*.exe"):
    shutil.move(exe_file, dst_fldr_exe);


# Moving zip/rar/7z files
dst_fldr_zip = r"C:\Users\Neil Dahiya\Downloads\ZIPs" ## Edit this
try:
  os.makedirs(dst_fldr_zip); ## it creates the destination folder
except:
  print ("Folder already exist or some error")

for zip_file in glob.glob(src_fldr+"\\*.zip"):
    shutil.move(zip_file, dst_fldr_zip);
for rar_file in glob.glob(src_fldr+"\\*.rar"):
    shutil.move(rar_file, dst_fldr_zip);
for sz_file in glob.glob(src_fldr+"\\*.7z"):
    shutil.move(sz_file, dst_fldr_zip);


# Moving pdf files
dst_fldr_pdf = r"C:\Users\Neil Dahiya\Downloads\PDFs" ## Edit this
try:
  os.makedirs(dst_fldr_pdf); ## it creates the destination folder
except:
  print ("Folder already exist or some error")

for pdf_file in glob.glob(src_fldr+"\\*.pdf"):
    shutil.move(pdf_file, dst_fldr_pdf);


# Moving document files
dst_fldr_xlsx = r"C:\Users\Neil Dahiya\Downloads\XLSXPPTDOC" ## Edit this
try:
  os.makedirs(dst_fldr_pdf); ## it creates the destination folder
except:
  print ("Folder already exist or some error")

for pdf_file in glob.glob(src_fldr+"\\*.xlsx"):
    shutil.move(pdf_file, dst_fldr_xlsx);
for pdf_file in glob.glob(src_fldr+"\\*.pptx"):
    shutil.move(pdf_file, dst_fldr_xlsx);
for pdf_file in glob.glob(src_fldr+"\\*.docx"):
    shutil.move(pdf_file, dst_fldr_xlsx);
for pdf_file in glob.glob(src_fldr+"\\*.ppt"):
    shutil.move(pdf_file, dst_fldr_xlsx);
for pdf_file in glob.glob(src_fldr+"\\*.doc"):
    shutil.move(pdf_file, dst_fldr_xlsx);
for pdf_file in glob.glob(src_fldr+"\\*.csv"):
    shutil.move(pdf_file, dst_fldr_xlsx);
for pdf_file in glob.glob(src_fldr+"\\*.pot"):
    shutil.move(pdf_file, dst_fldr_xlsx);
for pdf_file in glob.glob(src_fldr+"\\*.potx"):
    shutil.move(pdf_file, dst_fldr_xlsx);


# Moving mp3 files
dst_fldr_pdf = r"C:\Users\Neil Dahiya\Downloads\MP3" ## Edit this
try:
  os.makedirs(dst_fldr_pdf); ## it creates the destination folder
except:
  print ("Folder already exist or some error")

for pdf_file in glob.glob(src_fldr+"\\*.mp3"):
    shutil.move(pdf_file, dst_fldr_pdf);

# Moving psd files
dst_fldr_psd = r"C:\Users\Neil Dahiya\Downloads\PSD" ## Edit this
try:
  os.makedirs(dst_fldr_psd); ## it creates the destination folder
except:
  print ("Folder already exist or some error")

for pdf_file in glob.glob(src_fldr+"\\*.psd"):
    shutil.move(pdf_file, dst_fldr_psd);
