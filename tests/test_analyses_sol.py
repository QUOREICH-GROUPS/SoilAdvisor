def test_read_analyses_sol(test_client):
    response = test_client.get("/api/v1/analyses_sol/")
    assert response.status_code == 200
    # Tu peux ajouter d'autres vérifications selon le résultat attendu