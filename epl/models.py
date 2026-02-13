from epl import db
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

class Club(db.Model):
  __tablename__ = 'club'
  id: Mapped[int] = mapped_column(Integer, primary_key=True)
  name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
  stadium: Mapped[str] = mapped_column(String(50), nullable=False)
  year: Mapped[int] = mapped_column(Integer, nullable=False)
  logo: Mapped[str] = mapped_column(String(255), nullable=False)

  players: Mapped[List['Player']] = relationship(back_populates='club')

  def __repr__(self):
    return f'<Club: {self.name}>'

class Player(db.Model):
  __tablename__ = 'player'
  id: Mapped[int] = mapped_column(Integer, primary_key=True)
  name: Mapped[str] = mapped_column(String(50), nullable=False)
  position: Mapped[str] = mapped_column(String(20), nullable=False)
  nationality: Mapped[str] = mapped_column(String(50), nullable=False)
  goals: Mapped[int] = mapped_column(Integer, default=0, nullable=True)
  squad_no: Mapped[int] = mapped_column(Integer, nullable=True)
  img: Mapped[str] = mapped_column(String(255), nullable=False)
  club_id: Mapped[int] = mapped_column(Integer, ForeignKey(Club.id))
  clean_sheets: Mapped[int] = mapped_column(Integer, nullable=True)


  club: Mapped[Club] = relationship(back_populates='players')
  
  def __repr__(self):
    return f'<Club: {self.name}>'