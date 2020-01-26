question = {
    "title": "When did Charlemagne become king of France?",
    "answers": {
        "a": "800",
        "b": "700",
        "c": "750",
        "d": "780"
    },
    "right_answer": "a"
}


def quizz() -> bool:
    while True:
        print(question["title"])

        print(f"""a. {question["answers"]["a"]}\t b. {question["answers"]["b"]}""")
        print(f"""c. {question["answers"]["c"]}\t d. {question["answers"]["d"]}""")

        answer = input("Choose an answer (a, b, c, d): ")

        if answer not in question["answers"]:
            print("Please input one of the four choices: a, b, c, d")
            continue
        elif answer == question["right_answer"]:
            print("Congratulations, you won!")
            return True
        else:
            print("Wrong answer.")
            return False


if __name__ == "__main__":
    quizz()
