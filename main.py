from flask import Flask, jsonify
from flask.globals import request
from flask_restful import Resource, Api, abort, request

app = Flask(__name__)
api = Api(app)


class Main(Resource):
	def get(self):
		return jsonify(books)


class Book(Resource):
    def get(self, book_id: int):
        try:
            return jsonify(books[book_id])
        except:
            abort(404, message=f'El libro con el id {book_id} no existe')

    def put(self, book_id):
        jsonI = request.get_json(force=True)
        books[book_id] = jsonI
        return jsonify(books)

    def post(self, book_id):
        jsonI = request.get_json(force=True)
        data = jsonI
        return jsonify(books)

    def delete(self, book_id):
        books.pop(book_id)
        return jsonify(books)

print('hellouu')
print('hellouu')

api.add_resource(Main, '/books')
api.add_resource(Book, '/books/<book_id>')

if __name__ == '__main__':
    app.run(debug=True, port=8000)
