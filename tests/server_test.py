def test_get_root_response(client):
    
    response = client.get(
        '/'
    )

    assert response.status_code == 200

    assert response.json["status"] == 'ready'
    