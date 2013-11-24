__author__ = 'matthew'

import boundaryalias

def main():
    org_id = "3iCJZBSlCiIYREYrncvg45FOsho"
    api_key = "APHUPXJRBS2Iee8kDAQaZas4Nzv"
    omfg = boundaryalias.Boundaryalias(org_id, api_key)

    correct_ports = {
        "2003:6": "graphite",
        "2181:6": "zookeeper",
        "2888:6": "exhibitor",
        "3772:6": "storm-drpc",
        "3773:6": "storm-drpc-invocation",
        "6627:6": "storm-nimus-thrift",
        "7000:6": "cassandra-storage-port",
        "8140:6": "puppet",
        "9092:6": "kafka",
        "9160:6": "cassandra",
        "9300:6": "elasticsearch-transport",
        "9200:6": "elasticsearch-data",
        }

    print omfg.set_port_aliases(correct_ports)
    print omfg.get_port_aliases()

if __name__ == "__main__":
    main()
