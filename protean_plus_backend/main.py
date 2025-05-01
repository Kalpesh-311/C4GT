from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

from fastapi import FastAPI
from pydantic import BaseModel
from embedding import get_embedding
from database import SessionLocal, QueryLog

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.get("/")
def home():
    return {"message": "Protean Plus Backend working!"}

@app.post("/embed/")
def get_query_embedding(request: QueryRequest):
    embedding = get_embedding(request.query)
    db = SessionLocal()
    db_entry = QueryLog(query=request.query, embedding=str(embedding))
    db.add(db_entry)
    db.commit()
    db.close()
    return {"embedding": embedding}
def generate_response(prompt: str) -> str:
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    output = model.generate(
        **inputs,
        max_new_tokens=256,
        do_sample=True,
        temperature=0.7,
        top_k=50,
        top_p=0.95,
        eos_token_id=tokenizer.eos_token_id
    )
    decoded = tokenizer.decode(output[0], skip_special_tokens=True)
    return decoded[len(prompt):].strip()


from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

from embedding import generate_embedding
from translation import detect_language, translate_hi_to_en
from vector_store import create_schema, insert_query, search_similar

app = FastAPI()
create_schema()

# Load LLM
llm_model_id = "OpenChat/openchat-3.5-1210"
tokenizer = AutoTokenizer.from_pretrained(llm_model_id, use_fast=True)
model = AutoModelForCausalLM.from_pretrained(
    llm_model_id,
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
    device_map="auto"
)

class Query(BaseModel):
    query: str

def generate_response(prompt: str) -> str:
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    output = model.generate(
        **inputs,
        max_new_tokens=256,
        do_sample=True,
        temperature=0.7,
        top_k=50,
        top_p=0.95,
        eos_token_id=tokenizer.eos_token_id
    )
    decoded = tokenizer.decode(output[0], skip_special_tokens=True)
    return decoded[len(prompt):].strip()

@app.post("/embed/")
async def embed_query(item: Query):
    lang = detect_language(item.query)
    translated = item.query
    if lang == "hi":
        translated = translate_hi_to_en(item.query)

    vector = generate_embedding(translated)
    insert_query(translated, lang, vector)
    results = search_similar(vector)
    response = generate_response(translated)

    return {
        "language": lang,
        "translated_query": translated,
        "similar_queries": results,
        "llm_response": response,
        "status": "Processed"
    }
