import Blockchain

db=Blockchain.Blockchain()
db.create_user("Artem", "737373737")
db.create_user("Ilya", "874874744")
token=db.sign_in("Artem", "737373737")
token1=db.sign_in("Ilya", "874874744")
db.send_message("Artem", "Ilya", "hsdfkushdkf", token)
print(token)
print(db.get_connections("Artem", token))
print(db.get_connections("Ilya", token1))