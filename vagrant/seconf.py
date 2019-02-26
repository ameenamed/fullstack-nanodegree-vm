
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem
app = Flask(__name__)


engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
@app.route('/hello')
def HelloWorld():
    items=[]
    output=''
    restaurant = session.query(Restaurant).all()
    for j in range(len(restaurant)):
        items.append([])
         
        items.append(session.query(MenuItem).filter_by(restaurant_id=restaurant[j].id))
        
        for i in items[j]:
            output += i.name
            output+='</br>' 
            output+=i.price
            output+='</br>'
            output+=i.description
            output+='</br>'
            output+= '</br>'
        output+='</br>'
    return output

if __name__ == '__main__':
    app.debug = True
app.run(host='0.0.0.0', port=5000)
