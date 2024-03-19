from sqlalchemy import create_engine, String,select, or_
from sqlalchemy.orm import Session, DeclarativeBase, Mapped, mapped_column

engine = create_engine("sqlite:///data.db", echo=False)
class Base(DeclarativeBase):
    pass

class Cat(Base):
    __tablename__="Cats"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String[30])
    age: Mapped [int] = mapped_column()
    def __repr__(self) -> str:
        return f"Cat(id={self.id}, name={self.name}, age={self.age})"

Cat.metadata.create_all(engine)

# c = Cat(name='Vasya', age=2 )
# c1 = Cat(name='Gin', age=3 )
# s.add(c)
# s.add(c1)
# s.commit()

with Session(engine) as s:
    results = select(Cat).where(Cat.age==2)
    
    for result in s.scalars(results):
        print(result)
    
    
    