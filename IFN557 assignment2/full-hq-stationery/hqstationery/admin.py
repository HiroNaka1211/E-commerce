'''
CREATING A NEW DATABASE
-----------------------
Read explanation here: https://flask-sqlalchemy.palletsprojects.com/en/2.x/contexts/

In the terminal navigate to the project folder just above the hqstationery package
Type 'python' to enter the python interpreter. You should see '>>>'
In python interpreter type the following (hitting enter after each line):
    from hqstationery import db, create_app
    db.create_all(app=create_app())
The database should be created. Exit python interpreter by typing:
    quit()
Use DB Browser for SQLite to check that the structure is as expected before 
continuing.

ENTERING DATA INTO THE EMPTY DATABASE
-------------------------------------

# Option 1: Use DB Browser for SQLite
You can enter data directly into the cities or tours table by selecting it in
Browse Data and clicking the New Record button. The id field will be created
automatically. However be careful as you will get errors if you do not abide by
the expected field type and length. In particular the DateTime field must be of
the format: 2020-05-17 00:00:00.000000

# Option 2: Create a database seed function in an Admin Blueprint
See below. This blueprint needs to be enabled in __init__.py and then can be 
accessed via http://127.0.0.1:5000/admin/dbseed/
Database constraints mean that it can only be used on a fresh empty database
otherwise it will error. This blueprint should be removed (or commented out)
from the __init__.py after use.

Use DB Browser for SQLite to check that the data is as expected before 
continuing.
'''

from flask import Blueprint
from . import db
from .models import Category, Item, Order
import datetime


bp = Blueprint('admin', __name__, url_prefix='/admin/')

# function to put some seed data in the database
@bp.route('/dbseed/')
def dbseed():
    writingTools = Category(name='writing tools',image='writing_tools.jpg')
    studyItems = Category(name='study items', image='study_items.jpg')
    otherStationeries = Category(name='other stationeries', image='other_stationeries.jpg')
    
    try:
        db.session.add(writingTools)
        db.session.add(studyItems)
        db.session.add(otherStationeries)
        db.session.commit()
    except:
        return 'There was an issue adding the categories in dbseed function'

    Kuru_Toga_Standard_model = Item(category_id=writingTools.id, name='Kuru Toga Standard model', producer='uni MITUBISHI PENSHIL',\
        description='''Mecanical pencil that the lead revots and keeps a sharp point. You can keep writing thin letters, so your notes will be neat.''',\
            image='kurutoga.jpg', price=3.90, kind='mechanical pencil')
    sarasa_clip = Item(category_id=writingTools.id, name='SARASA CLIP0.3', producer='ZEBRA',\
        description='''Since it is a gel ink, it has a smooth and smooth writing taste.''',\
            image='Sarasa.jpg', price=1.30, kind='ballpoint pen')
    Kuru_Toga_with_rubber_grip = Item(category_id=writingTools.id, name='Kuru Toga with rubber grip blue', producer='uni MITUBISHI PENSHIL',\
        description='''A soft and elastic alpha gel is used for the grip. Because of it, it can achieve an excellent fit and comfort.''',\
            image='Kurtuga with rubber grip blue.jpg', price=8.45, kind='mechanical pencil')
    tombow8900 = Item(category_id=writingTools.id, name='Tombow 8900 (1 dozen)', producer='Tombow',\
        description='''Since it was launched in 1945, it is a pencil which has been widly used as the standard for office and learning pencils.''', 
        image='tombow8900.jpg', price=6.23, kind='pencil')
    jetstream = Item(category_id=writingTools.id, name='Jetstream Color Ink 0.5mm Blue', producer='uni MITUBISHI PENSHIL',\
        description='''Smooth writing taste that makes you addict, and it is quick dry.''',\
            image='Jetstream Color Ink 0.5mm Blue.jpg', price=2.00, kind='ballpoint pen')
    enerjel = Item(category_id=writingTools.id, name='Energel S', producer='Pentel',\
        description='''Uses EnerGel ink that allows for smooth and even writing. Writes dark and clear text with light writing, and it dries quickly.''',\
            image='Energel S.jpg', price=2.00, kind='ballpoint pen')
    mono = Item(category_id=studyItems.id, name='Mono Eraser', producer='Tombow',\
        description='''Since it was launched in 1969, it has been loved as an eraser that workes well''', 
        image='mono.jpg', price=1.30,kind='eraser')
    kadokeshi = Item(category_id=studyItems.id, name='Kadokeshi', producer='KOKUYO',\
        description='''Because of its shape, you can erase small letters easily''', 
        image='kadokeshi.jpg', price=1.77, kind='eraser')
    campus = Item(category_id=studyItems.id, name='Campus Notebook (5 books)', producer='KOKUYO',\
        description='''Lines that support "writing beautifully" By using dots that are evenly spaced on the ruled lines, you can write notes beautifully, and after writing, you can easily look back and learn efficiently.''',\
            image='campus.jpg', price=8.45, kind='notebook')
    tateyoko = Item(category_id=studyItems.id, name='Tateyoko (pencil case)', producer='NIKKEN BUNGU',\
        description='''This pen case can be used vertically or horizontally and can hold a lot of items''',\
            image='tateyoko.jpg', price=15.55, kind='pencil case')
    harinax = Item(category_id=otherStationeries.id, name='Harinax Press', producer='KOKUYO',\
        description='''This is a needleless stapler. Therefore, You can bind paper without making holes''',\
            image='Kokuyo_stapler.jpg', price=3.90, kind='stapler')
    boxCutter = Item(category_id=otherStationeries.id, name='OLFA Box Cutter', producer='OLFA',\
        description='''This is easy to handle even for those who are not familiar with large utility knives because of its compact size. When the blade is dull, you can fold blade and you can use a sharp blade again.''',\
            image='box_cutter.jpg', price=2.15, kind='cutter')
    mocha = Item(category_id=otherStationeries.id, name='Sakut Cut Hikigiri Titanium Coat Mocha', producer='Nakabayashi',\
        description='''Anti-glue blade" that is not sticky even when tape is cut''',\
            image='Scissors.jpg', price=11.80,kind='scissors') 
    
    try:
        db.session.add(Kuru_Toga_Standard_model)
        db.session.add(sarasa_clip)
        db.session.add(Kuru_Toga_with_rubber_grip)
        db.session.add(tombow8900)
        db.session.add(jetstream)
        db.session.add(enerjel)
        db.session.add(mono)
        db.session.add(kadokeshi)
        db.session.add(campus)
        db.session.add(tateyoko)
        db.session.add(harinax)
        db.session.add(boxCutter)
        db.session.add(mocha)
        db.session.commit()
    except:
        return 'There was an issue adding a item in dbseed function'

    return 'DATA LOADED'

