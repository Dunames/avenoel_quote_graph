import pathlib
import json

ABS_PATH = pathlib.PATH("/PATH/to/folder")
PATH = ABS_PATH.joinpath("avenoel_messages_June22.jsonl")


def load_jsonl(path):
	data = []
	with open(path, 'r', encoding='utf-8') as reader:
		for line in reader:
			data.append(json.loads(line))
	return data
	
	
def create_users_list(data):
	list_users = []
	N = len(data)
	for k in range(0, N):
		elmt = data[k]
		if len(elmt["user"]) > 0:
			if elmt["user"] not in list_users:
				list_users.append(elmt["user"])
		if len(elmt["quotes"]) > 0:
			p = len(elmt["quotes"])
			for i in range(0, p):
				if elmt["quotes"][i] not in list_users:
					list_users.append(elmt["quotes"][i])
	return list_users
	
	
def build_multikey_map(data, list_users):
	map = {}
	map["__README__"] = "map[user1][user2] is the number of times user2 quotes user1"
	#      map[user1][user2] is high when user1 is quoted a lot by user2
	#      map[user1][user2] = 62 means that user2 quoted user1 62 times
	for user in list_users:
		map[user] = {}
		
	for user1 in list_users:
		for user2 in list_users:
			map[user2][user1] = 0
	
	for elmt in data:
		bool1 = len(elmt["user"]) > 0
		bool2 = len(elmt["quotes"]) > 0
		if bool1 and bool2:
			user1 = elmt["user"]
			for user2 in elmt["quotes"]:
				map[user2][user1] += 1
	
	return map