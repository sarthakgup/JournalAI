# PowerShell script to run FastAPI server
Write-Host "Starting FastAPI server on http://127.0.0.1:8000..."
python -m uvicorn journal_api:app --reload