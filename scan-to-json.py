#! /usr/bin/python3

import json

def main():
	# Opening JSON file
	f = open('unsung-urls.json')
	unsung = json.load(f)
	f.close()
	#print(unsung)
	
	file1 = open('index-scan.txt', 'r')
	Lines = file1.readlines()
	
	vid_num = 1
	data = []
	# Strips the newline character
	for line in Lines:
		text = line.strip()
		
		if text == "":
			continue
			
		try:
			vid_num = int(text)
			continue
		except ValueError as e:
			pass
			
		print("Vid Num {}: {}".format(vid_num, text))
		data.append({"name": text, "unsung_heros_num": vid_num, "youtube_name": f"UNSUNG HEROES OF ILLUSTRATION {vid_num}", "youtube_url": unsung[str(vid_num)]})
		
		
		
	with open('illustrators.json', 'w') as f:
		json.dump(data, f)

if __name__ == "__main__": main()
