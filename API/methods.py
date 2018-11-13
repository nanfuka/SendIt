parcel = { 'order_id' : len(order_list)+1,
        'user_id' :user_id,
        'email':email,
        'status':status
def create(parcel):
    order_list.append(parcel)
    return jsonify({"parcel successfully created":parcel})