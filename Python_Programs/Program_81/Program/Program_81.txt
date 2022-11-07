# Import tqdm from tqdm module using the import keyword
from tqdm import tqdm
# Import sleep from time module using the import keyword
from time import sleep

# Loop till the 80 and if we specify initial argument then it will be the starting value of the progress bar
for i in tqdm(range(0, 80), initial = 20, desc ="PythonProgarms"):
    # Sleep for 2 seconds using the sleep() function
    sleep(.2)