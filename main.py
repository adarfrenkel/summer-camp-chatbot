import ApplicationPrompt
import QuestionPrompt
import RouterPrompt

if __name__ == '__main__':
    input_data = ""
    response = ""
    doneApplication = False
    print("Welcome to GenAi assistant (type exit to stop)")
    while input_data != "exit":
        print("How can I help?")
        input_data = input()
        if input_data.lower() == "exit":
            break
        intent, question = RouterPrompt.complete(input_data)
        if intent == "ASK":
            response = QuestionPrompt.complete(question)
        elif intent == "ENROLL":
            response = ApplicationPrompt.complete(question)

        print(response)
    print("Bye bye")