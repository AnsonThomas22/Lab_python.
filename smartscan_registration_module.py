import qrcode
from PIL import Image
from pyzbar.pyzbar import decode

user_records = []

create= lambda name, email: {'name': name, 'email': email}
insert= lambda user: user_records.append(user)
fetch= lambda: user_records


def generateqr(data):
    img = qrcode.make(data)
    img.save('imgqr.png')
    print("Image saved as imgqr.png")

def decodeqr(image_path):
    img = Image.open(image_path)
    decoded_data_raw = decode(img)
    if decoded_data_raw:
        decoded_data = decoded_data_raw[0].data.decode('utf-8')
        return decoded_data
    


def RegisterUserFromSmartScan(image_path):
    user_data = decodeqr(image_path)
    records = user_data.split('\n')
    
    for record in records:
            name, email = record.split(',')
            new_user = create(name, email)
            insert(new_user)
    
    
    print("\n Registered Users:")
    for user in fetch():
        print(f"Name: {user['name']}, Email: {user['email']}")