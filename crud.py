from sqlalchemy.orm import Session
from models import FiatPurchase
from schemas import FiatPurchaseCreate

def create_fiat_purchase(db: Session, purchase_data: FiatPurchaseCreate) -> FiatPurchase:
    purchase = FiatPurchase(
        asset=purchase_data.asset,
        quantity=purchase_data.quantity,
        original_amount=purchase_data.original_amount,
        original_currency=purchase_data.original_currency,
        usd_value=purchase_data.usd_value,
    )
    db.add(purchase)
    db.commit()
    db.refresh(purchase)
    return purchase

def get_fiat_purchases(db: Session):
    return db.query(FiatPurchase).all()