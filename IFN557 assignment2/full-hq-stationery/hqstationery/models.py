from . import db

class Category(db.Model):
    __tablename__='categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    image = db.Column(db.String(60), nullable=False, default = 'defaultcategory.jpg')
    items = db.relationship('Item', backref='Category', cascade="all, delete-orphan")

    def __repr__(self):
        str = "Id: {}, Name: {}, Image: {} \n" 
        str =str.format( self.id, self.name,self.image)
        return str

orderdetails = db.Table('orderdetails', 
    db.Column('order_id', db.Integer,db.ForeignKey('orders.id'), nullable=False),
    db.Column('item_id',db.Integer,db.ForeignKey('items.id'),nullable=False),
    db.PrimaryKeyConstraint('order_id', 'item_id'))

class Item(db.Model):
    __tablename__='items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64),nullable=False)
    description = db.Column(db.String(500), nullable=False)
    producer = db.Column(db.String(64),nullable=False)
    image = db.Column(db.String(60), nullable=False)
    price = db.Column(db.Float, nullable=False)
    kind = db.Column(db.String(60), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    
    def __repr__(self):
        str = "Id: {}, Name: {}, Description: {}, Producer: {} Image: {}, Price: {}, Kind: {}, Category: {}\n" 
        str =str.format( self.id, self.name, self.producer, self.description,self.image, self.price, self.kind, self.category_id)
        return str

class Order(db.Model):
    __tablename__='orders'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Boolean, default=False)
    firstname = db.Column(db.String(64))
    lastname = db.Column(db.String(64))
    email = db.Column(db.String(128))
    phone = db.Column(db.String(32))
    address = db.Column(db.String(64))
    date = db.Column(db.DateTime)
    items = db.relationship("Item", secondary=orderdetails, backref="orders")
    totalcost = db.Column(db.Float)

    def __repr__(self):
        str = "Id: {}, Status: {}, Firstname: {}, Lastname: {}, Email: {}, Phone: {}, Address: {}, Date: {}, Items: {}, Total Cost: {}\n" 
        str =str.format( self.id, self.status,self.firstname,self.lastname, self.email, self.phone, self.address, self.date, self.items, self.totalcost)
        return str

