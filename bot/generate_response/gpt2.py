from transformers import AutoTokenizer, AutoModelForCausalLM, GenerationConfig

model = "gpt2"

tokenizer = AutoTokenizer.from_pretrained(model)
tokenizer.pad_token = tokenizer.eos_token
model = AutoModelForCausalLM.from_pretrained(model)

# load the generation config
gen_config = GenerationConfig(
    max_length=100,
    do_sample=True,
    top_k=50,
    top_p=0.9,
    temperature=0.9,
    pad_token_id=tokenizer.pad_token_id
)

def generate_text(text):
    # encode the input text
    input_text = text
    input_ids = tokenizer.encode(input_text, return_tensors="pt")
    attention_mask = input_ids.ne(tokenizer.pad_token_id).long()

    # generate text continuation
    output_ids = model.generate(input_ids, attention_mask=attention_mask, **gen_config.to_dict())
    output_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)

    return output_text
