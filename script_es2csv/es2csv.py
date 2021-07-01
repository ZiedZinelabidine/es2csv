from elasticsearch import Elasticsearch
import csv

es = Elasticsearch()

# Replace the following Query with your own Elastic Search Query
res = es.search(index="data-27-06-2021", body=
                {
                    "_source": ["Category", "Customer", "u'DNS'", "Bugtraq ID", "Vuln Status" , "Last Detected" , "PCI Vuln" , "Associated Tags" , "First Detected" , "Times Detected" , "IP" , "Period" , "Title" , "Severity" , "QID" , "Tracking Method" , "IP Status" , "Type" , "@timestamp" , "Results", "CVE ID", "Class" ],
                    "query": {
                        "bool": {
                            "should": [
                                {"wildcard": {"Category": "TCP/IP"}}

                            ]
                        }
                    }
}, size=10)



with open('mycsvfile.csv', 'w') as f:  # Just use 'w' mode in 3.x
    header_present  = False
    for doc in res['hits']['hits']:
        my_dict = doc['_source'] 
        if not header_present:
            w = csv.DictWriter(f, my_dict.keys())
            w.writeheader()
            header_present = True


        w.writerow(my_dict)


