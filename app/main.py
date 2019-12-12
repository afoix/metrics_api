from fastapi import FastAPI
import psutil

app = FastAPI()

@app.get("/get_cpu_stats")
def cpu_stats():
    return {'cpu_load': str(psutil.cpu_times_percent())}

@app.get("/get_mem_stats")
def mem_stats():
    return {'ram usage': str(psutil.virtual_memory()[2])}

@app.get("/get_disk_stats")
def disk_stats():
    return {'disk usage':  str(psutil.disk_usage('/')[3])}
