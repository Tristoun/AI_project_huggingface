from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import torch
import sys
torch.backends.cuda.matmul.allow_tf32 = True
torch.backends.cudnn.benchmark = True


class Translator:
    def __init__(self):

        self.model_name = "Helsinki-NLP/opus-mt-en-fr"
        
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        

        self.model = AutoModelForSeq2SeqLM.from_pretrained(
            self.model_name,
            torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
            low_cpu_mem_usage=True
        ).to(self.device)
        

        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
    
    
    def translate_enfr(self, text: str, max_length: int = 100):

        inputs = self.tokenizer(
            text,
            return_tensors="pt",
            max_length=512,
            truncation=True
        ).to(self.device) 
        
        #To generate our translated text
        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_length=max_length,
                num_beams=4,
                early_stopping=True
            )
        

        translated_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return translated_text


if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_text = " ".join(sys.argv[1:])
        translator = Translator()
        translated_text = translator.translate(input_text)
        print(f"Texte traduit : {translated_text}")
    else:
    	#Human -- computer 
        input_text = input("Tap the text you want to be translated : ")
        translator = Translator()
        translated_text = translator.translate(input_text)
        print(f"Translated text : {translated_text}")

