from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

model_name = "deepset/tinyroberta-squad2"

nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)


def nlp_qna(context, question):
    QA_input = {
        'question': question,
        'context': context
    }
    res = nlp(QA_input)

    return res