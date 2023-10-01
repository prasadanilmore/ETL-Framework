from cassandra.cluster import Cluster

cassandra_host = 'cassandra'
cassandra_keyspace = 'my_keyspace'
cassandra_table = "merchandise_value"

def get_connection_session():
    cluster = Cluster([cassandra_host])
    session = cluster.connect()

    session.execute(
        f"CREATE KEYSPACE IF NOT EXISTS {cassandra_keyspace}"
        f"WITH REPLICATION = {{'class': 'SimpleStrategy', 'replication_factor':1}}"
    )

    session.set_keyspace(cassandra_keyspace)

    session.execute(
        f"CREATE TABLE IF NOT EXISTS {cassandra_table} ("
        f"customer_id TEXT PRIMARY KEY, "
        f"order_id UUID, "
        f"net_value DECIMAL )"
    )
    
    return cluster, session

def write_to_database(customer_id, order_id, net_value):
    cluster, session = get_connection_session()

    session.execute(
        f"INSERT INTO {cassandra_table} (customer_id, order_id, net_value)"
        f"VALUE ({customer_id}, {order_id}, {net_value})",
    )

    cluster.shutdown()

    

