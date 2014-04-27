__author__ = 'Aneesh Neelam <neelam.aneesh@gmail.com>'

import os

import webapp2
import jinja2

import DataStore
from gaesessions import get_current_session


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class ManagerHandler(webapp2.RequestHandler):
    def get(self):
        """
            Get Request handler for '/manager'
        """
        session = get_current_session()
        if session['type'] != "Manager":
            self.redirect('/')
        Users = DataStore.Users.all()
        Staff = []
        Customer = []
        for user in Users:
            if user.type == "Staff":
                Staff.append(user)
            elif user.type == "Customer":
                Customer.append(user)
        template_values = {
            'Staff': Staff,
            'Customer': Customer

        }
        template = JINJA_ENVIRONMENT.get_template('templates/manager.html')
        self.response.write(template.render(template_values))


class ManagerAssignHandler(webapp2.RequestHandler):
    def get(self):
        """
            Get Request handler for '/manager/assign'
        """
        session = get_current_session()
        if session['type'] != "Manager":
            self.redirect('/')
        else:
            Users = DataStore.Users.all()
            Staff = []
            for user in Users:
                if user.type == "Staff":
                    Staff.append(user)
            template_values = {
                'Staff': Staff
            }
            template = JINJA_ENVIRONMENT.get_template('templates/manager_assign.html')
            self.response.write(template.render(template_values))


class ManagerStaffHandler(webapp2.RequestHandler):
    def get(self):
        """
            Get Request handler for '/manager/staff'
        """
        session = get_current_session()
        if session['type'] != "Manager":
            self.redirect('/')
        else:
            template = JINJA_ENVIRONMENT.get_template('templates/manager_staff.html')
            self.response.write(template.render())


class ManagerReportHandler(webapp2.RequestHandler):
    def get(self):
        """
            Get Request handler for '/manager/reports'
        """
        session = get_current_session()
        if session['type'] != "Manager":
            self.redirect('/')
        else:
            reports = DataStore.Reports.all()
            template_values = {
                'Reports': reports
            }
            template = JINJA_ENVIRONMENT.get_template('templates/manager_reports.html')
            self.response.write(template.render(template_values))


class ManagerProcessHandler(webapp2.RequestHandler):
    def post(self):
        """
            Post Request handlers for all manager related form submissions
        """
        form_type = self.request.get('formType')
        if form_type == "new_staff":
            email = self.request.get('email')
            password = self.request.get('password')
            fname = self.request.get('fname')
            lname = self.request.get('lname')
            name = fname + " " + lname
            phone = self.request.get('phone')
            count = 0
            if email == "" or password == "" or fname == "" or lname == "" or phone == "":
                self.redirect("/manager/staff")
            else:
                users = DataStore.Users.all()
                for user in users:
                    if user.email == email:
                        count += 1
                if count == 0:
                    user = DataStore.Users(name=name, password=password, email=email, phone=phone, type="Staff")
                    user.put()
                    self.redirect("/manager")
                else:
                    self.redirect("/manager/staff")

        elif form_type == "assign":
            staff_email = self.request.get('staff_email')
            start_time = self.request.get('start_time')
            end_time = self.request.get('end_time')
            work = self.request.get('work')
            if work == "":
                self.redirect("/manager/assign")
            else:
                staff_members = DataStore.Staff.all()
                count = 0
                for user in staff_members:
                    if user.email == staff_email:
                        count += 1
                if count == 0:
                    duties = DataStore.Staff(email=staff_email, start_time=start_time, end_time=end_time, work=work)
                    duties.put()
                else:
                    for duties in staff_members:
                        if duties.email == staff_email:
                            duties.start_time = start_time
                            duties.end_time = end_time
                            duties.work = work
                            duties.put()
                self.redirect('/manager')