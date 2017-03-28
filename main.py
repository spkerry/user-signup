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

class MainHandler(webapp2.RequestHandler):
    def get(self):

        header = "<h1>Signup</h1>"

        signup_form = """
            <form method="post">
                <table>
                    <tbody>
                        <tr>
                            <td>
                                <label for="username">Username</label>
                            </td>
                            <td>
                                <input name="username" type="text"/>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <label for="password">Password</label>
                            </td>
                            <td>
                                <input name="password" type="password"/>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <label for="verify">Verify Password</label>
                            </td>
                            <td>
                                <input name="verify" type="password"/>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <label for="email">Email (optional)</label>
                            </td>
                            <td>
                                <input name="email" type="email"/>
                            </td>
                        </tr>
                    </tbody>
                </table>
                <input type="submit"/>
            </form>
            """

        main_content = header + signup_form
        content = page_header + main_content + page_footer
        self.response.write(content)

class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        name = self.request.get(username)
        content = "<strong>Welcome, " + name + "!</strong"
        self.response.write(content)


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcomme', WelcomeHandler)
], debug=True)
