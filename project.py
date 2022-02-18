from sharepoint import SharePoint

file_dir_path = r'C:\Users\Administrator.DEMO\Desktop\python.jpg'
file_name = 'python.jpg'
folder_name = 'Piyush'

# upload file
SharePoint().upload_file(file_dir_path, file_name, folder_name)
