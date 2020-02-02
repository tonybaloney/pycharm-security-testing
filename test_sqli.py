id = get_id()  # Could be a SQLi response..

query1 = f"SELECT * FROM users WHERE id = {0}"

query2 = "SELECT * FROM users WHERE id = {0}" % id

query3 = "SELECT * FROM users WHERE id = {0}".format(id)

query4 = f"UPDATE users SET is_admin = 1 WHERE id = {0}"

query5 = f"DELETE FROM users WHERE id = {0}"

query6 = f"INSERT INTO users (id) VALUES ( id = {0} )"

query7 = f"SELECT * FROM users WHERE id = {0}"

