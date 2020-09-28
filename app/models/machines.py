from app import db
from datetime import datetime


class Machine(db.Model):
    __tablename__ = 'machines'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    hostname = db.Column(db.String(50), nullable= False)
    tipping = db.Column(db.String(50), nullable= False)
    ur = db.Column(db.String(10))
    ip = db.Column(db.String(50))
    local = db.Column(db.String(50), nullable= False)
    sector = db.Column(db.String(80), nullable= False)
    ramal = db.Column(db.String(30), nullable= False)
    created_at = db.Column(db.TIMESTAMP, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    def __init__(self,hostname, tipping,ur,ip,local, sector,ramal,created_at,updated_at):
        self.hostname = hostname
        self.tipping = tipping
        self.ur = ur
        self.ip = ip
        self.local = local
        self.sector = sector
        self.ramal = ramal
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def __repr__(self):
        return f"<Machine: {self.hostname} {self.ip}>"