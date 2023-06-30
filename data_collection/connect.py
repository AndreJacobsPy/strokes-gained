
# connection str
CONN = "mongodb+srv://andre514:Jackie287@strokes-gained.hwkuxky.mongodb.net/?retryWrites=true&w=majority"

if __name__ == "__main__":
    from pymongo import MongoClient
    import pandas as pd

    # connecting to mongoDB client
    myclient = MongoClient("mongodb+srv://andre514:Jackie287@strokes-gained.hwkuxky.mongodb.net/?retryWrites=true&w=majority")
    db = myclient['strokes-gained']

    # show collections in database
    print(db.list_collection_names())

    # add data to tournament collection
    df = pd.read_csv('tournament_data.csv')
    # db['tournaments'].insert_many(df.to_dict('records'))

    # add data to players collection
    players = pd.read_csv('strokes_gained.csv')
    # db['players'].insert_many(players.to_dict('records'))


