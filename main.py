from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Win(Base):
    __tablename__ = 'wins'
    id = Column(Integer, primary_key=True)
    winner = Column(String)

engine = create_engine('sqlite:///game.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

list_wins = []

def Users(user1, user2):
    if user1 == user2:
        print("equal")
    elif (user1 == "s" and user2 == "gh") or (
            user1 == "k" and user2 == "s") or (
            user1 == "gh" and user2 == "k"):
        print("user 1 wins!")
        list_wins.append("user1")
    else:
        print("user 2 wins")
        list_wins.append("user2")

    print(list_wins)

    board_game_2 = list_wins.count("user2")
    board_game_1 = list_wins.count("user1")
    print(f"number of wins user1: {board_game_1}")
    print(f"number of wins user2: {board_game_2}")

    # ذخیره نتیجه در دیتابیس
    session.add(Win(winner="user1" if user1 == "user1" else "user2"))
    session.commit()

if __name__ == '__main__':
    print("welcome")
    rounds = int(input("enter number of rounds: "))
    print("please enter 's' for (sang), 'k' for kaghaz, and 'gh' for gheichi")

    for i in range(rounds):
        x = input("user 1 input your choice: ")
        y = input("user 2 input your choice: ")
        if x and y in ["s", "k", "gh"]:
            res = Users(x, y)
        else:
            print("please enter correct value")
