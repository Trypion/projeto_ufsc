from flask import Blueprint, render_template

class AuthRoutes(Blueprint):
    def __init__(self):        
        super().__init__('auth_bp', __name__)

        @self.route('/register')
        def register():
            return render_template("auth/register.html")
        
        @self.route('/login')
        def login():
            return render_template("auth/login.html")
