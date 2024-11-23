from transformers import AutoModelForCausalLM, AutoTokenizer
from huggingface_hub import login
import torch
torch.backends.cuda.matmul.allow_tf32 = True
torch.backends.cudnn.benchmark = True
login("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")

class ChatAI() :
    def __init__(self) -> None:
        self.model_name = "Qwen/Qwen2.5-1.5B-Instruct"
        self.model = AutoModelForCausalLM.from_pretrained(
            self.model_name,
            torch_dtype=torch.float16,
            device_map="auto",
            low_cpu_mem_usage=True, 
        )

        self.model.generation_config.temperature=None 
        self.model.generation_config.top_p=None
        self.model.generation_config.top_k=None

        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
    def generate_text(self, prompt, max_token = 20) :
        messages = [
            {"role": "system", "content": "You are my personnal assistant"},
            {"role": "user", "content": prompt}
        ]
        text = self.tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True
        )
        model_inputs = self.tokenizer([text], return_tensors="pt").to(self.model.device)
        print("Start generate answer...")
        generated_ids = self.model.generate(
            **model_inputs,
            max_new_tokens=max_token,
            do_sample=False,       # Disable sampling for faster deterministic outputs
            num_beams=1   
        )

        generated_ids = [
            output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
        ]

        response = self.tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
        return response