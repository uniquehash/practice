# https://hackernoon.com/how-to-build-a-simple-spam-detecting-machine-learning-classifier-4471fe6b816e

#runs once on training data
def train:
	total = 0
	numSpam = 0
	for email in trainData:
		if email.label == SPAM:
			numSpam += 1
		total += 1
		processEmail(email.body, email.label)
	pA = numSpam/(float)total
	pNotA = (total - numSpam)/(float)total

#counts the words in a specific email
def processEmail(body, label):
	for word in body:
		if label == SPAM:
			trainPositive[word] = trainPositive.get(word, 0) + 1
			positiveTotal += 1
		else:
			trainNegative[word] = trainNegative.get(word, 0) + 1
			negativeTotal += 1

#gives the conditional probability p(B_i | A_x)
def conditionalWord(word, spam):
	if spam:
		return trainPositive[word]/(float)positiveTotal
	return trainNegative[word]/(float)negativeTotal

# #laplace smoothing
# def contionalWord(word, spam):
# 	if spam:
# 		return (trainPositive.get(word, 0) + alpha)/(float)(positiveTotal + alpha * numWords)
# 	return (trainNegative.get(word, 0) + alpha)/(float)(negativeTotal + alpha * numWords)

#gives the conditional probability p(B | A_x)
def conditionalEmail(body, spam):
	result = 1.0
	for word in body:
		result *= conditionalWord(word, spam)
	return result

#classifies a new email as spam or not spam
def classify(email):
	isSpam = pA * conditionalEmail(email, True) # P (A | B)
	notSpam = pNotA * conditionalEmail(email, False) # P(not A | B)
	return isSpam > notSpam
