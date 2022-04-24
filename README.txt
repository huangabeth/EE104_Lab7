*****************************************LAB 7************************************

Author: Elizabeth Huang
Class: EE104

Video Demo: https://drive.google.com/file/d/1kKRY7AzcYYrUZ8MaweDd3T2oAcUI_STS/view?usp=sharing

*************************************************************************************
References:
Dr. Christopher Pham's Module 7 Lectures & Code
https://www.audiocheck.net/audiofrequencysignalgenerator_index.php
https://www.audacityteam.org/
https://www.kaggle.com/datasets/kinguistics/heartbeat-sounds?resource=download&select=set_a.csv
Coding Games In Python & its Python Games Resource Pack: Chapter 6 Red Alert

*************************************************************************************
ABOUT THE CODE
Code/files in Refs folder are from Dr. Christopher Pham's lectures used as reference.
	Refs folder also includes other several drafts and data files used in this lab.
wav2csv.py: source code used to convert wav -> csv

Pt. 1 FFT/IFFT Audio Signal Processing: Noise Cancelling App
	combined.wav: waveform of combined sine waves of frequencies 420, 640 & 980Hz.
	combined_Output_mono.csv: csv file containing amplitude and time data of combined.wav
	filterfreq.py: Python program that outputs plots of the combined waveform in time and
		frequency domain. Filters out high frequency, leaving 420Hz only and converts
		plot back to time domain.

Pt. 2 Heart Analysis
	Aunlabelledtest__201108011113Draft2.wav: audio recording of a heartbeat.
	Aunlabelledtest__201108011113Draft2_Output_mono.csv: CSV file with amplitude data
		of heartbeat.
	heart_analysis.py: Python program that plots heart rate signal and computes time-domain
		measurements like BPM.
	
Pt. 3 Game: Asteroid Alert!
	Game Files > red.py: run this code to play Asteroid Alert!
	Game Files > images > resize.py: code to resize images for game

*************************************************************************************
***MAKE SURE THAT THE FOLLOWING PYTHON MODULES ARE INSTALLED***
For Signal Processing with FFT:
	import numpy as np
	import scipy.optimize as opt
	import scipy.stats as st
	import math
	import matplotlib.pyplot as plt
	from scipy import fftpack

Heart Analysis:
	pip install heartpy
	import matplotlib.pyplot as plt
	

For the game Asteroid Alert!
	pip install pgzero on command line
	import pgzrun
	import pygame
	import pgzero
	import random
	import Actor
	import randint
*************************************************************************************
Instructions:
Pt. 1 FFT/IFFT Audio Signal Processing: Noise Canceling App
	1. Run filterfreq.py
	2. The program will output 4 plots:
		Fig. 1: The combined frequencies in time domain.
		Fig. 2: The combined frequencies in freq domain.
		Fig. 3: Post-filter of high frequencies. The filtered and original signals
			in time domain.
		Fig. 4: The filtered signal in freq domain.
	3. To insert your own data, simply change the csv file in lines 10 and 16.
	4. csv file of any audio recording can be obtained from wav2csv.py.
	5. Remember to adjut x and y limits of each plot.

Pt. 2 Heart Analysis
	1. Run heart_analysis
	2. The program will output 2 plots:
		Fig. 1: The heart rate signal.
		Fig. 2: The heart rate signal peak detection. Each heartbeat should have only 1
			green peak in order to output accurate results.
	3. The program will also print out the computed time-domain measurements.
		View the Kernal for results.
	4. Input data with csv file on line 11. Make sure CSV file only has amplitude data that
		has been scaled down (by dividing all data by 1000).
	5. Adjust sample rate on line 8 accordingly.
	6. csv file of recording of a heartbeat can be obtained from wav2csv.py.

Pt. 3 Game: Asteroid Alert!
	Help the Space-Cats save our planet by destroying the asteroids on their way to Earth!
	Run red.py in Game Files folder.
	1. Click on the asteroid to destroy it. Avoid your comrades, the Space-Cats!
	2. After each asteroid is successfully destroyed, the level will increase.
		More Space-Cats will arrive to the scene at different speeds, 
		so be sure to avoid destroying them!
	3. Messing up by accidentally destroying a Space-Cat or not clicking in time will
		result in GAME OVER. Click the space bar to try again.
	4. You can also play again even if you win the game after successfully completing
		all levels. :)