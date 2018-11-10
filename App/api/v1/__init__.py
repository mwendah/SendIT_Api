from flask import flask,jsonify,request,Resource
from flask import  Blueprint
 
#create dictioanry
 parcels=[{name:'create_order'}{name:'get_order'}{name:'delete_order'}]


@app.route('/',methods=['Get'])
def test():
	return  jsonify({'message': "running"})



app.route('/parcels',methods=['Get','Post','put'])
def returnAll():
	return jsonify({'parcels':parcels})

	
# endpoint to get user detail by id
@app.route("/user/<id>", methods=["GET"])
def user_detail(id):
    user = User.query.get(id)
    return user_schema.jsonify(user)


# endpoint to update user
@app.route("/user/<id>", methods=["PUT"])
def user_update(id):
    user = User.query.get(id)
    username = request.json['username']
    email = request.json['email']

    user.email = email
    user.username = username



	if _name_=='__main__'
	app.run(debug=True,port=5000)