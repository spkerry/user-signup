#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#

#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import cgi
import re
import os
import string

page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>User Signup</title>
    <style type="text/css">
        .error {
            color: red;
        }
    </style>
</head>
<body>
"""


page_footer = """
</body>
</html>
"""

username =""
signup_form = """
    <form  method="post">
        <header>
            <h1>Signup</h1>
        </header>
        <table>
            <tbody>
                <tr>
                    <td class="label">
                        Username
                    </td>
                    <td>
                        <input name="username" type="text" value="%(username)s">

                    </td>
                    <td>
                        <div class="error">%(error_username)s</div>
                    </td>
                </tr>
                <tr>
                    <td>
                        <label for="password">Password</label>
                    </td>
                    <td>
                        <input name="password" type="password" value="">
                    </td>
                    <td>
                        <div class="error">%(error_password)s</div>
                    </td>

                </tr>
                <tr>
                    <td>
                        <label for="verify">Verify Password</label>
                    </td>
                    <td>
                        <input name="verify" type="password" value="">
                    </td>
                    <td>
                        <div class="error">%(error_verify)s</div>
                    </td>
                </tr>
                <tr>
                    <td>
                        <label for="email">Email (optional)</label>
                    </td>
                    <td>
                        <input name="email" type="email" value="%(email)s">
                    </td>
                    <td>
                        <div class="error">%(error_email)s</div>
                    </td>
                </tr>
            </tbody>
        </table>
        <input type="submit">
    </form>
"""

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return username and USER_RE.match(username)

PASS_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    return password and PASS_RE.match(password)

EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")
def valid_email(email):
    return email or EMAIL_RE.match(email)


class MainHandler(webapp2.RequestHandler):

    def get(self,  username="", email="", error_username="",error_password="",
            error_verify="", error_email=""):
        content = page_header + signup_form % {"error_username" : error_username,
                                                "error_password" : error_password,
                                                "error_verify" : error_verify,
                                                "error_email" : error_email,
                                                "username" : username,
                                                "email":email}+ page_footer
        self.response.write(content)

    def post(self):
        error_username = ""
        error_password = ""
        error_verify = ""
        error_email = ""

        have_Error = False
        username = self.request.get("username")
        password = self.request.get("password")
        verify = self.request.get("verify")
        email = self.request.get("email")


        if not valid_username(username):
            error_username = "That's not a valid username."
            have_Error = True

        if not valid_password(password):
            error_password = "That wasn't a valid password"
            have_Error = True
        elif password != verify:
            error_verify = "Your passwords didn't match"
            have_Error = True

        if email and not valid_email(email):
            error_email = "That's not a valid email"
            have_Error = True

        params = {"error_username" : error_username,
                    "error_password" : error_password,
                    "error_verify" : error_verify,
                    "error_email" : error_email,
                    "username" : username,
                    "email":email}


        if have_Error:
            content = page_header + signup_form % params + page_footer
            self.response.write(content)
        else:
            self.redirect('/welcome?username=' + username)

class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        name = self.request.get("username")

        content = "<strong>Welcome, " + name + "!</strong"
        self.response.write(content)


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcome', WelcomeHandler)
], debug=True)
