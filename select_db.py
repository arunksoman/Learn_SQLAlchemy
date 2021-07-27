from models import SessionLocal, User, pretty_print
from tabulate import tabulate
from sqlalchemy.orm import aliased

db = SessionLocal()

# select 1 record
get_user = db.query(User).get(1)
pretty_print(get_user)

# filter_by
filter_user = db.query(User).filter_by(id=1).first()
pretty_print(filter_user)

# filter_by
filter_user = db.query(User).filter_by(is_active=True).first()
pretty_print(filter_user)

filter_user = db.query(User).filter_by(is_active=True).all()
pretty_print(filter_user)

# filter
filter_user = db.query(User).filter(
		User.id == 1
	).first()
pretty_print(filter_user)

# filter_user = db.query(User).add_columns((User.id * 2).label("twice")).filter(
# 		User.id == 2
# 	).first()
filter_user = db.query(User).add_columns((User.id * 2).label("twice")).filter(
		User.is_active
	).first()
pretty_print(filter_user[0])

# filter_user = db.query(User.id, ).
