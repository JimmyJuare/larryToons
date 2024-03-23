from .db import db, environment, SCHEMA, add_prefix_for_prod


class Book(db.Model):
    __tablename__= 'books'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    # channel_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('channels.id')), nullable=False)
    # owner_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)

    # channels = db.relationship('Channel', back_populates='messages')
    users = db.relationship('User', back_populates= 'messages')


    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "descripion": self.description,
            "price": self.price
        }
