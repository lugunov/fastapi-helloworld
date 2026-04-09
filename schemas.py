from pydantic import BaseModel
from datetime import datetime

class FiatPurchaseCreate(BaseModel):
    asset: str
    quantity: float
    original_amount: float
    original_currency: str
    usd_value: float

class FiatPurchaseResponse(BaseModel):
    id: int
    asset: str
    quantity: float
    original_amount: float
    original_currency: str
    usd_value: float
    created_at: datetime

    class Config:
        from_attributes = True