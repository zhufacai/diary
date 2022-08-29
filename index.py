from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
import uvicorn
import os


app = FastAPI()
index_html = ""

with open(os.path.join(os.path.dirname(__file__), "index.html"), 'r', encoding='utf-8') as f:
    index_html = f.read()

show_html = ""
with open(os.path.join(os.path.dirname(__file__), "show.html"), 'r', encoding='utf-8') as f:
    show_html = f.read()


@app.get('/')
async def index():
    return HTMLResponse(index_html)


@app.get("/show")
async def show(p=Query(None), t=Query(None), c=Query(None)):
    html = show_html
    if p:
        html = html.replace(".pic{display:none}", "").replace("<&p&>", p)
    if t:
        t = t.replace("\\n", "<br/>")
        html = html.replace(".title{display:none}", "").replace("<&t&>", t)
    if c:
        c = c.replace("\\n", "<br/>")
        html = html.replace(".content{display:none}", "").replace("<&c&>", c)
    return HTMLResponse(html)

if __name__ == '__main__':
    uvicorn.run(app='index:app', host="127.0.0.1",
                port=20020, reload=True, debug=True)
