"""
File: rotten_tomato.py
Name:
-------------------------------
This file shows basic AI in classification task:
movie review classification.
First, tokenize the review
Second, count each token and give them corresponding scores
Finally, calculate the score for each word such that we can
predict a movie review by summing over the scores
"""


# The file with labels and reviews
FILENAME = 'movie_review.txt'


def main():
	with open(FILENAME, 'r') as f:
		d = {}
		all_d = {'positive': [], 'natural': [], 'negative': []}
		for line in f:
			lst = line.split(':')
			score = lst[0]
			score = int(score[1:3])
			review = lst[1].strip()
			tokens = review.split()
			for token in tokens:
				token = string_manipulation(token)
				if token in d:
					d[token] += score
				else:
					d[token] = score
		for word, score in d.items():
			if score > 0:
				all_d['positive'].append(word)
			elif score == 0:
				all_d['natural'].append(word)
			else:
				all_d['negative'].append(word)
		print(all_d)


def string_manipulation(s):
	ans = ''
	for ch in s:
		if ch.isalpha():
			ans += ch.lower()
	return ans








if __name__ == '__main__':
	main()
