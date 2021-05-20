from typing import List, Dict, Optional

from pydantic import BaseModel

class Refilled(BaseModel):
    refil_id: int
    Products: Dict[str,int]