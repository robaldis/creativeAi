from transformers import pipeline, set_seed, TFGPT2LMHeadModel

def load_base_model():
    generator = pipeline('text-generation', model='distilgpt2')
    set_seed(42)
    return generator
    print(generator("Hello, I'm a language model,", max_length=30, num_return_sequences=5))



def load_fine_tuned(file_path):
    model = TFGPT2LMHeadModel.from_pretrained(file_path)
    generator = pipeline('text-generation', model=model, tokenizer='distilgpt2')
    return generator



def main():
    base = load_base_model()

    tuned = load_fine_tuned('./models/tuned/')
    print("---results---")

    print(base("fuck im lonely ", max_length=30, num_return_sequences=5), "base model")
    print(tuned("fuck im lonely ", max_length=30, num_return_sequences=5), "tuned model")

if __name__ == '__main__':
    main()
