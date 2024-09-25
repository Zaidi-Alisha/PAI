def save_question(sentence, question='questions.txt'):
    try:
        if sentence.strip().endswith('?'):
            with open(question, 'a') as fileObj:
                fileObj.write(sentence + '\n')
            print("Question saved to ", question)
        else:
            print("The sentence is not a question.")
    except Exception as e:
        print("An error occurred: ", e)

sentence = input("Enter a question: ")
save_question(sentence)
