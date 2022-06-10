import os
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import names
import uuid
import random

#If you add more server variables in the env-secret.yaml add them here too.
server0 = os.getenv("CASS_SERVER0")
server1 = os.getenv("CASS_SERVER1")
username = str(os.getenv("CASS_USERNAME"))
password = str(os.getenv("CASS_PASSWORD"))


auth_prov0 = PlainTextAuthProvider(username=username, password=password)
#If you add more server variables in the env-secret.yaml add them here too. ServerX
cluster = Cluster([server0, server1], auth_provider=auth_prov0)
rand_keyspace=names.get_first_name() + str(random.randint(1,10000))
print(rand_keyspace)
session = cluster.connect()
session.execute("CREATE KEYSPACE %s WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 2 };" % (rand_keyspace))
session.execute('use %s' % (rand_keyspace))
session.execute('CREATE TABLE users(user_id UUID, name text, credits int, PRIMARY KEY (user_id));')

#test
# rows = session.execute('SELECT name, age, email FROM users')

# for user_row in rows:
#     print user_row.name, user_row.age, user_row.email
while True:
    for j in range(99999):
        session.execute(
            """
            INSERT INTO users (name, credits, user_id)
            VALUES (%s, %s, %s)
            """,
            (names.get_full_name(), j, uuid.uuid1())
            )