from utils import file, audio_processing
import os
import pandas as pd


################# parameters ###################################


csv_path = r'/home/why/Projects/Sleep_Apnea/Sleep_Code_Data/Temporary_Files'

path = r'/home/why/Projects/Sleep_Apnea/Sleep_Code_Data/Raw Data'   #Raw_Data path
year = 2021
month = 2

wavcomb_path = r'/home/why/Projects/Sleep_Apnea/Sleep_Code_Data/Wav_Combine'     #Wav_Combine path
mel_path = r'/home/why/Projects/Sleep_Apnea/Sleep_Code_Data/All_Mel'


################# parameters ###################################


os.chdir(csv_path)
name = f'Date_and_ID_list_{year}_{month}.csv'
Date_and_ID_list = pd.read_csv(name)
Date_and_ID_list = [x for x in Date_and_ID_list['0']]



count = 0
for x in Date_and_ID_list:
    
    if count!=1:

        data = True
        source_path = file.full_path(wavcomb_path, year, month, x)[0]

        for files in os.listdir(mel_path):

            if files.endswith(f'{x[5:]}.png'):
                data = False


        os.chdir(source_path)
        for files in os.listdir():

            # Check whether file is in wav or not
            if files.endswith(".wav"):

                if data:

                    source = f'{source_path}/{files}'
                    destination = f'{mel_path}/{x[5:]}.png'
                    print(source)
                    print(destination)

                    audio_processing.mel(source[:-4], destination[:-4])
                    count+=1

                else:
                    print(f'{files}: Already transferred')

