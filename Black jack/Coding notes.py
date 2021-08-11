# define the card ranks, and suits
ranks = [_ for _ in range(2, 11)] + ['JACK', 'QUEEN', 'KING', 'ACE']
suits = ['SPADE', 'HEART ', 'DIAMOND', 'CLUB']

#drawing a card with shuffel and pop
deck = [[rank, suit] for rank in ranks for suit in suits]
shuffle(deck)
player_hand = [deck.pop(), deck.pop()]
