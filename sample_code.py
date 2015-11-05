from random import randint	# randint isn't in base Python

def random_noun():
	random_num = randint(0,1)
	if random_num == 0:
		return "sofa"
	return "llama"

def random_verb():
	random_verb = randint(0,1)
	if random_verb == 0:
		return "run"
	return "kayak"

def word_transformer(word):
	if word == "NOUN":
		return random_noun()
	if word == "VERB":
		return random_verb()
	else:
		return word[0]

def process_madlib(mad_lib):
	n = 0
	length = len(mad_lib)
	processed = ""
	if length == 0:
		return mad_lib
	while n < length:
		result = word_transformer(mad_lib[n:n+4])
		if len(result) > 1:
			n += 4
		else:
			n += 1
		processed = processed + result
		if n >= length:
			return processed

test_string_1 = "This is a good NOUN to use when you VERB your food."
test_string_2 = "I'm going to VERB to the store and pick up a NOUN or two."
test_string_3 = ""
print process_madlib(test_string_1)
print process_madlib(test_string_2)
print process_madlib(test_string_3)
