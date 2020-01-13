import csv
import pandas as pd

with open('next.txt', encoding = 'latin1') as f:
	read = csv.reader(f)
	rows = list(read)
