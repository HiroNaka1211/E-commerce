from flask import Blueprint, render_template, url_for, request, session, flash, redirect
from .models import Category, Item, Order
from datetime import datetime
from .forms import CheckoutForm
from . import db


bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    categories = Category.query.order_by(Category.id).all()
    recommend = Item.query.filter(Item.name.in_(['Kuru Toga Standard model','SARASA CLIP0.3','Harinax Press']))
    return render_template('index.html', categories = categories, recommend=recommend)

@bp.route('/items/<int:categoryid>/')
def categoryitems(categoryid):
    items = Item.query.filter(Item.category_id == categoryid)
    return render_template('categoryitems.html', items = items)



# Referred to as "Cart" to the user
@bp.route('/order', methods=['POST','GET'])
def order():
    item_id = request.values.get('item_id')

    # retrieve order if there is one
    if 'order_id'in session.keys():
        order = Order.query.get(session['order_id'])
        # order will be None if order_id stale
    else:
        # there is no order
        order = None

    # create new order if needed
    if order is None:
        order = Order(status = False, firstname='', lastname='', email='', phone='', address='', date=datetime.now(), totalcost=0,)
        try:
            db.session.add(order)
            db.session.commit()
            session['order_id'] = order.id
        except:
            print('failed at creating a new order')
            order = None
    
    # calcultate totalprice
    totalprice = 0
    if order is not None:
        for item in order.items:
            totalprice = totalprice + item.price
    
    # are we adding an item?
    if item_id is not None and order is not None:
        item = Item.query.get(item_id)
        if item not in order.items:
            try:
                order.items.append(item)
                db.session.commit()
            except:
                return 'There was an issue adding the item to your cart'
            return redirect(url_for('main.order'))
        else:
            flash('item already in cart')
            return redirect(url_for('main.order'))
    
    return render_template('order.html', order = order, totalprice = totalprice)


# Delete specific cart items
@bp.route('/deleteorderitem', methods=['POST'])
def deleteorderitem():
    id=request.form['id']
    if 'order_id' in session:
        order = Order.query.get_or_404(session['order_id'])
        item_to_delete = Item.query.get(id)
        try:
            order.items.remove(item_to_delete)
            db.session.commit()
            flash('The item deleted successfully')
            return redirect(url_for('main.order'))
        except:
            return 'Problem deleting item from order'
    return redirect(url_for('main.order'))
    


# Scrap cart
@bp.route('/deleteorder')
def deleteorder():
    if 'order_id' in session:
        del session['order_id']
        flash('All items deleted')
    return redirect(url_for('main.index'))


@bp.route('/checkout', methods=['POST','GET'])
def checkout():
    form = CheckoutForm() 
    if 'order_id' in session:
        order = Order.query.get_or_404(session['order_id'])
       
        if form.validate_on_submit():
            order.status = True
            order.firstname = form.firstname.data
            order.lastname = form.lastname.data
            order.email = form.email.data
            order.phone = form.phone.data
            order.address = form.address.data
            totalcost = 0
            for item in order.items:
                totalcost = totalcost + item.price
            order.totalcost = totalcost
            order.date = datetime.now()
            try:
                db.session.commit()
                del session['order_id']
                flash('Thank you for your order from HQ-stationery, your order is on the way')
                return redirect(url_for('main.index'))
            except:
                return 'There was an issue completing your order'
    return render_template('checkout.html', form = form)
    

@bp.route('/details/<int:itemid>/')
def itemdetails(itemid):
    itemdetails = Item.query.filter(Item.id == itemid)
    return render_template('itemdetails.html', items = itemdetails)


@bp.route('/items/')
def search():
	search = request.args.get('search')
	search = '%{}%'.format(search) # substrings will match
	items = Item.query.filter(Item.kind.like(search)).all()
	return render_template('categoryitems.html', items = items)