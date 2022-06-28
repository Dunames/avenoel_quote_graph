def sum_quotes(map, list_users, ref_user):
	n_quotes = 0
	for user2 in list_users:
		n_quotes += map[ref_user][user2]
	return n_quotes
	

def compute_number_messages(data, user):
	n_messages = 0
	for elmt in data:
		if len(elmt["user"]) > 0 and elmt["user"] == user:
			n_messages += 1
	return n_messages


def compute_stats_per_user(map, data, list_users):
	L = []
	for user in list_users:
		S_user = sum_quotes(map, list_users, user)
		N_user = compute_number_messages(data, user)
		L.append( (user, S_user, N_user, S / (N_user + 1)) )
	
	return L