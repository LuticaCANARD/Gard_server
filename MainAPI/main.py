from DB import DB
from Lathion_lib import Lathion
import fastapi as fa


la = Lathion()
app = fa.FastAPI()

@app.get('/')
async def test() :
    return {"msg":"server is okay!"}

@app.get('/DBtest')
async def dbtest():
    return dict(la.db_test())