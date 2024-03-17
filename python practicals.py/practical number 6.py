# Tuple of integer values
integer_tuple = (1, 2, 3, 4, 5, 2, 2, 6, 7, 8, 2)

# Display the number of occurrences of a given number in the tuple
given_number = 2
occurrences = integer_tuple.count(given_number)
print(f"The number {given_number} occurs {occurrences} times in the tuple.")

# Sets of players for Cricket and Football
cricket_players = {"Player1", "Player2", "Player3", "Player4", "Player5"}
football_players = {"Player3", "Player4", "Player6", "Player7", "Player8"}

# Display players of Cricket game
print("Players of Cricket game:", cricket_players)

# Display players of Football game
print("Players of Football game:", football_players)

# Display players who have participated in both Cricket and Football
common_players = cricket_players.intersection(football_players)
print("Players who have participated in both Cricket and Football:", common_players)

# Display list of all players and total number of players
all_players = cricket_players.union(football_players)
total_players = len(all_players)
print("List of all Players:", all_players)
print("Total number of players:", total_players)

# Display list of players who participated in Cricket but not in Football
cricket_only_players = cricket_players.difference(football_players)
print("Players who participated in Cricket but not in Football:", cricket_only_players)

# Display list of players who participated in Football but not in Cricket
football_only_players = football_players.difference(cricket_players)
print("Players who participated in Football but not in Cricket:", football_only_players)
