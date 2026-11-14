import urllib.request
import json

def test_health():
    url = "http://127.0.0.1:5000/health"
    try:
        response = urllib.request.urlopen(url)
        data = json.loads(response.read().decode())
        assert response.status == 200
        assert data["status"] == "healthy"
        print("✅ Health check test passed successfully!")
    except Exception as e:
        print(f"❌ Test failed: {e}")
        exit(1)

if __name__ == "__main__":
    test_health()
