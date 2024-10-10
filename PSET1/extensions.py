file_name = input("File name: ").strip().lower()


extensions = {
    ".gif": "image/gif",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".pdf": "application/pdf",
    ".txt": "text/plain",
    ".zip": "application/zip"
}


dot_index = file_name.rfind('.')
if dot_index != -1:
    extension = file_name[dot_index:]
else:
    extension = ''


media_type = extensions.get(extension, "application/octet-stream")

print(media_type)
