import tekore as tk


def auth():
    client_id = "89afa62d276e41f4b3ef97514bdf8e90"
    secret_key = "594af34e6bb04667a029015743d7954c"
    token = tk.request_client_token(client_id, secret_key)
    return tk.Spotify(token)
