from sqlalchemy import Column, Integer, String, Numeric, DateTime
from datetime import datetime
from database import Base

class FiatPurchase(Base):
    __tablename__ = "fiat_purchases"

    id = Column(Integer, primary_key=True, index=True)
    asset = Column(String, nullable=False)
    quantity = Column(Numeric(18, 8), nullable=False)
    original_amount = Column(Numeric(18, 2), nullable=False)
    original_currency = Column(String, nullable=False)
    usd_value = Column(Numeric(18, 2), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)