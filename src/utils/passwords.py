import bcrypt

def encrypt_password(password):
    try:

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        return {
            'success': True,
            'data': hashed_password.decode('utf-8')
        }

    except Exception as e:

        return {
            'success': False,
            'data': str(e)
        }
    
def test_password(password_provided, hashed_password):
    try:

        result = bcrypt.checkpw(password_provided.encode('utf-8'), hashed_password.encode('utf-8'))

        return {
            'success': True,
            'data': result
        }

    except Exception as e:

        print(f"Error testing password {e}")

        return {
            'success': False,
            'data': str(e)
        }