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
        session = get_current_session()
        if session['type'] != "Manager":
            self.redirect('/')
        template = JINJA_ENVIRONMENT.get_template('templates/manager.html')
        self.response.write(template.render())


class ManagerAssignHandler(webapp2.RequestHandler):
    def get(self):
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
        session = get_current_session()
        if session['type'] != "Manager":
            self.redirect('/')
        else:
            template = JINJA_ENVIRONMENT.get_template('templates/manager_staff.html')
            self.response.write(template.render())


class ManagerReportHandler(webapp2.RequestHandler):
    def get(self):
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
        formType = self.request.get('formType')
        if formType == "new_staff":
            email = self.request.get('email')
            passwd = self.request.get('password')
            name = self.request.get('fname') + " " + self.request.get('lname')
            phone = self.request.get('phone')

            count = 0
            users = DataStore.Users.all()
            for user in users:
                if user.email == email:
                    count += 1
            if count == 0:
                user = DataStore.Users(name=name, password=passwd, email=email, phone=phone, type="Staff")
                user.put()
            else:
                self.redirect("/manager")

        elif formType == "assign":
            staff_email = self.request.get('start_time')
            start_time = self.request.get('start_time')
            end_time = self.request.get('end_time')
            work = self.request.get('work')
            staff_members = DataStore.Staff.all()
            count = 0
            for user in staff_members:
                duties = DataStore.Staff(start_time=start_time, end_time=end_time, work=work)
            self.redirect('/manager')