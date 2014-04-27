__author__ = 'Aneesh Neelam <neelam.aneesh@gmail.com>'

from gaesessions import SessionMiddleware


def webapp_add_wsgi_middleware(app):
    app = SessionMiddleware(app,
                            cookie_key="379d4dd06bc2b2fc80b9402ced35b77364f37e6ea54d61fb4c4748bb9e01744e577b61630c44b2d3c77b5a4305f7a7f6132cc17f841bdc8c48bab52557decf61")
    return app