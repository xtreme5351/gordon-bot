import torch
import os.path
from transformers import T5Tokenizer, T5ForConditionalGeneration


class Summarizer:
    def summarize(self, text):
        preprocessed_text = "summarize:" + text.strip().replace("\n", "")
        tokenized = self.token.encode(preprocessed_text, return_tensors="pt").to(self.device)
        summarized = self.model.generate(tokenized,
                                         num_beams=8,
                                         no_repeat_ngram_size=2,
                                         min_length=30,
                                         max_length=100,
                                         early_stopping=True)
        output_text = self.token.decode(summarized[0], skip_special_tokens=True)
        return output_text

    def save_summaries(self, text_to_save, index_num):
        title = "outputText_{}.txt".format(str(index_num))
        completed_path = os.path.join(self.output_path, title)
        file = open(completed_path, 'w')
        file.write(text_to_save.replace(".", "\n"))
        file.close()
        print("EVENT: Summary generated and saved")

    def __init__(self):
        self.output_path = '/Users/pc/Code/Python/gordon_bot/outputs'
        self.device = torch.device('cpu')
        self.model = T5ForConditionalGeneration.from_pretrained('t5-small')
        self.token = T5Tokenizer.from_pretrained('t5-large')
