def test_fails_when_user_is_not_authenticated(graphql_client):
    resp = graphql_client.query(
        """
        {
            me {
                email
            }
        }
        """
    )

    assert resp["errors"]
    assert resp["errors"][0]["message"] == "User not logged in"


def test_works_when_user_is_logged_in(user, graphql_client):
    graphql_client.force_login(user)

    resp = graphql_client.query(
        """
        {
            me {
                email
            }
        }
        """
    )

    assert "errors" not in resp
    assert resp["data"]["me"]["email"] == user.email


def test_get_country(graphql_client):
    country = "IT"
    resp = graphql_client.query(
        """
        query($code: String!) {
            country(code: $code) {
                code
                name
            }
        }
        """,
        variables={"code": country},
    )

    assert resp["data"]["country"]["code"] == country
    assert resp["data"]["country"]["name"] == "Italy"


def test_get_countries(graphql_client):
    resp = graphql_client.query(
        """
        query {
            countries {
                code
                name
            }
        }
        """
    )

    assert len(resp["data"]["countries"]) == 249


def test_get_country_not_exist(graphql_client):
    country = "XY"
    resp = graphql_client.query(
        """
        query($code: String!) {
            country(code: $code) {
                code
                name
            }
        }
        """,
        variables={"code": country},
    )

    assert resp["errors"][0]["message"] == "'XY' is not a valid country."
