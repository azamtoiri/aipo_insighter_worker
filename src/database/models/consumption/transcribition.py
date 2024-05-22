from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP, BigInteger, CHAR, Text, DECIMAL, TIME
from sqlalchemy.dialects.postgresql import INTERVAL
from sqlalchemy.orm import relationship

from src.database.models.base_model import ModelBase


class TranscribedTexts(ModelBase):
    __tablename__ = 'transcribed_texts'

    id = Column(BigInteger, primary_key=True)
    text = Column(Text, nullable=False)
    initiator_user_id = Column(BigInteger, nullable=False)
    transcription_date = Column(TIMESTAMP, nullable=False)
    transcription_time = Column(TIMESTAMP, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'text': self.text,
            'initiator_user_id': self.initiator_user_id,
            'transcription_date': self.transcription_date.isoformat(),
            'transcription_time': self.transcription_time.isoformat(),

        }
