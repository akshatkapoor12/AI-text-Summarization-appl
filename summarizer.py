from transformers import pipeline

def get_summarizer(model_name='t5'):
    if(model_name=='t5'):
        return pipeline("summarization",model="t5-base")
    else:
        return pipeline("summarization",model="facebook/bart-large-cnn")
    
def summarize_text(text,summarizer):
    return summarizer(text,max_length=150,min_length=40,do_sample=False)[0]['summary_text']
