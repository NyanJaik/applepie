# jtext -- A library to handle your text-based needs.
# Jake Ledoux, 2017
import os

data = {}

for dataset in os.listdir(os.path.realpath(__file__)[:-11]):
	if ".txt" in dataset:
		with open(os.path.realpath(__file__)[:-11]+dataset,"r") as f:
			data[dataset[:-4]] = f.read().strip().split()
