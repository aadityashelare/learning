def test_hello_world():
    """Test function to check if the server returns status code 200 OK"""
    try:
        response = requests.get("http://127.0.0.1:8080/")
        if response.status_code == 200:
            print("Test Passed: Status Code 200 OK")
        else:
            print(f"Test Failed: Unexpected Status Code {response.status_code}")
    except Exception as e:
        print(f"Test Failed: {e}")

def trigger_syntax_error():
    """This function intentionally contains a syntax error"""
    eval("print('This will work')")
    # Uncomment below line to trigger a syntax error
    # eval("print('This will fail'")  # Missing closing parenthesis