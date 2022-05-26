def create_classes(db):
    class News(db.Model):
        __tablename__ = 'fake_news_input'

        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(255))
        text = db.Column(db.String(255))
        subject = db.Column(db.String(255))
        news_date = db.Column(db.String(10))
        #model_resp = db.Column(db.String(1))

        def __repr__(self):
            return '<News %r>' % (self.title)
    return News




    # def create_classes(db):
    # class News(db.Model):
    #     __tablename__ = 'FakeNewsArticlesInput'

    #     id = db.Column(db.Integer, primary_key=True)
    #     articletitle = db.Column(db.String(255))
    #     articletext = db.Column(db.String(255))
    #     articlesubject = db.Column(db.String(255))
    #     articledate = db.Column(db.String(255))
    #     articlestatus = db.Column(db.String(5))

    #     def __repr__(self):
    #         return '<News %r>' % (self.articletitle)
    # return News
