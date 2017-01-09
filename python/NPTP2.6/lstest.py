def get_question():
    return[["What color is the daytime sky on a clear day? ", "blue"],
           ["What is the answer to life, the universe and everything? ", 42],
           ["What is a three letter word for mouse trap? ", "cat"],
           ["What noise does a truly advanced machine make?","ping"]]
           

def check_quesiton(question_and_answer):
    question = question_and_answer[0]
    answer = question_and_answer[1]
    given_answer = raw_input(question)
    if answer == given_answer:
        print "Corrent"
        return True
    else:
        print "Incorrent, corrent was ", answer
        return False

def run_test(question):
    if len(question) ==0:
        print "No Question were given"
        return 
    index = 0
    right = 0
    while index < len(question):
        if check_quesiton(question[index]):
            right += 1
            index += 1
        else:
            index += 1
    print "You got", right * 100 /len(question),\
          "% right out of", len(question)

run_test(get_question())