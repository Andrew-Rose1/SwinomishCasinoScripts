import os
import time
import shutil

src = "\\\\argus\\Compliance\\T31"
dest = "D:\\T31"


try:
# Clean up dest
    print(f'Cleaning up:. Please wait...')
    for i in os.listdir(dest):
        if os.path.isdir(f'{dest}\\{i}'):
            shutil.rmtree(f'{dest}\\{i}')
        else:
            os.remove(f'{dest}\\{i}')

# Copy all from src to dest
    for i in os.listdir(src):
        print(f'Copying: "{i}"... Please wait...')
        if os.path.isdir(f'{src}\\{i}'):
            shutil.copytree(f'{src}\\{i}', f'{dest}\\{i}')
        else:
            shutil.copy(f'{src}\\{i}', f'{dest}\\{i}')
    print("Success!") 
except Exception as e:
    print("There was an error! Please contact IT!")
    print(e)
print("This window will automatically close in 15 seconds...")
time.sleep(15)