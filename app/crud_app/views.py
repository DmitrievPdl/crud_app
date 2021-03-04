# app/crud_app/views.py

from flask import abort, flash, redirect, render_template, url_for
from app import db
from .forms import FarmForm, RoleForm, FarmerForm
from app.models import Farm, Role, Farmer
from . import crud_app
# Farm Views

@crud_app.route('/farms', methods=['GET', 'POST'])
def list_farms():
    " List all Farms "

    farms = Farm.query.all()

    return render_template('crud_app/farms/farms.html',
                           farms=farms, title="Farms")


@crud_app.route('/farms/add', methods=['GET', 'POST'])
def add_farm():
    " Add a farm to the database "

    add_farm = True

    form = FarmForm()
    if form.validate_on_submit():
        farm = Farm(name=form.name.data,
                    location=form.location.data,
                    total_field_area=form.total_field_area.data,
                    average_temperature=form.average_temperature.data)
        try:
            # add form to the database
            db.session.add(farm)
            db.session.commit()
            flash('You have successfully added a new farm.')
        except:
            # in case farm name already exists
            flash('Error: farm name already exists.')

        # redirect to farms page
        return redirect(url_for('crud_app.list_farms'))

    # load farm template
    return render_template('crud_app/farms/farm.html',
                            action="Add",
                            add_farm=add_farm,
                            form=form,
                            title="Add Farm")


@crud_app.route('/farms/edit/<int:id>', methods=['GET', 'POST'])
def edit_farm(id):
    " Edit farm "

    add_farm = False

    farm = Farm.query.get_or_404(id)
    form = FarmForm(obj=farm)

    if form.validate_on_submit():
        farm.name = form.name.data
        farm.location = form.location.data
        farm.total_field_area = form.total_field_area.data
        farm.average_temperature = form.average_temperature.data

        db.session.commit()
        flash('You have successfully edited the farm.')

        # redirect to the farms page
        return redirect(url_for('crud_app.list_farms'))

    form.name.data = farm.name
    form.location.data = farm.location
    form.total_field_area = form.total_field_area
    form.average_temperature = form.average_temperature
    return render_template('crud_app/farms/farm.html',
                            action="Edit",
                            add_farm=add_farm,
                            form=form,
                            farm=farm,
                            title="Edit Farm")


@crud_app.route('/farms/delete/<int:id>', methods=['GET', 'POST'])
def delete_farm(id):
    " Delete a farm from database "

    farm = Farm.query.get_or_404(id)
    db.session.delete(farm)
    db.session.commit()
    flash('You have successfully deleted the farm.')

    # redirect to the farms page
    return redirect(url_for('crud_app.farms_list'))

    return render_template(title="Delete Farm")

# Role Views 

@crud_app.route('/roles')
def list_roles():
    " List all rules "
    roles = Role.query.all()
    return render_template('crud_app/roles/roles.html',
                           roles=roles,
                           title='Roles')


@crud_app.route('/roles/add', methods=['GET', 'POST'])
def add_role():
    " Add a role to the database "

    add_role = True

    form = RoleForm()
    if form.validate_on_submit():
        role = Role(name=form.name.data,
                    description=form.description.data)

        try:
            # add role to the database
            db.session.add(role)
            db.session.commit()
            flash('You have successfully added a new role.')
        except:
            # in case role name already exists
            flash('Error: role name already exists.')

        # redirect to the roles page
        return redirect(url_for('crud_app.list_roles'))

    # load role template
    return render_template('crud_app/roles/role.html',
                            add_role=add_role,
                            form=form,
                            title='Add Role')


@crud_app.route('/roles/edit/<int:id>', methods=['GET', 'POST'])
def edit_role(id):
    " Edit Rule"

    add_role = False

    role = Role.query.get_or_404(id)
    form = RoleForm(obj=role)
    if form.validate_on_submit():
        role.name = form.name.data
        role.description = form.description.data
        db.session.add(role)
        db.session.commit()
        flash('You have successfully edited the role.')
        # redirect to the roles page
        return redirect(url_for('crud_app.list_roles'))

    form.description.data = role.description
    form.name.data = role.name
    return render_template('crud_app/roles/role.html', add_role=add_role,
                           form=form, title="Edit Role")


@crud_app.route('/roles/delete/<int:id>', methods=['GET', 'POST'])
def delete_role(id):
    " Delete Rule from database"

    role = Role.query.get_or_404(id)
    db.session.delete(role)
    db.session.commit()
    flash('You have successfully deleted the role.')

    # redirect to the roles page
    return redirect(url_for('crud_app.list_roles'))

    return render_template(title="Delete Role")

# Farmers Views

@crud_app.route('/farmers')
def list_farmers():
    " List of farmers "

    farmers = Farmer.query.all()
    return render_template('crud_app/farmers/farmers.html',
                           farmers=farmers, title='Farmers')


@crud_app.route('/farmeres/add', methods=['GET', 'POST'])
def add_farmer():
    " Add farmer to the database "

    add_farm=True

    form = FarmerForm()
    if form.validate_on_submit():
        farmer = Farmer(email=form.email.data,
                        username =form.username.data,
                        first_name=form.first_name.data,
                        last_name=form.last_name.data,
                        farm_id=form.farm.data.id,
                        role_id=form.role.data.id)

        try:
            # add farmer to the database
            db.session.add(farmer)
            db.session.commit()
            flash('You have successfully added a new farmer.')
        except:
            # in case famrmer already exists
            flash('Error: farmer already exists.')

        # redirect to the roles page
        return redirect(url_for('crud_app.list_farmers'))

    # load role template
    return render_template('crud_app/farmers/farmer.html',
                            add_farmer=add_farmer,
                            form=form,
                            title='Add Farmer')

@crud_app.route('/farmers/edit/<int:id>', methods=['GET', 'POST'])
def edit_farmer(id):
    " Edit farmer"

    add_farmer = False

    farmer = Farmer.query.get_or_404(id)
    form = FarmerForm(obj=farmer)
    if form.validate_on_submit():
        farmer.email = form.email.data
        farmer.username = form.username.data
        farmer.first_name = form.first_name.data
        farmer.last_name = form.last_name.data
        farmer.farm = form.farm.data
        farmer.role = form.role.data

        db.session.add(farmer)
        db.session.commit()
        flash('You have successfully edited the farmer.')

        # redirect to the farmers page
        return redirect(url_for('crud_app.list_farmers'))

    form.email.data = farmer.email
    form.username.data = farmer.username
    form.first_name.data = farmer.first_name
    form.last_name.data = farmer.last_name
    form.farm.data = farmer.farm
    form.role.data = farmer.role
    return render_template('crud_app/farmers/farmer.html',
                            add_farmer=add_farmer,
                            form=form,
                            title="Edit Farmer")


@crud_app.route('/farmers/delete/<int:id>', methods=['GET', 'POST'])
def delete_farmer(id):
    " Delete Farm from database"

    farmer = Farmer.query.get_or_404(id)
    db.session.delete(farmer)
    db.session.commit()
    flash('You have successfully deleted the farmer.')

    # redirect to the farmer page
    return redirect(url_for('crud_app.list_farmers'))

    return render_template(title="Delete Farmer")