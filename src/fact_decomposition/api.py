from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .pipeline import FactDecompositionPipeline

app = FastAPI(
    title="Fact Decomposition API",
    description="API for analyzing text and extracting facts",
    version="1.0.0"
)

class AnalysisRequest(BaseModel):
    input_text: str
    output_text: str
    model: str = "gpt-4"

pipeline_instances = {}

@app.post("/analyze")
async def analyze_text(request: AnalysisRequest):
    try:
        if request.model not in pipeline_instances:
            pipeline_instances[request.model] = FactDecompositionPipeline(request.model)
        
        pipeline = pipeline_instances[request.model]
        analysis = pipeline.process_text(request.input_text, request.output_text)
        
        return {
            "common_facts": analysis.common_facts,
            "hallucinations": analysis.hallucinations,
            "missing_facts": analysis.missing_facts,
            "highlighted_output": analysis.highlighted_output
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))